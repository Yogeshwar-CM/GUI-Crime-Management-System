import tkinter as tk, mysql.connector as ms
from tkinter import ttk
import matplotlib.pyplot as pt

guest = tk.Tk()
guest.title('CRIME RECORD')
guest.iconbitmap('police-order.ico')

#GEOMETRY

guest.geometry('450x320')

##############################################################################################################################

wl = tk.Label(guest, text = 'Welcome! You are signed in as Guest', font = ('courrier new',10, 'bold')).grid(row = 0, column = 0, columnspan = 3, sticky = 'N', padx = 10, pady = 5)

ttk.Label(guest, text="Enter your complain:\n(add your contact also)",
          font=("Times New Roman", 13)).grid(column=0, row=15, padx=10, pady=25, sticky = 'N')
  
t = tk.Text(guest, width=30, height=10)
  
t.grid(column=1, row=15)

def fi():
	t.delete('1.0','end-1c')
	#t.insert('1.0',fq)
	pt.show()

def get_input():
   value=t.get("1.0","end-1c")
   t.delete('1.0','end-1c')
   with open('complain.txt','a') as f:   	
   	f.write(value)
   	f.write('\n---------------------------\n')
   sl = tk.Label(text = 'We will look into your complain as soon as possible!', font = ('Felix Titling',10)).grid(columnspan = 3, pady = 10)

sb = tk.Button(guest, text = 'SUBMIT', command = get_input, font = ('Felix Titling',15)).grid(columnspan = 3, pady = 10)
fb = tk.Button(guest, text = 'Frequency Graph', command = fi, font = ('Felix Titling',10)).grid(columnspan = 3, pady = 10)

con = ms.connect(host = 'localhost', user ='root', passwd = 'yog14', database = 'project')
cursor = con.cursor()
cursor.execute('select count(name),name from crime_type group by name order by count(name) desc')
fq = cursor.fetchall()

fl = tk.LabelFrame(guest,text = 'Most Wanted Criminals').grid(columnspan = 3, pady = 5)
	

def close():
	guest.destroy()	


def logo():	
	guest.destroy()
	import login

def refresh():
	global ace
	ace.destroy()
	import ace

x = []
y = []
for i in fq:
	x.append(i[-1])
	y.append(i[0])

pt.plot(x, y)


my_menu = tk.Menu(guest)
guest.config(menu = my_menu)
file_menu =tk.Menu(my_menu)
my_menu.add_cascade(label = 'File', menu = file_menu)
file_menu.add_command(label = 'Logout', command = logo)
file_menu.add_command(label = 'Refresh', command = refresh)
file_menu.add_command(label = 'Exit', command = close)


con.close()
guest.mainloop()
