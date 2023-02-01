from tkinter import *
import mysql.connector as ms
import tkinter.messagebox

root = Tk()
root.geometry('500x500')
root.title("LOGIN INTERFACE")
Label1 = Label(root, text="WELCOME TO CRIMINAL DATABASE", font=(
    "Algerian", 18, "bold"), fg="grey", relief=GROOVE)
Label1.pack(fill=BOTH)

logo = PhotoImage(file='crime records.png')
photo_label = Label(root, image=logo).pack()


def toggle():
    root1.destroy()
    import login


def submitt(x, y):
    global root1, top
    with open('temp_data.txt', 'w') as temp_data:
        temp_data.write(x)
    pwd = ''
    con = ms.connect(host='localhost', user='root',
                     passwd='yog14', database='project')
    cursor = con.cursor()
    cursor.execute(f"select password from user_info where name = '{x}' ")
    pwd = cursor.fetchone()

    try:
        if pwd[0] == y:
            cursor.execute(f"select RANKING from user_info where name = '{x}'")
            rank = cursor.fetchone()[0]

            if rank == 'ACE':
                top.destroy()
                import ace
                try:
                    if root.winfo_exists():
                        root.destroy()
                except TclError:
                    pass
            if rank == 'CROWN':
                top.destroy()
                import crown
                try:
                    if root.winfo_exists():
                        root.destroy()
                except TclError:
                    pass
            if rank == 'DIAMOND':
                top.destroy()
                import diamond

                try:
                    if root.winfo_exists():
                        root.destroy()
                except TclError:
                    pass

        else:
            Label3 = Label(top, text="wrong pwd/username try again",
                           font="ALGERIAN ", fg='black').pack(fill=BOTH)

    except TypeError:
        Label3 = Label(top, text="wrong pwd/username try again",
                       font="ALGERIAN ", fg='black').pack(fill=BOTH)


def loginn():
    global top, Entry1, Entry2
    try:
        root.destroy()
    except TclError:
        pass
    top = Tk()
    top.geometry('500x500')

    top.title("CRIME RECORDS")
    Label1 = Label(top, text="USERNAME : ", font=(
        "Felix Titling", 12, "bold"), fg='#554540')
    Label1.place(x=150, y=150)
    var1 = StringVar()
    Entry1 = Entry(top, text=var1)
    Entry1.place(x=300, y=150)
    Label2 = Label(top, text="PASSWORD : ", font=(
        "Felix Titling", 12, "bold"), fg='#554540')
    Label2.place(x=150, y=180)
    var2 = StringVar()
    Entry2 = Entry(top, text=var2, show='*')
    Entry2.place(x=300, y=182)

    b1 = Button(top, text="QUIT", command=top.destroy, padx=2, pady=2)
    b1.place(x=420, y=460)

    b2 = Button(top, text="SUBMIT", fg='black',
                command=lambda: submitt(Entry1.get(), Entry2.get()))
    b2.place(x=350, y=460)


def quitt():
    root.destroy()


def gt():
    root.destroy()
    import guest


def log():
    l1 = Label(root1, text="WELCOME TO OUR SERVER!!",
               font=("Alegrian", 15, 'bold')).pack()
    con = ms.connect(host='localhost', user='root',
                     passwd='yog14', database='project')
    cursor = con.cursor()
    qry = f"INSERT INTO user_info(name, password, DOB, age, experience) VALUES('{Entry1.get()}','{Entry2.get()}','{Entry3.get()}',{Entry5.get()},{Entry6.get()})"
    cursor.execute(qry)
    con.commit()


def register():
    global root1, Entry1, Entry2, Entry5, Entry6, Entry3
    try:
        root.destroy()
    except TclError:
        pass
    root1 = Tk()
    root1.geometry('400x400')
    root1.title("REGISTER")
    Label1 = Label(root1, text="Enter Your Name : ",
                   font=("Felix Titling", 11, "bold")).pack()
    a1 = StringVar()
    Entry1 = Entry(root1, text=a1)
    Entry1.pack()
    Label2 = Label(root1, text="Enter Password : ",
                   font=("Felix Titling", 11, 'bold')).pack()
    a2 = StringVar()
    Entry2 = Entry(root1, text=a2, show="*")
    Entry2.pack()
    a3 = StringVar()
    Label3 = Label(root1, text="DOB:", font=(
        'Felix Titling', 11, 'bold')).pack()
    Entry3 = Entry(root1, text=a3)
    Entry3.pack()
    Label5 = Label(root1, text="AGE", font=(
        "Felix Titling", 11, "bold")).pack()
    a5 = StringVar()
    Entry5 = Entry(root1, text=a5)
    Entry5.pack()
    Label6 = Label(root1, text="EXPERIENCE", font=(
        "Felix Titling", 11, "bold")).pack()
    a6 = StringVar()
    Entry6 = Entry(root1, text=a6)
    Entry6.pack()

    Button1 = Button(root1, text="SUBMIT", command=log)

    Button1.pack(padx=4)
    B2 = Button(root1, text="QUIT", command=root1.destroy)
    B2.place(x=320, y=360)

    b3 = Button(root1, text="BACK", font=("Countryside", 8), command=toggle)
    b3.place(x=270, y=360)

    root1.mainloop()


Button1 = Button(root, text="LOGIN", font="Algerian",
                 fg='black', bg='white', relief=RIDGE, command=loginn)
Button1.place(x=225, y=370)

Button2 = Button(root, text="EXIT", font="Algerian", fg='black',
                 bg='white', relief=RIDGE, command=quitt)
Button2.place(x=125, y=370)


Button3 = Button(root, text="SIGN UP", font="Algerian",
                 fg='black', bg='white', relief=RIDGE, command=register)
Button3.place(x=325, y=370)

Button4 = Button(root, text="Continue as guest", font="Algerian",
                 fg='black', bg='white', relief=RIDGE, command=gt)
Button4.place(x=175, y=425)


var3 = StringVar()


root.mainloop()
