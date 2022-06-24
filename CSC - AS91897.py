# Created by: Krishan Chand

#######################################################################
#  This program is for Julie's Party Hire company to track her items  #
#######################################################################


# import tkinter 
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import sqlite3

# Creating the screen and titling 
root = Tk()
root.title("Julie's Party Hire Item Tracker")
root.geometry('1000x850')

# using global variables
global item_details, entry1, entry2, entry3, entry4, entry5, total_entries, row_count
total_entries = 0
item_details = []
row_count = 0 

# Creating button commands
def print():
    global item_details, entry1, entry2, entry3, entry4, entry5, total_entries, row_count
    
    while row_count < total_entries:
        Label(root, text = row_count).grid(column=0,row=row_count+9)
        Label(root, text="                                    "+(item_details[row_count][0])+"                                   ").grid(column=1,row=row_count+9)
        Label(root, text="                                    "+(item_details[row_count][1])+"                                   ").grid(column=2,row=row_count+9)
        Label(root, text="                                    "+(item_details[row_count][2])+"                                   ").grid(column=3,row=row_count+9)
        Label(root, text="                                    "+(item_details[row_count][3])+"                                   ").grid(column=4,row=row_count+9)
        row_count += 1 

# creating a button to quit the screen 
def quit(): 
    root.destroy()

# creating a fucntion which checks if the entered value is a integer
def check(data, data_type):
    try:
        data_type(data)
        return True
    except ValueError:
        return False

# adding the next item to the list 
def append():
    global item_details, entry1, entry2, entry3, entry4, entry5, total_entries, row_count, error1, error2, error3
    if len(entry1.get()) !=0 and len(entry2.get()) !=0 and len(entry3.get()) !=0 and len(entry4.get()) !=0 and check(entry2.get(), int) and check(entry4.get(),int):
        if 1 <= int(entry4.get()) <=500:
            item_details.append([entry1.get(), entry2.get(), entry3.get(), entry4.get()])
            entry1.delete(0, 'end')
            entry2.delete(0, 'end')
            entry3.delete(0, 'end')
            entry4.delete(0, 'end')
            total_entries += 1 











































































































































root.mainloop()
