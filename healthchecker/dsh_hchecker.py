from tkinter import*
import tkinter 
from PIL import Image,ImageTk
import sys
import os

def hc():
    os.system('python hchecker.py')
def cvd():
    os.system('python cvd19.py')
    
    
dsh=Tk()
dsh.title('Healthcare Dashboard')
dsh.geometry('1000x600')
dsh.iconbitmap(r'hc_images\dsh.ico')

img  = PhotoImage(file="hc_images//dshbg2.png")
img1 = PhotoImage(file="hc_images//hck1.png")
img2 = PhotoImage(file="hc_images//cvd1.png")

bgl = Label(dsh,image=img)
bgl.place(relwidth=1,relheight = 1)
btn1 = Button(dsh,image=img1,command=hc,border=0,)
btn1.pack(side = LEFT, expand = True, fill = X)

btn2 = Button(dsh,image=img2,command=cvd,border=0,)
btn2.pack(side = RIGHT, expand = True, fill =X)

dsh.mainloop()