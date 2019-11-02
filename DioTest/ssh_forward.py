# Author: YangXiaoShuai
# Date: 2019/10/31 15:14
# Project / File: dio_core : ssh_forward 
# Desc:  


from sshtunnel import SSHTunnelForwarder


ssh_user = "root"  # ldap账号，用于登录跳板机
ssh_password = "676592ccyok"  # ldap密码， 用于登录跳板机

server = SSHTunnelForwarder(('120.78.137.207', 22), ssh_username=ssh_user, ssh_password=ssh_password,
                            remote_bind_address=('127.0.0.1', 8080), local_bind_address=('127.0.0.1', 8080))
server.start()
