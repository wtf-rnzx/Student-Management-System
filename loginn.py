from tkinter import *
from tkinter import messagebox
import ast
import customtkinter as ctk
from tkinter import ttk
from PIL import ImageTk, Image


root = ctk.CTk()
root.title('Login')
root.geometry('500x500+300+200')
ctk.set_appearance_mode('light')
root.configure(bg ='white')
root.resizable(False, False)

def sign_in():
    username = user.get()
    passwrd = password.get()    

    file = open('data.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    print(r.keys())
    print(r.values())

    if username in r.keys() and  passwrd==r[username]:
        messagebox.showinfo('Success', 'Welcome')
        root.destroy()
        import system 

    else:
        messagebox.showerror('Invalid', 'Invalid username or password')

def signup():
    root.destroy()
    import signup

def toggle_password():
    if show_password.get():
        password.config(show="*")
        password_toggle_button.config(image=hide_img)
    else:
        password.config(show="")
        password_toggle_button.config(image=eye_img)
    show_password.set(not show_password.get()) 

show_password = BooleanVar()
show_password.set(True)
hide_img = PhotoImage(file='hidden.png')
eye_img = PhotoImage(file='eye.png')

frame = Frame(root, width= 800, height= 700, bg='white')
frame.place(x=0, y=0)

frame2 = Frame(root, width= 300, height= 700, bg='white')
frame2.place(x=500, y=0)

img = ImageTk.PhotoImage(Image.open('lol.png'))
label = Label(frame, image= img, bg='white').place(x=250, y=60)

heading = Label(frame, text='Sign in', fg='black', bg='white', font=('times new roman', 22, 'bold'))
heading.place(x=280, y=180)


username_img =PhotoImage(file='user.png')
usernameLabel = Label(image=username_img, text='Username:  ', compound=LEFT, bg='white', font=('arial', 11))
usernameLabel.place(x=160, y=250)
user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('times new roman', 13 ))
user.place(x=290, y=260)

Frame(frame, width=200, height=2, bg='black').place(x=280, y=280)

password_img =PhotoImage(file='padlock.png')
passwordLabel = Label(image=password_img, text='Password:  ', compound=LEFT, bg='white', font=('arial', 11))
passwordLabel.place(x=160, y=320)
password = Entry(frame, width=25, fg='black', border=0, bg='white', font=('times new roman', 13 ), show='*')
password.place(x=290, y=330)

Frame(frame, width=200, height=2, bg='black').place(x=280, y=350)

Button(frame, width=30, pady=7, text='Sign in', bg='crimson', fg='white', border=0, command=sign_in).place(x=220, y=450)

label = Label(frame, text="Dnt't have an account?", fg= 'black', bg='white', font=('times new roman', 10))
label.place(x=155, y=530)

sign_up =Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='crimson', command=signup)
sign_up.place(x=290, y=530)

password_toggle_button = Button(frame, image=hide_img, width=20, height=20, bg='white', border=0, command=toggle_password)
password_toggle_button.place(x=460, y=320)

style = ttk.Style()
style.configure('Add.TButton', font=('times new roman', 12), width=20, height=10)
style.configure('Treeview', rowheight = 40, font=('times new roman', 11, 'bold'), foreground= 'red4')
style.configure('Treeview.Heading', font=('times new roman', 13, 'bold'))


root.mainloop()