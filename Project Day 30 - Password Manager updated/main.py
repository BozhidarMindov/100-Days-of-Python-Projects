import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

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
    
    new_data = {website:{
        "email": email,
        "password": password
    }}

    if len(website) == 0 or len(password)==0 or len(email) == 0:
        messagebox.showwarning(title="Warning!", message="You have a field that is empty!")
    else:
        try:
            with open("data.json", "r") as file:
                #reading old data
                data = json.load(file)
                #updating old data with new data
                data.update(new_data)

            with open("data.json", "w") as file:
                #saving the updated data
                json.dump(data, file, indent=4)
        
        except FileNotFoundError:
            #creating a new data.json file
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
        
        #The exceptions can be handled with in a different way (with a try/except/else/finally statement).
        #However, I am keeping it as it is, since this as the first solution that came up in my mind
        #It is arguably more readable too :)

# ---------------------------- SEARCH WEBSITE(find password) ------------------------------- #
def search():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showwarning(title="Warning!", message="Please enter a website to search!")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
            
        except FileNotFoundError:
            messagebox.showwarning(title="Warning!", message="No Data File Found!")
        
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message= f"Email: {email} \nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No data for the website {website} exists!")

# ---------------------------- Change Email/Username entry ------------------------------- #
def change():
    email_entry.delete(0, END)

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
website_entry.grid(column=1, row=1)
website_entry.focus()

#email entry box
email_entry = Entry(width=42)
email_entry.grid(column=1, row=2)
email_entry.insert(0, "abcd@gmail.com")

#password entry box
password_entry = Entry(width = 42)
password_entry.grid(column=1, row=3)

#generate password button
generate_password_button = Button(text="Generate password", width=21, command=generate_password)
generate_password_button.grid(column=2, row=3)

#add button
add_button = Button(text="Add", width=35, command=add)
add_button.grid(column=1, row =6)

#search button
search_button = Button(text="Search", width=21, bg="#0277bd",command=search)
search_button.grid(column=2, row=1)

#change email/username entry
change_button = Button(text="Change Email/Username", width=21, command=change)
change_button.grid(column=2, row = 2)


window.mainloop()
