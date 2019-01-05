#!/usr/local/bin/python
# encoding:utf-8
import logging
import time

import paramiko


# 远程下载
def remote_scp(host, port, user, pwd, remote_path, save_path):
    t = paramiko.Transport((host, port))
    t.connect(username=user, password=pwd)  # 登录远程服务器

    # sftp传输协议
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.get(remote_path, save_path)
    t.close()


def ssh_execute(host, port, user, pwd, handle):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, user, pwd)
    logging.info("connect host:[{}][{}]".format(host, port))
    # 处理函数
    handle(ssh)
    ssh.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format="[%(asctime)s]-[%(name)s]-[%(levelname)s]: %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")

    tb = "dt.other.muying.common"
    job_id = "app_test_20181230154742_074_9"

    OUTPUT_FILE = "muyin.baby.bbs1.csv"
    SQL = """select * from "{}" where "pk" like '%{}%' and "publish_date" < '20180910000000'""".replace("\"", '\\"').format(tb, job_id)
    # SQL = """select * from "dt.rhino.app.yili_ecomm_cmt_v2" where "site"in ('亚马逊', 'Jet', '沃尔玛') and "keyword" in ('dextran','oat','Corn','Ramulus mori','Fennel','Morinda officinalis','Red deer bone') """.replace("\"", '\\"')

    def unline_handle(ssh):
        script = ("cd /home/zeus/changshuai/dt-rhino-serv-api/target;"
                  "echo \"{}\" > temp.sql;"
                  "sh run.sh PhoenixSQLExecutorCli -sqlFile temp.sql -resultFile {} -split ',';"
                  "rm temp.sql;") \
            .format(SQL, OUTPUT_FILE)

        logging.info("execute script {}".format(script))
        output = ssh.exec_command(script)

        logging.error("output error")
        # logging.error(output[0].readlines())

        logging.info("get output")
        logging.info("".join(output[1].readlines()))


    def online_handle(ssh):

        script = ("cd /home/changshuai/rhino/dt-rhino-serv-api/target;"
                  "echo \"{}\" > temp.sql;"
                  "sh run.sh PhoenixSQLExecutorCli -sqlFile temp.sql -resultFile {} -split ',';"
                  "rm temp.sql;") \
            .format(SQL, OUTPUT_FILE)

        logging.info("execute script {}".format(script))

        output = ssh.exec_command(script)

        logging.error("output error")
        logging.error(output[0].readlines())

        logging.info("get output")
        for line in output[1].readlines():
            print(line.strip())

    online_kwargs = {
        "host": "121.46.23.216",
        "port": 56000,
        "pwd": "676592CCyok-",
        "user": "changshuai",
    }

    unline_kwargs = {
        "host": "dev1",
        "port": 22,
        "pwd": "data123$%^",
        "user": "zeus",
    }

    ssh_online_kwargs = online_kwargs.copy()
    ssh_online_kwargs.update({"handle": online_handle})

    ssh_unline_kwargs = unline_kwargs.copy()
    ssh_unline_kwargs.update({"handle": unline_handle})

    ssh_execute(**ssh_unline_kwargs)
    scp_online_kwargs = online_kwargs.copy()
    scp_online_kwargs.update({"remote_path": "/home/changshuai/rhino/dt-rhino-serv-api/target/" + OUTPUT_FILE})
    scp_online_kwargs.update({"save_path": OUTPUT_FILE})

    scp_unline_kwargs = unline_kwargs.copy()
    scp_unline_kwargs.update({"remote_path": "/home/zeus/changshuai/dt-rhino-serv-api/target/" + OUTPUT_FILE})
    scp_unline_kwargs.update({"save_path": OUTPUT_FILE})

    remote_scp(**scp_unline_kwargs)
