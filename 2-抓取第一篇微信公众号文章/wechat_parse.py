
# -*- coding:utf-8 -*-

def extract_data(html_content):
    """
    从html页面中提取历史文章数据
    :param html_content 页面源代码
    :return: 历史文章列表
    """
    import re
    import html
    import json
     
    rex = "msgList = '{.*?}'"
    rex = "msgList = '({.*?})'"
    pattern = re.compile(pattern=rex, flags=re.S)
    #print(pattern)
    match = pattern.search(html_content)
    #print(match)
    if match:
        data = match.group(1)
        data = html.unescape(data)
        data = json.loads(data)
        articles = data.get("list")
        #for item in articles:
            #print(item)
        return articles

def read(filename):
    f = open(filename, 'r', encoding="utf-8")                  
    result = u''
    for line in f.readlines():                          
        line = line.strip()
        #解决sublime print gbk格式的html报UnicodeEncodeError错误
        #print(line.encode('gbk','ignore').decode('gbk'))
        if not len(line) or line.startswith('#'):
            continue
        result+=line
    f.close()
    return result

data = read("weixin_history.html")
#print(data.encode('gbk','ignore').decode('gbk'))
print(extract_data(data))