with open('movie.txt','a',encoding='utf-8') as f:
	#把字典，列表，转化成字符串
	#json.dumps，将python对象编码成字符串。
	#json.loads，将字符串返回为python对象编码。

	data='123456' + ',\n'
	#write的内容，必须是str字符串
	f.write(data) 