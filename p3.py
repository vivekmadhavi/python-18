from requests import *
from datetime import * 
import re


try:
	url="https://zenquotes.io/api/image"
	res=get(url)
	print(res)

	dt= datetime.now()
	print(dt)
	ndt = re.sub("[-.: ]","_",str(dt))
	fn ="mm_" + str(ndt) + ".jpg"
	print(fn)
	f = open(fn ,"wb")
	f.write(res.content)
	print("download complete")
	f.close()
	
except Exception as e:
	print("issue",e)