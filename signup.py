from tkinter import *
from tkinter import messagebox
import ast
import customtkinter as ctk
from PIL import ImageTk, Image

window = ctk.CTk()
window.title("SignUp")
window.geometry('500x500+300+200')
ctk.set_appearance_mode('light')
window.configure(bg= 'white')
window.resizable(False, False)

def sign_up():
    username = user.get()
    passwrd = password.get()
    confirm_pass = confirm.get()

    if passwrd == confirm_pass:
        try:
            with open('data.txt', 'r') as file:
                d = file.read()
                if d:
                    r = ast.literal_eval(d)
                else:
                    r = {}

            r[username] = passwrd

            with open('data.txt', 'w') as file:
                file.write(str(r))

            messagebox.showinfo('SignUp', 'Successfully signed up')
            window.destroy()
            import loginn  
        except Exception as e:
            messagebox.showerror('Error', f"An error occurred: {e}")

    else:
        messagebox.showerror('Invalid', 'Passwords do not match')

def signin():
    window.destroy()
    import loginn

def toggle_password():
    if show_password.get():
        password.config(show="")
        password_toggle_button.config(image=eye_img)
        confirm.config(show="")
        confirm_toggle_button.config(image=eye_img)
    else:
        password.config(show="*")
        password_toggle_button.config(image=hide_img)
        confirm.config(show="*")
        confirm_toggle_button.config(image=hide_img)
    show_password.set(not show_password.get())

show_password = BooleanVar()
show_password.set(False)
eye_img = PhotoImage(file='eye.png')
hide_img = PhotoImage(file='hidden.png')

frame = Frame(window, width= 700, height= 700, bg='white')
frame.place(x=0, y=0)

img = ImageTk.PhotoImage(Image.open('lol.png'))
label = Label(frame, image= img, bg='white').place(x=250, y=40)


heading = Label(frame, text='Sign up', fg='black', bg='white', font=('times new roman', 22, 'bold'))
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

confirm = Entry(frame, width=25, fg='black', border=0, bg='white', font=('times new roman', 13 ), show='*')
confirm.place(x=330, y=400)
confirm_img =PhotoImage(file='padlock.png')
confirmLabel = Label(image=password_img, text='Confirm Password:  ', compound=LEFT, bg='white')
confirmLabel.place(x=160, y=390)

Frame(frame, width=250, height=2, bg='black').place(x=280, y=420)

def enter(e):
    confirm.delete(0, 'end')

def leave(e):
    name =  confirm.get()
    if name == '':
        confirm.insert(0, 'Confirm Password')


Button(frame, width=30, pady=7, text='Sign up', bg='crimson', fg='white', border=0, command=sign_up).place(x=220, y=480)
label = Label(frame, text="I have account", fg= 'black', bg='white', font=('times new roman', 9))
label.place(x=160, y=560)

password_toggle_button = Button(frame, image=hide_img, width=20, height=20, bg='white', border=0, command=toggle_password)
password_toggle_button.place(x=460, y=320)
confirm_toggle_button = Button(frame, image=hide_img, width=20, height=20, bg='white', border=0, command=toggle_password)
confirm_toggle_button.place(x=500, y=390)

sign_in =Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='crimson', command= signin)
sign_in.place(x=250, y=560)

window.mainloop()