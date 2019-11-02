from DioCore.Utils import JsonUtil, HtmlParseUtil

python = JsonUtil.getPythonFromFile("/home/changshuai/PycharmProjects/dio_core/Test/Data/twitter_post.json")

soup = HtmlParseUtil.parse(python["page"])
print(soup.text)