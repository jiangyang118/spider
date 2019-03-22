
# -*- coding:utf-8 -*-

import requests

def headers_to_dict(headers):
    """
    将字符串
    '''
    Host: mp.weixin.qq.com
    Connection: keep-alive
    Cache-Control: max-age=
    '''
    转换成字典对象
    {
        "Host": "mp.weixin.qq.com",
        "Connection": "keep-alive",
        "Cache-Control":"max-age="
    }
    :param headers: str
    :return: dict
    """
    headers = headers.split("\n")
    d_headers = dict()
    for h in headers:
        if h:
            k, v = h.split(":", 1)
            d_headers[k] = v.strip()
    return d_headers

h = '''
    Host: mp.weixin.qq.com
    Cookie: devicetype=iOS12.1.4; lang=zh_CN; pass_ticket=NqOMSpSgkqt7TbKCa5PTGIIpnzJAF62XnhxKoXaomMNOZXeRivMUoIIh4SEk2vEl; version=17000329; wap_sid2=CITbl7QCElxqZXBLR1RhYTBVeFk2ZnVaM2hyQmZTRFBiT1lBeGk1NjQ5RXh1Q0ZLNVNjLXVLSXpub1dfUGEwdnpvQTdDa2dZa3lsbXlIWnZHNW5SMGpSNnVlMTZJdWtEQUFBfjC489HkBTgNQJVO; wxuin=646311300; wxtokenkey=777; rewardsn=; pgv_pvid=8969838003; pgv_pvi=60331008; _scan_has_moon=1; ts_uid=3719156268; tvfe_boss_uuid=5682fb061e2059e3; sd_cookie_crttime=1545398450253; sd_userid=35071545398450253
    X-WECHAT-KEY: f52813a727c4005786099e7aadb653b1c11a9aa9c4024ed157dbaa3cc3d9a9544e66b7c889d1ad72cd4fffd91d208720dae5c896e2faa43231b3230c4c6193010a98b616478246349cc616153552afcf
    X-WECHAT-UIN: NjQ2MzExMzAw
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57 MicroMessenger/7.0.3(0x17000321) NetType/WIFI Language/zh_CN
    Accept-Language: zh-cn
    Accept-Encoding: br, gzip, deflate
    Connection: keep-alive
'''
#print(headers_to_dict(h))

# v0.1
def crawl(url,headers):
    
    headers = headers_to_dict(headers)
    #print(headers)
    response = requests.get(url, headers=headers, verify=False)
    #print(response.text)
    return response.text

url = "https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MjM5MjAxNDM4MA==&scene=126&bizpsid=1553233877&sessionid=1553233877&subscene=0&devicetype=iOS12.1.4&version=17000329&lang=zh_CN&nettype=WIFI&a8scene=0&fontScale=100&pass_ticket=NqOMSpSgkqt7TbKCa5PTGIIpnzJAF62XnhxKoXaomMNOZXeRivMUoIIh4SEk2vEl&wx_header=1"
url ="https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MjM5MjAxNDM4MA==&scene=126&bizpsid=1553233877&sessionid=1553233877&subscene=0&devicetype=iOS12.1.4&version=17000329&lang=zh_CN&nettype=WIFI&a8scene=0&fontScale=100&pass_ticket=NqOMSpSgkqt7TbKCa5PTGIIpnzJAF62XnhxKoXaomMNOZXeRivMUoIIh4SEk2vEl&wx_header=1"
headers='''
Host: mp.weixin.qq.com
Cookie: devicetype=iOS12.1.4; lang=zh_CN; pass_ticket=NqOMSpSgkqt7TbKCa5PTGIIpnzJAF62XnhxKoXaomMNOZXeRivMUoIIh4SEk2vEl; version=17000329; wap_sid2=CITbl7QCElxqZXBLR1RhYTBVeFk2ZnVaM2hyQmZWS2RFT3FUZEkwaFVKSmZKX25kbVRkbVhQSHF1WFpCLTBnVi1OSG1lRk9qc0kzSzFyOHZVQVlhX2ZNSFZRcVdldWtEQUFBfjCC9dHkBTgNQJVO; wxuin=646311300; wxtokenkey=777; rewardsn=; pgv_pvid=8969838003; pgv_pvi=60331008; _scan_has_moon=1; ts_uid=3719156268; tvfe_boss_uuid=5682fb061e2059e3; sd_cookie_crttime=1545398450253; sd_userid=35071545398450253
X-WECHAT-KEY: 3ab2ebf7938f0c885d94f23ebbfab9475d3ee268c159dad9377cee9ad6b6a86fa71538b1a0c7caeca92b54ee8e76fd78fd6594aef35c48a88376a937f25c65a11516320624d36e9d5f73ba4b7127f4d3
X-WECHAT-UIN: NjQ2MzExMzAw
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57 MicroMessenger/7.0.3(0x17000321) NetType/WIFI Language/zh_CN
Accept-Language: zh-cn
Accept-Encoding: br, gzip, deflate
Connection: keep-alive
'''
#crawl(url,headers)

def write(filename,content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

write("weixin_history.html",crawl(url,headers))


