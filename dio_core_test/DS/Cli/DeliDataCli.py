from dio_core.utils import file_util

rows = file_util.readRows("/home/changshuai/PycharmProjects/dio_core/dio_core_test/Data/cp_3539-changshuai_20190722.data")

lastWord = ""
curWord = ""

for ind, row in enumerate(rows):
    if ind % 2 == 0:
        lastWord = row
        continue
    else:
        curWord = row
        if curWord != lastWord:
            print(curWord, lastWord)