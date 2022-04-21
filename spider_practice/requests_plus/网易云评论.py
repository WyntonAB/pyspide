# -*- coding = utf-8 -*-
# @Time : 2022/4/20 7:57 下午
# @Author : WyntonAB
# @File : 网易云评论.py
# @Software : PyCharm

# 1.找到未加密的参数                        # window.asrsea(参数,xxxx,xxxx)
# 2.想办法把参数进行加密（必须参考网易的逻辑），encText => params，encSecKey => encSecKey
# 3.请求到网易，拿到评论信息

# 需要安装pycrypto模块进行AES加密

from Crypto.Cipher import AES
from base64 import b64decode
import json
import requests


url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
# 请求方式是POST
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1376142151",
    "threadId": "R_SO_4_1376142151"
}
e = '010001'
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'
i = 'd5bpgMn9byrHNtAh'

def get_encSecKey():
    return "1b5c4ad466aabcfb713940efed0c99a1030bce2456462c73d8383c60e751b069c24f82e60386186d4413e9d7f7a9c7cf89fb0640e52f28b84b87866476738012b81ec60a3ff70a00b005c886a6600c012b61dbf418af84eb0be5b735988addafbd7221903c44d027b2696f1cd50c49917e515398bcc6080233c71142d226ebb"

def get_params(data):   # 默认这里收到的是字符串,所以要将data从字典转换为字符串
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second   # 返回的就是params

def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data

def enc_params(data,key):   # 加密过程
    iv = '0102030405060708'
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC)    # 加密器
    bs = aes.encrypt(data.encode("utf-8"))  # 加密,加密的内容的参数必须是16的倍数        # bs不能直接用.decode("utf-8")转化
    return str(b64decode(bs), "utf-8", "ignore")  # 转化为字符串返回

# 处理加密过程
"""
    function a(a = 16) {    # 返回的随机的16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)  # 循环16次4
            e = Math.random() * b.length,   # 随机数
            e = Math.floor(e),  # 取整
            c += b.charAt(e);   # 取字符串中的xxx位置
        return c
    }
    function b(a, b) {  # a是要加密的内容
        var c = CryptoJS.enc.Utf8.parse(b) # b是密钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)  # e是数据
          , f = CryptoJS.AES.encrypt(e, c, {    # c是加密的密钥
            iv: d,  # 偏移量
            mode: CryptoJS.mode.CBC # 加密模式：cbc
        });
        return f.toString()
    }
    function c(a, b, c) {   # c里面不产生随机数
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {    d:数据, e:010001, f:很长, g:0CoJUm6Qyw8W8jud
        var h = {}
          , i = a(16);  # i就是一个16位的随机值
        return h.encText = b(d, g), # g就是密钥
        h.encText = b(h.encText, i),    # 返回的就是params，i也是密钥
        h.encSecKey = c(i, e, f),   # 得到的就是encSecKey，e和f是定死的值，如果把i固定，得到的key一定是固定的
        h
    }
    
    两次加密：
    数据+g => b => 第一次加密的结果+i => params
"""

if __name__ == '__main__':
    resp = requests.post(url, data={
        "params": get_params(json.dumps(data)),
        "encSecKey": get_encSecKey()
    })    # 使用json模块将字典类型的data转换为字符串类型的data
    print(resp.text)