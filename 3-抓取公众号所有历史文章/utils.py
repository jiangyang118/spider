

def str_to_dict(headers):
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
#print(str_to_dict(h))
