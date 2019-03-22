import requests
import json

class SimpleCrawler:
    def total(self,params):
        response = self.crawlCore(params);
        text = json.loads(response.text);
        return text['paging']['totals'];

    def crawlCore(self,params):
        num = 0;
        if params['num'] != None:
            num = params['num'];
        # 必须指定UA，否则知乎服务器会判定请求不合法
        url = "https://www.zhihu.com/api/v4/columns/pythoneer/followers"
        # 查询参数
        params = {"limit": 20,
                  "offset": num,
                  "include": "data[*].follower_count, gender, is_followed, is_following"}

        headers = {
            "authority": "www.zhihu.com",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        }
        return requests.get(url, headers=headers, params=params)

    def crawlData(self, params):
        response = self.crawlCore(params);
        print("请求URL：", response.url)
        # 你可以先将返回的响应数据打印出来，拷贝到 http://www.kjson.com/jsoneditor/ 分析其结构。
        print("返回数据：", response.text)

        # 解析返回的数据
        for follower in response.json().get("data"):
            print(follower)

    def crawlAllData(self, params):
        total = self.total(params);
        start = 0;
        params['num'] = 0;
        while params['num'] < total:
            response = self.crawlData(params);
            params['num'] = params['num'] + 20;
            print("params['num'] = "+ str(params['num']));
        

if __name__ == '__main__':
    params = {};
    params['num'] = 0;
    text = SimpleCrawler().total(params);
    print(text)
    #SimpleCrawler().crawlAllData(params);
    SimpleCrawler().crawlData(params);