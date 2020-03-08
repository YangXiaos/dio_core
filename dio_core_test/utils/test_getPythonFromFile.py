from dio_core.utils import json_util, file_util


def test_get_python_from_file():
    rows = file_util.readRows("/home/changshuai/Temp/5dcdd0a7-8842-4695-8fd8-9553b191d346.tmp")
    data = []
    for row in rows:
        datum = json_util.to_python(row)
        if datum["jobName"] == "yili_ecomm_v2_20190605131709_003_27":
            data.append(datum)
    print(data)

