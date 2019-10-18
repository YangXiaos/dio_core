import logging

import paramiko
import pymysql
from sshtunnel import SSHTunnelForwarder


class SSH(object):
    """
    ssh 工具类
    """
    ssh_user = "changshuai"
    ssh_password = "676592CCyok-"
    server = None
    con = None

    def __int__(self):
        self.server = self.get_server()
        self.server.start()

    @classmethod
    def get_server(cls):
        """获取 server"""
        server = SSHTunnelForwarder(
            ('120.31.140.132', 56000),
            ssh_username=cls.ssh_user,
            ssh_password=cls.ssh_password,
            remote_bind_address=('mysql.proxy.hdp', 3005),
            local_bind_address = ("127.0.0.1", 5555)
        )
        return server

    def __enter__(self):
        self.server = self.get_server()
        self.server.start()
        return self.server

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.server.close()


class DB(object):

    def __init__(self, isOnline):
        if isOnline:
            self.server = SSH.get_server()
            self.server.start()
            self.connection = DB.get_v3(self.server)
            self.cur = self.connection.cursor()
        else:
            self.server = None
            self.connection = DB.get_rhino()
            self.cur = self.connection.cursor()

    def __enter__(self):
        return self.cur

    def __exit__(self, *other):
        self.cur.close()
        self.connection.close()
        if self.server is not None:
            self.server.close()

    @classmethod
    def get_rhino(cls):
        return pymysql.connect("devrhino1", "rhino", "rhino", "db_datatub_rhino",
                                 port=3306, cursorclass=pymysql.cursors.DictCursor, charset='utf8')

    @classmethod
    def get_v3(cls, server):
        return pymysql.connect( user='rhino', passwd='rhino', host="127.0.0.1", db='db_datatub_rhino_v3',
                                port=server.local_bind_port, cursorclass=pymysql.cursors.DictCursor, charset='utf8')


class SSHConnection(object):

    def __init__(self, host="", port="", user="", pwd=""):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, user, pwd)
        logging.info("connect host:[{}][{}]".format(host, port))
        self.ssh = ssh

    def __enter__(self):
        return self.ssh

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ssh.close()


if __name__ == '__main__':
    with SSH() as server:
        print(server.is_active)

