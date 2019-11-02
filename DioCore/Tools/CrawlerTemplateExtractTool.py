from DioCore.Utils import TextUtil, UrlUtil


postData = """
Map<String, Object> postData = new HashMap<>();
{}
"""


class ExtractTool(object):
    """
    抽取工具
    """
    def __init__(self, text):
        self.text = text

    def extractDetail(self):
        split = self.text.split("\n\n")
        body = ""

        # 协议分裂
        if len(split) == 1:
            agreement = split[0]
        elif len(split) == 2:
            agreement, body = split
        else:
            raise Exception("异常协议体！！！")

        # headers
        lines = agreement.split("\n")
        relativeUrl = TextUtil.getFirstMatch(lines[0], "[GET|POST] (.*?) HTTP/\d.\d").replace("amp; ", "")
        headers = {}

        # # post
        # postMapping = {}
        # for tup in body.split("&"):
        #     field, value = tup.split("=")
        #     postMapping.update({field: UrlUtil.unquote(value)})

        for line in lines[1:]:
            headerName, headerVal = line.split(": ")
            headers[headerName] = headerVal.replace('"', '\\\"').strip()

        return {
            "url": "http://{}{}".format(headers["Host"], relativeUrl),
            "headers": headers,
            # "post": postMapping
        }

    def printTemplate(self):
        detail = self.extractDetail()
        headersText = "\n".join(["downloader.getDownloadSetting().getHeaders().put(\"{}\", \"{}\");".format(key, val) for key, val in detail["headers"].items()])
        postBody = postData.format("\n".join(["""postData.put("{}", "{}");""".format(field, value) for field, value in detail["post"].items()]))

        print("""
List<Message> ret = new ArrayList<>();
CommonDownloader downloader = new CommonDownloader(new DownloadSetting());
downloader.getDownloadSetting().setOpenProxy(true);
{headers}
{post}
String html = downloader.processUrl("{url}");
""".format(**{"headers": headersText, "url": detail["url"], "post": postBody}))

    def printPythonTemplate(self):
        detail = self.extractDetail()

        headersText = "\n".join(["setting.headers[\"{}\"] = \"{}\"".format(key, val.replace('"', '\"')) for key, val in detail["headers"].items()])

        # postDataText = """\npostData = {}\n""" + "\n".join(["postData[\"{}\"] = \"{}\"".format(field, value.replace("\"", "\\\"")) for field, value in detail["post"].items()])
        print("""

setting = Setting()
{headers}
downloader = Downloader(setting=setting)
downloader.get("{url}")
""".format(**{"url": detail["url"], "headers": headersText}))


if __name__ == '__main__':
    text_ = """GET https://detail.m.tmall.com/item.htm?id=539420474226&ali_trackid=2:mm_113567256_12244709_63774409:1570688047_156_649487662&e=yuR4VWGhnPVZ4n0e03qrklW8hb0G-vE1wVg8v5vEluAv6MXsAPDA3MhDgPU1n4WFEEEqFLZR5mioHPcCZPGnw9ZGToH9SulvPVl9F_szcremHmLFx92Exl4lcZi5IzC39hEgZRSkBKNGzXgVSi7qUN_d9JcqiOB2NJ5dGX5kS8HhihfKUUKNOhqiFKxmsrJJv9FbCnVozLjl6LvVq-de2PhYQxVxy5FKNBtF-bRPmqHCMFzrESockg_bbsAXrYop_O1SGq3JV13U4vk3CD6Efmk0R1_mWGRdzdsb64jzmUQSsfMxQGGtL3oYf4_GIfqN6PLvaBtL_KcQhLuJYpg5pUM8AxvU817Bd96MsKEJpWMDRb1Etzp3Lw&type=2&tk_cps_param=113567256&tkFlag=0&tk_cps_ut=2 HTTP/1.1
Host: detail.m.tmall.com
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: https://s.click.taobao.com/t_js?tu=https%3A%2F%2Fs.click.taobao.com%2Ft%3Fe%3Dm%253D2%2526s%253DCCc8t1ny7%252B0cQipKwQzePOeEDrYVVa64yK8Cckff7TVRAdhuF14FMQmXVQ2yl4YX5x%252BIUlGKNpVadRz5j%252FuZu60cGZm22H2%252FKdV2K2IzJSK18D%252FE1TAQKHbOdFtc4uDS06qvb4lce%252B8uFtjdCU9sOUnXCBD8lICzehh%252Fj8Yh%252Bo0vynyZqoK2AH1rFI2aA%252BUQGIOpZxOu46AFM10XmhqFZX%252FwZgjJWHDAgj5DY%252BVAJJSiZ%252BQMlGz6FQ%253D%253D%26union_lens%3DlensId%3A0bb0d4fb_0ccb_16d7541e486_1eca%26ref%3D%26et%3DV1liFQ9UQyTWKTcvEovoSIjJ0ENnWxBu
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,en-US;q=0.9
Cookie: cna=FR0lFrl6Ri4CAdoUB1VJl4y3; t=6ceacf14fb12b2bf2e1c5f0fff6d36b4; _tb_token_=5d138371aae89; cookie2=1250444c9e536ed0969ecd180eb6f81a; _m_h5_tk=612b440ae060f15c9847a81f14b81037_1570697207359; _m_h5_tk_enc=e60cab3b8621c8fb48a254f91e3818d9; isg=BFdXfBNLxjA5j0K8tq98ayn87clhNDS8FRUBNqmEciaN2HYasW3PTjf5Px7hHAN2; tkmb=e=yuR4VWGhnPVZ4n0e03qrklW8hb0G-vE1wVg8v5vEluAv6MXsAPDA3MhDgPU1n4WFEEEqFLZR5mioHPcCZPGnw9ZGToH9SulvPVl9F_szcremHmLFx92Exl4lcZi5IzC39hEgZRSkBKNGzXgVSi7qUN_d9JcqiOB2NJ5dGX5kS8HhihfKUUKNOhqiFKxmsrJJv9FbCnVozLjl6LvVq-de2PhYQxVxy5FKNBtF-bRPmqHCMFzrESockg_bbsAXrYop_O1SGq3JV13U4vk3CD6Efmk0R1_mWGRdzdsb64jzmUQSsfMxQGGtL3oYf4_GIfqN6PLvaBtL_KcQhLuJYpg5pUM8AxvU817Bd96MsKEJpWMDRb1Etzp3Lw&iv=1&et=1570688047&tk_cps_param=113567256&tkFlag=0&tk_cps_ut=2
X-Requested-With: com.miui.personalassistant
"""
    tool = ExtractTool(text_)
    tool.printPythonTemplate()
    # print(tool.extractDetail())