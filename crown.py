import tkinter as tk, mysql.connector as ms
from tkinter import ttk

crown = tk.Tk()
crown.title('CRIME RECORD')
crown.iconb 
	result_frame.place(x = 280, y = 10)
	#sb = tk.Scrollbar(result_frame, orient='vertical')
	#sb.grid(row=0, column=1, sticky='ns')
	my_tree = ttk.Treeview(result_frame)
	#my_tree.config(yscrollcommand=sb.set)
	#sb.config(command=my_tree.yview)
	
	my_tree['columns'] = ("ID","Name","DOB","Rank","Age","EXPERIENCE")
	my_tree.column("#0", width = 0, stretch = 'no') 
	my_tree.column("ID",width = 50)
	my_tree.column("Name", width = 120)
	my_tree.column("DOB", width = 90)
	my_tree.column("Rank", width = 90)
	my_tree.column("Age", width  = 60)
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



def user_data():
	global ent_frame, Name_e, DOB_e, Rank_e, ID_e, Age_e, Exp_e	, my_tree
	crown.geometry('800x500')	
	ent_frame.grid(row = 3, column = 0, pady = 10, columnspan = 3)
	
	my_tree.grid(row = 0,pady = 10, padx = 15)	
	ID_l = tk.Label(ent_frame, text = 'ID', font = ('STENCIL',10))
	ID_l.grid(row = 0, column = 0, pady = 5)
	Name_l = tk.Label(ent_frame, text = 'Name', font = ('STENCIL',10))
	Name_l.grid(row = 1, column = 0, pady = 5)
	DOB_l = tk.Label(ent_frame, text = 'DOB', font = ('STENCIL',10))
	DOB_l.grid(row = 2, column = 0, pady = 5)
	ID_e = tk.Entry(ent_frame, font = ('Bookman Old style',10))
	ID_e.grid(row = 0, column = 1, pady = 5)
	Name_e = tk.Entry(ent_frame, font = ('Bookman Old style',10))
	Name_e.grid(row = 1, column = 1, pady = 5)
	DOB_e = tk.Entry(ent_frame, font = ('Bookman Old style',10))
	DOB_e.grid(row = 2, column = 1, pady = 5)
	Age_l = tk.Label(ent_frame, text = 'Age', font = ('STENCIL',10))
	Age_l.grid(row = 4, column = 0, pady = 5)
	Exp_l = tk.Label(ent_frame, text = 'Experience', font = ('STENCIL',10))
	Exp_l.grid(row = 5, column = 0, pady = 5)
	Age_e = tk.Entry(ent_frame, font = ('Bookman Old style',10))
	Age_e.grid(row = 4, column = 1, pady = 5)
	Exp_e = tk.Entry(ent_frame, font = ('Bookman Old style',10))
	Exp_e.grid(row = 5, column = 1, pady = 5)
	edit_data_b = tk.Button(ent_frame, font = ('Candara', 10), bg = '#D0F2CF', text = 'EDIT', command = edit_data, width = 10)
	edit_data_b.grid( row = 6, column = 0, pady = 5, columnspan = 2)

		
def edit_data():		
		con = ms.connect(host = 'localhost', user = 'root', passwd = 'yog14', database = 'project')
		cursor = con.cursor()
		error_l = tk.Label(text = 'ERROR ENTER ID!', font =('Candara',15), fg = 'red')
		if ID_e.get() == '':
			error_l.place(x = 320, y = 270)
			user_data()
			return 
		q = ''
		if Name_e.get() != '':
			q+= f"name = '{Name_e.get()}', "
		if DOB_e.get() != '':
			q += f'DOB = "{DOB_e.get()}", '		
		if Age_e.get()!= '':
			age = int(Age_e.get())
			q+= f'age = {age}, '
		if Exp_e.get() != '':
			exp = int(Exp_e.get())
			q+= f'experience = {exp}, '
		qry = q[:len(q)-2:1]
		fq = f'UPDATE user_info set {qry} where ID = {ID_e.get()}'
		if error_l.winfo_exists():
			error_l.place_forget()
		cursor.execute(fq)	
		con.commit()
		con.close()
		edit()
		user_data()	

def crime_edit():	
	con = ms.connect(host = 'localhost', user = 'root', passwd = 'yog14', database = 'project')
	cursor = con.cursor()
	if IDce.get() == '':
		error_l.place(x = 270, y =270)
		return
	else:
		q = ''
		if Ofce.get() != '':
			q+= f"offence = '{Ofce.get()}', "
		if Sce != '':
			q += f'IPC = "{Sce.get()}", '
		if Cce.get() != '':
			q += f'comment = "{Cce.get()}", '
		if CNce.get()!= '':
			CN = CNce.get()
			q+= f'name = {CN}, '		
		qry = q[:len(q)-2:1]
		fq = f'UPDATE crime_type set {qry} where ID = {IDce.get()}'
		cursor.execute(fq)	
		con.commit()
	con.close()	
	criminal_data()

ct = ttk.Treeview(cr)

def criminal_data():
	global crown, IDce, Ofce, Sce, Cce, CNce, CEnt, cr
	back()
	crown.geometry('800x500')
	
	cr.place(x = 325, y = 10)	
	
	ct['columns'] = ("ID","Name","Offence","IPC","Comment")
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
	ct.grid()

	
	CEnt.grid(row = 3, column = 0, pady = 10, columnspan = 3)
	IDcl = tk.Label(CEnt, text = 'ID:', font = ('Bookman Old style', 10, 'bold')).grid(row = 0, column = 0, sticky= 'W', padx = 5, pady = 5)
	IDce = tk.Entry(CEnt, font = ('Bookman Old style', 10))
	IDce.grid(row = 0, column = 1, padx = 5, pady = 5)
	Ofcl = tk.Label(CEnt, text = 'Offence Name:', font = ('Bookman Old style', 10, 'bold')).grid(row = 1, column = 0, sticky= 'W', padx = 5, pady = 5)
	Ofce = tk.Entry(CEnt, font = ('Bookman Old style', 10))
	Ofce.grid(row = 1, column = 1, padx = 5, pady = 5)
	Scl = tk.Label(CEnt, text = 'Section', font = ('Bookman Old style', 10, 'bold')).grid(row = 2, column = 0, sticky= 'W', padx = 5, pady = 5)
	Sce = tk.Entry(CEnt, font = ('Bookman Old style', 10))
	Sce.grid(row = 2, column = 1, padx = 5, pady = 5)
	Ccl = tk.Label(CEnt, text = 'Comment:', font = ('Bookman Old stylea', 10, 'bold')).grid(row = 3, column = 0, sticky= 'W', padx = 5, pady = 5)
	Cce = tk.Entry(CEnt, font = ('Bookman Old stylea', 10))
	Cce.grid(row = 3, column = 1, padx = 5, pady = 5)
	CNcl = tk.Label(CEnt, text = 'Criminal Name:', font = ('Bookman Old style', 10, 'bold')).grid(row = 4, column = 0, sticky= 'W', padx = 5, pady = 5)
	CNce = tk.Entry(CEnt, font = ('Bookman Old style', 10))
	CNce.grid(row = 4, column = 1, padx = 5, pady = 5)

	Scb = tk.Button(CEnt, text = 'SUBMIT', font = ('Bookman Old style', 10), command = crime_edit)
	Scb.grid(row = 5, columnspan = 2, pady = 10)


def back():
	global CEnt, cr
	if ct.winfo_exists():
		ct.place_forget()
	if ent_frame.winfo_exists():
		ent_frame.grid_forget()	
	if record_frame.winfo_exists():
		record_frame.grid_forget()
	if edit_frame.winfo_exists():
		edit_frame.grid_forget()
	if result_frame.winfo_exists():
		result_frame.place_forget()
	if CEnt.winfo_exists():
		CEnt.grid_forget()
	if cr.winfo_exists():
		cr.place_forget()

	crown.geometry('500x500')


def close():
	crown.destroy()	

def refresh():
	global crown
	crown.destroy()
	import crown

def add_record():
	global ID	
	name, off, ipc, comm = c_name_e.get(), c_off_e.get(), c_ipc_e.get(), c_comm_e.get()
	con = ms.connect(host = 'localhost', user ='root', passwd = 'yog14', database = 'project')
	cursor = con.cursor()
	qry = 'insert into crime_type(name,offence,IPC,comment) values("{}","{}","{}","{}")'.format(name, off, ipc, comm)
	cursor.execute(qry)
	con.commit()	
	con.close()
	SL = tk.Label(record_frame, text = 'SUBMITTED!', fg = 'green', font = ('Lucida bright',10)).grid(row = 5, columnspan = 2, column = 0)
	
result_frame = tk.Frame(crown)

def add():	
	global my_tree, c_name_e, c_off_e, c_ipc_e, c_comm_e
	back()
		
	crown.geometry('800x500')

	record_frame.grid(row = 0, column = 1, columnspan = 4, rowspan = 4, padx = 40)
	c_name_l = tk.Label(record_frame, text = 'Criminal Name :', font = ('Lucida bright', 12, 'bold')).grid(row = 0, column = 0, sticky = 'nw')
	c_off_l = tk.Label(record_frame, text = 'Offence :', font = ('Lucida bright', 12, 'bold')).grid(row = 1, column = 0, sticky = 'nw')
	c_ipc_l = tk.Label(record_frame, text = 'IPC :', font = ('Lucida bright', 12, 'bold')).grid(row = 2, column = 0, sticky = 'nw')
	c_comm_l = tk.Label(record_frame, text = 'Comment :', font = ('Lucida bright', 12, 'bold')).grid(row = 3, column = 0, sticky = 'nw')
	c_name_e = tk.Entry(record_frame, width = 50)
	c_name_e.grid(row = 0, column = 1, sticky = 'w')
	c_off_e = tk.Entry(record_frame, width = 50)
	c_off_e.grid(row = 1, column = 1, sticky = 'w')
	c_ipc_e = tk.Entry(record_frame, width = 50)
	c_ipc_e.grid(row = 2, column = 1, sticky = 'w')
	c_comm_e = tk.Entry(record_frame, width = 50)
	c_comm_e.grid(row = 3, column = 1, sticky = 'w')	

	sub_b = tk.Button(record_frame, text = 'Enter', command = add_record, font = ('Lucida bright', 12),bg = '#EED0B2', width = 10).grid(pady = 10,row = 4, column = 0, columnspan = 2)

def logo():	
	crown.destroy()
	import login

my_menu = tk.Menu(crown)
crown.config(menu = my_menu)
file_menu =tk.Menu(my_menu)
my_menu.add_cascade(label = 'File', menu = file_menu)
file_menu.add_command(label = 'Log out', command = logo)
file_menu.add_command(label = 'Back', command = back)
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
ID = c.fetchone()[0]
con.close()

logo = tk.PhotoImage(file ='crown.png')
logo = logo.subsample(3)
photo_label = tk.Label(crown, image = logo)


profile_frame = tk.Frame(crown)
option_frame = tk.LabelFrame(crown, text = 'Options', font = ('Lucida bright',10), width = 400, height = 300)
record_frame = tk.Frame(crown, width = 500, height = 300)
edit_frame = tk.Frame(crown, width = 500, height = 300)
ent_frame = tk.Frame(crown)

p_name = tk.Label(profile_frame, text =username, fg = 'black', font = ('Lucida bright',13, 'bold'))
p_rank = tk.Label(profile_frame, text =rank, fg = '#80193C', font = ('Lucida bright',13, 'bold'))
p_id = tk.Label(profile_frame, text =f'ID:{ID}', fg = 'Black', font = ('Lucida bright',13, 'bold'))


add_button = tk.Button(option_frame, text = 'ADD RECORD', font = ('Lucida bright',10), command = add, bg ='#D9D5E9')
edit_button = tk.Button(option_frame, text = 'EDIT RECORD', font = ('Lucida bright',10), bg = '#D9D5E9', command = edit)

photo_label.grid(row = 0, column = 0, sticky = 'W')
p_name.grid(row = 0, column = 0, sticky = 'W')
p_rank.grid(row = 0, column = 1, sticky = 'W')
p_id.grid(row = 0, column = 2, sticky = 'W')
profile_frame.place(x = 110, y = 5)
option_frame.grid(row = 1, column = 0, pady = 10, sticky = 'W')
add_button.grid(row = 0, column = 0, rowspan = 2, padx = 5, pady = 5)
edit_button.grid(row = 0, column = 1, rowspan = 2, padx = 5, pady = 5)


crown.mainloop()
