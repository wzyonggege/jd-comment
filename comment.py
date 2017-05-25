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
    'Cookie': 'TrackID=1KDj0EMrDOWB-lsxXlr0Mc40j5KkleXovhwq1cZA0oYt-JpLlqujw0mIYzcJ9mjRe19EWFpx7xGcPMgWwxDRu_oCq6W8jscTCeXT2b5BcLjQ; pinId=vHbiCQJPub5Lo-LADemRyg; user-key=1f0826ae-a816-4e2d-83de-d49865973f93; cn=0; ipLoc-djd=1-72-2799-0; unpl=V2_ZzNtbRdREUV9WEADL04LDWJUGw5LAkUQdggUU39JWwZhCkIIclRCFXMUR1BnGl8UZwoZXEVcRhNFCHZXfBpaAmEBFl5yBBNNIEwEACtaDlwJBhddSlZKHHcNRlRLKV8FVwMTbUJSSxV3DkZWeRFfB2QDElhDVkcddg12ZHwpbDVuARNZRFZzFEUJdhYvRVkBYAsTEEJSSxV3DkZWeRFfB2QDElhDVkcddg12VUsa; __jdv=122270672|baidu-search|t_262767352_baidusearch|cpc|44190883411_0_d7ca9a7feff94f8b8d7421c65a6278ad|1495447608177; ipLocation=%u5317%u4EAC; areaId=1; __jda=122270672.1491371339232114005924.1491371339.1495617920.1495702371.19; __jdb=122270672.7.1491371339232114005924|19.1495702371; __jdc=122270672; __jdu=1491371339232114005924; 3AB9D23F7A4B3C9B=QVI7J6IHOADSKOBLMQX35KZCIAUFSZGRODDPL5IM2AZQ3HZOEVN53XHRLJBE2NGEILHKHMIMHW5L6MQHFFJ7E4H6NQ'
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
