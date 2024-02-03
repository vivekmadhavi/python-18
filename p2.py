from requests import *
from datetime import * 


try:
	url="https://zenquotes.io/api/image"
	res=get(url)
	print(res)

	dt= datetime.now()
	print(dt)
	ndt = str(dt).replace("-" ,"_")
	ndt = str(ndt).replace(" " ,"_")
	ndt = str(ndt).replace(":" ,"_")
	ndt = str(ndt).replace("." ,"_")
	fn ="mm_" + str(ndt) + ".jpg"
	print(fn)
	f = open(fn ,"wb")
	f.write(res.content)
	print("download complete")
	f.close()
	
except Exception as e:
	print("issue",e)