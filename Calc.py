import tkinter

root = tkinter.Tk()
root.title("Calculator")


e = tkinter.Entry(root, width=40, borderwidth=5)
e.grid(row=0, columnspan=4, padx=10, pady=20)

Eval = ""

def Number_click(number):
	Current = e.get()
	e.delete(0, tkinter.END)
	e.insert(0, str(Current)+str(number))

def Add():
	Current = ""
	Current = e.get()
	e.delete(0, tkinter.END)
	global Eval
	Eval += str(Current)
	Eval += "+"

def Sub():
	Current = ""
	Current = e.get()
	e.delete(0, tkinter.END)
	global Eval
	Eval += str(Current)
	Eval += "-"

def mul():
	Current = e.get()
	e.delete(0, tkinter.END)
	global Eval
	Eval += str(Current)
	Eval += "*"

def div():
	Current = ""
	Current = e.get()
	e.delete(0, tkinter.END)
	global Eval
	Eval += str(Current)
	Eval += "/"

def equal():
	global Eval
	Eval += str(e.get())
	e.delete(0, tkinter.END)
	e.insert(0,eval(Eval))
	Eval = ""

def clear():
	e.delete(0, tkinter.END)
	global Eval
	Eval = ""
	

B7 = tkinter.Button(root, text='7', padx=40, pady=20, command=lambda: Number_click(7))
B8 = tkinter.Button(root, text=8, padx=40, pady=20, command=lambda: Number_click(8))
B9 = tkinter.Button(root, text=9, padx=40, pady=20, command=lambda: Number_click(9))
B4 = tkinter.Button(root, text=4, padx=40, pady=20, command=lambda: Number_click(4))
B5 = tkinter.Button(root, text=5, padx=40, pady=20, command=lambda: Number_click(5))
B6 = tkinter.Button(root, text=6, padx=40, pady=20, command=lambda: Number_click(6))
B1 = tkinter.Button(root, text=1, padx=40, pady=20, command=lambda: Number_click(1))
B2 = tkinter.Button(root, text=2, padx=40, pady=20, command=lambda: Number_click(2))
B3 = tkinter.Button(root, text=3, padx=40, pady=20, command=lambda: Number_click(3))
B0 = tkinter.Button(root, text=0, padx=40, pady=20, command=lambda: Number_click(0))
B_equal = tkinter.Button(root, text='=', padx=40, pady=21, command=equal).grid(row=4, column=0)
B_add = tkinter.Button(root, text="+", padx=20, pady=21, command=Add).grid(column=3, row=1, rowspan = 1)
B_sub = tkinter.Button(root, text="-", padx=20, pady=21, command=Sub).grid(column=3, row = 2, rowspan=1)
B_mul = tkinter.Button(root, text="x", padx=20, pady=21, command=mul).grid(column=3, row = 3, rowspan=1)
B_div = tkinter.Button(root, text="/", padx=20, pady=21, command=div).grid(column=3, row = 4, rowspan=1)
B_clear = tkinter.Button(root, text="CLEAR", padx=20, pady=21, command=clear).grid(column=2, row = 4, rowspan=1)

B7.grid(row=1, column=0)
B8.grid(row=1, column=1)
B9.grid(row=1, column=2)
B4.grid(row=2, column=0)
B5.grid(row=2, column=1)
B6.grid(row=2, column=2)
B1.grid(row=3, column=0)
B2.grid(row=3, column=1)
B3.grid(row=3, column=2)
B0.grid(row = 4, column = 1)


root.mainloop()
