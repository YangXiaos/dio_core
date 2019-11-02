from DioCore.Utils import JsonUtil, FileUtil


def test_getPythonFromFile():
    rows = FileUtil.readRows("/home/changshuai/Temp/5dcdd0a7-8842-4695-8fd8-9553b191d346.tmp")
    data = []
    for row in rows:
        datum = JsonUtil.toPython(row)
        if datum["jobName"] == "yili_ecomm_v2_20190605131709_003_27":
            data.append(datum)
    print(data)

