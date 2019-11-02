import requests

url = "https://www.amazon.ae/s"

headers = {
    'cookie': "session-id=262-1303045-4193915; i18n-prefs=AED; ubid-acbae=262-6047108-5915305; session-token=n6zGAJb1MUNhUE8iDgWj4hRIqdEyJwRJXYaZtRVGouLTQFcTgeg7O1DaybIgg3sUZuO0LabaJ9tZMnYMaeELRhECpSsBZPrUd6UFtLRtxDV65SIzemOhQ8kknAzLPy4rXggKs3u57801WzsQmht56PFw2l0pCX4bZkoDzBrLNl/rkOhk/6e++ng4SxeiBef4; x-wl-uid=1kflW/tx8LCgGJ7OPN+8vxeMMzcCFB++nMJgilqDejVNdJnIqrQ2JP7+IDSBtdgV1f/6AB9YRdWg=; arp_scroll_position=3968; csm-hit=tb:s-G656BQDE2CQ68X1YFT8S|1559650581877&t:1559650582222&adb:adblk_no; session-id-time=2082758401l",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'cache-control': "max-age=0",
    'authority': "www.amazon.ae",
    'referer': "https://www.amazon.ae/s?k=HUAWEI&page=2&qid=1559649242&ref=sr_pg_2",
    'Host': "www.amazon.ae",
    'Connection': "keep-alive"
    }

session = requests.session()

response = session.get("https://www.amazon.ae/s?k=HUAWEI&page=2&ref=sr_pg_2", headers=headers)

print(len(response.text))