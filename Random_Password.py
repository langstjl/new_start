#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 08:57:40 2023

@author: Jeff
"""


# Create a Random password 

import random
import tkinter as tk

password_combo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@$%^&*?'

def extract_pass_length():
    extract_length = entry_length.get()
    return extract_length

output_statement = "Your semi-random password of ",(extract_length)," characters is:","\n",(final_password)"
# Above to be used in second window ouput.
extract_length = isdigit()

first_window = tk.Tk()
first_window.Title(text = "Random Password Generator")
first_window.geometry("300x250")
length_entry = tk.Entry(first_window,
                        text = "Insert character length for the password",
                        justify = "left",
                       fg = "black",
                       bg = "white",
                       )

submit_button = tk.Button(first_window,
                          text="Submit",
                          command=extract_pass_length)

submit_button.pack()

def character_check():
    if int(extract_length) != 'true':
        warning_window = tk.Tk()
        warning_window.Title(text = "WARNING")
        warning_window.Label(text = "Please enter a number with no spaces",
                            font = (Arial, 24),
                             fg = "black",
                             bg = "yellow",
                            )
        warning_window.geometry("200x175")
        warning_button = tk.Button(warning_window,
                                   text = "Understood",
                                   command = warning_window.destroy()
                                  )
    elif:
        if extract_length == 0:
            warning_window.Title(text = "WARNING")
            warning_window.Label(text = "Please enter a number larger than zero",
                            font = (Arial, 24),
                             fg = "black",
                             bg = "yellow",
                            )
        warning_window.geometry("200x175")
        warning_button = tk.Button(warning_window,
                                   text = "Understood",
                                   command = warning_window.destroy()
                                  )
    else:
        pass



def rand_password (password_length, password_composition) :
    new_password = ''
    for i in range(password_length) :
        new_password += random.choice(password_composition)
    return new_password

#length_pwd = input('How long do you want the password to be: ')
#length_pwd = int(length_pwd)


final_password = (rand_password(extract_length, password_combo))
print (final_password)

second_window = tk.Tk()
second_window.Title("Password Results")
second_window.geometry("300x250")
second_window.Label(text = (output_statement),
                    font = (Arial, 24),
                    fg = "black"
                   )
end_and_copy_button = tk.Button(second_window,
                                text = ("Copy Password and Close"),
                                

def copy_password_clipboard():
    global final_password
    second_window.clipboard_clear()
    second_window.clipboard_append(final_password)
    second_window.update()

first_windown.mainloop()
second_window.mainloop()
















































































