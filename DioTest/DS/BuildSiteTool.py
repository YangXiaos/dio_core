import time
from typing import Union

from DioCore.Network.Downloader import Downloader
from DioCore.Network.Downloader.Downloader import Setting
from DioCore.Utils import UrlUtil, JsonUtil

MAIN_URL = "http://v3.rhino.datatub.com/api/site/add"
GET_SITE_INFO_URL = "http://v3.rhino.datatub.com/api/site/getSite?id={}"
BUILD_TEMPLATE_URL = "http://v3.rhino.datatub.com/api/site/addTpl"
BUILD_TASK_URL = "http://v3.rhino.datatub.com/api/site/addTask"
TEST_TEMPLATE_URL = "http://v3.rhino.datatub.com/api/site/testTpl"

HEADERS = {
    'Cookie': "JSESSIONID=BE46071C4181E9CF7AEB700C8E1ADDE7",
    'Origin': "http://v3.rhino.datatub.com",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "zh-CN,zh;q=0.9",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
    'Accept': "*/*",
    'Referer': "http://v3.rhino.datatub.com/",
    'X-Requested-With': "XMLHttpRequest",
    'Connection': "keep-alive",
    'cache-control': "no-cache",
}


# 创建站点
def buildSite(body):
    """创建站点"""
    payload = UrlUtil.urlencode(body)
    s = Setting(request="POST", headers=HEADERS)
    res = Downloader.payload(MAIN_URL, data=payload, setting=s)
    print(res.json())
    return res.json()["data"]["id"]


# 创建模板
def buildTemplate(body):
    """创建模板"""
    payload = UrlUtil.urlencode(body)
    s = Setting(request="POST", headers=HEADERS)
    res = Downloader.payload(BUILD_TEMPLATE_URL, data=payload, setting=s)
    return res.json()["data"]["id"]


# 创建任务
def buildTask(body):
    payload = UrlUtil.urlencode(body)
    s = Setting(request="POST", headers=HEADERS)
    res = Downloader.payload(BUILD_TASK_URL, data=payload, setting=s)
    print(res.json())
    return res.json()["data"]["id"]


# 测试模板
def testTp(body):
    payload = UrlUtil.urlencode(body)
    s = Setting(request="POST", headers=HEADERS)
    res = Downloader.payload(TEST_TEMPLATE_URL, data=payload, setting=s)
    return res.json()["data"]


# 站点创建
#     {
#       "code": 0,
#       "data": {
#         "site": {
#           "cron": "",
#           "maxDepth": "2",
#           "agent": [],
#           "domain": "news.modernweekly.com",
#           "name": "周末画报_新闻频道",
#           "interval": "20",
#           "category": "3",
#           "params": {
#             "rhino.task.unique.manager.cache_size": "1000",
#             "rhino.task.job.info.collector.class": "com.datatub.rhino.framework.component.collector.LocalJobInfoCollector",
#             "rhino.task.unique.manager.class": "com.datatub.rhino.framework.component.operatior.manager.unique.RedisListUniqueManager",
#             "spark.executor.core.num": "1",
#             "fail_queue": "OFF",
#             "spark.executors.num": "1",
#             "error_fail": "0.9"
#           },
#           "parentId": "1202947",
#           "tags": []
#         }
#       }
#     }
def getSiteInfo(siteId: int):
    url = GET_SITE_INFO_URL.format(siteId)
    s = Setting()
    s.setParams(headers=HEADERS)
    return Downloader.get(url, setting=s).json()["data"]["site"]


def buildMainSite(url: str, parentId: int=-1):
    """
    建立主站点
    :param parentId: 父级站点
    :param url: 站点url
    :param domain: 站点domian
    :param name:
    :return: siteId
    """
    soup = Downloader.getBs4(url)
    title = soup.select_one("title").text.replace("--", "dio").replace("-", "dio").replace("_", "dio")\
        .replace("——", "dio").replace("|", "dio").replace("·", "dio").replace(" ", "dio")
    name = ""
    host = UrlUtil.getHost(url)
    print("host 为" + host)

    for n in title.split("dio"):
        print("site name 为: " + n)
        if input() in ("", "y", "Y", "Yes"):
            name = n.strip()
            break

    if parentId != -1:
        mainSiteName = getSiteInfo(parentId)["name"]
        name = "{}_{}".format(mainSiteName, name)

    if input("是否添加频道后缀") in ("", "y", "Y", "Yes"):
        name = "{}{}".format(name, "频道  ")
    print("输出name为: {}".format(name))
    siteQuery = {
        "name": name,
        "domain": UrlUtil.getHost(url),
        "tags": [],
        "maxDepth": "2",
        "overtime": "",
        "params": {
            "spark.executors.num": "1",
            "spark.executor.core.num": "1",
            "error_fail": "0.9",
            "fail_queue": "OFF",
            "rhino.task.unique.manager.class": "com.datatub.rhino.framework.component.operatior.manager.unique.RedisListUniqueManager",
            "rhino.task.unique.manager.cache_size": "1000",
            "rhino.task.job.info.collector.class": "com.datatub.rhino.framework.component.collector.LocalJobInfoCollector"
        },
        "threshold": "",
        "frequency": "",
        "interval": "20",
        "cron": "",
        "template": [],
        "agent": [],
        "category": "3"
    }

    query = {"parentId": parentId, "site": JsonUtil.toJson(siteQuery)}
    siteId = buildSite(query)
    print("输出页面url为: " + "http://v3.rhino.datatub.com/#/gather/siteManager?site={}".format(siteId))
    return siteId


def buildNavTemplate(parentId, navUrls: list, regex="", match_regex= ""):
    site = getSiteInfo(parentId)
    regex = input("输入正则: ") if not regex else regex
    match_regex = input("输入抽取正则: ") if not match_regex else match_regex

    rules = [
        {
            "id": "7",
            "param": ""
        },
        {
            "id": "12",
            "name": "正则匹配链接抽取处理器",
            "param": JsonUtil.toJson({
                "match_regex": match_regex
            })
        }
    ]
    desc = "{}-导航页".format(site["name"])
    print("模板名为{}".format(desc))
    template = {
        "urlReg": regex,
        "desc": desc,
        "tags": [],
        "rules": JsonUtil.toJson(rules),
        "type": "link",
        "lang": "",
        "entrance_seed": "",
        "after_ids": "",
        "validate_rules": "",
        "remark": navUrls[0]
    }
    tpId = buildTemplate({"parentId": parentId, "template": JsonUtil.toJson(template)})
    print("模板id {} 输出导航页页面url为:  http://v3.rhino.datatub.com/#/gather/siteManager/template/edit?templateId={}".format(tpId, tpId))
    return tpId


# 内容模板创建
def buildContentTemplate(parentId, navUrls: list, regex=""):
    site = getSiteInfo(parentId)

    rules = [
        {"id": "7", "param": ""},
        {
            "id": "11",
            "name": "通用新闻正文抽取处理器",
            "param": JsonUtil.toJson({"url_key":"full_url","useLegacy":"false"})
        },
        {
            "id": "4",
            "name": "内容抽取处理器",
            "param": JsonUtil.toJson([
                {"inputKey":"_html_","outputKey":"","type":"selector","exp":"","attr":"","script":"","func":""
             }])
        }
    ]
    regex = input("输入正则: ") if not regex else regex
    desc = "{}-内容页".format(site["name"])
    print("模板名为: {}".format(desc))
    template = {
        "urlReg": regex,
        "desc": desc,
        "tags": [],
        "rules": JsonUtil.toJson(rules),
        "type": "content",
        "lang": "",
        "entrance_seed": "",
        "after_ids": "",
        "validate_rules": "",
        "remark": navUrls[0]
    }
    tpId = buildTemplate({"parentId": parentId, "template": JsonUtil.toJson(template)})
    print("模板id {} 输出内容页页面url为:  http://v3.rhino.datatub.com/#/gather/siteManager/template/edit?templateId={}".format(tpId, tpId))
    return tpId


# 任务列表创建
def buildListTask(taskList):
    for task in taskList:
        if not task:
            print("建立taskId pass")
            continue
        print(task)
        parentId = task["siteId"]
        task = {
            "name": task["name"].strip(),
            "enterUrl": task["enterUrl"].strip(),
            "maxDepth": "2",
            "overtime": "",
            "params": {
                "rhino.task.unique.manager.cache_size": "1000",
                "rhino.task.job.info.collector.class": "com.datatub.rhino.framework.component.collector.LocalJobInfoCollector",
                "rhino.task.unique.manager.class": "com.datatub.rhino.framework.component.operatior.manager.unique.RedisListUniqueManager",
                "spark.executor.core.num": "1",
                "fail_queue": "OFF",
                "spark.executors.num": "1",
                "error_fail": "0.9"
            },
            "threshold": "",
            "frequency": "",
            "interval": "{}".format(task["interval"].strip()),
            "cron": "",
            "tags": [],
            "template": task["template"],
            "category": "3",
            "agent": [],
            "parentId": "{}".format(task["siteId"].strip())
        }
        tkId = buildTask({"parentId": parentId, "task": task})
        print("建立taskId成功: " + "http://v3.rhino.datatub.com/#/gather/siteManager/task/edit?taskId={}".format(tkId))
        time.sleep(3)


# 模板测试函数
def testNavTemplate(urls: list, tpId: Union[str, int]):
    for url in urls:
        print("测试url {}".format(url))
        config = {"url": url, "params": {}}
        data = testTp({"config": config, "id": tpId})
        print("输出数据数量 {}".format(len(data["result"])))
        for item in data["result"]:
            print(item["full_url"])


if __name__ == '__main__':
    taskList = [
{"name":"周末画报_新闻频道-热点", "enterUrl": "http://news.modernweekly.com/hots", "siteId": "1202953", "interval": "30", "template": ["23664",	"23667",]},
{"name":"周末画报_财富频道-财富", "enterUrl": "http://business.modernweekly.com/lead", "siteId": "1202973", "interval": "30", "template": ["23664",	"23667",]},
{"name":"Esquire时尚先生网-首页", "enterUrl": "http://www.esquire.com.cn/", "siteId": "1202974", "interval": "30", "template": ["23668",	"23669",]},
{"name":"Esquire时尚先生网-这就是先生", "enterUrl": "http://www.esquire.com.cn/c/esquire/", "siteId": "1202974", "interval": "30", "template": ["23668",	"23669",]},
{"name":"Esquire时尚先生网-性感", "enterUrl": "http://www.esquire.com.cn/c/sexy/", "siteId": "1202974", "interval": "30", "template": ["23668",	"23669",]},
{"name":"Esquire时尚先生网-潮流", "enterUrl": "http://www.esquire.com.cn/c/trends/", "siteId": "1202974", "interval": "30", "template": ["23668",	"23669",]},
{"name":"GQ男士网-潮流", "enterUrl": "http://www.gq.com.cn/fashion/", "siteId": "1202975", "interval": "30", "template": ["23670",	"23671",]},
{"name":"GQ男士网-生活", "enterUrl": "http://www.gq.com.cn/living/", "siteId": "1202975", "interval": "30", "template": ["23670",	"23671",]},
{"name":"GQ男士网-话题", "enterUrl": "http://www.gq.com.cn/topic/", "siteId": "1202975", "interval": "30", "template": ["23670",	"23671",]},
{"name":"时尚芭莎-首页", "enterUrl": "http://www.bazaar.com.cn/ ", "siteId": "1202976", "interval": "30", "template": ["23672",	"23673",]},
{"name":"时尚芭莎-明星娱乐", "enterUrl": "http://star.bazaar.com.cn/ ", "siteId": "1202976", "interval": "30", "template": ["23672",	"23673",]},
{"name":"时尚芭莎-时装潮流", "enterUrl": "http://fashion.bazaar.com.cn/ ", "siteId": "1202976", "interval": "30", "template": ["23672",	"23673",]},
{"name":"时尚芭莎-美容造型", "enterUrl": "http://beauty.bazaar.com.cn/", "siteId": "1202976", "interval": "30", "template": ["23672",	"23673",]},
{"name":"时尚芭莎-职场乐活", "enterUrl": "http://lifestyle.bazaar.com.cn/", "siteId": "1202976", "interval": "30", "template": ["23672",	"23673",]},
{"name":"上观-首页", "enterUrl": "https://www.jfdaily.com/home ", "siteId": "1202977", "interval": "30", "template": ["23674",	"23675",]},
{"name":"上观-政情", "enterUrl": "https://www.jfdaily.com/news/list?section=1 ", "siteId": "1202977", "interval": "30", "template": ["23674",	"23675",]},
{"name":"上观-财经 ", "enterUrl": "https://www.jfdaily.com/news/list?section=2 ", "siteId": "1202977", "interval": "30", "template": ["23674",	"23675",]},
{"name":"上观-区情 ", "enterUrl": "https://www.jfdaily.com/news/list?section=35 ", "siteId": "1202977", "interval": "30", "template": ["23674",	"23675",]},
{"name":"上观-城事 ", "enterUrl": "https://www.jfdaily.com/news/list?section=22 ", "siteId": "1202977", "interval": "30", "template": ["23674",	"23675",]},
{"name":"上观-文化 ", "enterUrl": "https://www.jfdaily.com/news/list?section=4 ", "siteId": "1202977", "interval": "30", "template": ["23674",	"23675",]},
{"name":"上观-天下", "enterUrl": "https://www.jfdaily.com/news/list?section=21 ", "siteId": "1202977", "interval": "30", "template": ["23674",	"23675",]},
{"name":"上观-互动", "enterUrl": "https://www.jfdaily.com/news/list?section=40 ", "siteId": "1202977", "interval": "30", "template": ["23674",	"23675",]},
{"name":"上观-活动", "enterUrl": "https://www.jfdaily.com/news/list?section=29 ", "siteId": "1202977", "interval": "30", "template": ["23674",	"23675",]},
{"name":"上观-专题", "enterUrl": "https://www.jfdaily.com/mapSpecTopic/list ", "siteId": "1202977", "interval": "1440", "template": ["23718","23719",	"23675",]},
{"name":"北国网-首页", "enterUrl": "http://liaoning.lnd.com.cn/", "siteId": "1010207", "interval": "30", "template": ["23676",	"23677",]},
{"name":"北国网-今日辽宁", "enterUrl": "http://liaoning.lnd.com.cn/jrln/index.shtml", "siteId": "1010207", "interval": "30", "template": ["23676",	"23677",]},
{"name":"北国网-重要动态", "enterUrl": "http://liaoning.lnd.com.cn/zydt/index.shtml", "siteId": "1010207", "interval": "30", "template": ["23676",	"23677",]},
{"name":"北国网-时政要闻", "enterUrl": "http://liaoning.lnd.com.cn/szyw/index.shtml", "siteId": "1010207", "interval": "30", "template": ["23676",	"23677",]},
{"name":"北国网-民生热点", "enterUrl": "http://liaoning.lnd.com.cn/msrd/index.shtml", "siteId": "1010207", "interval": "30", "template": ["23676",	"23677",]},
{"name":"北国网-社会新闻", "enterUrl": "http://liaoning.lnd.com.cn/shxw/index.shtml", "siteId": "1010207", "interval": "30", "template": ["23676",	"23677",]},
{"name":"北国网-全省各地", "enterUrl": "http://liaoning.lnd.com.cn/qsgd/index.shtml", "siteId": "1010207", "interval": "30", "template": ["23676",	"23677",]},
{"name":"大连海力网-新闻", "enterUrl": "http://www.hilizi.com/html/index/dalianxinwen/ ", "siteId": "1202981", "interval": "30", "template": ["23678",	"23679",]},
{"name":"大连海力网-大连", "enterUrl": "http://www.hilizi.com/html/index/dalianxinwen/ ", "siteId": "1202981", "interval": "30", "template": ["23678",	"23679",]},
{"name":"大连海力网-24小时", "enterUrl": "http://www.hilizi.com/html/index/focus_top/ ", "siteId": "1202981", "interval": "30", "template": ["23678",	"23679",]},
{"name":"大连海力网-公益大连", "enterUrl": "http://www.hilizi.com/html/index/economic/ ", "siteId": "1202981", "interval": "30", "template": ["23678",	"23679",]},
{"name":"大连海力网-社区", "enterUrl": "http://www.hilizi.com/html/index/shequ/ ", "siteId": "1202981", "interval": "30", "template": ["23678",	"23679",]},
{"name":"大连海力网-专题", "enterUrl": "http://www.hilizi.com/html/index/forum/ ", "siteId": "1202981", "interval": "1440", "template": ["23720","23723",	"23679",]},
{"name":"大连海力网-娱乐", "enterUrl": "http://www.hilizi.com/html/index/yule/ ", "siteId": "1202981", "interval": "30", "template": ["23678",	"23679",]},
{"name":"大连海力网-体育", "enterUrl": "http://www.hilizi.com/html/index/tiyu/ ", "siteId": "1202981", "interval": "30", "template": ["23678",	"23679",]},
{"name":"ZAKER新闻_APP-大连", "enterUrl": "http://app.myzaker.com/index.php?app_id=10192 ", "siteId": "1004913", "interval": "30", "template": ["23680",	"20683",]},
{"name":"新闻晨报-时政", "enterUrl": "http://www.shxwcb.com/category/shizheng", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报-要闻", "enterUrl": "http://www.shxwcb.com/category/event/yaowen", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报-中国", "enterUrl": "http://www.shxwcb.com/category/event/zhongguo", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报-国际", "enterUrl": "http://www.shxwcb.com/category/event/guoji", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报-城事", "enterUrl": "http://www.shxwcb.com/category/live/chengshi", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报-吐槽", "enterUrl": "http://www.shxwcb.com/category/live/tucao", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报-公益", "enterUrl": "http://www.shxwcb.com/category/live/gongyi", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报-健康", "enterUrl": "http://www.shxwcb.com/category/health/yiyao", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报-食安", "enterUrl": "http://www.shxwcb.com/category/health/shian", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报教育频道-首页", "enterUrl": "http://shxwcbjy.com/", "siteId": "1202983", "interval": "30", "template": ["23683",	"23684",]},
{"name":"新闻晨报-升学", "enterUrl": "http://www.shxwcb.com/category/teach/shengxue", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报-亲子", "enterUrl": "http://www.shxwcb.com/category/teach/qinzi", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报-文艺", "enterUrl": "http://www.shxwcb.com/category/wenti/wenyi", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报-体育", "enterUrl": "http://www.shxwcb.com/category/wenti/tiyu", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报-理财", "enterUrl": "http://www.shxwcb.com/category/finance/licai", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报-科技", "enterUrl": "http://www.shxwcb.com/category/finance/keji", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报-地产", "enterUrl": "http://www.shxwcb.com/category/finance/dichan", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报-去处", "enterUrl": "http://www.shxwcb.com/category/trip/quchu", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报-民宿", "enterUrl": "http://www.shxwcb.com/category/trip/minsu", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报-穿越", "enterUrl": "http://www.shxwcb.com/category/trip/chuanyue", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报-乐活", "enterUrl": "http://www.shxwcb.com/category/life/lehuo", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报-好物", "enterUrl": "http://www.shxwcb.com/category/life/haowu", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报-时尚", "enterUrl": "http://www.shxwcb.com/category/life/shishang", "siteId": "1202982", "interval": "30", "template": ["23681",	"23682",]},
{"name":"新闻晨报-专题", "enterUrl": "http://www.shxwcb.com/category/zhuanti", "siteId": "1202982", "interval": "1440", "template": ["23724","23726",	"23682",]},
{"name":"新闻晨报电子报-电子报", "enterUrl": "http://epaper.zhoudaosh.com/html/2019-02/26/node_3464.html", "siteId": "1203088", "interval": "1440", "template": ["23736","23733",	"23736",]},
{"name":"城视网_壹深圳-推荐", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=6552&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-政闻", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=5352&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-热心一壶", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=7032&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-民心桥", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=4834&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-光明区", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=9155&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-安全", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=6664&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-第一现场", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=4831&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-健康", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=10307&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-直播港澳台", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=4832&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-深圳卫视", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=6487&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-深视体育", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=7089&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-剧透社", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=7765&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-生活", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=4833&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-创财经", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=7769&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-娱乐", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=6495&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-乐活", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=9986&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-食客准备", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=7773&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-粤深圳", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=7418&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-先锋898", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=10135&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-全民大汽车", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=7745&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-大美深圳", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=7818&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-龙岗", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=8261&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-盐田", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=10255&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"城视网_壹深圳-最新", "enterUrl": "https://api.scms.sztv.com.cn:8443/api/com/article/getArticleList?tenantId=ysz&catalogId=9830&page=1&banner=1", "siteId": "1202985", "interval": "30", "template": ["23685",	"23696",]},
{"name":"荔枝网-时政", "enterUrl": "http://www.gdtv.cn/politics/", "siteId": "1202991", "interval": "30", "template": ["23698",	"23697",]},
{"name":"荔枝网-社会", "enterUrl": "http://www.gdtv.cn/local/", "siteId": "1202991", "interval": "30", "template": ["23698",	"23697",]},
{"name":"荔枝网-国际", "enterUrl": "http://www.gdtv.cn/world/", "siteId": "1202991", "interval": "30", "template": ["23698",	"23697",]},
{"name":"荔枝网-科技", "enterUrl": "http://www.gdtv.cn/tech/", "siteId": "1202991", "interval": "30", "template": ["23698",	"23697",]},
{"name":"荔枝网-体育", "enterUrl": "http://www.gdtv.cn/sports/", "siteId": "1202991", "interval": "30", "template": ["23698",	"23697",]},
{"name":"荔枝网-财经", "enterUrl": "http://www.gdtv.cn/finance/", "siteId": "1202991", "interval": "30", "template": ["23698",	"23697",]},
{"name":"荔枝网-军事", "enterUrl": "http://www.gdtv.cn/mil/", "siteId": "1202991", "interval": "30", "template": ["23698",	"23697",]},
{"name":"荔枝网-文娱", "enterUrl": "http://www.gdtv.cn/ent/", "siteId": "1202991", "interval": "30", "template": ["23698",	"23697",]}]

    taskList = [{"name": "每经网-首页", "enterUrl": "http://www.nbd.com.cn/", "siteId": "1203251", "interval": "30", "template": [23749,	23750]},
{"name": "每经网-宏观", "enterUrl": "http://economy.nbd.com.cn/", "siteId": "1203251", "interval": "30", "template": [23749,	23750]},
{"name": "每经网-金融", "enterUrl": "http://finance.nbd.com.cn/", "siteId": "1203251", "interval": "30", "template": [23749,	23750]},
{"name": "每经网-公司", "enterUrl": "http://industry.nbd.com.cn/", "siteId": "1203251", "interval": "30", "template": [23749,	23750]},
{"name": "每经网-券商", "enterUrl": "http://stocks.nbd.com.cn/", "siteId": "1203251", "interval": "30", "template": [23749,	23750]},
{"name": "每经网-新文化", "enterUrl": "http://movie.nbd.com.cn/", "siteId": "1203251", "interval": "30", "template": [23749,	23750]},
{"name": "每经网-未来商业", "enterUrl": "http://tmt.nbd.com.cn/", "siteId": "1203251", "interval": "30", "template": [23749,	23750]},
{"name": "每经网-国际", "enterUrl": "http://world.nbd.com.cn/", "siteId": "1203251", "interval": "30", "template": [23749,	23750]},
{},
{"name": "每经网_粉巷财经-首页", "enterUrl": "http://fx.nbd.com.cn/", "siteId": "1203252", "interval": "30", "template": [23751,	23752]},
{"name": "每经网-智库", "enterUrl": "http://ntt.nbd.com.cn/", "siteId": "1203251", "interval": "30", "template": [23749,	23750]},
{"name": "每经网-新经济", "enterUrl": "http://www.nbd.com.cn/xinsanban", "siteId": "1203251", "interval": "30", "template": [23749,	23750]},
{"name": "上海证券报-首页", "enterUrl": "http://www.cnstock.com/", "siteId": "1203253", "interval": "30", "template": [23753,	23754]},
{"name": "上海证券报-要闻", "enterUrl": "http://news.cnstock.com/", "siteId": "1203253", "interval": "30", "template": [23753,	23754]},
{"name": "上海证券报-产业", "enterUrl": "http://news.cnstock.com/industry", "siteId": "1203253", "interval": "30", "template": [23753,	23754]},
{"name": "上海证券报-公司", "enterUrl": "http://company.cnstock.com/", "siteId": "1203253", "interval": "30", "template": [23753,	23754]},
{"name": "上海证券报-市场", "enterUrl": "http://stock.cnstock.com/", "siteId": "1203253", "interval": "30", "template": [23753,	23754]},
{"name": "上海证券报-新三板", "enterUrl": "http://jrz.cnstock.com/", "siteId": "1203253", "interval": "30", "template": [23753,	23754]},
{"name": "证券日报网-首页", "enterUrl": "http://www.zqrb.cn/", "siteId": "1203254", "interval": "30", "template": [23755,	23756]},
{"name": "证券日报网-财经", "enterUrl": "http://www.zqrb.cn/finance/index.html", "siteId": "1203254", "interval": "30", "template": [23755,	23756]},
{"name": "证券日报网-市场", "enterUrl": "http://www.zqrb.cn/stock/index.html", "siteId": "1203254", "interval": "30", "template": [23755,	23756]},
{"name": "证券日报网-金融", "enterUrl": "http://www.zqrb.cn/jrjg/index.html", "siteId": "1203254", "interval": "30", "template": [23755,	23756]},
{"name": "证券日报网-产经", "enterUrl": "http://www.zqrb.cn/gscy/index.html", "siteId": "1203254", "interval": "30", "template": [23755,	23756]},
{"name": "广东新周刊杂志社-首页", "enterUrl": "http://www.neweekly.com.cn/", "siteId": "1203255", "interval": "30", "template": [23759,	23759]},
{},
{"name": "广东新周刊杂志社-新媒体", "enterUrl": "http://www.neweekly.com.cn/newmedia", "siteId": "1203255", "interval": "30", "template": [23759,	23759]},
{"name": "上海广播电视台-首页", "enterUrl": "https://www.smg.cn/review/index.html", "siteId": "1203256", "interval": "30", "template": [23760,	23761]},
{"name": "看看新闻网-首页", "enterUrl": "http://www.kankanews.com/", "siteId": "140785", "interval": "30", "template": [23763,	22380]},
{"name": "上海广播电视台-广而告知", "enterUrl": "https://www.smg.cn/review/news_list_9/index_1.html", "siteId": "1203256", "interval": "30", "template": [23760,	23761]},
{},
{"name": "北京广播网-首页", "enterUrl": "http://www.rbc.cn/", "siteId": "139331", "interval": "30", "template": [6047,	23764]},
{"name": "北京时间-首页", "enterUrl": "https://www.btime.com/", "siteId": "140623", "interval": "30", "template": [23765,	23766]},
{"name": "北广网-首页", "enterUrl": "http://www.bgtv.com.cn/", "siteId": "1203267", "interval": "30", "template": [23767,	23768]},
{},]
    buildListTask(taskList)
    # buildNavTemplate(1202953, ["http://news.modernweekly.com/hots"])
    # print("[{\"inputKey\":\"_html_\",\"outputKey\":\"\",\"type\":\"selector\",\"exp\":\"\",\"attr\":\"\",\"script\":\"\",\"func\":\"\"}]")
    # https?://(www\\.)?news\\.modernweekly\\.com/\\w+/\\d+$
    # buildContentTemplate(1202953, ["http://news.modernweekly.com/hots/29774"])
    # "http://www.shxwcb.com/category/\w+(/\w+)?"

    kwargs = {
        "site_url": "http://www.nbd.com.cn/",
        "nav_url": "http://movie.nbd.com.cn/",
        "cont_url": "http://www.nbd.com.cn/articles/2019-03-01/1305408.html",
        "nav_regex": "http://(.*?).nbd.com.cn/(\w+)?$",
        "content_regex": "http://www.nbd.com.cn/articles/\d+-\d+-\d+/\d+.html"
    }
    kwargs = {
        "site_id": "1203252",
        # "site_url": "http://www.nbd.com.cn/",
        "nav_url": "http://fx.nbd.com.cn/",
        "nav_regex": "http://fx.nbd.com.cn/$",
        "cont_url": "http://fx.nbd.com.cn/articles/2019-02-28/1305017.html",
        "content_regex": "http://fx.nbd.com.cn/articles/\d+-\d+-\d+/\d+.html"
    }
    kwargs = {
        # "site_id": "1203252",
        "site_url": "http://www.cnstock.com/",
        "nav_url": "http://www.cnstock.com/",
        "nav_regex": "http://(.*?).cnstock.com/(\w+)?$",
        "cont_url": "http://news.cnstock.com/news,bwkx-201903-4345324.htm",
        "content_regex": "http://(.*?).cnstock.com/(\w+/){1,2}\d+/\d+.htm|http://news.cnstock.com/news,\w+-\d+-\d+.htm"
    }

    kwargs = {
        "site_url": "http://www.zqrb.cn/",
        "nav_url": "http://www.zqrb.cn/",
        "nav_regex": "http://www.zqrb.cn/(\w+/index.html)?$",
        "cont_url": "http://www.zqrb.cn/jrjg/quanshang/2019-03-06/A1551805489893.html",
        "content_regex": "http://www.zqrb.cn/\w+/\w+/\d+-\d+-\d+/\w+.html"
    }

    kwargs = {
        "site_url": "http://www.neweekly.com.cn/",
        "nav_url": "http://www.neweekly.com.cn/",
        "nav_regex": "http://www.neweekly.com.cn/(\w+)?$",
        "cont_url": "http://www.neweekly.com.cn/article/107383",
        "content_regex": "http://www.neweekly.com.cn/article/\d+"
    }

    kwargs = {
        "site_url": "https://www.smg.cn/review/index.html",
        "nav_url": "https://www.smg.cn/review/index.html",
        "nav_regex": "https://www.smg.cn/review/index.html$|https://www.smg.cn/review/news_list_\d+/index_\d+.html",
        "cont_url": "https://www.smg.cn/review/201903/0164399.html",
        "content_regex": "https://www.smg.cn/review/\d+/\d+.html"
    }
    kwargs = {
        "site_url": "http://www.kankanews.com/",
        "nav_url": "http://www.kankanews.com/",
        "nav_regex": "http://www.kankanews.com/$",
        "cont_url": "http://www.kankanews.com/a/2019-03-06/0038775158.shtml?appid=465259",
        "content_regex": "http://www.kankanews.com/a/\d+-\d+-\d+/\d+.shtml\?appid=\d+"
    }
    kwargs = {
        "site_url": "http://www.bgtv.com.cn/",
        "nav_url": "http://www.bgtv.com.cn/",
        "nav_regex": "http://www.bgtv.com.cn/$",
        "cont_url": "http://www.bgtv.com.cn/bgrw/fm/11195.htm",
        "content_regex": "http://www.bgtv.com.cn/\w+/\w+/\d+.htm"
    }

    def build(site_url="", nav_url="", cont_url="", nav_regex="", content_regex="", site_id=""):
        site = buildMainSite(site_url) if not site_id else site_id
        buildNavTemplate(site, [nav_url], regex=nav_regex, match_regex=content_regex)
        buildContentTemplate(site, [cont_url], regex=content_regex)

    build(**kwargs)
    # testNavTemplate(["http://www.zqrb.cn/"], 23755)
