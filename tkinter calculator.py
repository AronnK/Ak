#calculator
from tkinter import *

window = Tk()
window.title("Calculator")

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_del():
    global expression
    val = str(expression)
    expression = val[0:-1]
    input_text.set(expression)
    
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    try:
 
        global expression
        total = str(eval(expression))
 
        input_text.set(total)
 
        expression = ""

    except:
 
        input_text.set(" error ")
        expression = ""

expression = ""
input_text = StringVar()

input_frame = Frame(window, bd = 0, highlightbackground = "black", highlightcolor = "black")
input_frame.pack(side = TOP)

input_field = Entry(input_frame, font = ('arial', 10, 'bold'), textvariable = input_text, width = 50, bg = '#eee', bd = 0)
input_field.pack(ipady = 10)

btns_frame = Frame(window, bg = 'grey')
btns_frame.pack()

delt= Button(btns_frame, text = "delt", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5", command = btn_del).grid(row=5,column=1)
clear = Button(btns_frame, text = "C", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5", command = btn_clear).grid(row=5,column=2)
bt9 = Button(btns_frame, text = "9", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36", command = lambda:btn_click(9)).grid(row=1, column=2)
bt8 = Button(btns_frame, text = "8", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36", command = lambda:btn_click(8)).grid(row=1, column=1)
bt7 = Button(btns_frame, text = "7", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36", command = lambda:btn_click(7)).grid(row=1, column=0)
bt6 = Button(btns_frame, text = "6", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36", command = lambda:btn_click(6)).grid(row=2, column=2)
bt5 = Button(btns_frame, text = "5", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36", command = lambda:btn_click(5)).grid(row=2, column=1)
bt4 = Button(btns_frame, text = "4", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36", command = lambda:btn_click(4)).grid(row=2, column=0)
bt3 = Button(btns_frame, text = "3", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36", command = lambda:btn_click(3)).grid(row=3, column=2)
bt2 = Button(btns_frame, text = "2", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36", command = lambda:btn_click(2)).grid(row=3, column=1)
bt1 = Button(btns_frame, text = "1", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36", command = lambda:btn_click(1)).grid(row=3, column=0)
bt0 = Button(btns_frame, text = '0', width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36", command = lambda:btn_click(0)).grid(row=4, column=0)
btx = Button(btns_frame, text = '(', width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36", command = lambda:btn_click('(')).grid(row=4, column=1)
bty = Button(btns_frame, text = ')', width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36", command = lambda:btn_click(')')).grid(row=4, column=2)
bte = Button(btns_frame, text = "=", width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#fe9037", command = lambda:btn_equal()).grid(row=5, column=3)
btadd = Button(btns_frame, text = '+', width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36", command = lambda:btn_click('+')).grid(row=1, column=3)
btsub = Button(btns_frame, text = '-', width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36", command = lambda:btn_click('-')).grid(row=2, column=3)
btmul = Button(btns_frame, text = '*', width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36", command = lambda:btn_click('*')).grid(row=3, column=3)
btdiv = Button(btns_frame, text = '/', width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36", command = lambda:btn_click('/')).grid(row=4, column=3)
btdec = Button(btns_frame, text = '.', width=5, height=1, font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5", command = lambda:btn_click('.')).grid(row=5, column=0)
