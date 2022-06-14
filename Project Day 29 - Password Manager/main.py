import random
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
              'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_Letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(numbers) for _ in range(random.randint(2,4))]
    password_numbers = [random.choice(symbols) for _ in range(random.randint(2,4))]

    password_list = password_Letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password)==0 or len(email) == 0:
        messagebox.showwarning(title="Warning!", message="You have a field that is empty!")
    else:
        answer = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?")

        if answer:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

#creating a window
window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)

#creating a canvas
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row = 0)

#website label
website_label = Label(text = "Website:")
website_label.grid(column=0, row=1)

#email/username label
email_uname_label = Label(text = "Email/Username:")
email_uname_label.grid(column=0, row=2)

#password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#website entry box
website_entry = Entry(width=42)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

#email entry box
email_entry = Entry(width=42)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "abcd@gmail.com")

#password entry box
password_entry = Entry(width = 42)
password_entry.grid(column=1, row=3)

#generate password button
generate_password_button = Button(text="Generate password", width=35, command=generate_password)
generate_password_button.grid(column=1, row=4)

#add button
add_button = Button(text="Add", width=30, command=add)
add_button.grid(column=1, row =5, columnspan = 2)



window.mainloop()
