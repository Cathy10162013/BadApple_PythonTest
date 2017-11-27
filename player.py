from sys import argv
import os
import time
import Tkinter  

TXTPATH = os.getcwd()+'\\text\\'
#WIDTH = 80
#HEIGHT = 60
IMGNUM = sum([len(x) for _, _, x in os.walk(os.path.dirname(TXTPATH+'img0.png'))])   # get the num of pictures
FRAMETIME = 20


window = Tkinter.Tk()  
window.title('Bad Apple Player') 
#window.geometry('500x400')  
window.geometry('1000x850')  
#window['width'] = window.winfo_screenwidth()
#window['height'] = window.winfo_screenheight()
#window.overrideredirect(True)

x = 1
txtpage = ""
player = Tkinter.Label(window,text = txtpage,width=800,height=600,font=('Consolas',8),justify="left")  
player.pack()  
#time1 = time.time()
#print str(time1)

def trickit():
	global x 
	global time1
	txtpage = ""
	f = open(TXTPATH+'txt'+str(x)+'.txt','r')
	for line in f:
		txtpage = txtpage + line
	player.config(text = txtpage)
	window.update()
	f.close()
	x += 1
	if x <= IMGNUM:
		player.after(FRAMETIME, trickit)
#	else : 
	#	time2 = time.time() 
	#	print str(time2)
	#	print str(time2-time1)
	#	player.config(text = str(time2 - time1),font=('Consolas',8))

def trickit2():
    currentTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    
player.after(0, trickit)
window.mainloop()