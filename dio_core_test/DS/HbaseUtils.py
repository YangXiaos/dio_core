import logging

from DioTest.DS import DBUtil


class SQLExecutor(object):
    """
    execute hbase sql
    """
    def __init__(self, host="", port="", user="", pwd=""):
        self.sshConnection = DBUtil.SSHConnection(host, port, user, pwd)

    def execute(self, sql):
        return self.sshConnection.ssh.exec_command(sql)

    def __del__(self):
        self.sshConnection.ssh.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format="[%(asctime)s]-[%(name)s]-[%(levelname)s]: %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")

    online_kwargs = {
        "host": "120.31.140.132",
        "port": 56000,
        "pwd": "676592CCyok-",
        "user": "changshuai",
    }

    unline_kwargs = {
        "host": "dev2",
        "port": 22,
        "pwd": "676592CCyok-",
        "user": "changshuai",
    }


    def online_execute(sql="", is_online=True):
        script = ("source /etc/profile;"
                  "cd /home/changshuai/rhino/dt-rhino-serv-api-phoenix/target/;"
                  "java -cp dt-rhino-serv-api-3.2.68-SNAPSHOT-jar-with-dependencies.jar "
                  "com.datatub.rhino.api.cli.hbase.PhoenixSQLExecuteCLi -sql '{}' ").format(sql)
        executor = SQLExecutor(**online_kwargs) if is_online else SQLExecutor(**unline_kwargs)
        logging.info("execute sql {}".format(script))
        output = executor.execute(script)

        for line in output[1].readlines():
            print(line)
        try:
            logging.error(output[0].readlines())
        except:
            pass
        try:
            logging.info(output[2].readlines())
        except:
            pass


    def buildSQL(table_name="", field_list=[]):
        field_list.remove("pk")
        return """ create table "{}" ("pk" VARCHAR PRIMARY KEY{})"""\
            .format(table_name, "".join([""","raw"."{}"  VARCHAR""".format(field) for field in field_list]))


    drop_table_kwargs = {
            "is_online" : True,
            "sql" : """ drop table "dt.rhino.tmp.test.miao" """
    }

    create_unline_table_kwargs = {
        "is_online" : False,
        "sql" : """ create table "dt.rhino.tmp.ftp" ("pk" VARCHAR PRIMARY KEY, "raw"."file_name" VARCHAR, "raw"."item_id" VARCHAR, "raw"."url" VARCHAR, "raw"."nextDirName" VARCHAR) """
    }

    create_online_table_kwargs = {
        "is_online" : True,
        "sql" : buildSQL("dt.rhino.tmp.douyin.video", ["pk","jobName","keyword","site","uid","user_name","title","content","publish_date","author","like_count","view_count","review_count","share_count","item_id","video_id","url","thumbnail","duration_seconds","video_urls","audio_urls","challenge_list","tags","region","data_type","is_private","update_date","sourceCrawlerId"])
    }

    create_online_table_kwargs = {
        "is_online" : True,
        "sql" : buildSQL("dt.rhino.tmp.xhs.note", ["pk","jobName","keyword","unique_id","item_id","site","site_id","uid","author","full_url","url","note_type","title","content","publish_date","image_url_list","image_stickers","note_stickers","note_ats","location","like_count","collection_num","review_count","image_url","view_count","is_main_post","other_data","update_date","_data_type_","_kafka_data_type_","_track_count_","sourceCrawlerId","repost_count",])
    }

    create_online_table_kwargs = {
        "is_online" : True,
        "sql" : buildSQL("dt.rhino.tmp.xhs.cmt", ["pk","jobName","keyword","unique_id","item_id","parent_id","site","site_id","is_main_post","uid","author","full_url","url","title","content","publish_date","like_count","other_data","update_date","_data_type_","_kafka_data_type_","_track_count_","sourceCrawlerId",])
    }

    create_table_kwargs = {
        "is_online" : True,
        "sql" : """ create table "dt.rhino.tmp.twitter.post" ("pk" VARCHAR PRIMARY KEY,"raw"."shop_id" VARCHAR,"raw"."sourceCrawlerId" VARCHAR,"raw"."repost_count" VARCHAR,"raw"."like_count" VARCHAR,"raw"."tweet_id" VARCHAR,"raw"."locate_test" VARCHAR,"raw"."top_parent_twitter_id" VARCHAR,"raw"."review_count" VARCHAR,"raw"."proxy_id" VARCHAR,"raw"."display_name" VARCHAR,"raw"."url" VARCHAR,"raw"."update_date" VARCHAR,"raw"."content" VARCHAR,"raw"."is_main_post" VARCHAR,"raw"."screen_name" VARCHAR,"raw"."publish_date" VARCHAR,"raw"."keyword" VARCHAR) """
    }

    add_raw_kwargs = {
        "is_online" : True,
        "sql" : """ ALTER TABLE "dt.rhino.tmp.ftp" ADD "raw"."update_date" varchar """
    }


    online_execute(**create_online_table_kwargs)
    # online_execute(**create_online_table_kwargs)
    # online_execute(**add_raw_kwargs)



