import socket
import sys
import tkinter
import select
from tkinter import messagebox
from tkinter import *
import threading
from threading import Thread

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#ip=input("Enter the ip address")
host="192.168.1.117"
port=9999
name=input('Enter your name : ')
sock.connect((host,port))
print("connected")
data1,server=sock.recvfrom(4096)
servername=data1.decode('ascii')
sent1=sock.sendto(name.encode('ascii'),(host,port))
root = Tk()
text = Text(root)
root.configure(bg='pink')
root.minsize(300,100)
root.geometry("360x650")
root.resizable(width=False, height=False)
text.configure(bg='pink',fg='black',height=50,width=150,font='Georgia')
root.title(servername)
nos = tkinter.Entry()
nos.pack(side=BOTTOM,anchor=E,fill=X)
def check():
	nums = (nos.get())
	sent=sock.sendto(nums.encode('ascii'),(host,port))
	nos.delete(0,END)
	if(nums!=''):
		text.insert(INSERT,"\n"+name+":"+nums)

def close():
	root.destroy()
	Thread(target = check).join()
	Thread(target = recdata).join()
		
	
b4 = Button(root, text = 'SEND',width=10, command = check)
b4.pack(side=BOTTOM,anchor=SE)
b3 = Button(root, text = 'QUIT',width=10, command = close)
b3.pack(side=BOTTOM,anchor=SE)

def recdata():
	flag=True
	while flag:
		data, server = sock.recvfrom(4096)	
		print("data in client",data)
		if data:
			text.insert(INSERT,"\n"+servername+":"+data.decode('ascii'))
	
		else:
			break

Thread(target = check).start()
Thread(target = recdata).start()

text.pack()
root.mainloop()
			
print ( 'closing socket')
sock.close()


