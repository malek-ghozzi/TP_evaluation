import tkinter as tk
from tkinter import *
from tkinter import Entry, Label, Radiobutton
import os
from threading import Thread

def run_cl1():
    
    os.system(r"D:\Kraya\2DNI\TP\Eval_Perfor\TP3_evalperform\To_open\Client_1.lnk")

def run_cl2():
    
    Thread(target = run_cl1).start()
    os.system(r"D:\Kraya\2DNI\TP\Eval_Perfor\TP3_evalperform\To_open\Client_2.lnk")

def run_cl3():

    Thread(target = run_cl1).start()
    Thread(target = run_cl2).start()
    os.system(r"D:\Kraya\2DNI\TP\Eval_Perfor\TP3_evalperform\To_open\Client_3.lnk")

def run_proxy():
    
    os.system(r"D:\Kraya\2DNI\TP\Eval_Perfor\TP3_evalperform\To_open\Proxy_Server.lnk")


def run_web():
    
    os.system(r"D:\Kraya\2DNI\TP\Eval_Perfor\TP3_evalperform\To_open\Web_Server.lnk")
    
def background(func):
    
    Thread(target=func).start()
    

win = tk.Tk()
win.title("TP3 évaluation de performance")
win.geometry("400x500")
frame = tk.Frame(win)
frame.pack()
var = IntVar()
rad1 = Radiobutton(frame,text='Un Client', variable=var, value=1, command=lambda: background(run_cl1))
rad1.deselect()
rad2 = Radiobutton(frame,text='Deux Clients', variable=var, value=2, command=lambda: background(run_cl2))
rad2.deselect()
rad3 = Radiobutton(frame,text='Trois Clients', variable=var, value=3, command=lambda: background(run_cl3))
rad3.deselect()

rad1.grid(column=3, row=0,pady=10,padx=100)
rad2.grid(column=3, row=1,pady=10,padx=100)
rad3.grid(column=3, row=2,pady=10,padx=100)

btn_proxy = tk.Button(frame,text="Serveur Proxy",fg="red",height="5",width="12", command=lambda: background(run_proxy))
btn_proxy.grid(row=3,column=3,pady=10,padx=100)
btn_web = tk.Button(frame,text="Serveur Web",fg="blue",height="5",width="12", command=lambda: background(run_web))
btn_web.grid(row=4,column=3,pady=10,padx=100)

txt=Label(frame,text="© Malek Ghozzi & Med Amine Boufares")
txt.grid(row=6,column=3,pady=50,padx=100)

win.mainloop()