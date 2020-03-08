import chardet
import codecs

from numpy import unicode

from dio_core.utils import file_util

# text = file_util.readText("/home/changshuai/Documents/HUAWEI/华为（亚马逊评论）_changshuai_20190606.csv")
fin = codecs.open("/home/changshuai/Documents/HUAWEI/华为（亚马逊评论）_changshuai_20190606.csv", encoding='utf-8')

w = open("/home/changshuai/Documents/HUAWEI/华为（亚马逊评论）_changshuai_20190606.gbk.v3.csv", 'w')
# file2 = open("/home/changshuai/Documents/HUAWEI/华为（亚马逊评论）_changshuai_20190606.gbk.csv", "w")

s = fin.read()
w.write(bytes(s, encoding='utf-8').decode("GBK"))
# byte = unicode(s)

print()
# reader = codecs.getreader('gbk')(fin)
# writer = codecs.getwriter('gbk')(fout)
#
# data = fin.read()
# 10是最大字节数，默认值为-1表示尽可能大。可以避免一次处理大量数据
# while data:
#     writer.write(data)
# file2.close()
utf.encode("GB18030")
