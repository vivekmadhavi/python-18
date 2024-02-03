from requests import *
import os


try:
	url="https://zenquotes.io/api/image"
	res=get(url)
	print(res)
	
	filename=input("enter filename")
	if os.path.exists(filename):
		print(filename,"already exists")
	else:
		f=open(filename,"wb")
		f.write(res.content)
		print("download complete")
		f.close()
except Exception as e:
	print("issue",e)