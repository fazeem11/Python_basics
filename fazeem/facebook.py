from tkinter import*
from tkinter import ttk
root=Tk()

path= PhotoImage(file="C:/Users/Python/Downloads/fb2.png")
label_image= Label(root, image=path,width=250,height=250)
label_image.pack(side=TOP, pady=0)

root.geometry('340x560')
root.title("facebook ")
font_style = ('Arial', 24, 'bold')  # Font type, size, and style (bold)
font_color = 'blue'  # Text color
font_label = ('Arial', 14)
font_entry = ('Arial', 14)
font_button = ('Arial', 14)
font_style2 = ('Arial', 9)


l1 = Label(root, text="Facebook", font=font_style, fg=font_color)
l1.pack(side=TOP, pady=3)
login_label = Label(root, text="Email or Phone Number", font=font_label)
login_label.pack(pady=(1, 5))
login_entry = Entry(root, font=font_entry)
login_entry.pack(pady=(0, 20))

password_label = Label(root, text="Password", font=('Arial', 14))
password_label.pack(pady=(10, 5))
password_entry = Entry(root, font=('Arial', 14), show='*')  
password_entry.pack(pady=(0,20))

forgot_label= Label(root,text="Forgotten password ?",font=font_style2,fg=font_color)
forgot_label.pack()


login_button = Button(root, text="Log In", font=font_button, bg=font_color, fg='white', relief=RAISED)
login_button.pack(pady=20)

root.mainloop()
