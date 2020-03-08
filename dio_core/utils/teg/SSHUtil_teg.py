#!/usr/local/bin/python
# encoding:utf-8
import logging
import time

import paramiko


# 远程下载
def remote_scp(host, port, user, pwd, remote_path, save_path):
    t = paramiko.Transport((host, port))
    t.connect(username=user, password=pwd)  # 登录远程服务器
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.get(remote_path, save_path)
    t.close()


# 远程上传
def remote_put(host, port, user, pwd, remote_path, location_path):
    t = paramiko.Transport((host, port))
    t.connect(username=user, password=pwd)  # 登录远程服务器
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(location_path, remote_path)
    t.close()


#
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

    job_list = [
        "teg_google_news_20190109165331_895_53",
        "teg_google_news_20190109165328_154_62",
        "teg_google_news_20190109165323_646_11",
        "teg_google_news_20190109165315_367_93",
        "teg_google_news_20190109165144_679_3",
    ]

    tb = "dt.rhino.app.teg.common"
    job_id = "teg_google_news_20190110184324_855_60"
    OUTPUT_FILE = "teg_google_news_20190110184324_855_60.all.csv"
    condition = ""

    SQL = """select * from "{}" where "pk" like '%{}%' {}"""\
        .format(tb, job_id, condition).replace("\"", '\\"')
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
                  "sh run.sh PhoenixSQLExecutorCli -sqlFile temp.sql -resultFile {} -split ',';") \
            .format(SQL, OUTPUT_FILE)

        logging.info("execute script {}".format(script))

        output = ssh.exec_command(script)

        logging.error("output error")
        # try:
        #     logging.error(output[0].readlines())
        # except Exception as e:
        #     print(e)

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

    scp_online_kwargs = online_kwargs.copy()
    scp_online_kwargs.update({"remote_path": "/home/changshuai/rhino/dt-rhino-serv-api/target/" + OUTPUT_FILE})
    scp_online_kwargs.update({"save_path": OUTPUT_FILE})

    scp_unline_kwargs = unline_kwargs.copy()
    scp_unline_kwargs.update({"remote_path": "/home/zeus/changshuai/dt-rhino-serv-api/target/" + OUTPUT_FILE})
    scp_unline_kwargs.update({"save_path": OUTPUT_FILE})

    ssh_execute(**ssh_online_kwargs)
    remote_scp(**scp_online_kwargs)

    # for i in range(0, 12):
    # file = "dio.txt"
    # scp_online_kwargs.update({"remote_path": "/home/changshuai/rhino/dt-rhino-commons-crawlers/target/" + file})
    # scp_online_kwargs.update({"save_path": file})
    # remote_scp(**scp_online_kwargs)

    # scp_online_kwargs.update({"remote_path": "/home/changshuai/dio.py"})
    # scp_online_kwargs.update({"location_path": "/home/changshuai/PycharmProjects/dio_core/dio_core/utils/test.py"})
    # remote_put(**scp_online_kwargs)

    # file = "temp.0.html"
    # scp_online_kwargs.update({"remote_path": "/home/changshuai/" + file})
    # scp_online_kwargs.update({"save_path": file})
    # remote_scp(**scp_online_kwargs)
    #
    #
    # for i in range(0, 12):
    #     file = "temp.{}.html".format(i*10)
    #     scp_online_kwargs.update({"remote_path": "/home/changshuai/" + file})
    #     scp_online_kwargs.update({"save_path": file})
    #     remote_scp(**scp_online_kwargs)

    # file = "test.3.tmp"
    # scp_online_kwargs.update({"remote_path": "/home/changshuai/rhino/dt-rhino-commons-crawlers/target/" + file})
    # scp_online_kwargs.update({"save_path": file})
    # remote_scp(**scp_online_kwargs)