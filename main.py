from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]

    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)

    pyperclip.copy(password)


# --------------------------- SEARCH PASSWORD ------------------------------ #
def search_password():
    website = website_input.get()
    try:
        with open("password.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Details", message=f"No data in file")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title="Details",
                                message=f"The details of {website}:\n Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Details", message=f"{website} details not found")
    finally:
        website_input.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "Email": email,
            "Password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("password.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("password.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("password.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.minsize(width=900, height=650)
window.config(bg="white", padx=20, pady=20)

canvas = Canvas(width=300, height=300, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(150, 200, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website Name:: ", font=("courier", 20), bg="white", fg="black", pady=5)
website_label.grid(column=0, row=1)

website_input = Entry(width=46, bg="white", fg="black")
website_input.grid(column=1, row=1, columnspan=1)
website_input.focus()

search_button = Button(text="Search", bg="white", font=("courier", 18), highlightthickness=0, width=16)
search_button.config(command=search_password)
search_button.grid(column=2, row=1, columnspan=1)

username_label = Label(text="Email/Username:: ", font=("courier", 20), bg="white", fg="black", pady=5)
username_label.grid(column=0, row=2)

email_input = Entry(width=70, bg="white", fg="black")
email_input.insert(0, "abhilashjanarrdhan@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:: ", font=("courier", 20), bg="white", fg="black", pady=5)
password_label.grid(column=0, row=3)

password_input = Entry(width=46, bg="white", fg="black")
password_input.grid(column=1, row=3, columnspan=1)

password_button = Button(text="Generate Password", bg="white", font=("courier", 18), highlightthickness=0, width=16)
password_button.config(command=generate_password)
password_button.grid(column=2, row=3, columnspan=1)

add_button = Button(text="Add", bg="white", width=47, font=("courier", 20), highlightthickness=0)
add_button.config(command=add_pass)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
