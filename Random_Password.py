#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 08:57:40 2023

@author: Jeff
"""


# Create a Random password 

import random


password_combo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@$%^&*?'

def rand_password (password_length, password_composition) :
    new_password = ''
    for c in range(password_length) :
        new_password += random.choice(password_composition)
    return new_password


length_pwd = input('How long do you want the password to be: ')
length_pwd = int(length_pwd)


ab = (rand_password(length_pwd, password_combo))
print (ab)


#def rand_password (password_length, password_composition) :
   # new_password = ''
    #for char in range(num_passwords) :
        #while len(new_password) < password_length :
   # for c in range(password_length) :
            #object_holder = random.choice(password_composition)
       # new_password += random.choice(password_composition)
   # return new_password


#length_pwd = input('How long with the password be: ')
#length_pwd = int(length_pwd)

#num_pwd = input('How many passwords do you need: ')
#num_pwd = int(num_pwd)


#ab = (rand_password(length_pwd, password_combo))
#print (ab)


#number = input('Number of passwords to generate: ')
#number = int(number)

#length = input('How long will the password(s) be: ')
#length = int(length)

#print('\nHere are your passwords: ')

#for pwd in range(number) :
 #   passwords = ''
  #  for i in range(length) :
   #     passwords += random.choice(password_combo)
    #print (passwords)


















































































