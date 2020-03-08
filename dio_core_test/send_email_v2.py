# Author: YangXiaoShuai
# Date: 2019/10/23 11:27
# Project / File: dio_core : send_email
# Desc:
import poplib
import re
from email.header import decode_header
from email.parser import Parser
from email.utils import parseaddr


#解析消息头中的字符串
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

#将邮件附件或内容保存至文件
#即邮件中的附件数据写入附件文件
def savefile(file_name, data, path):
    try:
        file_path = path + file_name
        print('Save as: ' + file_path)
        f = open(file_path, 'wb')
    except:
        print(file_path + ' open failed')
        #f.close()
    else:
        f.write(data)
        f.close()

#获取邮件的字符编码，首先在message中寻找编码，如果没有，就在header的Content-Type中寻找
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos+8:].strip()
    return charset

#解析邮件的函数，首先打印收件人、发件人、标题
#然后调用message的walk循环处理邮件中的每一个子对象（包括文本、html、附件一次或多次）
#邮件头属性中的file_name存在则该子对象是附件，对附件名称进行编码并将附件下载到指定目录
#由于网络上传输的邮件都是编码以后的格式，需要在get_payload的时候指定decode=True来转换成可输出的编码
#如果邮件是text或者html格式，打印格式并输出转码以后的子对象内容
def print_info(msg):
    for header in ['From', 'To', 'Subject']:
        value = msg.get(header, '')
        if value:
            if header == 'Subject':
                value = decode_str(value)
            else:
                hdr, addr = parseaddr(value)
                name = decode_str(addr)
                value = name + ' < ' + addr + ' > '
        print(header + ':' + value)


# email = "developer@zhaoyl.com"
# password = "Zdev#7yl86"
# pop3_server = "pop.qiye.aliyun.com"

email = 'fghjrtyucvbn876444@gmail.com'
password = 'Zyl@123456'
pop3_server = 'pop.gmail.com'
mypath = ''

server = poplib.POP3_SSL(pop3_server)
server.user(email)
server.pass_(password)
print('Message: %s. Size: %s' % server.stat())

resp, mails, objects = server.list()
index = len(mails)

# 取出某一个邮件的全部信息
resp, lines, octets = server.retr(index)


#邮件取出的信息是bytes，转换成Parser支持的str
lists = []
for e in lines:
    lists.append(e.decode())
msg_content = ''.join(lists)
msg = Parser().parsestr(msg_content)
# print(msg_content)
print(re.search("is (\d*). For enquire", msg_content).group(1))

#server.dele(index)
#提交操作信息并退出
server.quit()
