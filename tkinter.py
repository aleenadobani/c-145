# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:47:58 2022

@author: User
"""

from tkinter import *
root = Tk()

root.title("Addition")
root.geometry("400x200")

show_result=Label(root)

def add():
    result = 4+1
    show_result["text"]=result
    
btn = Button(root,text="Add",command=add)
btn.pack()

show_result.pack()

root.mainloop()