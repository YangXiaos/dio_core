#!/usr/local/bin/python
# encoding:utf-8
import logging
import typing

import paramiko


# 远程下载
from DioCore.Utils import FileUtil, Md5Util, TextUtil
from DioCore.Utils.FileUtil import CSVUtil


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

unline_tmp_ecomm_item_tb = "dt.rhino.tmp.ecomm.item"
unline_douyin_user_detail_tb = "dt.rhino.app.radar_douyin_user"
unline_tmp_article_tb = "dt.rhino.tmp.article"
unline_tmp_ecomm_cmt_tb = "dt.rhino.tmp.ecomm.comment"
online_ipsos_comment = "dt.rhino.app.radar_data.ipsos.comment"


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
        "host": "datatub5",
        "port": 22,
        "pwd": "datatub",
        "user": "root",
    }

    # 下载数据
    def download_data(tb: str="", job_id: typing.Union[str, list]="", output_file: str="", sql: str="", is_online: bool=True,
                      condition: str="", fields="*", field_list=[], limit=""):
        if sql:
            SQL = sql.replace("\"", '\\"')
        else:
            if not condition:
                if isinstance(job_id, str):
                    condition = "\"pk\" like '%{}%'".format(job_id)
                else:
                    condition = " or ".join(["\"pk\" like '%{}%'".format(_) for _ in job_id])

            if limit:
                condition = condition + " {}".format("limit {}".format(limit))

            if field_list:
                fields = ",".join(["\"{}\"".format(field) for field in field_list ])
            SQL = sql if sql else """select {} from "{}" where {} """.format(fields, tb, condition)
            SQL = SQL.replace("\"", '\\"')

        scp_online_kwargs = online_kwargs.copy()
        scp_online_kwargs.update({"remote_path": "/home/changshuai/rhino/dt-rhino-serv-api/target/" + output_file})
        scp_online_kwargs.update({"save_path": output_file})

        scp_unline_kwargs = unline_kwargs.copy()
        scp_unline_kwargs.update({"remote_path": "/home/dota/changshuai/rhino/dt-rhino-serv-api/target/" + output_file})
        scp_unline_kwargs.update({"save_path": output_file})

        def unline_handle(ssh):
            script = ("source /etc/profile;"
                      "cd /home/dota/changshuai/rhino/dt-rhino-serv-api/target;"
                      "echo \"{}\" > temp.sql;"
                      "sh run.sh PhoenixSQLExecutorCli -sqlFile temp.sql -resultFile {} -split \',\';"
                      ) \
                .format(SQL, output_file)

            logging.info("execute script {}".format(script))
            output = ssh.exec_command(script)
            logging.info("get output")
            logging.info("".join(output[1].readlines()))

        def online_handle(ssh):
            script = ("source /etc/profile;"
                      "cd /home/changshuai/rhino/dt-rhino-serv-api/target;"
                      "echo \"{}\" > temp.sql;"
                      "sh run.sh PhoenixSQLExecutorCli -sqlFile temp.sql -resultFile {} -split ',';"
                      ) \
                .format(SQL, output_file)

            logging.info("execute script {}".format(script))
            output = ssh.exec_command(script)
            logging.info("get output")
            logging.info("".join(output[1].readlines()))

        ssh_online_kwargs = online_kwargs.copy()
        ssh_online_kwargs.update({"handle": online_handle})

        ssh_unline_kwargs = unline_kwargs.copy()
        ssh_unline_kwargs.update({"handle": unline_handle})

        if not is_online:
            ssh_execute(**ssh_unline_kwargs)
            remote_scp(**scp_unline_kwargs)
        else:
            ssh_execute(**ssh_online_kwargs)
            remote_scp(**scp_online_kwargs)


    taobao_CP_2186_kwawrgs = {
        "output_file": "app_ecomm_all_20190129183102_078_19.comment.csv",
        "tb": "dt.rhino.tmp.ecomm.comment",
        "job_id": "app_ecomm_all_20190129183102_078_19",
        "is_online": False
    }

    taobao_unline_kwawrgs = {
        "output_file": "app_ecomm_all_20190215185307_798_82.item.csv",
        "tb": "dt.rhino.tmp.ecomm.item",
        "job_id": "app_ecomm_all_20190215185307_798_82",
        "is_online": False
    }
    taobao_unline_comment_kwawrgs = {
        "output_file": "app_ecomm_all_20190215191536_941_84.item.csv",
        "tb": "dt.rhino.tmp.ecomm.item",
        "job_id": "app_ecomm_all_20190215191536_941_84",
        "is_online": False
    }

    ecomm_online_kwawrgs_1 = {
        "output_file": "app_test_20190521190227_278_43.item.csv",
        "tb": "dt.rhino.tmp.ecomm.item",
        "job_id": "app_test_20190521190227_278_43",
        "fields": "\"keyword\", \"shop\", \"url\", \"item_id\"",
        "is_online": True
    }

    ecomm_online_kwargs = {
        "output_file": "app_ecomm_all_20190618142312_916_97.item.csv",
        "tb": "dt.rhino.tmp.ecomm.item",
        "job_id": "app_ecomm_all_20190618142312_916_97",
        "is_online": True
    }

    ecomm_online_article_kwargs = {
        "output_file": "app_ecomm_all_20190618142312_916_97.item.csv",
        "tb": "dt.rhino.tmp.articlev2",
        "job_id": "app_ecomm_all_20190618142312_916_97",
        "is_online": True
    }

    ecomm_unline_comment_kwargs = {
        "output_file": "app_ecomm_all_20190826145816_561_72.comment.csv",
        "tb": "dt.rhino.tmp.ecomm.comment",
        "job_id": "app_ecomm_all_20190826145816_561_72",
        "is_online": False
    }

    ecomm_unline_douyin_user_kwargs = {
        "output_file": "changshuai_test_miaomiao_20190902111439_036_14.comment.csv",
        "tb": "dt.rhino.app.radar_douyin_user",
        "job_id": "changshuai_test_miaomiao_20190902111439_036_14",
        "is_online": False
    }

    ecomm_online_comment_kwargs = {
        "output_file": "yili_ecomm_v2_20190625141831_881_67.comment.csv",
        "tb": "dt.rhino.tmp.ecomm.comment",
        "job_id": "yili_ecomm_v2_20190625141831_881_67",
        "is_online": False
    }

    ecomm_unline_item_kwargs = {
        "output_file": "app_ecomm_all_20190808144435_794_7.item.csv",
        "tb": "dt.rhino.tmp.ecomm.item",
        "job_id": "app_ecomm_all_20190808144435_794_7",
        # "limit": "10000",
        # "fields": "\"item_url\",\"other_data\",\"sub_category\",\"category\"",
        "is_online": False
    }

    ecomm_online_item_kwargs = {
        "output_file": "app_test_20190812203737_656_50.csv",
        "tb": "dt.rhino.tmp.ecomm.item",
        "job_id": "app_test_20190812203737_656_50",
        # "fields": "\"item_url\",\"other_data\",\"sub_category\",\"category\"",
        "is_online": True
    }

    # ecomm_unline_item_kwargs = {
    #     "output_file": "app_ecomm_all_20190606145053_847_71.item.csv",
    #     "tb": "dt.rhino.tmp.ecomm.item",
    #     "job_id": "app_ecomm_all_20190606145053_847_71",
    #     "is_online": False,
    #     "fields": """ "is_main_post", "brand_name", "title", "price", "promo_price", "site", "shop_name",  "item_url", "review_count", "score" """.strip()
    # }
    ecomm_unline_item_condition_kwargs = {
        "output_file": "changshuai_test_miaomiao_20190602131823_853_8.item.csv",
        "tb": "dt.rhino.tmp.ecomm.item",
        "job_id": "changshuai_test_miaomiao_20190602131823_853_8",
        "fields": "\"pk\", \"full_url\",\"keyword\"",
        "is_online": False
    }

    ecomm_cmt_unline_kwawrgs = {
        "output_file": "app_ecomm_all_20190514174023_044_44.cmt.csv",
        "tb": "dt.rhino.tmp.ecomm.comment",
        "job_id": "app_ecomm_all_20190514174023_044_44",
        "is_online": False
    }

    google_online_kwargs_1 = {
        "output_file": "teg_google_news_20190222155643_789_63.item.csv",
        "tb": "dt.rhino.app.teg.common",
        "job_id": "teg_google_news_20190222155643_789_63",
        "is_online": True
    }
    google_unline_kwargs_1 = {
        "output_file": "teg_google_news_20190227210508_009_87.item.csv",
        "tb": "dt.rhino.app.teg.common",
        "job_id": "teg_google_news_20190227210508_009_87",
        "is_online": True
    }
    google_online_kwargs = {
        "output_file": "teg_google_news_20190225202303_644_70.item.csv",
        "tb": "dt.rhino.app.teg.common",
        "job_id": "teg_google_news_20190225202303_644_70",
        "is_online": True
    }
    ingredion_unline_kwargs = {
        "output_file": "app_test_20190221190639_725_21.item.csv",
        "tb": "dt.rhino.koubei.comment",
        "job_id": "app_test_20190221190639_725_21",
        "is_online": False
    }
    weitao_unline_comment_kwawrgs = {
        "output_file": "app_ecomm_all_20190228170105_091_38.item.csv",
        "tb": "dt.rhino.tmp.article",
        "job_id": "app_ecomm_all_20190228170105_091_38",
        "is_online": False
    }

    weitao_online_search_kwawrgs = {
        "output_file": "app_ecomm_all_20190228192543_918_94.item.csv",
        "tb": "dt.rhino.tmp.articlev2",
        "job_id": "app_ecomm_all_20190228192543_918_94",
        "is_online": True
    }

    ecomm_unline_article_kwargs = {
        "output_file": "app_ecomm_all_20190807184531_459_90.article.csv",
        "tb": "dt.rhino.tmp.article",
        "job_id": "app_ecomm_all_20190807184531_459_90",
        "is_online": False
    }

    ecomm_online_article_kwargs = {
        "output_file": "app_ecomm_all_20190711175538_546_17.article.csv",
        "tb": "dt.rhino.tmp.articlev2",
        "job_id": "app_ecomm_all_20190711175538_546_17",
        "is_online": True
    }

    test = {
        "sql": """select count(*) from "dt.rhino.app.yili_zongyi_post_v2" where "jobName" = 'yili_article_v2_20190226161030_362_13' """,
        "is_online": True,
        "output_file": "test.txt"
    }

    teg_online_search_kwargs_1 = {
        "output_file": "teg_google_news_20190305104410_005_55.item.csv",
        "tb": "dt.rhino.app.teg.common",
        "job_id": "teg_google_news_20190305104410_005_55",
        "is_online": True
    }
    teg_online_search_kwargs_2 = {
        "output_file": "teg_google_news_20190305104422_261_89.item.csv",
        "tb": "dt.rhino.app.teg.common",
        "job_id": "teg_google_news_20190305104422_261_89",
        "is_online": True
    }
    teg_online_search_kwargs_3 = {
        "output_file": "teg_google_news_20190305104431_102_25.item.csv",
        "tb": "dt.rhino.app.teg.common",
        "job_id": "teg_google_news_20190305104431_102_25",
        "is_online": True
    }

    teg_online_search_kwargs_1 = {
        "output_file": "app_test_20190305120645_517_6.item.part.csv",
        "tb": "dt.rhino.app.teg.common",
        "fields": "\"full_url\", \"url\", \"keyword\"",
        "job_id": "app_test_20190305120645_517_6",
        "is_online": True
    }
    teg_online_search_kwargs_2 = {
        "output_file": "app_test_20190305120659_172_50.item.part.csv",
        "tb": "dt.rhino.app.teg.common",
        "fields": "\"full_url\", \"url\", \"keyword\"",
        "job_id": "app_test_20190305120659_172_50",
        "is_online": True
    }
    teg_online_search_kwargs_3 = {
        "output_file": "app_test_20190305120709_824_24.item.part.csv",
        "tb": "dt.rhino.app.teg.common",
        "fields": "\"full_url\", \"url\", \"keyword\"",
        "job_id": "app_test_20190305120709_824_24",
        "is_online": True
    }

    teg_online_search_kwargs_1 = {
        "output_file": "app_test_20190305171526_201_49.item.csv",
        "tb": "dt.rhino.app.teg.common",
        "fields": "\"url\", \"keyword\", \"publish_date\"",
        "job_id": "app_test_20190305171526_201_49",
        "is_online": False
    }
    teg_online_search_kwargs_2 = {
        "output_file": "app_test_20190305120524_441_97.item.csv",
        "tb": "dt.rhino.app.teg.common",
        "fields": "\"full_url\", \"url\", \"keyword\"",
        "job_id": "app_test_20190305120524_441_97",
        "is_online": True
    }
    teg_online_search_kwargs_3 = {
        "output_file": "app_test_201903051l20535_123_45.item.csv",
        "tb": "dt.rhino.app.teg.common",
        "fields": "\"full_url\", \"url\", \"keyword\"",
        "job_id": "app_test_20190305120535_123_45",
        "is_online": True
    }

    teg_online_search_kwargs_4 = {
        "output_file": "app_test_20190313214734_812_66.item.csv",
        "tb": "dt.rhino.app.teg.common",
        "fields": "\"full_url\", \"url\", \"keyword\"",
        "job_id": "app_test_20190313214734_812_66",
        "is_online": True
    }
    xhs_online_note_kwargs = {
        "output_file": "app_ecomm_all_20190328174432_709_19.note.csv",
        "tb": "dt.rhino.app.media_radar.xhs.note_v2",
        "condition": "\"jobName\" = 'app_ecomm_all_20190328174432_709_19'",
        "is_online": True
    }
    xhs_online_comment_kwargs = {
        "output_file": "app_ecomm_all_20190328174432_709_19.comment.csv",
        "tb": "dt.rhino.app.media_radar.xhs.comment_v2",
        "condition": "\"jobName\" = 'app_ecomm_all_20190328174432_709_19'",
        "is_online": True
    }

    teg_online_search_kwargs_4 = {
        "output_file": "yy_crawler_20190322120021_670_80.item.csv",
        "tb": "dt.rhino.tmp.ecomm.item",
        "job_id": "yy_crawler_20190322120021_670_80",
        "is_online": True
    }
    taobao_unline_search_kwargs = {
        "output_file": "app_ecomm_all_20190329190540_842_7.item.csv",
        "tb": "dt.rhino.tmp.ecomm.item",
        "condition": "\"jobName\"='app_ecomm_all_20190329190540_842_7' ",
        "is_online": False
    }
    teg_online_kwargs = {
        "output_file": "app_test_20190401120208_451_37.item.csv",
        "tb": "dt.rhino.app.teg.common",
        "job_id": "app_test_20190401120208_451_37",
        "is_online": True
    }

    teg_online_search_kwargs_4 = {
        "output_file": "app_test_20190401120124_007_66.item.csv",
        "tb": "dt.rhino.app.teg.common",
        "job_id": "app_test_20190401120124_007_66",
        "is_online": True
    }

    teg_online_search_kwargs_5 = {
        "output_file": "app_ecomm_all_20190509120607_099_77.item.csv",
        "tb": "dt.rhino.app.teg.common",
        "job_id": "app_ecomm_all_20190509120607_099_77",
        "is_online": True
    }
    teg_online_search_kwargs_6 = {
        "output_file": "teg_google_news_20190515160840_969_45.item.csv",
        "tb": "dt.rhino.app.teg.common",
        "job_id": "teg_google_news_20190515160840_969_45",
        "is_online": True
    }

    taobao_unline_search_kwargs_4 = {
        "output_file": "app_ecomm_all_20190401202226_822_52.item.csv",
        "tb": "dt.rhino.tmp.taobao.tmp",
        "job_id": "app_ecomm_all_20190401202226_822_52",
        "is_online": False
    }

    yili_radar_kwargs = {
        "output_file": "yili_radar_people_20190404145346_956_46.item.csv",
        "tb": "dt.rhino.app.yili_zongyi_post_v2",
            "condition": "\"jobName\" = 'yili_radar_people_20190404145346_956_46'",
        "is_online": True
    }

    jd_comment_kwargs = {
        "output_file": "app_ecomm_all_20190520103732_404_88.comment.csv",
        "tb": "dt.rhino.tmp.ecomm.comment",
        "job_id": "app_ecomm_all_20190520103732_404_88",
        "is_online": True
    }

    tb_shop_keyword_kwargs = {
        "output_file": "app_ecomm_all_20190422180635_614_80.seed.csv",
        "tb": "dt.rhino.tmp.taobao.tmp",
        "job_id": "app_ecomm_all_20190422180635_614_80",
        "is_online": False
    }
    test_kwargs =  {
        "output_file": "yili_cmt.3.csv",
        "sql": """select count(*) from "dt.rhino.app.yili_ecomm_cmt_v2" where "publish_date" > '20190514000000' and "site"='天猫'""",
        "is_online": True
    }

    test_kwargs =  {
        "output_file": "item_id.csv",
        # "sql": """select count(distinct "review_id"), "item_id" from "dt.rhino.tmp.ecomm.comment" where "pk" like '%app_ecomm_all_20190602004131_486_28%' or "pk" like '%app_ecomm_all_20190531212317_439_31%' group by "item_id" """,
        "sql": """select "item_id", "title" from "dt.rhino.tmp.ecomm.item" where "sourceCrawlerId" = '236' limit 240000 """,
        "is_online": False
    }


    unline_tb_good_item_search = {
        "output_file": "app_ecomm_all_20190415191104_249_31.seed.csv",
        "tb": "dt.rhino.tmp.article",
        "job_id": "app_ecomm_all_20190415191104_249_31",
        "is_online": False
    }

    unline_tb_toutiao_search = {
        "output_file": "app_ecomm_all_20190416184219_971_30.article.csv",
        "tb": "dt.rhino.tmp.article",
        "job_id": "app_ecomm_all_20190416184219_971_30",
        "is_online": False
    }

    online_yili = {
        "output_file": "app_ecomm_yili_20190416161026_828_3.article.csv",
        "tb": "dt.rhino.tmp.ecomm.item",
        "job_id": "app_ecomm_yili_20190416161026_828_3",
        "is_online": True
    }
    unline_tb_article = {
        "output_file": "app_ecomm_all_20190418184452_243_56.article.csv",
        "tb": "dt.rhino.tmp.article",
        "job_id": "app_ecomm_all_20190418184452_243_56",
        "is_online": False
    }

    unline_tb_article = {
        "output_file": "app_ecomm_all_20190426104949_867_17.article.csv",
        "tb": "dt.rhino.tmp.article",
        "job_id": "app_ecomm_all_20190426104949_867_17",
        "is_online": False
    }

    online_article_article = {
        "output_file": "yili_article_v2_20190415231004_412_5.article.csv",
        "tb": "dt.rhino.tmp.yili_zongyi_post_v2",
        "condition": """ "site" = '芒果TV' and "update_date" > '20190415000000' """,
        "is_online": True
    }

    online_philips_comment_kwargs = {
        "output_file": "philips_jd.comments.csv",
        "tb": "dt.rhino.app.radar_data.philips.comment",
        "condition": """ "site" = '京东' and ("pk" like '%philips_ecomm_video_20190415151719_924_43%' or "pk" like '%philips_ecomm_video_20190415151720_130_67%' or "pk" like '%philips_ecomm_video_20190415151720_301_35%' or "pk" like '%philips_ecomm_video_20190415151720_434_11%' or "pk" like '%philips_ecomm_video_20190415151720_593_88%' or "pk" like '%philips_ecomm_video_20190415151720_714_88%' or "pk" like '%philips_ecomm_video_20190415151720_835_38%') """,
        "is_online": True
    }

    online_philips_comment_kwargs = {
        "output_file": "philips_jd.comments.csv",
        "tb": "dt.rhino.app.radar_data.philips.comment",
        "condition": """  """,
        "is_online": True
    }

    twitter_online_kwargs_1 = {
        "output_file": "HUAWEI.SEARCH.csv",
        "tb": "dt.rhino.tmp.twitter.post",
        "job_id": ["app_test_20190609230510_015_44", "app_test_20190609231059_049_71", "app_test_20190609231124_322_94", "app_test_20190609231303_905_11"],
        "is_online": True
    }

    ftp_kwargs = {
        "output_file": "common_img_download_20190611185359_799_31.ftp.csv",
        "tb": "dt.rhino.tmp.ftp",
        "job_id": "common_img_download_20190611185359_799_31",
        "is_online": True
    }

    yili_ecomm_cmt_kwargs = {
        "output_file": "yili_milk_cat_v2_20190624164304_910_53.cmt.csv",
        "tb": "dt.rhino.app.yili_ecomm_cmt_v2",
        "condition": """ "jobName" = 'yili_milk_cat_v2_20190624164304_910_53' """,
        "is_online": True
    }

    online_xhs_note_kwargs = {
        "output_file": "彩妆_changshuai_20190711.csv",
        "tb": "dt.rhino.tmp.xhs.note",
        "job_id": "app_test_20190711170423_796_91",
        "is_online": True
    }

    online_xhs_cmt_kwargs = {
        "output_file": "彩妆评论_changshuai_20190711.cmt.csv",
        "tb": "dt.rhino.tmp.xhs.cmt",
        "job_id": "app_test_20190711170423_796_91",
        "is_online": True
    }

    online_douyin_video_kwargs = {
        "output_file": "彩妆抖音_changshuai_20190701.video.csv",
        "tb": "dt.rhino.tmp.douyin.video",
        "job_id": "app_test_20190711163957_276_85",
        "is_online": True
    }

    online_douyin_cmt_kwargs = {
        "output_file": "面膜抖音_changshuai_20190701.cmt.csv",
        "tb": "dt.rhino.app.douyin_comment",
        "job_id": "app_test_20190711163957_276_85",
        "is_online": True
    }

    unline_xhs_article_tb = {
        "output_file": "monitor_xhs_user_20190725161058_973_36.article.csv",
        "tb": unline_tmp_article_tb,
        "job_id": "monitor_xhs_user_20190725161058_973_36",
        "is_online": False
    }

    online_ipsos_jd_comment_kwargs = {
        "output_file": "ipsos_mdlz_20190708164510_709_25.comment.csv",
        "tb": online_ipsos_comment,
        "condition": """ "pk" like '764|ipsos_mdlz_20190708164510_709_25%' """,
        "is_online": True
    }

    online_ipsos_jd_comment_kwargs = {
        "output_file": "demo.comment.csv",
        "tb": online_ipsos_comment,
        "condition": """ "comment_url" = 'http://club.jd.com/repay/100003245341_14cc16be-95f8-4230-a5a4-6f086748a01b_1.html' """,
        "is_online": True
    }

    unline_kaola_comment_kwargs = {
        "output_file": "app_ecomm_all_20190730150959_830_69.comment.csv",
        "tb": unline_tmp_ecomm_cmt_tb,
        "job_id": "app_ecomm_all_20190730150959_830_69",
        "is_online": False
    }


    # download_data(**unline_kaola_comment_kwargs)
    # download_data(**unline_xhs_article_tb)
    # download_data(**online_ipsos_jd_comment_kwargs)
    # download_data(**unline_douyin_user_detail_tb)
    # download_data(**online_douyin_cmt_kwargs)
    # download_data(**online_douyin_video_kwargs)
    # download_data(**online_xhs_cmt_kwargs)
    # download_data(**ecomm_unline_article_kwargs)
    # download_data(**ecomm_online_article_kwargs)
    # download_data(**yili_ecomm_cmt_kwargs)
    # download_data(**ecomm_unline_item_kwargs)
    # download_data(**twitter_online_kwargs_1)
    # download_data(**ecomm_unline_item_kwargs)
    # download_data(**ecomm_online_item_kwargs)
    # download_data(**ecomm_unline_comment_kwargs)
    # download_data(**ecomm_unline_douyin_user_kwargs)
    # download_data(**ecomm_unline_article_kwargs)
    # download_data(**ecomm_online_comment_kwargs)
    # download_data(**ecomm_unline_item_kwargs)
    # download_data(**ecomm_unline_item_condition_kwargs)e

    # download_data(**teg_online_search_kwargs_6)
    # download_data(**ecomm_online_kwawrgs)
    # download_data(**ecomm_cmt_unline_kwawrgs)
    # download_data(**teg_online_search_kwargs_6)
    # download_data(**jd_comment_kwargs)

    # download_data(**ftp_kwargs)1

    download_data(**test_kwargs)
    # print(FileUtil.readText(test_kwargs["output_file"]))



    # for row in CSVUtil.getDictFromCsv("app_test_20190227112110_419_53.item.csv"):
    #     print(row["url"])

    # keywords = FileUtil.readRows("/home/changshuai/PycharmProjects/dio_core/Test/Data/yili.keyword.0314.txt")
    # for keyword in keywords:
    #     print(Md5Util.md5(keyword)[:8])
    #     yili_kwargs = {
    #         "output_file": "yili_ecomm_v2_20190314003005_365_98.item.csv",
    #         "tb": "dt.rhino.app.yili_ecomm_cmt_v2",
    #         "fields": "\"pk\",\"url\",\"keyword\",\"site\",\"update_date\",\"sourceCrawlerId\"",
    #         "job_id": "yili_ecomm_v2_20190314003005_365_98",
    #         "is_online": Trueff
    #     }
    # kwargs = {
    #     "host": "120.31.140.132",
    #     "port": 56000,
    #     "pwd": "676592CCyok-",
    #     "user": "changshuai",
    #     "remote_path": "/home/changshuai/tfp_seeds.txt",
    #     "save_path": "tfp_seeds.txt"
    # }
        # remote_scp(**kwargs)1