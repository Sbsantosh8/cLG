# # # from tkinter import *
# # # from PIL import ImageTk,Image
# # # from tkinter import messagebox
# # # import pymysql

# # # def bookRegister():
    
# # #     bid = bookInfo1.get()
# # #     title = bookInfo2.get()
# # #     author = bookInfo3.get()
# # #     status = bookInfo4.get()
# # #     status = status.lower()
    
# # #     insertBooks = "insert into "+bookTable+" values('"+bid+"','"+title+"','"+author+"','"+status+"')"
# # #     try:
# # #         cur.execute(insertBooks)
# # #         con.commit()
# # #         messagebox.showinfo('Success',"Book added successfully")
# # #     except:
# # #         messagebox.showinfo("Error","Can't add data into Database")
    
# # #     print(bid)
# # #     print(title)
# # #     print(author)
# # #     print(status)


# # #     root.destroy()
    
# # # def addBook(): 
    
# # #     global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
# # #     root = Tk()
# # #     root.title("Library")
# # #     root.minsize(width=400,height=400)
# # #     root.geometry("600x500")

# # #     # Add your own database name and password here to reflect in the code
# # #     mypass = "Sdsantosh@8"
# # #     mydatabase="library"

# # #     con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
# # #     cur = con.cursor()

# # #     # Enter Table Names here
# # #     bookTable = "books" # Book Table

# # #     Canvas1 = Canvas(root)
    
# # #     Canvas1.config(bg="#ff6e40")
# # #     Canvas1.pack(expand=True,fill=BOTH)
        
# # #     headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
# # #     headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

# # #     headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',15))
# # #     headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


# # #     labelFrame = Frame(root,bg='black')
# # #     labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
# # #     # Book ID
# # #     lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
# # #     lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
# # #     bookInfo1 = Entry(labelFrame)
# # #     bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
# # #     # Title
# # #     lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
# # #     lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
# # #     bookInfo2 = Entry(labelFrame)
# # #     bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
# # #     # Book Author
# # #     lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white')
# # #     lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
# # #     bookInfo3 = Entry(labelFrame)
# # #     bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
# # #     # Book Status
# # #     lb4 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white')
# # #     lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
# # #     bookInfo4 = Entry(labelFrame)
# # #     bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
# # #     #Submit Button
# # #     SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister)
# # #     SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
# # #     quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
# # #     quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
# # #     root.mainloop()

# # from tkinter import *
# # from PIL import ImageTk,Image
# # from tkinter import messagebox
# # import pymysql


# # def bookRegister():
# #     title = bookInfo2.get()
# #     author = bookInfo3.get()
# #     status = bookInfo4.get().lower()

# #     # Insert entry into the books table
# #     insertBook = f"INSERT INTO {bookTable} (Title, Author, Status) VALUES ('{title}', '{author}', '{status}')"
# #     try:
# #         cur.execute(insertBook)
# #         con.commit()
# #         messagebox.showinfo('Success', "Book added successfully")
# #     except Exception as e:
# #         messagebox.showinfo("Error", f"Can't add book data into Database: {e}")

# #     # Get the last inserted BookID
# #     cur.execute("SELECT LAST_INSERT_ID()")
# #     last_insert_id = cur.fetchone()[0]

# #     # Insert entry into the book_copies table
# #     num_copies = int(bookInfo5.get())
# #     for _ in range(num_copies):
# #         insertCopy = f"INSERT INTO book_copies (BookID) VALUES ('{last_insert_id}')"
# #         try:
# #             cur.execute(insertCopy)
# #             con.commit()
# #         except Exception as e:
# #             messagebox.showinfo("Error", f"Can't add book copy data into Database: {e}")

# #     root.destroy()

# # def addBook():
# #     global bookInfo2, bookInfo3, bookInfo4, bookInfo5, con, cur, bookTable, root

# #     root = Tk()
# #     root.title("Library")
# #     root.minsize(width=400, height=400)
# #     root.geometry("600x500")

# #     # Add your own database name and password here to reflect in the code
# #     mypass = "Sdsantosh@8"
# #     mydatabase = "library"

# #     con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
# #     cur = con.cursor()

# #     # Enter Table Names here
# #     bookTable = "books"  # Book Table

# #     Canvas1 = Canvas(root)
# #     Canvas1.config(bg="#ff6e40")
# #     Canvas1.pack(expand=True, fill=BOTH)

# #     headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
# #     headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

# #     headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier', 15))
# #     headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# #     labelFrame = Frame(root, bg='black')
# #     labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

# #     # Title
# #     lb2 = Label(labelFrame, text="Title : ", bg='black', fg='white')
# #     lb2.place(relx=0.05, rely=0.35, relheight=0.08)

# #     bookInfo2 = Entry(labelFrame)
# #     bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

# #     # Book Author
# #     lb3 = Label(labelFrame, text="Author : ", bg='black', fg='white')
# #     lb3.place(relx=0.05, rely=0.50, relheight=0.08)

# #     bookInfo3 = Entry(labelFrame)
# #     bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

# #     # Book Status
# #     lb4 = Label(labelFrame, text="Status(Avail/issued) : ", bg='black', fg='white')
# #     lb4.place(relx=0.05, rely=0.65, relheight=0.08)

# #     bookInfo4 = Entry(labelFrame)
# #     bookInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

# #     # Number of Copies
# #     lb5 = Label(labelFrame, text="Number of Copies: ", bg='black', fg='white')
# #     lb5.place(relx=0.05, rely=0.80, relheight=0.08)

# #     bookInfo5 = Entry(labelFrame)
# #     bookInfo5.place(relx=0.3, rely=0.80, relwidth=0.62, relheight=0.08)

# #     # Submit Button
# #     SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=bookRegister)
# #     SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

# #     quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
# #     quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

# #     root.mainloop()


# # if __name__ == "__main__":
# #     addBook()

# from tkinter import *
# from PIL import ImageTk,Image
# from tkinter import messagebox
# import pymysql

# def bookRegister():
#     title = bookInfo2.get()
#     author = bookInfo3.get()
#     status = bookInfo4.get().lower()

#     # Validation to check if the Book ID is empty
#     bid = bookInfo1.get()
#     if not bid.strip():
#         messagebox.showerror("Error", "Please enter Book ID.")
#         return

#     # Insert entry into the books table
#     insertBook = f"INSERT INTO {bookTable} (BookID, Title, Author, Status) VALUES ('{bid}', '{title}', '{author}', '{status}')"
#     try:
#         cur.execute(insertBook)
#         con.commit()
#         messagebox.showinfo('Success', "Book added successfully")
#     except Exception as e:
#         messagebox.showinfo("Error", f"Can't add book data into Database: {e}")

#     root.destroy()

# def addBook():
#     global bookInfo1, bookInfo2, bookInfo3, bookInfo4, bookInfo5, con, cur, bookTable, root

#     root = Tk()
#     root.title("Library")
#     root.minsize(width=400, height=400)
#     root.geometry("600x500")

#     # Add your own database name and password here to reflect in the code
#     mypass = "Sdsantosh@8"
#     mydatabase = "library"

#     con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
#     cur = con.cursor()

#     # Enter Table Names here
#     bookTable = "books"  # Book Table

#     Canvas1 = Canvas(root)
#     Canvas1.config(bg="#ff6e40")
#     Canvas1.pack(expand=True, fill=BOTH)

#     headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
#     headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

#     headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier', 15))
#     headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

#     labelFrame = Frame(root, bg='black')
#     labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

#     # Book ID
#     lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
#     lb1.place(relx=0.05, rely=0.20, relheight=0.08)

#     bookInfo1 = Entry(labelFrame)
#     bookInfo1.place(relx=0.3, rely=0.20, relwidth=0.62, relheight=0.08)

#     # Title
#     lb2 = Label(labelFrame, text="Title : ", bg='black', fg='white')
#     lb2.place(relx=0.05, rely=0.35, relheight=0.08)

#     bookInfo2 = Entry(labelFrame)
#     bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

#     # Book Author
#     lb3 = Label(labelFrame, text="Author : ", bg='black', fg='white')
#     lb3.place(relx=0.05, rely=0.50, relheight=0.08)

#     bookInfo3 = Entry(labelFrame)
#     bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

#     # Book Status
#     lb4 = Label(labelFrame, text="Status(Avail/issued) : ", bg='black', fg='white')
#     lb4.place(relx=0.05, rely=0.65, relheight=0.08)

#     bookInfo4 = Entry(labelFrame)
#     bookInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

#     # Number of Copies
#     lb5 = Label(labelFrame, text="Number of Copies: ", bg='black', fg='white')
#     lb5.place(relx=0.05, rely=0.80, relheight=0.08)

#     bookInfo5 = Entry(labelFrame)
#     bookInfo5.place(relx=0.3, rely=0.80, relwidth=0.62, relheight=0.08)

#     # Submit Button
#     SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=bookRegister)
#     SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

#     quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
#     quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

#     root.mainloop()


# if __name__ == "__main__":
#     addBook()


from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

def bookRegister():
    # Fetching data from entry fields
    bid = bookInfo1.get()
    title = bookInfo2.get().lower()
    author = bookInfo3.get().lower()
    status = bookInfo4.get().lower()

    # Validation to check if the Book ID is empty
    if not bid.strip():
        messagebox.showerror("Error", "Please enter Book ID.")
        return

    # Insert entry into the books table
    insertBook = f"INSERT INTO {bookTable} (bid,title, author, status) VALUES ('{bid}', '{title}', '{author}', '{status}')"


    try:
        cur.execute(insertBook)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except pymysql.Error as e:
     error_message = f"Error: {e.args[0]} - {e.args[1]}"
     messagebox.showerror("Error", error_message)

    root.destroy()

def addBook():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, con, cur, bookTable, root

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "Sdsantosh@8"
    mydatabase = "library"

    # Establish database connection
    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books"  # Book Table

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.20, relheight=0.08)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.20, relwidth=0.62, relheight=0.08)

    # Title
    lb2 = Label(labelFrame, text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Book Author
    lb3 = Label(labelFrame, text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    # Book Status
    lb4 = Label(labelFrame, text="Status(Avail/issued) : ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)

    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=bookRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


if __name__ == "__main__":
    addBook()
