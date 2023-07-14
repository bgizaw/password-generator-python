import random
import string
import tkinter as tk

# create a window
window = tk.Tk()
# window title
window.title('Password Generator')
# dimensions of window
window.geometry('500x500')
# give the window a label
title_label = tk.Label(window, font='bold 10', text='PASSWORD GENERATOR')
title_label.pack()


# function to create password
def password_generate(length):
    # these are all the characters allowed in the password
    valid_char = string.ascii_letters + string.digits + '@_'
    # random generation of the password
    password = ''.join(random.sample(valid_char, length))
    # display the password
    password_label.config(text=password)


password_label = tk.Label(window, text = 'password', font=('bold', 20))
password_label.pack()

# convert string input in each checkbox to integer
len_var = tk.IntVar()

# create checkboxes
tk.Radiobutton(window, text='4 character', variable=len_var, value=4).pack()
tk.Radiobutton(window, text='6 character', variable=len_var, value=6).pack()
tk.Radiobutton(window, text='8 character', variable=len_var, value=8).pack()


# defines what length will be passes to the password_generate() function
def get_len():
    length = len_var.get()
    if length == 4:
        password_generate(4)
    elif length == 6:
        password_generate(6)
    elif length == 8:
        password_generate(8)
    # if no checkbox is selected, generate a 6 character password
    else:
        password_generate(6)


# create a button named Generate that runs the get_len() function when clicked
generate_button = tk.Button(window, text='Generate', font=('normal', 10), bg='pink', command=get_len)
generate_button.pack()
password_generate(6)
# run the window
window.mainloop()
