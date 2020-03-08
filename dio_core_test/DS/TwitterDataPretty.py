from dio_core.utils import json_util, parse_html_util

python = json_util.get_python_from_file("/home/changshuai/PycharmProjects/dio_core/Test/Data/twitter_post.json")

soup = parse_html_util.parse(python["page"])
print(soup.text)