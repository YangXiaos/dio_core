# Author: YangXiaoShuai
# Date: 2019/10/23 11:27
# Project / File: dio_core : send_email
# Desc:
import poplib
import traceback

hostname = 'pop.gmail.com'
user = 'gygsjhobxgus@gmail.com'
passwd = 'Zyl@123456'

p = poplib.POP3_SSL(hostname)  # 与SMTP一样，登录gmail需要使用POP3_SSL() 方法，返回class POP3实例
try:
    # 使用POP3.user(), POP3.pass_()方法来登录个人账户
    p.user(user)
    p.pass_(passwd)
except poplib.error_proto as e: # 可能出现的异常
    traceback.print_exc()
    print('login failed')

