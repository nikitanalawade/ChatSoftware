import socket
import sys
import tkinter
from tkinter import *
import threading
from threading import Thread

# Create a UDP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
host=socket.gethostbyname('192.168.1.117')
port=9999
name=input('Enter your name : ')
sock.bind((host,port))
sock.listen(1)
csocket, addr = sock.accept() 
sent1=csocket.sendto(name.encode('ascii'),(host,port))
data1,server=csocket.recvfrom(4096)
servername=data1.decode('ascii')
root = tkinter.Tk()
text = Text(root)
root.configure(bg='pink')
root.minsize(300,100)
root.geometry("350x650")
root.resizable(width=False, height=False)
text.configure(bg='pink',fg='black',height=50,width=150,font='Georgia')
root.title(servername)
nos = tkinter.Entry()
nos.pack(side=BOTTOM,anchor=E,fill=X)
def check():
	nums = (nos.get())
	sent=csocket.sendto(nums.encode('ascii'),(host,port))
	nos.delete(0,END)
	if(nums!=''):
		text.insert(INSERT,"\n"+name+":"+nums)

def close():
	root.destroy()
	t=Thread(target = check).join()
	t1=Thread(target = recdata).join()

b4 = Button(root, text = 'SEND',width=10, command = check)
b4.pack(side=BOTTOM,anchor=SE)
b3 = Button(root, text = 'QUIT',width=10, command = close)
b3.pack(side=BOTTOM,anchor=SE)

def recdata():
	flag=True
	while True:
		data, server = csocket.recvfrom(4096)
		if data:
			text.insert(INSERT,"\n"+servername+":"+data.decode('ascii'))
			print(servername,': %s' % data.decode('ascii'))
		else:
			break

Thread(target = check).start()
Thread(target = recdata).start()

text.pack()
root.mainloop()
print('closing socket')
sock.close()