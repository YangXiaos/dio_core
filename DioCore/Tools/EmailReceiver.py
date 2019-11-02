import sys

from imapclient import IMAPClient

user = "vrfghytserh3710@gmail.com"
password = "Zyl@123456"

c = IMAPClient('imap.gmail.com', ssl= True)
try:
    c.login(user, password) #登录个人帐号
except c.Error:
    print('Could not log in')
    sys.exit(1)
