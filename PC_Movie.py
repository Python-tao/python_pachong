#爬取猫眼电影，用xpath

import requests
from lxml import etree
import json

def getonepage(n):
	url='https://maoyan.com/board/4?offset={}'.format(n*10)
	header={'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}


	r=requests.get(url,headers=header)
	return r.text




def parse(text):
	#初始化 标准化
	
	html=etree.HTML(text)
	#提取信息
	names=html.xpath('//div[@class="movie-item-info"]/p[@class="name"]/a/@title')
	items=html.xpath('//p[@class="star"]/text()')
	stars=list()
	for item in items:
		stars.append(item.lstrip().rstrip())

		
	reltimes=html.xpath('//p[@class="releasetime"]/text()')
	
	movies={}
	for name,star,reltime in zip(names,stars,reltimes):
		movies['name']=name
		movies['star']=star
		movies['reltime']=reltime
		#生成器类型 循环迭代 . 因为字典列表，每次都是保存最新的值。通过yield，返回了当前页面的电影列表的generator类型数据，需要用for取出。。
		yield movies
	
	
	
#保存数据	
def save2file(data):
		#打开文件，模式为追加写入。
		with open('movie.json','a',encoding='utf-8') as f:
			#把字典，列表，转化成字符串
			#json.dumps，将python对象编码成字符串。
			#json.loads，将字符串返回为python对象编码。

			data=json.dumps(data,ensure_ascii=False) + ',\n'
			#write的内容，必须是str字符串
			f.write(data)
		print('文件写入完成。')	
def printfile():
	with open('movie.json',encoding='utf-8') as f:
		file=json.load(f)
		print(json.dumps(file))

			
	
def run():	
	for n in range(0,10):	
		data=getonepage(n)
		

		for movie in parse(data):
			print(movie)
			save2file(movie)
	#printfile()		


if __name__=='__main__':
	run()
