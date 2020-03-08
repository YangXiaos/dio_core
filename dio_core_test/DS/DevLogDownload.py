from typing import Union

from paramiko import SSHClient


# 指定某个文件下载
def downloadLog(ssh: SSHClient, threadId: Union[str, int], jobId: str):
    ssh.exec_command("cd /home/dota/logs/dt-whale-serv-deploy/logs/;"
                     "grep -l {} *{}*;"
                     ""
                     .format(threadId, jobId))


