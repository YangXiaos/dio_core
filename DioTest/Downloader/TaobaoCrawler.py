from typing import Union, Dict

from requests import Response

from DioCore.Network.Downloader import MiddleWare, Setting, Downloader
from DioCore.Utils import LoggerUtil, TextUtil, JsonUtil, RandomUtil


class ProxyMiddleWare(MiddleWare):
    """代理 middle ware"""
    downloader = Downloader()

    def __init__(self):
        self.logger = LoggerUtil.getLogger(self.__class__)

    def before(self, url: str, data: Union[str, Dict], setting: Setting):
        bs4 = self.downloader.getBs4("http://proxy.datastory.com.cn/getADAllHost?id=rhino")
        ip = RandomUtil.getRandomEleFromList(bs4.select("ipserver ips ip"))
        setting.setProxies(ip.select_one("host").text, ip.select_one("port").text)
        self.logger.info("使用代理ip {} {}".format(ip.select_one("host").text, ip.select_one("port").text))

    def after(self, url: str, data: Union[str, Dict], setting: Setting, res: Response):
        pass


class TaobaoCrawler(object):

    downloader = Downloader()
    BASE_INFO_URL = "https://detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId={}&sellerId={}&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,page,originalPrice,tradeContract&callback=onSibRequestSuccess"

    def run(self):
        url = "https://item.taobao.com/item.htm?id=593167331763"
        # self.downloader.middleWares.append(ProxyMiddleWare())
        res = self.downloader.get(url)

        itemId = TextUtil.getFirstMatch(res.text, "itemId\s+:\s+'(\d+)',")
        sellerId = TextUtil.getFirstMatch(res.text, "sellerId\s+:\s+'(\d+)'")
        shopName = TextUtil.getFirstMatch(res.text, "shopName\s*:\s*'(.*?)'")
        skuMap = TextUtil.getFirstMatch(res.text, "skuMap\s*:\s*({.*})")
        title = TextUtil.getFirstMatch(res.text, "title\s*:\s*'(.*)'")
        propertyMemoMap = TextUtil.getFirstMatch(res.text, "propertyMemoMap\s*:\s*({.*})")

        self.downloader.setting.headers.update({"Referer": url})
        self.downloader.setting.headers.update({"Cookie": "t=192584b50433a81c5feae77e9e99411f; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; OUTFOX_SEARCH_USER_ID_NCOO=1427643707.8819768; enc=V2PIbfvRYC7hvhCHq8qkNaMekFaEJPNApT08%2FgVaEAQ2OC%2BI2X4ku9sCq5dBhGRyaf7sP3uWnXEnmirxNFKDhQ%3D%3D; cna=4vCbFAVQ8hgCAbc/WcslocCr; cookie2=1931f04989f237d225904534cc89e2a7; _tb_token_=4e1edb04afa8; v=0; miid=1429757782455434771; tk_trace=oTRxOWSBNwn9dPyorMJE%2FoPdY8zZPEr%2FCrvCMS%2BG3sTRRWrQ%2BVVTl09ME1KrXE7g7f5SykjbFjU2EbuQocCrCuXu%2BxnGiDUI4y7SiU8R5wYO2UYEEivSgzo9bmwuwMAMEhtH43hBt535uXkDsXTju7V5XRRxfiOYs5k5VhVmShunGRh%2FOIXRI5LD3ngB8VZblVPU62%2FNCVT0brygusVvRPUvgT3iMfNN3l4HrDoNlJ1N88B%2FsJExCyaSkUuHnRgisCCXwa6iP2ttiJOjfsdh9kgRqJM2cYKE5mdnN7YlWI7MtgU0YitBpzvFoYM9wDlxNIrehSt32D2awKXRliVeBIw%3D; uc3=id2=UUpnjMGWeTDxMA%3D%3D&vt3=F8dBy3MLoylZjTIKqDw%3D&lg2=W5iHLLyFOGW7aA%3D%3D&nk2=suEMAecR; csg=f0359cd1; lgc=%5Cu6768%5Cu7545%5Cu5E05; dnk=%5Cu6768%5Cu7545%5Cu5E05; skt=d1c02800fe0af2e7; existShop=MTU2Njg4NjA4OA%3D%3D; uc4=id4=0%40U2gtHRBkJk9a2SFfxwUCZdl9g6Mj&nk4=0%40sOlUtvsiedjt3d5KnKNpEJI%3D; tracknick=%5Cu6768%5Cu7545%5Cu5E05; _cc_=V32FPkk%2Fhw%3D%3D; tg=0; mt=ci=19_1; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; whl=-1%260%260%261566893100933; _m_h5_tk=ed82048ac357de15b1d9f408c5a87f3b_1567332023191; _m_h5_tk_enc=1ce5e64614f05ae7b3fe320776816210; uc1=cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&cookie21=U%2BGCWk%2F7p4mBoUyS4E9C&existShop=false&pas=0&cookie14=UoTaH0QlXL3bSQ%3D%3D&tag=8&lng=zh_CN; isg=BAUFdlAy9O_vYtC8ivmC0CRlFEiT0L5xhaOb-wdr0zw7niYQwREaJYs_qILN3tEM; l=cBNHS6EVqJJZw89-BOfNVQLf1P_OuIOf1sPP2doM4IB1951TMdIxHHwIzx_Bp3QQE95xUExySDo_2Rnp7yz3rAonhFSjOC0eQ"})
        self.downloader.middleWares = []
        res = self.downloader.get(self.BASE_INFO_URL.format(itemId, sellerId))
        TextUtil.getFirstMatch(res.text, "onSibRequestSuccess\((.*)\);")
        info = JsonUtil.toPython(TextUtil.getFirstMatch(res.text, "onSibRequestSuccess\((.*)\);"))

        print({
            "itemId": itemId,
            "sellerId": sellerId,
            "shopName": shopName.encode('utf-8').decode("unicode-escape"),
            "title": title.encode('utf-8').decode("unicode-escape"),
            "skuMap": JsonUtil.toPython(skuMap),
            "propertyMemoMap": propertyMemoMap,
            "soldTotalCount": info["data"]["soldQuantity"]["confirmGoodsCount"],
            "stock": info["data"]["dynStock"]["stock"]
        }, end="\n")

        # self.downloader.setting.headers.update({"Referer": url})


if __name__ == '__main__':
    TaobaoCrawler().run()
