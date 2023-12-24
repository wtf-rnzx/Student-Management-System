from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox, filedialog
import pymysql
import pandas
import customtkinter as ctk
from PIL import ImageTk, Image


def Export_data():
    url = filedialog.asksaveasfilename(defaultextension= '.csv')
    indexing =  student_table.get_children()
    new_list = []
    for index in indexing:
        content = student_table.item(index)
        data_list = content['values']
        new_list.append(data_list)

    table = pandas.DataFrame(new_list, columns= ['Sr-Code', 'Name', 'Mobile no.', 'Email', 'Address', 'Gender', 'Birthay', 'Course', 'Section', 'Date'])
    table.to_csv(url, index=False)
    messagebox.showinfo('Success', 'Data is saved')
    
def Get_previous_birthday():
        # Fetch the current selected student's data
        indexing = student_table.focus()
        content = student_table.item(indexing)
        list_data = content['values']
        
        # Extract the current birthday information
        previous_birthday = list_data[6]  # Assuming birthday is at index 6 in the values list
        return previous_birthday

def Update_student():
    def Update_data():
        combined_date = f"{bdayMonthEntry.get()}/{bdayDateEntry.get()}/{bdayYearEntry.get()}"
        query = 'update student set name=%s, mobile=%s, email=%s, address=%s, gender=%s, birthday=%s, course=%s, section=%s, date=%s where srcode=%s'
        mycursor.execute(query, (nameEntry.get(), mobileEntry.get(), emaileEntry.get(), addressEntry.get(), genderVar.get(), combined_date, courseEntry.get(), secEntry.get(), date, srcodeEntry.get()))
        con.commit()
        messagebox.showinfo('Success', f'Sr-Code {srcodeEntry.get()} is updated successfully',)
        update_window.destroy()
        Show_student()

    update_window = ctk.CTkToplevel()
    update_window.title('Update Student')
    update_window.grab_set()
    update_window.resizable(False, False)
    srcodeLabel = ctk.CTkLabel(update_window, text='Sr-Code', font=('times new roman', 20, 'bold'))
    srcodeLabel.grid(row= 0, column= 0, padx= 30, pady= 15, sticky=W)
    srcodeEntry = ctk.CTkEntry(update_window, font=('times new roman', 15, 'bold'))
    srcodeEntry.grid(row= 0, column= 1, padx= 15, pady=10)

    nameLabel = ctk.CTkLabel(update_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row= 1, column= 0, padx= 30, pady= 15, sticky=W)
    nameEntry = ctk.CTkEntry(update_window, font=('times new roman', 15, 'bold'))
    nameEntry.grid(row= 1, column= 1, padx= 15, pady=10)

    mobileLabel = ctk.CTkLabel(update_window, text='Mobile No.', font=('times new roman', 20, 'bold'))
    mobileLabel.grid(row= 2, column= 0, padx= 30, pady= 15, sticky=W)
    mobileEntry = ctk.CTkEntry(update_window, font=('times new roman', 15, 'bold'))
    mobileEntry.grid(row= 2, column= 1, padx= 15, pady=10)

    emailLabel = ctk.CTkLabel(update_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row= 3, column= 0, padx= 30, pady= 15, sticky=W)
    emaileEntry = ctk.CTkEntry(update_window, font=('times new roman', 15, 'bold'))
    emaileEntry.grid(row= 3, column= 1, padx= 15, pady=10)

    addressLabel = ctk.CTkLabel(update_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row= 4, column= 0, padx= 30, pady= 15, sticky=W)
    addressEntry = ctk.CTkEntry(update_window, font=('times new roman', 15, 'bold'))
    addressEntry.grid(row= 4, column= 1, padx= 15, pady=10)

    genderLabel = ctk.CTkLabel(update_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row= 5, column= 0, padx= 30, pady= 15, sticky=W)
    genderOptions = ['Male', 'Female', 'Other']
    genderVar = StringVar(update_window)
    genderVar.set(genderOptions[0])  # Default value

    genderDropdown = OptionMenu(update_window, genderVar, *genderOptions)
    genderDropdown.config(width=15, font=('times new roman', 15, 'bold'))
    genderDropdown.grid(row=5, column=1, padx=15, pady=10)
    
    bdayLabel = ctk.CTkLabel(update_window, text='Birthday', font=('times new roman', 20, 'bold'))
    bdayLabel.grid(row= 6, column= 0, padx= 30, pady= 15, sticky=W)
    # Dropdown menu for month
    months = [str(i) for i in range(1, 13)]
    bdayMonthEntry = ttk.Combobox(update_window, values=months, font=('times new roman', 15, 'bold'), width=15, state="readonly")
    bdayMonthEntry.grid(row=6, column=1, padx=0, pady=10)
    bdayMonthEntry.set("Month")  # Set default value

    # Dropdown menu for date (1 to 31)
    datee = [str(i) for i in range(1, 32)]
    bdayDateEntry = ttk.Combobox(update_window, values=datee, font=('times new roman', 15, 'bold'), width=15, state="readonly")
    bdayDateEntry.grid(row=6, column=2, padx=0, pady=10)
    bdayDateEntry.set("Day")  # Set default value

    year = [str(i) for i in range(2000, 2023)]
    bdayYearEntry = ttk.Combobox(update_window, values=year, font=('times new roman', 15, 'bold'), width=15, state="readonly")
    bdayYearEntry.grid(row=6, column=3, padx=0, pady=10)
    bdayYearEntry.set("Year")  # Set default value

    courseLabel = ctk.CTkLabel(update_window, text='Course', font=('times new roman', 20, 'bold'))
    courseLabel.grid(row= 7, column= 0, padx= 30, pady= 15, sticky=W)
    courseEntry = ctk.CTkEntry(update_window, font=('times new roman', 15, 'bold'))
    courseEntry.grid(row= 7, column= 1, padx= 15, pady=10)

    secLabel = ctk.CTkLabel(update_window, text='Section', font=('times new roman', 20, 'bold'))
    secLabel.grid(row= 8, column= 0, padx= 30, pady= 15, sticky=W)
    secEntry = ctk.CTkEntry(update_window, font=('times new roman', 15, 'bold'))
    secEntry.grid(row= 8, column= 1, padx= 15, pady=10)

    update_stud_button = ctk.CTkButton(update_window, text='Update', command= Update_data)
    update_stud_button.grid(row= 9, columnspan=4, pady= 15)

    indexing = student_table.focus()
    content = student_table.item(indexing)
    list_data = content['values']
    srcodeEntry.insert(0, list_data[0])
    nameEntry.insert(0, list_data[1])
    mobileEntry.insert(0, list_data[2])
    emaileEntry.insert(0, list_data[3])
    addressEntry.insert(0, list_data[4])
    genderVar.set(list_data[5])
    courseEntry.insert(0, list_data[7])
    secEntry.insert(0, list_data[8])

    existing_birthday = list_data[6]  # Assuming birthday is at index 6
    if existing_birthday:
            month, day, year = existing_birthday.split('/')
            bdayMonthEntry.set(month)
            bdayDateEntry.set(day)
            bdayYearEntry.set(year)

def Show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    for data in fetched_data:
        student_table.insert('', END, values=data)

def Delete_student():
    ask = messagebox.askquestion('Delete Student', 'Do you want to delete this student?')
    if ask == 'yes':
        indexing = student_table.focus()
        content = student_table.item(indexing)
        content_id = content['values'][0]
        query = 'delete from student where srcode=%s'
        mycursor.execute(query, content_id)
        con.commit()
        messagebox.showinfo('Deleted', f'This {content_id} is deleted successfully')
        query = 'select * from student'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        student_table.delete(*student_table.get_children())
        for data in fetched_data:
            student_table.insert('', END, values=data)
    else:
        pass


def Search_student():
    def search_data():
        query = 'select * from student where {}=%s'.format(selected_field.get())
        mycursor.execute(query, (searchEntry.get(),))
        student_table.delete(*student_table.get_children())
        fetched_data = mycursor.fetchall()
        for data in fetched_data:
            student_table.insert('', END, values=data)

    search_window = ctk.CTkToplevel()
    search_window.title('Search Student')
    search_window.grab_set()
    search_window.resizable(False, False)

    search_fields = [
        'srcode', 'name', 'mobile', 'email', 'address', 'gender', 'birthday', 'course', 'section'
    ]

    selected_field = ttk.Combobox(search_window, values=search_fields, state="readonly")
    selected_field.grid(row=0, column=0, padx=15, pady=10)
    selected_field.current(0)  # Set default value

    searchEntry = ctk.CTkEntry(search_window, font=('times new roman', 15, 'bold'))
    searchEntry.grid(row=0, column=1, padx=15, pady=10)

    search_stud_button = ctk.CTkButton(search_window, text='Search Student', command=search_data)
    search_stud_button.grid(row=1, columnspan=2, pady=15)

def Add_student():
    def add_data():
        def contains_digits(string):
            return any(char.isdigit() for char in string)
        def contains_non_digits(string):
            return any(not char.isdigit() for char in string)
        def contains_non_digit(string):
            return any(not char.isdigit() and char != "-" for char in string)  # Allowing "-" character
        
        bday_combined = f"{bdayMonthEntry.get()}/{bdayDateEntry.get()}/{bdayYearEntry.get()}"
        
        if contains_digits(nameEntry.get()):
            messagebox.showerror('Error', 'Name cannot contain numbers!', parent=add_window)
        elif contains_non_digit(srcodeEntry.get()):
            messagebox.showerror('Error', 'Sr-Code. should contain only numbers!', parent=add_window)
        elif contains_non_digits(mobileEntry.get()):
            messagebox.showerror('Error', 'Mobile No. should contain only numbers!', parent=add_window)
        elif srcodeEntry.get()=='' or nameEntry.get()=='' or mobileEntry.get()=='' or emaileEntry.get()=='' or addressEntry.get()=='' or genderVar.get()=='' or courseEntry.get()=='' or secEntry.get()=='':
            messagebox.showerror('Error', 'All information are required!', parent= add_window)
        else:
            try:
                query = 'insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query, (srcodeEntry.get(), nameEntry.get(), mobileEntry.get(), emaileEntry.get(), addressEntry.get(), genderVar.get(), bday_combined, courseEntry.get(),secEntry.get(), date))
                con.commit()
                result = messagebox.askquestion('Confirm', 'Data was Added, Do you want to clear the form?', parent= add_window)
                if result:
                    srcodeEntry.delete(0, END)
                    nameEntry.delete(0, END) 
                    mobileEntry.delete(0, END) 
                    emaileEntry.delete(0, END) 
                    addressEntry.delete(0, END)  
                    courseEntry.delete(0, END)
                    secEntry.delete(0,END)
                    genderVar.set(genderOptions[0])  # Set the default gender
                    bdayMonthEntry.set("Month")  # Reset birthday month to default
                    bdayDateEntry.set("Day")  # Reset birthday day to default
                    bdayYearEntry.set("Year")
                else:
                    pass     
            except:
                messagebox.showerror('Error', 'Id cannot be repeated', parent= add_window)
                return

        query = 'select * from student'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        student_table.delete(* student_table.get_children())
        for data in fetched_data:
            student_table.insert('', END, values= data)


    add_window = ctk.CTkToplevel()
    add_window.grab_set()
    add_window.resizable(False, False)
    srcodeLabel = ctk.CTkLabel(add_window, text='Sr-Code', font=('times new roman', 20, 'bold'))
    srcodeLabel.grid(row= 0, column= 0, padx= 30, pady= 15, sticky=W)
    srcodeEntry = ctk.CTkEntry(add_window, font=('times new roman', 15, 'bold'))
    srcodeEntry.grid(row= 0, column= 1, padx= 15, pady=10)

    nameLabel = ctk.CTkLabel(add_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row= 1, column= 0, padx= 30, pady= 15, sticky=W)
    nameEntry = ctk.CTkEntry(add_window, font=('times new roman', 15, 'bold'))
    nameEntry.grid(row= 1, column= 1, padx= 15, pady=10)

    mobileLabel = ctk.CTkLabel(add_window, text='Mobile No.', font=('times new roman', 20, 'bold'))
    mobileLabel.grid(row= 2, column= 0, padx= 30, pady= 15, sticky=W)
    mobileEntry = ctk.CTkEntry(add_window, font=('times new roman', 15, 'bold'))
    mobileEntry.grid(row= 2, column= 1, padx= 15, pady=10)

    emailLabel = ctk.CTkLabel(add_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row= 3, column= 0, padx= 30, pady= 15, sticky=W)
    emaileEntry = ctk.CTkEntry(add_window, font=('times new roman', 15, 'bold'))
    emaileEntry.grid(row= 3, column= 1, padx= 15, pady=10)

    addressLabel = ctk.CTkLabel(add_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row= 4, column= 0, padx= 30, pady= 15, sticky=W)
    addressEntry = ctk.CTkEntry(add_window, font=('times new roman', 15, 'bold'))
    addressEntry.grid(row= 4, column= 1, padx= 15, pady=10)

    genderLabel = ctk.CTkLabel(add_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row= 5, column= 0, padx= 30, pady= 15, sticky=W)
    genderOptions = ['Male', 'Female', 'Other']
    genderVar = StringVar(add_window)
    genderVar.set(genderOptions[0])  # Default value

    genderDropdown = OptionMenu(add_window, genderVar, *genderOptions)
    genderDropdown.config(width=15, font=('times new roman', 15, 'bold'))
    genderDropdown.grid(row=5, column=1, padx=15, pady=10)

    bdayLabel = ctk.CTkLabel(add_window, text='Birthday', font=('times new roman', 20, 'bold'))
    bdayLabel.grid(row= 6, column= 0, padx= 30, pady= 15, sticky=W)
    # Dropdown menu for month
    months = [str(i) for i in range(1, 13)]
    bdayMonthEntry = ttk.Combobox(add_window, values=months, font=('times new roman', 15, 'bold'), width=15, state="readonly")
    bdayMonthEntry.grid(row=6, column=1, padx=0, pady=10)
    bdayMonthEntry.set("Month")  # Set default value

    # Dropdown menu for date (1 to 31)
    dates = [str(i) for i in range(1, 32)]
    bdayDateEntry = ttk.Combobox(add_window, values=dates, font=('times new roman', 15, 'bold'), width=15, state="readonly")
    bdayDateEntry.grid(row=6, column=2, padx=0, pady=10)
    bdayDateEntry.set("Day")  # Set default value

    year = [str(i) for i in range(2000, 2023)]
    bdayYearEntry = ttk.Combobox(add_window, values=year, font=('times new roman', 15, 'bold'), width=15, state="readonly")
    bdayYearEntry.grid(row=6, column=3, padx=0, pady=10)
    bdayYearEntry.set("Year")  # Set default value

    courseLabel = ctk.CTkLabel(add_window, text='Course', font=('times new roman', 20, 'bold'))
    courseLabel.grid(row= 7, column= 0, padx= 30, pady= 15, sticky=W)
    courseEntry = ctk.CTkEntry(add_window, font=('times new roman', 15, 'bold'))
    courseEntry.grid(row= 7, column= 1, padx= 15, pady=10)

    secLabel = ctk.CTkLabel(add_window, text='Section', font=('times new roman', 20, 'bold'))
    secLabel.grid(row= 8, column= 0, padx= 30, pady= 15, sticky=W)
    secEntry = ctk.CTkEntry(add_window, font=('times new roman', 15, 'bold'))
    secEntry.grid(row= 8, column= 1, padx= 15, pady=10)

    add_stud_button = ctk.CTkButton(add_window, text='Add Student', command=add_data)
    add_stud_button.grid(row= 9, columnspan=4, pady= 15)

def Exit():
    quit = messagebox.askquestion('Exit','Do you want to Exit')
    if quit == 'yes':
        root.destroy()
    else:
        pass


con = pymysql.connect(host='localhost', user='root', password='')
mycursor = con.cursor()

try:
    query = 'create database studentmanagementsystem'
    mycursor.execute(query)
    query = 'use studentmanagementsystem'
    mycursor.execute(query)
    query = 'create table student(srcode varchar(30) primary key, name varchar(30), mobile varchar(30), email varchar(30), address varchar(100), gender varchar(30), birthday varchar(30), course varchar(30), section varchar(30), date varchar(30))'
    mycursor.execute(query)
except:
    query = 'use studentmanagementsystem'
    mycursor.execute(query)
      
        
        
def clock():
    global date,current_time
    date = time.strftime('%m/%d/%Y')
    current_time = time.strftime('%H:%M:%S')
    DateTimeLabel.config(text= f'  Date: {date}\nTime: {current_time}')
    DateTimeLabel.after(1000, clock)

# **********GUI***************
root = ctk.CTk()
ctk.set_appearance_mode('light')
root.geometry('1200x730+0+0')
root.title('Student Management System')
root.resizable(False, False)

DateTimeLabel = Label(root, font=('times new roman', 12, 'bold'))
DateTimeLabel.place(x=5, y=5)
clock()

stud = 'Student Management System'
sliderLabel = ctk.CTkLabel(root, text=stud, font=('times new roman', 28, 'bold'))
sliderLabel.place(x= 450, y= 0)


right_Frame = Frame(root)
right_Frame.place(x= 1200, y= 20, width=270, height=800)

logo_image = ImageTk.PhotoImage(Image.open('lol.png'))
logo_Label = Label(right_Frame, image=logo_image)
logo_Label.grid(row= 0, column= 0, pady= 30, padx= 0)


add_stud_button = ttk.Button(right_Frame, text='Add Student', width=25, command=Add_student, style='Add.TButton')
add_stud_button.grid(row= 1, column= 0, pady= 30, padx= 30)


search_stud_button = ttk.Button(right_Frame, text='Search Student', width=25, command=Search_student, style='Add.TButton')
search_stud_button.grid(row= 2, column= 0, pady= 30, padx= 0)

delete_stud_button = ttk.Button(right_Frame, text='Delete Student', width=25,  command= Delete_student, style='Add.TButton')
delete_stud_button.grid(row= 3, column= 0, pady= 30, padx= 0)

update_stud_button = ttk.Button(right_Frame, text='Update Student', width=25, command= Update_student, style='Add.TButton')
update_stud_button.grid(row= 5, column= 0, pady= 30, padx= 0)

show_stud_button = ttk.Button(right_Frame, text='Show Student',  width=25, command= Show_student, style='Add.TButton')
show_stud_button.grid(row= 6, column= 0, pady= 30, padx= 0)

export_stud_button = ttk.Button(right_Frame, text='Export Student', width=25, command= Export_data, style='Add.TButton')
export_stud_button.grid(row= 7, column= 0, pady= 30, padx= 0)

exit_button = ttk.Button(right_Frame, text='Exit', width=25,command=Exit ,style='Add.TButton')
exit_button.grid(row= 8, column= 0, pady= 30, padx= 0)

left_frame = Frame(root, bg='white')
left_frame.place(x= 50, y= 80, width=1150, height=800)

scroll_bar_x = Scrollbar(left_frame, orient=HORIZONTAL)
scroll_bar_y = Scrollbar(left_frame, orient=VERTICAL)
scroll_bar_x.pack(side=BOTTOM, fill=X)
scroll_bar_y.pack(side=RIGHT, fill=Y)

student_table = ttk.Treeview(left_frame, columns=('Sr-Code', 'Name', 'Mobile No.', 'Email', 'Address','Gender', 'Birthday', 'Course','Section', 'Added Date'), 
                             xscrollcommand=scroll_bar_x.set, yscrollcommand=scroll_bar_y.set)
student_table.pack(fill=BOTH, expand=1)

scroll_bar_x.config(command=student_table.xview)
scroll_bar_y.config(command=student_table.yview)

student_table.config(show='headings')

student_table.heading('Sr-Code', text='Sr-Code')
student_table.heading('Name', text='Name')
student_table.heading('Mobile No.', text='Mobile No.')
student_table.heading('Email', text='Email')
student_table.heading('Address', text='Address')
student_table.heading('Gender', text='Gender')
student_table.heading('Birthday', text='Birthday')
student_table.heading('Course', text='Course')
student_table.heading('Section', text='Section')
student_table.heading('Added Date', text='Date')

student_table.column('Sr-Code', width=150, anchor=CENTER)
student_table.column('Name', width=250, anchor=CENTER)
student_table.column('Mobile No.', width=200, anchor=CENTER)
student_table.column('Email', width=250, anchor=CENTER)
student_table.column('Address', width=300, anchor=CENTER)
student_table.column('Gender', width=150, anchor=CENTER)
student_table.column('Birthday', width=200, anchor=CENTER)
student_table.column('Course', width=250, anchor=CENTER)
student_table.column('Section',width=150, anchor=CENTER)
student_table.column('Added Date', width=200, anchor=CENTER)

style = ttk.Style()
style.configure('Add.TButton', font=('times new roman', 13), width=20, height=20)
style.configure('Treeview', rowheight = 40, font=('times new roman', 11, 'bold'), foreground= 'red4')
style.configure('Treeview.Heading', font=('times new roman', 13, 'bold'))

root.mainloop()