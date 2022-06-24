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












































































































































root.mainloop()
