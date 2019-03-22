
import html

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


def sub_dict(d, keys):
    return {k: html.unescape(d[k]) for k in d if k in keys}

def str_to_dict(s, join_symbol="\n", split_symbol=":"):
    """
    key与value通过split_symbol连接， key,value 对之间使用join_symbol连接
    例如： a=b&c=d   join_symbol是&, split_symbol是=
    :param s: 原字符串
    :param join_symbol: 连接符
    :param split_symbol: 分隔符
    :return: 字典
    """
    s_list = s.split(join_symbol)
    data = dict()
    for item in s_list:
        item = item.strip()
        if item:
            k, v = item.split(split_symbol, 1)
            data[k] = v.strip()
    return data


def save(msg_list):

    msg_list = msg_list.replace("\/", "/")
    data = json.loads(msg_list)
    msg_list = data.get("list")
    for msg in msg_list:
        p_date = msg.get("comm_msg_info").get("datetime")
        msg_info = msg.get("app_msg_ext_info")  # 非图文消息没有此字段
        if msg_info:
            WeiXinCrawler._insert(msg_info, p_date)
            multi_msg_info = msg_info.get("multi_app_msg_item_list") # 多图文推送，把第二条第三条也保存
            for msg_item in multi_msg_info:
                WeiXinCrawler._insert(msg_item, p_date)
        else:
            logger.warning(u"此消息不是图文推送，data=%s" % json.dumps(msg.get("comm_msg_info")))


def _insert(item, p_date):
    keys = ('title', 'author', 'content_url', 'digest', 'cover', 'source_url')
    sub_data = utils.sub_dict(item, keys)
    post = Post(**sub_data)
    p_date = datetime.fromtimestamp(p_date)
    post["p_date"] = p_date
    logger.info('save data %s ' % post.title)
    try:
        post.save()
    except Exception as e:
        logger.error("保存失败 data=%s" % post.to_json(), exc_info=True)


if __name__ == '__main__':
    d = {"a": "1", "b": "2", "c": "3"}
    print(sub_dict(d, ["a", "b"]))
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
    print(str_to_dict(h))