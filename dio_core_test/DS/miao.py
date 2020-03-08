import re

word = "296h,46m,11s"
seeds = 167157


h = int(re.findall("(\\d+)h", word)[0])
m = int(re.findall("\\d+h,(\\d+)m", word)[0])
s = int(re.findall("\\d+h,\\d+m,(\\d+)s", word)[0])

time = (h * 60 * 60 + m * 60 + s)
print(time)
print(time/seeds)
