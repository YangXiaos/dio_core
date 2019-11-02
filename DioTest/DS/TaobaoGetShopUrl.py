import time

import requests

session = requests.Session()


keywords = ["针织衫",
"套头针织衫",
"毛衣",
"针织衫/毛衣",
"纯色毛衣",
"针织衫/毛衣",
"拼接毛衣",
"薄款毛衣",]


url = "https://list.tmall.com/search_product.htm"


for keyword in keywords:
    querystring = {"q": keyword, "click_id": keyword}

    headers = {
        'cookie': "cna=4vCbFAVQ8hgCAbc/WcslocCr; _tb_token_=706657eee0ab0; _m_h5_tk=e4bf41a2d249130b25edc562ee7a48de_1558012636547; _m_h5_tk_enc=b2598f87e8b0545809579b1c904c1888; arp_scroll_position=0; t=7ae381515778b6f554454a7f4c7f5ebc; lid=%E6%9D%A8%E7%95%85%E5%B8%85; cookie2=15d45dbe475828433a42f4178a089c91; hng=""; uc1=cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie21=UIHiLt3xThH8t7YQoFNq&cookie15=UIHiLt3xD8xYTw%3D%3D&existShop=false&pas=0&cookie14=UoTZ7HEGf72JUg%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dBy3vKtnn%2FJoT2LNE%3D&id2=UUpnjMGWeTDxMA%3D%3D&nk2=suEMAecR&lg2=VT5L2FSpMGV7TQ%3D%3D; tracknick=%5Cu6768%5Cu7545%5Cu5E05; ck1=""; lgc=%5Cu6768%5Cu7545%5Cu5E05; csg=e859fef7; skt=898ba6e4db10af05; _uab_collina=155842975336048647430925; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; swfstore=49624; enc=PvL3IigDBRg%2Bg9dC77iwtZuqHGoyhqaYc74N4K96YcQyo5lGXBw3sCg6%2FjrtPdsaJ%2FuFYhKk1howaUWmuqdkqg%3D%3D; x=__ll%3D-1%26_ato%3D0; tt=tmall-main; _med=dw:1920&dh:1080&pw:1727.9999542236328&ph:971.9999742507935&ist:0; pnm_cku822=098%23E1hvApvUvbpvUvCkvvvvvjiPRLLpsji8nLLhsj1VPmPO1jnvn2zZsjYnRsFh6jr2iQhvCvvv9UUCvpvVvvpvvhCvuphvmvvv927XUixIkphvC99vvpH0BfyCvm9vvvvAphvvvvvv9BrvpCCWvvm2phCvhRvvvUnvphvpPvvvvcEvpvAKmphvLvQRhQvjnaFy%2BnezrmphQPclIbw7b9jU6PjvDE6kZE7HdJA1%2B2n79WLWTEvsnxKn647Yn1p6Vb0yqw0qr2BcI4mYib01Ux8x9W2IRfUPvpvhvv2MMsyCvvpvvvvv; res=scroll%3A990*5317-client%3A806*1027-offset%3A806*5318-screen%3A1920*1080; whl=-1%260%260%260; tk_trace=1; isg=BMXFOgv5NafV_xGeZ0Eih3mq1AhTkH7GczZZx8cqEvwLXubQjNPP5C13bMINHpHM; l=bBPR3t0IvPv24DL1BOfgZQLf1Lb93IRf1sPP2doihICP_y1M5WXFWZtmNTLHC3GVZ1lH83RBOYAYBVThBzsR.",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'cache-control': "max-age=0",
        'authority': "list.tmall.com",
        'referer': "https://www.tmall.com/",
        'Host': "list.tmall.com",
        'Connection': "keep-alive"
    }

    response = session.request("GET", url, headers=headers, params=querystring)
    print(response.text)

    time.sleep(10)
