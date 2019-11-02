import poplib
import smtplib
from email.mime.text import MIMEText
from email.parser import Parser

DEFAULT_EMAIL_CONFIG = {
    "host": "smtp.qiye.aliyun.com",
    "port": 465,
    "user": "developer@zhaoyl.com",
    "password": "Zdev#7yl86"
}


# DEFAULT_EMAIL_CONFIG = {
#     "host": "smtp.qq.com",
#     "port": 465,
#     "user": "178069857@qq.com",
#     "password": "dazqeiimlmzkcbbd"
# }
msg_to = '178069857@qq.com'  # 收件人邮箱

#
# # 发送邮件
# def sendEmail(to: str, text: str, email_config=None, subject: str = "这是来自 dio 的邮件") -> None:
#
#     if email_config is None:
#         email_config = DEFAULT_EMAIL_CONFIG
#     smpt = smtplib.SMTP_SSL(email_config["host"], email_config["port"])
#     smpt.login(email_config["user"], email_config["password"])
#
#     msg = MIMEText(text)
#     msg['Subject'] = subject
#     msg['From'] = email_config["user"]
#     msg['To'] = to
#     smpt.sendmail(email_config["user"], to, msg.as_string())
#     print("发送成功")


def getEmail():
    email = "developer@zhaoyl.com"
    password = "Zdev#7yl86"
    pop3_server = "pop.qiye.aliyun.com"

    server = poplib.POP3(pop3_server, 110)
    server.set_debuglevel(1)
    server.user(email)
    server.pass_(password)

    resp, mails, octets = server.list()
    print(mails)

    index = len(mails)
    resp, lines, octets = server.retr(index)

    msg_content = b''.join(lines).decode('utf-8')
    msg = Parser().parsestr(msg_content)

    server.quit()
    print(msg_content)  # 注册内容，是html格式的话要格式化一下


if __name__ == '__main__':
    getEmail()
