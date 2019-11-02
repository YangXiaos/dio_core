import requests
from fontTools.ttLib import TTFont


# 获取ttf url
ttfUrl = "https://s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/2ef84fdd.woff"


ttfMatch = {
    str([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]): 6,
    str([1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]): 3,
    str([1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1]): 1,
    str([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]): 4,
    str([1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]): 0,
    str([1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]): 5,
    str([1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0]): 8,
    str([1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0]): 9,
    str([1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1]): 2,
    str([1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1]): 7,
}
# decrypt = decrypt_collection.find_one({"_id": 1})["match"]


fileName = ttfUrl.split("/")[-1]
match = {}

# 获取ttf 文件
res = requests.get(ttfUrl)
with open(fileName, "wb") as file:
    file.write(res.content)

# ttf 文件解析
font = TTFont(fileName)
font.get("glyf")
font.getTableData("glyf")

for key in font["glyf"].glyphs:
    f = font["glyf"].glyphs[key]
    if not hasattr(f, "flags"):
        continue
    if str(f.flags.tolist()) in ttfMatch:
        match[key.lower().replace("uni", "&#x") + ";"] = str(ttfMatch[str(f.flags.tolist())])

# 粘贴到system_config 表
print("'{}': {}".format(fileName.split(".")[0], match))
