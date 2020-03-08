import collections
from collections import OrderedDict

from dio_core.utils import url_util

python = OrderedDict({'&#xec72;': 2, '&#xe0e1;': 5, '&#xe81b;': 3, '&#xef58;': 7, '&#xe9bd;': 0, '&#xef6b;': 1, '&#xe130;': 4, '&#xe740;': 9, '&#xef6f;': 8, '&#xf6b5;': 6})
keyword = "ttfMatch"

post_data = "wmPoiId=1055283243735476&spuTag=112454037&tag=112454037&pageIndex=0&uuid=2E42332BF3FA3E12F5CFCFA99E799888E8883DB85EF252B10CB184761FFDB340&platform=3&partner=4&originUrl=https%3A%2F%2Fh5.waimai.meituan.com%2Fwaimai%2Fmindex%2Fmenu%3FmtShopId%3D1055283243735476%26initialLat%3D%26initialLng%3D%26actualLat%3D23.125764%26actualLng%3D113.334692%26source%3Dsearchresult&riskLevel=71&optimusCode=10&wm_latitude=0&wm_longitude=0&wm_actual_latitude=23125764&wm_actual_longitude=113334692&openh5_uuid=2E42332BF3FA3E12F5CFCFA99E799888E8883DB85EF252B10CB184761FFDB340&_token=eJyFk22PokgUhf8LyfqlK0IVUAWdmI2KTqPSvqC0OtOZICDQCiVQ4stm%2F%2FuWtjUzH2ayCQnPPffcOpVL%2BEcq7VB6hgokCgRSHZXSswSbShNLQGIV7%2BiYEIx0%2FkANSMFPjUsIYgNIm9KzpOevpkaAieD7TZjx%2Bis0kQKgYijvQLCqvwOk8efmsrlJShg7VM%2BynOjNk59mftrMopQd%2FbwZ0Ez%2BlOQszcPoLGdRfvw7PLgJPdhhq5GxB5mIYBUbUCeqoSta48iy7xU9lkHUajzeFXfu04o10jxlqb8f%2Baz1g%2FO41fADHnqXEWrqpop1IjTehlBrQpUHEL4WiV8%2Bm98urxoAGRqX7qAKQAKgAOUBxBRABOgCxDgRZnw3EwFYgC5A%2BwU%2Bp24ABSABqgBNgC4ACzAeYIhzDDFuiCnjblY53EMRQOY9C3JQb0vZ3ZfyF%2BiMrRVvfDsqCkSi%2BoN8r%2BD%2FmH4r80D%2Fl68ALNvjDl3DQFUeBcIEaLoqKgUgBOzPFeoKBu6k%2FcorDAEmqqiIogHyeRpPYLeEW5LD%2FwverdI45xQNLmzRg%2BW5217IXZMYg6SXI%2BzGh%2Fnrhrr9yWzu50k42HSHr1%2FoGT3Jk3Kbzw40CKLECq7j6mm9Xx%2B9l3B3njF4VfZ2d9qhnVXssAEdsLO3rnBJGSZFUXysQmQtPP%2FkJQfnpc%2BqnjcKw1XaVyzW6xwtVvbWEcPn5ZfuMpb9ui4GH5cX56KMo4%2FLibhvaHelV9deFJswIDvvQlVUbwrnuh2ed8E83wUqkdnudE4Pcb9NY98L3X4VssFp7NQW2bSj8XqwNUYfbsfqvL6Vx526R65jT8cx1ov4vFhuhxuN4k09Ky7euB3Ay2JSX8M93qFpVE6GIc2zmRaY%2Bmna12py2kLqrqNVOXeMxVs0me73zG67iSfTLaFG5ka5fCnjtU2WS2er1N4sxYeyPdq2J9cwT4bFhrKn2aCeG4fRMXkqvMRszyc9avVa0r%2F%2FAYofUig%3D"
python = url_util.unquote_post_data(post_data)
keyword = "post_data"


python = {
        "lng": "113.334715",
        "lat": "23.125752",
        "gpsLng": "113.334715",
        "gpsLat": "23.125752",
        "shopId": "0",
        "mtWmPoiId": "",
        "startIndex": "0",
        "labelId": "0",
        "scoreType": "0",
        "uuid": "2E42332BF3FA3E12F5CFCFA99E799888E8883DB85EF252B10CB184761FFDB340",
        "platform": "3",
        "partner": "4",
        "originUrl": "http://h5.waimai.meituan.com/waimai/mindex/menu?dpShopId=&mtShopId={}&utm_source=&source=shoplist&initialLat=&initialLng=&actualLat=23.125752&actualLng=113.334715".format(""),
        "riskLevel": "71",
        "optimusCode": "10",
        "wm_latitude": "0",
        "wm_longitude": "0",
        "wm_actual_latitude": "23125752",
        "wm_actual_longitude": "113334715",
        "openh5_uuid": "2E42332BF3FA3E12F5CFCFA99E799888E8883DB85EF252B10CB184761FFDB340"
    }
keyword = "post_data"

post_data = "geoType=2&mtWmPoiId=1117860917317656&dpShopId=-1&source=searchresult&skuId=&uuid=2E42332BF3FA3E12F5CFCFA99E799888E8883DB85EF252B10CB184761FFDB340&platform=3&partner=4&originUrl=https%3A%2F%2Fh5.waimai.meituan.com%2Fwaimai%2Fmindex%2Fmenu%3FmtShopId%3D1117860917317656%26initialLat%3D%26initialLng%3D%26actualLat%3D23.125753%26actualLng%3D113.334699%26source%3Dsearchresult&riskLevel=71&optimusCode=10&wm_latitude=0&wm_longitude=0&wm_actual_latitude=23125753&wm_actual_longitude=113334699&openh5_uuid=2E42332BF3FA3E12F5CFCFA99E799888E8883DB85EF252B10CB184761FFDB340&_token=eJxlk9tuq1YQht%2BFi9xkyawzECmq4lOCsV0DNtlm71wABoNtwOHgU9XH6ZP0xbrAsdOqEkgf%2F8z6Z9aM%2BEMq9JX0hCBSIALSISykJwl1YIdLQKpKEWFcURlGRONQBVLwL41xqmIGJL9w%2BtLTT6RhCDSMPhrFEsJVQVCFH%2BDGhH0ATMXTZOkiSYqral8%2ByXLMOkcvSb2kk4ZJVXtZJ8hT%2BSrJaZKtwpOchln9W1rZcb7XV88IMoZVgilRCKMKf0iypEq83dirnu%2BcrZ8fvED4tTImHYSZwulNE2GESIcQyjX8UOZ1EYTPZegVQVyEZb2rxBgk0Ws6b3pFmgIQVTQhYkjAFYgKMBJAFAhIo4heQCNQTQWomSNlKiCsAYQAb1KIpgGVfoEY%2Fo1Ie05sAlG1JeHESXtSRNt6lIqo1tpyAjBsfTUuqK2N8Y34nVTtizi65XFKb8S%2BSbkRh%2F%2FXmntCpfXjooOmLkPihsr1ikLjsBnVth3VT9D9vb8UkTv8KoA%2BnS3mAv%2F%2B646%2FaggR%2FP707zj8bw66%2BogC3n0XmKugrzv3ddxPXJfyFbsu5jsmZsBvTQlb8aE3tlVj29hPxC8gQmWyzgSFo3O1GKDxqf%2BykHuacp4g%2FEMbQ%2FOYnJX5cq0MhqbqJ4Np4cYpt7eJd5BJ0VOKXA9n84ueqlvfTX3nQh83Wagpq%2FU03878%2FZItJ%2FojijR96gxM7yUvLz%2BGljlI9pf0PFHszZsZrevc9TfTSc%2BgjFoH%2B6X2IDVJ5AwdX7zuLoVB%2BYnGOBtNApMU%2B3x5Nsh4HQ3rud8lw8N0FHvvx8NrMHc%2BF6%2BuewlPMKpYvSDzre2%2B5b5lJq5vdPGrfakL2DccL3X44x59eoERaaMgOBzVPC9UGw4YWxHsru03y1KO1ma77qVd24neDbNrD0b6bhc47%2BnpmL3b46FB%2Fcy59Nh0UGb9yC7Ny3Qr9w4o3b1uh7Px0o4iNjENc1LGVn8lvx202QqG2kw7rKxjeErROh7tg2B2iYt4M3EHCPasyOVBNWZyYYWRaZDI8wzpz38AMhpJ7g%3D%3D"
python = url_util.unquote_post_data(post_data)
keyword = "post_data"

python = collections.OrderedDict({"actualLanguageCode":"zh-CN","countryId":"CN","countryNumCode":"156","currencyCode":"CNY"})



keyword = "params"
for k, v in python.items():
    print("{}.put(\"{}\", \"{}\");".format(keyword, k, str(v).replace('"', '\\"')))

print("{\"actualLanguageCode\":\"zh-CN\",\"countryId\":\"CN\",\"countryNumCode\":\"156\",\"currencyCode\":\"CNY\"}")

