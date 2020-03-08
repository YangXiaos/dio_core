import functools
import logging
import traceback

from itertools import zip_longest
from dio_core.utils.teg.SSHUtil import ssh_execute
from DioTest.DS import Config


devFuc = functools.partial(ssh_execute, **Config.UNLINE_DEVRHINO1_KWARGS)


def devRestart(group="full", branch="test"):
    def handle(ssh):
        script = (("source /etc/profile; /home/dota/changshuai/update_crawler.sh {} {}".format(group, branch)))
        logging.info("execute script {}".format(script))
        chain = ssh.invoke_shell()
        chain.send(script + '\n')
        while True:
            try:
                output = chain.recv(9720).decode("utf8")
                print(output, end="")
                # if "dota@devrhino1" in output:
                #     break
                if "/var/spool/mail/dota" in output:
                    break

            except Exception as e:
                traceback.print_exc()
                break

    devFuc(handle=handle)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format="[%(asctime)s]-[%(name)s]-[%(levelname)s]: %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")




    # devRestart(group="incrMonitor", branch="test")
