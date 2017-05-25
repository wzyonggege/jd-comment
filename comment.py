# coding:utf-8
import requests
import json


headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'club.jd.com',
    'Referer': 'https://item.jd.com/3867555.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Cookie': 'B3C9B=Q'
}

def crawler(page):
    url = 'https://club.jd.com/comment/productPageComments.action?' \
          'callback=fetchJSON_comment98vv12621&' \
          'productId=3867555&' \
          'score=0&' \
          'sortType=5&' \
          'page={}&pageSize=10&isShadowSku=0&fold=1'.format(page)
    result = requests.get(url, headers=headers).content\
        .replace('fetchJSON_comment98vv12621(', '').replace(');', '')
    r = json.loads(result, encoding='GBK')
    return r
    # for i in r['comments']:
    #     print u'时间: {}'.format(i['creationTime'])
    #     print u'颜色: {}'.format(i['productColor'])
    #     print u'规格: {}'.format(i['productSize'])
    #     print u'用户: {}'.format(i['userClientShow'])
    #     print u'等级: {}'.format(i['userLevelName'])
    #     print u'评分: {}'.format(i['score'])
    #     print u'内容: {}'.format(i['content'])
    #     print '============================================'

if __name__ == '__main__':
    for i in range(100):
        res = crawler(i+1)
        print '第{}页 done'.format(i+1)
        with open('data.txt', 'ab+') as f:
            f.write(json.dumps(res))
            f.write('\n')
