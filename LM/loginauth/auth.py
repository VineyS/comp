####################################
######   IMPORTING MODULES    ######
####################################
from tkinter import Tk, Toplevel, Label, Button, Entry, StringVar, Message, Frame, font, mainloop , PhotoImage, Canvas
from tkinter.constants import CURRENT, E, END, HIDDEN, LEFT, NO, RIGHT, VERTICAL, Y
from tkinter import ttk
from datetime import datetime
from loginauth import mysqlauth
####################################
######   SQL AUTHENTICATION   ######
####################################
mysql = mysqlauth.db_login()
cursor = mysql.cursor(buffered = True)

print("Connection Established!!")
'''
try:
    cursor.execute("CREATE DATABASE TEST")
except:
    cursor.execute("USE TEST")
    #cursor.execute("CREATE TABLE AUTHENTICATION(id int(255) auto_increment, PRIMARY KEY(id), email varchar(256), password varchar(256), uuid text(256))")
else:
    cursor.execute("USE TEST")
    cursor.execute("CREATE TABLE AUTHENTICATION(id int(255) auto_increment, PRIMARY KEY(id), email varchar(256), password varchar(256), uuid text(256))")
   '''             
                


email_verification = ""



##############################################
######      AUTHORIZATION  WINDOW       ######
##############################################

def main_window():
    window = Tk()
    window.title("Client Area Login")
    filename = PhotoImage(file = "loginauth/assets/user.png")
    # user.png image
    background_label = Label(window, image=filename)
    background_label.place(x=150, y=10, height=190, width=110)
    window.geometry("400x470")
    window.configure(bg = "#29095E")

    # window text
    text = Label(window, text= "Client Login")
    text.pack()
    text.config(font=("Arial", 25), background= "#29095E", foreground="white")
    text.place(x=120, y = 200)
    email_text = Label(window, text= "Email: ")
    email_text.config(font= ("Arial", 15), background= "#29095E", foreground= "white")
    email_text.place(x = 60, y = 250)
    pass_text = Label(window, text= "Password: ")
    pass_text.config(font= ("Arial", 15), background= "#29095E", foreground= "white")
    pass_text.place(x = 60, y = 280)
    end_text = Label(window,text = "CLASS 12 © 2021 ")
    end_text.config(font = ("Arial", 10), foreground="grey", background= "#29095E")
    end_text.place(x = 150, y = 450)

    # Fields
    email = StringVar()
    password = StringVar()
    email_entry = Entry(window, textvariable= email)
    password_entry = Entry(window, textvariable= password, show = "•")
    email_entry.config(font= ("Arial", 10))
    password_entry.config(font= ("Arial", 10))
    email_entry.place(x = 170, y = 255)
    password_entry.place(x = 170, y = 285)
    #functions

    def login():
        email_get = email.get()
        password_get = password.get()
        if not email_get:
            warn = Toplevel(window)
            warn.geometry('300x10')
            warn.title('Empty Field Error')
            a = Label(warn, text="Email Section is empty, please fill it with your email.")
            a.pack()
        elif email_get.lstrip(' ') == '':
            warn = Toplevel(window)
            warn.geometry('300x10')
            warn.title('Empty Field Error')
            a = Label(warn, text="Email Section is empty, Enter a valid email")
            a.pack()
        elif '@' not in email_get:
            warn = Toplevel(window)
            warn.geometry('100x100')
            warn.title('Invalid Email')
            a = Label(warn, text="Invalid Email! Enter a valid email.")
            a.pack()
        elif password_get.lstrip(' ') == '':
            warn = Toplevel(window)
            warn.geometry('500x10')
            warn.title('Empty Field Error')
            a = Label(warn, text="Password Section is filled with spaces only, Enter a valid password.")
            a.pack()
        else:
            cursor.execute(f'SELECT * FROM AUTHENTICATION WHERE email = "{email_get}"')
            result = cursor.fetchone()
            if result is None:
                def error_stats():
                    error = Toplevel(window)
                    error.title("Unknown Email")
                    error.geometry('300x300')
                    a = Label(error, text=f"No Email Was Found! Kindly Register!")
                    a.pack()
                    error.mainloop()
                error_stats()
            elif result is not None:
                cursor.execute(f'SELECT password from AUTHENTICATION where email = "{email_get}"')
                result1 = cursor.fetchone()
                if result1[0] == password_get:
                    access = Toplevel(window)
                    access.geometry("500x100")
                    access.title("Access Granted")
                    access1 = Label(access, text="Logged In Successfully , Click OK to continue")
                    access1.pack()
                    access2 = Label(access, text ="")
                    access2.pack()
                    access3 = Label(access, text ="")
                    access3.pack()
                    access4 = Label(access, text ="")
                    access4.pack()
                    def destroy():
                        access.destroy()
                        window.destroy()
                        global email_verification
                        email_verification = email_get

                        ######################################
                        ########     MAIN PROGRAM     ########
                        ######################################
                        verify = f"SELECT uuid FROM AUTHENTICATION WHERE email = '{email_get}'"
                        cursor.execute(verify)
                        result2 = cursor.fetchone()
                        #dec = decode24(result2[0])
                        #ultra_dec = dec.decode('utf-8')
                        ultra_dec = result2[0]
                        print(ultra_dec)
                        if ultra_dec == email_verification:
                            window2 = Tk()
                            #ultra_dec = "viney@gmail.com"
                            window2.geometry("650x550")
                            window2.title("Main Page  -  Library Management")
                            title = Label(window2, text="ADMIN PANEL")
                            title.config(font=("Helvetica", 30), background= "lightgreen")
                            title.place(x = 20, y = 30)
                            em_display = Label(window2,text= ultra_dec)
                            em1_display = Label(window2, text= "LOGGED IN AS")
                            em1_display.config(font=('Arial', 10), background= "lightgreen")
                            em_display.config(font = ('Arial', 15), background="lightgreen")
                            em_display.place(x = 420, y = 20)
                            em1_display.place(x = 420, y = 5)
                            line_break = Label(window2, text= "___________________________________________________________________")
                            line_break.config(font= ("Arial"), background= "lightgreen")
                            line_break.place(x = 0, y = 80)
                            def logout():
                                window2.destroy()
                                main_window()
                            log_out = Button(window2, text= "LOGOUT", command=logout)
                            log_out.config(font=("Arial", 10))
                            log_out.place(x=550,y=55)

                            ##########################
                            ##### BUTTON COMMANDS ####
                            ##########################
                            def add():
                                addbook = Toplevel(window2)
                                addbook.title("ADD RECORD")
                                addbook.geometry("450x450")
                                atitle = Label(addbook, text = "ADD BOOK")
                                atitle.config(font= ("Arial",25))
                                atitle.place(x = 130, y = 20)
                                a1 = Label(addbook, text= "Book Name: ")
                                a1.config(font= ("Arial",15))
                                book_author = Label(addbook, text= "Book Author: ")
                                book_author.config(font = ("Arial", 15))
                                book_author.place(x = 10, y = 120+30)
                                a1.place(x = 10,y = 80+30)
                                a2 = Label(addbook, text= "Borrower's Name: ")
                                a2.config(font= ("Arial", 15))
                                a2.place(x = 10,y = 160+30)
                                a3 = Label(addbook, text= "Date Of Withdrawal: ")
                                a3.config(font= ("Arial", 15))
                                a3.place(x = 10,y = 200+30)
                                a4 = Label(addbook, text= "Date Of Return: ")
                                a4.config(font= ("Arial", 15))
                                a4.place(x = 10,y = 240+30)
                                a5 = Label(addbook, text= "Current Status :  ")
                                a5.config(font= ("Arial", 15))
                                a5.place(x = 10,y = 280+30)

                                book = StringVar()
                                author = StringVar()
                                date_of_withdrawal = StringVar()
                                date_of_return = StringVar()
                                status = StringVar()
                                withd = StringVar()

                                book_entry = Entry(addbook, textvariable = book)
                                book_entry.config(font= ("Arial", 10))
                                book_entry.place(x = 140, y = 85+30)
                                author_entry = Entry(addbook, textvariable = author)
                                author_entry.config(font= ("Arial", 10))
                                author_entry.place(x = 180, y = 155)
                                stuname = Entry(addbook, textvariable= withd)
                                stuname.config(font = ("Arial", 10))
                                stuname.place(x = 200, y = 195)
                                dow_entry = Entry(addbook, textvariable = date_of_withdrawal)
                                dow_entry.config(font= ("Arial", 10))
                                dow_entry.place(x = 200, y = 205+30)
                                dow_entry.insert(END, datetime.today().strftime("%Y-%m-%d"))
                                dor_entry = Entry(addbook, textvariable = date_of_return)
                                dor_entry.config(font= ("Arial", 10))
                                dor_entry.place(x = 160, y = 245+30)
                                status_entry = Entry(addbook, textvariable = status)
                                status_entry.config(font= ("Arial", 10))
                                status_entry.place(x = 160, y = 285+30)
                                status_entry.insert(END, "Borrowed/Returned")
                                def add_sub():
                                    b = book.get()
                                    a = author.get()
                                    dow = date_of_withdrawal.get()
                                    dor = date_of_return.get()
                                    st = status.get()
                                    w = withd.get()
                                    sql = f'INSERT INTO `{ultra_dec}` (book, author, date_of_withdrawal, date_of_return, withdrawer_name, current_status) VALUES (%s,%s,%s,%s,%s,%s)'
                                    val = (b,a,dow,dor,w,st)
                                    cursor.execute(sql, val)
                                    mysql.commit()
                                    def success_window():
                                        sw = Toplevel(addbook)
                                        sw.title("SUCCESS")
                                        book_entry.delete(0, END)
                                        author_entry.delete(0, END)
                                        stuname.delete(0, END)
                                        dor_entry.delete(0, END)
                                        status_entry.delete(0, END)
                                        s = Label(sw, text= "Records Added Successfully!")
                                        s.pack()
                                    success_window()
                                sub = Button (addbook, text = "SUBMIT", command= add_sub)
                                sub.config(font= ("Arial", 10), width= 30)
                                sub.place(x = 100, y = 360)

                                addbook.mainloop()

                            def remove():
                                removebook = Toplevel(window2)
                                removebook.title("REMOVE RECORD")
                                removebook.geometry("450x300")
                                atitle = Label(removebook, text = "REMOVE BOOK")
                                atitle.config(font= ("Arial",25))
                                atitle.place(x = 130, y = 20)
                                a1 = Label(removebook, text= "Enter ID: ")
                                a1.config(font= ("Arial",15))
                                a1.place(x = 10,y = 110)

                                id_check = StringVar()
                                id_entry = Entry(removebook, textvariable = id_check)
                                id_entry.config(font= ("Arial", 10))
                                id_entry.place(x = 140, y = 115)
                                
                                def remove_sub():
                                    id_get = id_check.get()
                                    cursor.execute(f"SELECT id FROM `{ultra_dec}` WHERE id = {id_get}")
                                    result1 = cursor.fetchone()
                                    if result1 is None:
                                        def error_stats():
                                            error = Toplevel(removebook)
                                            error.title("Unknown Record")
                                            error.geometry('300x300')
                                            a = Label(error, text=f"No Record Found with ID: {id_get}")
                                            a.pack()
                                            error.mainloop()
                                        error_stats()
                                    elif result1 is not None:
                                        sql = f"DELETE FROM `{ultra_dec}` WHERE id = %s"
                                        val = (id_get,)
                                        cursor.execute(sql, val)
                                        mysql.commit()
                                        def success_window():
                                            sw = Toplevel(removebook)
                                            sw.title("SUCCESS")
                                            s = Label(sw, text= "Record Removed Successfully!")
                                            id_entry.delete(0, END)
                                            s.pack()
                                        success_window()
                                sub = Button (removebook, text = "SUBMIT", command= remove_sub)
                                sub.config(font= ("Arial", 10), width= 30)
                                sub.place(x = 100, y = 150)

                                removebook.mainloop()
                            
                            def update():
                                updatebook = Toplevel(window2)
                                updatebook.title("EDIT RECORD")
                                updatebook.geometry("450x300")
                                atitle = Label(updatebook, text = "EDIT RECORD")
                                atitle.config(font= ("Arial",25))
                                atitle.place(x = 130, y = 20)
                                a1 = Label(updatebook, text= "Enter ID: ")
                                a1.config(font= ("Arial",15))
                                a1.place(x = 10,y = 110)

                                id_check = StringVar()
                                id_entry = Entry(updatebook, textvariable = id_check)
                                id_entry.config(font= ("Arial", 10))
                                id_entry.place(x = 140, y = 115)
                                
                                def update_sub():
                                    id_get = id_check.get()
                                    cursor.execute(f"SELECT * FROM `{ultra_dec}` WHERE id = '{id_get}'")
                                    result = cursor.fetchone()
                                    if result is None:
                                        def error_stats():
                                            error = Toplevel(updatebook)
                                            error.title("Unknown Record")
                                            error.geometry('300x300')
                                            a = Label(error, text=f"No Record Found with ID: {id_get}")
                                            a.pack()
                                            error.mainloop()
                                        error_stats()
                                    elif result is not None:
                                        print("Success")
                                        print(result)
                                        ini_book = result[1]
                                        ini_author = result[2]
                                        ini_dow = result[3]
                                        ini_dor = result[4]
                                        ini_withname = result[5]
                                        ini_status = result[6]
                                        def success_window():
                                            sw = Toplevel(updatebook)
                                            sw.title("Editing Record")
                                            sw.geometry("450x450")
                                            atitle = Label(sw, text = "EDIT BOOK")
                                            atitle.config(font= ("Arial",25))
                                            atitle.place(x = 130, y = 20)
                                            a1 = Label(sw, text= "Book Name: ")
                                            a1.config(font= ("Arial",15))
                                            book_author = Label(sw, text= "Book Author: ")
                                            book_author.config(font = ("Arial", 15))
                                            book_author.place(x = 10, y = 120+30)
                                            a1.place(x = 10,y = 80+30)
                                            a2 = Label(sw, text= "Borrower's Name: ")
                                            a2.config(font= ("Arial", 15))
                                            a2.place(x = 10,y = 160+30)
                                            a3 = Label(sw, text= "Date Of Withdrawal: ")
                                            a3.config(font= ("Arial", 15))
                                            a3.place(x = 10,y = 200+30)
                                            a4 = Label(sw, text= "Date Of Return: ")
                                            a4.config(font= ("Arial", 15))
                                            a4.place(x = 10,y = 240+30)
                                            a5 = Label(sw, text= "Current Status :  ")
                                            a5.config(font= ("Arial", 15))
                                            a5.place(x = 10,y = 280+30)

                                            book = StringVar()
                                            author = StringVar()
                                            date_of_withdrawal = StringVar()
                                            date_of_return = StringVar()
                                            status = StringVar()
                                            withd = StringVar()

                                            book_entry = Entry(sw, textvariable = book)
                                            book_entry.config(font= ("Arial", 10))
                                            book_entry.place(x = 140, y = 85+30)
                                            book_entry.insert(END, ini_book)
                                            author_entry = Entry(sw, textvariable = author)
                                            author_entry.config(font= ("Arial", 10))
                                            author_entry.place(x = 180, y = 155)
                                            author_entry.insert(END, ini_author)
                                            stuname = Entry(sw, textvariable= withd)
                                            stuname.config(font = ("Arial", 10))
                                            stuname.place(x = 200, y = 195)
                                            stuname.insert(END, ini_withname)
                                            dow_entry = Entry(sw, textvariable = date_of_withdrawal)
                                            dow_entry.config(font= ("Arial", 10))
                                            dow_entry.place(x = 200, y = 205+30)
                                            dow_entry.insert(END, ini_dow)
                                            dor_entry = Entry(sw, textvariable = date_of_return)
                                            dor_entry.config(font= ("Arial", 10))
                                            dor_entry.place(x = 160, y = 245+30)
                                            dor_entry.insert(END, ini_dor)
                                            status_entry = Entry(sw, textvariable = status)
                                            status_entry.config(font= ("Arial", 10))
                                            status_entry.place(x = 160, y = 285+30)
                                            status_entry.insert(END, ini_status)
                                            def up_sub():
                                                b = book.get()
                                                a = author.get()
                                                dow = date_of_withdrawal.get()
                                                dor = date_of_return.get()
                                                st = status.get()
                                                w = withd.get()
                                                sql = f'UPDATE `{ultra_dec}` SET book = %s, author = %s, date_of_withdrawal = %s, date_of_return = %s, withdrawer_name = %s, current_status = %s'
                                                val = (b,a,dow,dor,w,st)
                                                cursor.execute(sql, val)
                                                mysql.commit()
                                                def success_window1():
                                                    sw1 = Toplevel(sw)
                                                    sw1.title("SUCCESS")
                                                    s = Label(sw1, text= "Records Updated Successfully!")
                                                    s.pack()
                                                success_window1()
                                            sub = Button (sw, text = "SUBMIT", command= up_sub)
                                            sub.config(font= ("Arial", 10), width= 30)
                                            sub.place(x = 100, y = 360)
                                        success_window()
                                sub = Button (updatebook, text = "SUBMIT", command= update_sub)
                                sub.config(font= ("Arial", 10), width= 30)
                                sub.place(x = 100, y = 150)

                                updatebook.mainloop()


                            def view():
                                viewbook = Tk()
                                viewbook.title("ALL RECORD(S) LIST")
                                viewbook.geometry("1100x400")
                                v1 = Label(viewbook, text = "")
                                v1.pack()
                                frm = Frame(viewbook)
                                frm.pack(side = LEFT, padx = 20)
                                tv = ttk.Treeview(frm, column = (1,2,3,4,5,6,7), show= 'headings',height= '15', selectmode= 'browse')
                                scr = ttk.Scrollbar(frm,orient="vertical",command=tv.yview)
                                scr.pack(side=RIGHT ,fill=Y)
                                tv.heading(1, text="ID")
                                tv.column(1, minwidth = 0, width =20, stretch = NO)
                                tv.heading(2, text="Book Name")
                                tv.heading(3, text="Author")
                                tv.heading(4, text="Date Of Withdrawal")
                                tv.column(4, minwidth = 0, width = 100, stretch = NO)
                                tv.heading(5, text="Date of Return")
                                tv.column(5, minwidth = 0, width = 100, stretch = NO)
                                tv.heading(6, text ="Borrower's Name")
                                tv.heading(7, text= "Status")
                                cursor.execute(f"SELECT * FROM `{ultra_dec}`")
                                rows = cursor.fetchall()
                                print(rows)
                                for i in rows:
                                    tv.insert('', 'end', values = i)
                                tv.pack()
                                tv.configure(yscrollcommand= scr.set)
                                viewbook.mainloop()
                            ###########################
                            #### BUTTONS      #########
                            ###########################
                            addimage = PhotoImage(file = "loginauth/assets/add-record-icon1.png")
                            add_record_button = Button(window2, image=addimage, command= add)
                            add_record_button.config(background="lightgreen", height= 150, width= 150, activebackground= "lightgreen")
                            add_record_button.place( x =40, y = 120)
                            add_record_button_text = Label(window2, text= "ADD RECORD")
                            add_record_button_text.config(background="lightgreen", font=("Arial", 10))
                            add_record_button_text.place( x = 60, y = 280)


                            viewimage = PhotoImage(file = "loginauth/assets/view_image.png")
                            view_record_button = Button(window2, image = viewimage, command= view)
                            view_record_button.config(background= "lightgreen", activebackground="lightgreen")
                            view_record_button.place(x = 450, y =120)
                            view_record_button_text = Label(window2, text= "VIEW ALL RECORDS")
                            view_record_button_text.config(background="lightgreen", font=("Arial", 10))
                            view_record_button_text.place(x = 470, y = 280)


                            editimage = PhotoImage(file="loginauth/assets/edit-record.png")
                            edit_record_button = Button(window2, image= editimage, command= update)
                            edit_record_button.config(background="lightgreen", activebackground="lightgreen", height= 150)
                            edit_record_button.place(x = 250, y = 120)
                            edit_record_button_text = Label(window2, text= "EDIT RECORD")
                            edit_record_button_text.config(background="lightgreen", font= ("Arial", 10))
                            edit_record_button_text.place(x = 280, y = 280)

                            deleteimage = PhotoImage(file = "loginauth/assets/delete_record.png")
                            delete_record_button = Button(window2, image= deleteimage, command= remove)
                            delete_record_button.config(background="lightgreen", activebackground="lightgreen")
                            delete_record_button.place(x = 150, y = 340)
                            delete_record_button_text = Label(window2, text = "DELETE RECORD")
                            delete_record_button_text.config(background= "lightgreen", font = ("Arial", 10))
                            delete_record_button_text.place(x = 170, y  =500)

                            def exit():
                                window2.destroy()

                            exitimage = PhotoImage(file = "loginauth/assets/exitimage.png")
                            exit_record_button = Button(window2, image= exitimage, command=exit)
                            exit_record_button.config(background= "lightgreen", activebackground="lightgreen")
                            exit_record_button.place(x = 380, y = 340)
                            exit_record_button_text = Label(window2, text = "EXIT ")
                            exit_record_button_text.config(background= "lightgreen", font = ("Arial", 10))
                            exit_record_button_text.place(x = 440, y = 500)

                            window2.configure(background= "lightgreen")
                            window2.resizable(False, False)
                            window2.mainloop()
                            
                        else:
                            print("Access Denied")

                    final = Button(access, text= "OK", command= destroy)
                    final.pack()
                elif result1[0] != password_get:
                    error = Toplevel(window)
                    error.title("Access Denied")
                    error.geometry("500x10")
                    error1 = Label(error, text= "Wrong Password Please Try Again!")
                    error1.pack()
                else:
                    print("An internal error occured!")
            #print
    def register():
        email_get = email.get()
        password_get = password.get()
        if not email_get:
            warn = Toplevel(window)
            warn.geometry('300x10')
            warn.title('Empty Field Error')
            a = Label(warn, text="Email Section is empty, please fill it with your email.")
            a.pack()
        elif email_get.lstrip(' ') == '':
            warn = Toplevel(window)
            warn.geometry('300x10')
            warn.title('Empty Field Error')
            a = Label(warn, text="Email Section is empty, Enter a valid email")
            a.pack()
        elif '@' not in email_get:
            warn = Toplevel(window)
            warn.geometry('100x100')
            warn.title('Invalid Email')
            a = Label(warn, text="Invalid Email! Enter a valid email.")
            a.pack()
        elif password_get.lstrip(' ') == '':
            warn = Toplevel(window)
            warn.geometry('500x10')
            warn.title('Empty Field Error')
            a = Label(warn, text="Password Section is filled with spaces only, Enter a valid password.")
            a.pack()
        else:
            cursor.execute(f'SELECT * FROM AUTHENTICATION WHERE email = "{email_get}"')
            result = cursor.fetchone()
            if result is None:
                sql = 'INSERT INTO AUTHENTICATION (email, password, uuid) VALUES (%s,%s,%s)'
                ui =bytes(email_get, encoding="utf8")
                uui = email_get
                val  = (email_get, password_get, uui)
                cursor.execute(sql, val)
                mysql.commit()
                sql2 = f'CREATE TABLE `{uui}` (ID int(255) auto_increment, PRIMARY KEY(ID), book TEXT(256), author TEXT(256), date_of_withdrawal TEXT(256), date_of_return TEXT(256), withdrawer_name TEXT(256), current_status TEXT(256))'
                cursor.execute(sql2)
                temp = Toplevel(window)
                temp.title('Registration Success')
                temp.geometry('500x10')
                t = Label(temp, text = "Account Registration Success. Please Continue to Login Now.")
                t.pack()
            elif result is not None:
                temp = Toplevel(window)
                temp.title('Registration Failed')
                temp.geometry('500x10')
                t = Label(temp, text = "Account Registration Failed. An account associated with this email exists. Try Again with another email")
                t.pack()
    #button
    login_button = Button(window, text = "Login", background= "lightblue", foreground= "red",activeforeground= "red", activebackground= "lightblue", command= login)
    login_button.config(font = ("Arial", 10), width = 10, height= 1)
    login_button.place(x = 40 , y = 320)
    register_button = Button(window, text = "Register", foreground= "yellow", background= "green",activeforeground= "yellow", activebackground= "green", command=register)
    register_button.config(font = ("Arial", 10), width = 10, height= 1)
    register_button.place(x = 270 , y = 320)    

    window.resizable(False, False)
    window.mainloop()

