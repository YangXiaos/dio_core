from ftplib import FTP

from DioCore.Utils import FileUtil

ftp = FTP()
ftp.set_debuglevel(2)
ftp.connect("120.31.140.156", 21)
ftp.login("datastory", "datastoryFtp@2016")


ftp.cwd("/temp/2012-06-06")
files = ftp.nlst()

rows = FileUtil.readRows("/home/changshuai/Back/PythonProject/PyWork/data/ftp_file_path.txt")

i = 0
r = 0
for row in rows:
    if row not in files:
        i+= 1
        print(row, i, r)
    r+= 1
print(i)


