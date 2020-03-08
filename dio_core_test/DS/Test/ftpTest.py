from ftplib import FTP

from dio_core.utils import file_util

ftp = FTP()
ftp.set_debuglevel(2)
ftp.connect("120.31.140.156", 21)
ftp.login("datastory", "datastoryFtp@2016")


ftp.cwd("/temp/2012-06-06")
files = ftp.nlst()

rows = file_util.readRows("/home/changshuai/Back/PythonProject/PyWork/data/ftp_file_path.txt")

i = 0
r = 0
for row in rows:
    if row not in files:
        i+= 1
        print(row, i, r)
    r+= 1
print(i)


