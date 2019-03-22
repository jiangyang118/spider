# crawler.py
# -*- coding: utf-8 -*-

import logging
import utils
import requests
import time

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


class WeiXinCrawler:
    def crawl(self,url, headers,offset):
        """
        爬取更多文章
        :return:
        """
        url = url.format(offset=offset)
        response = requests.get(url, headers=headers, verify=False)
        result = response.json()
        if result.get("ret") == 0:
            msg_list = result.get("general_msg_list")
            logger.info("抓取数据：offset=%s, data=%s" % (offset, msg_list))
            # 递归
            has_next = result.get("can_msg_continue")
            if has_next == 1:
                next_offset = result.get("next_offset")
                time.sleep(2)
                self.crawl(url,headers,next_offset)
        else:
            # 错误消息
            # {"ret":-3,"errmsg":"no session","cookie_count":1}
            logger.error("无法正确获取内容，请重新从Fiddler获取请求参数和请求头")
            exit()


if __name__ == '__main__':
    crawler = WeiXinCrawler()
    offset = 10
    url = "https://mp.weixin.qq.com/mp/profile_ext?" \
              "action=getmsg&" \
              "__biz=MjM5MjAxNDM4MA==&" \
              "f=json&" \
              "offset={offset}&" \
              "count=10&" \
              "is_ok=1&" \
              "scene=126&" \
              "uin=777&" \
              "key=777&" \
              "pass_ticket=NqOMSpSgkqt7TbKCa5PTGIIpnzJAF62XnhxKoXaomMNOZXeRivMUoIIh4SEk2vEl&" \
              "wxtoken=&" \
              "appmsg_token=1001_2i83IvTNI8q300WZIViVq4aBpcsB_dQcmtYBVw~~&" \
              "x5=0&" \
              "f=json"  # 请将appmsg_token和pass_ticket替换成你自己的
    headers = """
Host: mp.weixin.qq.com
Accept-Encoding: br, gzip, deflate
Cookie: devicetype=iOS12.1.4; lang=zh_CN; pass_ticket=NqOMSpSgkqt7TbKCa5PTGIIpnzJAF62XnhxKoXaomMNOZXeRivMUoIIh4SEk2vEl; version=17000329; wap_sid2=CITbl7QCElxDcVVSblZ5Y3NnVkwxblE4NUZsNGNOVm9Dd05YVnprZWQtdFVSYVQxYk9Edmx0bEVBZWNuWXhyVmRXVjctczZfX1BCdVphZzNBZV9YRmJPNTYwTUF2ZWtEQUFBfjCDqNLkBTgNQJVO; wxuin=646311300; wxtokenkey=777; rewardsn=; pgv_pvid=8969838003; pgv_pvi=60331008; _scan_has_moon=1; ts_uid=3719156268; tvfe_boss_uuid=5682fb061e2059e3; sd_cookie_crttime=1545398450253; sd_userid=35071545398450253
Connection: keep-alive
Accept: */*
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57 MicroMessenger/7.0.3(0x17000321) NetType/WIFI Language/zh_CN
Referer: https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MjM5MjAxNDM4MA==&scene=126&bizpsid=1553240795&sessionid=1553240795&subscene=0&devicetype=iOS12.1.4&version=17000329&lang=zh_CN&nettype=WIFI&a8scene=0&fontScale=100&pass_ticket=NqOMSpSgkqt7TbKCa5PTGIIpnzJAF62XnhxKoXaomMNOZXeRivMUoIIh4SEk2vEl&wx_header=1
Accept-Language: zh-cn
X-Requested-With: XMLHttpRequest"""
    headers = utils.str_to_dict(headers)
    #crawler.crawl(url,headers,10)
