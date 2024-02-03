from tkinter import *
from requests import *
from datetime import *
import re
from PIL import Image,ImageTk 


root=Tk()
root.title("motivational image")
root.geometry("12000x600+50+50")
f=("Century" , 20,"bold")



def gi():
	try:
		#accesing the api
		url="https://zenquotes.io/api/image"
		res=get(url)
		print(res)

		#downloading the image
		dt= datetime.now()
		print(dt)
		ndt = re.sub("[-.: ]","_",str(dt))
		fn ="mm_" + str(ndt) + ".jpg"
		f = open(fn ,"wb")
		f.write(res.content)
		f.close()

		#show image in window
		im = Image.open(fn)
		imt = ImageTk.PhotoImage(image=im)
		lab.configure(image=imt)
		lab.photo=imt
	except Exception as e:
		print("issue",e)


btn = Button(root,text="get image",font=f,command=gi)
btn.pack(pady=20)
lab = Label(root)
lab.pack(pady=20)

root.mainloop()
	


		
	