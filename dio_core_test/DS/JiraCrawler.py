import time
import traceback

from dio_core.network.downloader.downloader import Downloader
from dio_core.network.downloader.downloader import Setting
from dio_core.utils import file_util, parse_util, json_util
from dio_core_test.utils import text_util

setting = Setting()
setting.headers["Cookie"] = ("DSCKID=91aecd4c-9d62-49ad-ae1b-9eb177c787ac; JSESSIONID=5AD6666BE97FEC415491055AFAFA60FE;"
                             " seraph.rememberme.cookie=13124%3A5ad60cddb478faeca22570e7f156f07e5138011a; atlassian.xsr"
                             "f.token=BP2B-R8C4-N6CQ-HZD4_9ab65e787a0932dd3b1abcc52a792e40d154415c_lin; jira.editor.use"
                             "r.mode=wysiwyg")
setting.htmlParse = True

rows = list(file_util.readRows("/home/changshuai/PycharmProjects/dio_core/dio_core_test/Data/JIRA_LIST.txt"))

allMsg = []

for url in rows:

    try:
        res = Downloader.get(url, setting)
        repeatsText = text_util.get_first_match(res.text, "WRM._unparsedData\[\"activity-panel-pipe-id\"\]=\"(.*)\";")
        repeats = repeatsText.encode("utf-8").decode("unicode-escape").encode("utf-8").decode("unicode-escape").replace("\\/", "/")
        soup = parse_util.get_bs4_soup(repeats.strip("\""))

        [_.extract() for _ in res.soup.select_one("#description-val").select(".user-hover")]
        msgInfo = {
            "title": res.soup.select_one("#summary-val").text.strip(),
            "id": text_util.get_first_match(url, "/(CP-\d+)").strip(),
            "url": url.strip(),
            "desc": res.soup.select_one("#description-val").text.strip(),
            "type": res.soup.select_one("#type-val").text.strip()
        }

        for item in res.soup.select("#issuedetails > li.item"):
            field = item.select_one(".wrap > strong").text
            val = item.select_one(".wrap > span,.wrap > div").text
            if "优先级" in field:
                msgInfo["level"] = val.strip()
            elif "模块:" in field:
                msgInfo["model"] = val.strip()

        descList = []
        for tag in soup.select(".issue-data-block"):
            detail = tag.select_one(".action-body")
            header = tag.select_one(".action-head")

            desc = {
                "content": detail.text,
            }
            [_.extract() for _ in detail.select(".user-hover")]
            desc["contentClr"] = detail.text
            desc["author"] = header.select_one(".user-hover.user-avatar").text
            desc["date"] = header.select_one(".livestamp").text
            descList.append(desc)
        msgInfo["descList"] = descList

        allMsg.append(msgInfo)
    except Exception as e:
        print("{} 跑数异常".format(url))
        traceback.print_exc()
    finally:
        print("{} 跑数".format(url))
    time.sleep(1)

json_util.dump_python2_file(allMsg, "/home/changshuai/PycharmProjects/dio_core/output/jira.v2.json")


