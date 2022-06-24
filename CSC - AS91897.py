# Made by : Krishan Chand
# Started/Finished :  07/ 06 / 22 - 24/ 06 / 22 


##############################################################
###This program is for Juiles Party Hire to track her items###
##############################################################


#importing tkinter
from tkinter import *
from tkinter import ttk 
import sqlite3 

#creating my screen and title 
root=Tk()
root.title("Julie's Party Hire Item Tracker")
root.geometry('1000x850')

global item_details, entry1, entry2, entry3, entry4, entry5, total_entries, row_count
total_entries = 0
item_details = []
row_count = 0


#Button commands

def print(): 
    global item_details, entry1, entry2, entry3, entry4, entry5, total_entries, row_count
    
    #checks the info stored on the item_details list and then places them on the grid
    while row_count < total_entries :
            Label(root, text=row_count).grid(column=0,row=row_count+9) 
            Label(root, text="                                  "+(item_details[row_count][0])+"                                 ").grid(column=1,row=row_count+9)
            Label(root, text="                                  "+(item_details[row_count][1])+"                                 ").grid(column=2,row=row_count+9)
            Label(root, text="                                  "+(item_details[row_count][2])+"                                 ").grid(column=3,row=row_count+9)
            Label(root, text="                                  "+(item_details[row_count][3])+"                                 ").grid(column=4,row=row_count+9)
            row_count +=  1 #adds a row so the next print goes on the following line

def quit(): #code for button# to leave the screen/root
    root.destroy()#destroys root

def check(data, data_type): #function used to check if the entered value is an integer
    try:
        data_type(data)
        return True
    except ValueError:
        return False            

def append():  # add next item to the list
    #global variables used
    global item_details, entry1, entry2, entry3, entry4, entry5, total_entries, row_count, error1, error2, error3

    #checking all the requirements
    if len(entry1.get()) !=0 and len(entry2.get()) !=0 and len(entry3.get()) !=0 and len(entry4.get()) !=0 and check(entry2.get(), int) and check(entry4.get(), int):

        #checking if the items hired is between 1 and 500
        if 1 <= int(entry4.get()) <= 500:

            #storing the list into item_details
            item_details.append([entry1.get(),entry2.get(),entry3.get(),entry4.get()])

            #emptying all the entry fields
            entry1.delete(0,'end')
            entry2.delete(0,'end')
            entry3.delete(0,'end')
            entry4.delete(0,'end')
            total_entries +=  1


            #destroying any error messages
            for obj in root.grid_slaves(row=4, column=4):
                obj.destroy()

            for obj in root.grid_slaves(row=2, column=4):
                obj.destroy()

        else:

            #destroying any error messages
            for obj in root.grid_slaves(row=4, column=4):
                obj.destroy()
            for obj in root.grid_slaves(row=2, column=4):
                obj.destroy()

            #error message if item hired is not between 1 and 500
            error1 = Label(root, text="Enter a number between 1 and 500", fg="red").grid(column=4, row=4)
            

    else :

        #destroying any error messages
        for obj in root.grid_slaves(row=4, column=4):
                obj.destroy()
        for obj in root.grid_slaves(row=2, column=4):
                obj.destroy()

        #error message if receipt number and items hired entered values are not integers
        error2 = Label(root, text="Only Numbers", fg="red").grid(column=4, row=2)
        error1 = Label(root, text="Only Numbers", fg="red").grid(column=4, row=4)


def delete():


    #global values used
    global item_details, entry1, entry2, entry3, entry4, entry5, total_entries, row_count, error1, error2, error3
    #find which row is to be deleted and delete it
    if entry5.get() == "":

            #destroying any error messages
            for obj in root.grid_slaves(row=5, column=4):
                obj.destroy()

            #error message if there is no value in row number
            error3 = Label(root, text="Please enter a row number", fg="red").grid(column=4, row=5)

    elif check(entry5.get(), int):

        if int(entry5.get()) + 1 > row_count:
            
            #destroying any error messages
            for obj in root.grid_slaves(row=5, column=4):
                    obj.destroy()

                    # error message if the value entered in row number does not exist
            error3 = Label(root, text="Please enter a valid number", fg="red").grid(column=4, row=5)

        else:

            #destroying any error messages
            for obj in root.grid_slaves(row=5, column=4):
                    obj.destroy()

                  
            selectedrow = int(entry5.get())
            total_entries -= 1
            row_count -= 1
            entry5.delete(0,'end')
            #clear the last item displayed on the GUI
            Label(root, text="                                  ").grid(column=0,row=selectedrow+9) 
            Label(root, text="                                  ").grid(column=1,row=selectedrow+9)
            Label(root, text="                                  ").grid(column=2,row=selectedrow+9)
            Label(root, text="                                  ").grid(column=3,row=selectedrow+9)
            Label(root, text="                                  ").grid(column=4,row=selectedrow+9)
            #print all the items in the list
            del item_details[selectedrow]
            print()

    
    else:
            #destroying any error messages
            for obj in root.grid_slaves(row=5, column=4):
                obj.destroy()

                #error message if the value entered in row number is not an integer
                error3 = Label(root, text="Please enter a number", fg="red").grid(column=4, row=5)


