import tkinter as tk, mysql.connector as ms
from tkinter import ttk

diamond = tk.Tk()
diamond.title('CRIME RECORD')
diamond.iconbitmap('police-order.ico')

#GEOMETRY

w, h = 500, 500
sw = diamond.winfo_screenwidth()
sh = diamond.winfo_screenheight()

print(sw,sh)
x = (sw/2)-(w/2)
y = (sh/2)-(h/2)

diamond.geometry(f'{w}x{h}+{int(x)}+{int(y)}')

##############################################################################################################################

cr = tk.Frame(diamond)

def back():
	if cr.winfo_exists():
		cr.place_forget()
	if ct.winfo_exists():
		ct.grid_forget()
	if ut.winfo_exists():
		ut.grid_forget()

	diamond.geometry('500x500')


def close():
	diamond.destroy()	

def refresh():
	global diamond
	diamond.destroy()
	import diamond

ut= ttk.Treeview(cr)
ct = ttk.Treeview(cr)

def logo():	
	diamond.destroy()
	import login


my_menu = tk.Menu(diamond)
diamond.config(menu = my_menu)
file_menu =tk.Menu(my_menu)
my_menu.add_cascade(label = 'File', menu = file_menu)
file_menu.add_command(label = 'Back', command = back)
file_menu.add_command(label = 'Log Out', command = logo)
file_menu.add_command(label = 'Refresh', command = refresh)
file_menu.add_command(label = 'Exit', command = close)


con = ms.connect(host = 'localhost',
				user = 'root',
				passwd = 'yog14',
				database = 'project')
c = con.cursor()
with open('temp_data.txt','r') as f:
	username = f.read()

c.execute(f'select ranking from user_info where name = "{username}"')
rank = c.fetchone()
c.execute(f'select ID from user_info where name = "{username}"')
ID = c.fetchone()[0]ghm
con.close()kleb PhotoImage
 grid_forget 
logo = tk.PhotoImage(file ='diamond.png')
logo = logo.subsample(2)
photo_label = tk.Label(diamond, image = logo)


profile_frame = tk.Frame(diamond)

p_name = tk.Label(profile_frame, text =username, fg = 'black', font = ('Lucida bright',13, 'bold'))
p_rank = tk.Label(profile_frame, text =rank, fg = '#80193C', font = ('Lucida bright',13, 'bold'))
p_id = tk.Label(profile_frame, text =f'ID:{ID}', fg = 'Black', font = ('Lucida bright',13, 'bold'))

diamond.geometry('550x600')
cr.place(x = 30, y = 80)	
	
ct['columns'] = ("ID","Name","Offence","IPC","Comment").grid width gjd;,diamond  
ct.column("#0", width = 0, stretch = 'no')
ct.column("ID",width = 70)
ct.column("Name", width = 100)
ct.column("Offence", width = 90)
ct.column("IPC", width = 70)
ct.column("Comment", width = 120)

ct.heading("#0", text = '')
ct.heading("ID", text = 'Criminal ID', anchor = 'w')
ct.heading("Name", text = 'Name', anchor = 'w')
ct.heading("Offence", text = 'Offence', anchor = 'center')
ct.heading("IPC", text = "IPC")
ct.heading("Comment", text = "Comment")

con = ms.connect(host = 'localhost', user = 'root', passwd = 'yog14', database= 'project')
cursor = con.cursor()
cursor.execute("SELECT * FROM crime_type")
x = cursor.fetchall()
for i in x:
	ct.insert(parent = '', index = 'end', text = "", values = (i[0], i[1],i[2],i[-2],i[-1]))
con.close()
ct.grid(row = 1 , column = 0, padx = 20, pady = 7)

my_tree = ttk.Treeview(cr)

my_tree['columns'] = ("ID","Name","DOB","Rank","Age","EXPERIENCE")
my_tree.column("#0", width = 0, stretch = 'no')
my_tree.column("ID",width = 50)
my_tree.column("Name", width = 120)
my_tree.column("DOB", width = 90)
my_tree.column("Rank", width = 90)
my_tree.column("Age", width = 60)
my_tree.column("EXPERIENCE", width = 80)

my_tree.heading("#0", text = '')
my_tree.heading("ID", text = 'User ID', anchor = 'w')
my_tree.heading("Name", text = 'UserName', anchor = 'w')
my_tree.heading("DOB", text = 'DOB', anchor = 'center')
my_tree.heading("Rank", text = "Rank")
my_tree.heading("Age", text = "Age")
my_tree.heading("EXPERIENCE", text = "Experience")

con = ms.connect(host = 'localhost', user = 'root', passwd = 'yog14', database= 'project')
cursor = con.cursor()
cursor.execute("SELECT * FROM user_info")
x = cursor.fetchall()
for i in x:
	my_tree.insert(parent = '', index = 'end', text = "", values = (i[0], i[1],i[3],i[4],i[-2],i[-1]))
con.close()

my_tree.grid(row = 0, column = 0, pady = 7)

con = ms.connect(host = 'localhost', user = 'root', passwd = 'yog14', database= 'project')
cursor = con.cursor()
cursor.execute("SELECT * FROM crime_type")
x = cursor.fetchall()
for i in x:
	ut.insert(parent = '', index = 'end', text = "", values = (i[0], i[1],i[2],i[-2],i[-1]))
con.close()
ut.grid(row = 1, column = 0)


photo_label.grid(row = 0, column = 0, sticky = 'W')
p_name.grid(row = 0, column = 0, sticky = 'W')
p_rank.grid(row = 0, column = 1, sticky = 'W')
p_id.grid(row = 0, column = 2, sticky = 'W')
profile_frame.place(x = 90, y = 5)

diamond.mainloop()
