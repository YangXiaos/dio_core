from Crypto.Cipher import AES
import base64

def add_to_16(par):
    par = par.encode() #先将字符串类型数据转换成字节型数据
    while len(par) % 16 != 0: #对字节型数据进行长度判断
        par += b'\x00' #如果字节型数据长度不是16倍整数就进行 补充
    return par

password = 'jvzempodf8f9anyt'  # 秘钥
text = '{"ts":1565836186395,"cts":1565836890261,"brVD":[559,921],"brR":[[1920,1080],[1920,1035],24,24],"aM":""}'
model = AES.MODE_CBC
aes = AES.new(password.encode("utf-8"), model, iv="0000000000000000".encode("utf-8"))

en_text = aes.encrypt(add_to_16(text))
print(en_text)
en_text = base64.encodebytes(en_text)
print(en_text)
# en_text = en_text.decode('utf8')
# print(en_text.strip())
