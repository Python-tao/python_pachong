#PC-1.py
#爬取微博粉丝
import requests
from html.parser import HTMLParser
from my_module import person
from bs4 import BeautifulSoup
import json
#获取的cookie值存放在这
myHeader = {"Cookie":"SINAGLOBAL=9609693934392.922.1542876975421; login_sid_t=7b3893e5a7179833a9d3b8a73fe8c88c; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=5743798807159.846.1543807197108; ULV=1543807197124:2:1:1:5743798807159.846.1543807197108:1542876975745; UOR=post.smzdm.com,weibo.com,www.baidu.com; SCF=AvGaFkl5siVOQHKRJE0jXQTJudahIS3C4OBZhjZ15reUoyzH7i5U1seaZX4iNH0QqURMtLkvOc1JB1EsBT2KVik.; SUB=_2A25xANrZDeRhGedP7VMX9i3JwziIHXVSdEsRrDV8PUNbmtBeLVfCkW9NX3oWBXfRQTL_FHKeqONDBKt1gMdoBo5j; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh8ZVEv6yLGA1zpcz1hDdi15JpX5K2hUgL.Fo2pSo2cSoef1hB2dJLoIpjLxKqLB.zL1KBLxKqLBK5L1K2LxKqLBK5L1K2t; SUHB=0auByYE0YoimRb; ALF=1544414770; SSOLoginState=1543809673; wvr=6"}
#要爬去的账号的粉丝列表页面的地址
r = requests.get('https://weibo.com/p/1005051678105910/follow?relate=fans&from=100505&wvr=6&mod=headfans&current=fans#place',headers=myHeader)
f = open("test.html", "w", encoding="UTF-8")
parser = HTMLParser()
parser.feed(r.text)
htmlStr = r.text

# 通过script来切割后边的几个通过js来显示的json数组，通过观看源代码
fansStr = htmlStr.split("</script>")
#因为在测试的时候，发现微博每一次返回的dom的顺序不一样，粉丝列表的dom和一个其他内容的dom的位置一直交替，所以在这加了一个判断
tmpJson = fansStr[-2][17:-1] if fansStr[-2][17:-1].__len__()>fansStr[-3][17:-1].__len__() else fansStr[-3][17:-1]
dict = json.loads(tmpJson) #对JSON文件解码
 
soup = BeautifulSoup(dict['html'], 'html')
 
soup.prettify()
f.write(soup.prettify())
 
for divTag in soup.find_all('div'):
    if divTag['class'] == ["follow_inner"]:
        followTag = divTag
 
if locals().get("followTag"):
    for personTag in followTag.find_all('dl'):
        p = person.person(personTag)
        print(p.__dict__)