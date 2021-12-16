# GUI Example

# PyQt5 pip install PyQt5

# Tkinter pip install tkinter

# Kivy pip install kivy

# importing functions from tkinter library
from tkinter import *

# importing sqlite3
import sqlite3

#########################
#   CREATING THE GUI    #
#########################

# Create tkinter window
root = Tk()

# giving window title
root.title('Address Book')

# size of window in pixels
root.geometry("400x400")

##################################
#   CONNECTING TO SQL DATABASE   #
##################################

# creating a variabel that stores the connection to the database
# that we want to connect to
# if database does not exist, it creates a new one
address_book_connect = sqlite3.connect('address_book.db')

# creating a cursor
# object that links us to the database
address_book_cur = address_book_connect.cursor()

# execute different queries or different ddl/dml commands
# creating table addresses with attributes: first_name, last_name
# street, city, state, and zipcode
# address_book_cur.execute('''CREATE TABLE addresses(
#                             first_name text, 
#                             last_name text, 
#                             street text, 
#                             city text, 
#                             state text, 
#                             zipcode integer)''')

# execute can be connected to buttons or other things in the GUI

# insert values into the database through a GUI component

# creating a function called submit using this function as a button
# to insert values into the database
def submit():
    # connecting to database
    submit_conn = sqlite3.connect('address_book.db')

    # linking to db
    submit_cur = submit_conn.cursor()

    submit_cur.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :street, :city, :state, :zipcode)",
                       {
                           'f_name': f_name.get(),
                           'l_name': l_name.get(),
                           'street': street.get(),
                           'city': city.get(),
                           'state': state.get(),
                           'zipcode': zipcode.get()
                       })

    # commit changes
    submit_conn.commit()
    
    # close connection
    submit_conn.close()


# define input query structure

def input_query():
    input_query_connect = sqlite3.connect('address_book.db')
    input_query_cursor = input_query_connect.cursor()
    input_query_cursor.execute("SELECT first_name, last_name FROM addresses WHERE state = ? AND city = ? ",
                            (state.get(), city.get(),)) 
    
    # Go through the db and save the output to output records
    output_records = input_query_cursor.fetchall()
    
    # console print out
    # print(output_records)
    print_records = ''
    
    for output_record in output_records:
        print_records += str(output_record[0] + " " + output_record[1] + "\n")
    
    # print(print_records)
    
    # print out the names below 
    input_query_label = Label(root, text = print_records)
    input_query_label.grid(row = 9, column = 0, columnspan = 2)
    

# define general query structure


####################################
#   BUILDING THE GUI COMPONENTES   #
####################################

# pack place grid 
    # pack - pack components in a certain area
    # place - certain coordinate to place the components
    # grid - put it in a grid like strucutre with rows and columns
    
# create text boxes
    # entry is the component for text boxes

f_name = Entry(root, width = 30)
# place it in a position, padx is a padding in pixels
f_name.grid(row = 0, column = 1, padx = 20)

l_name = Entry(root, width=30)
l_name.grid(row = 1, column = 1, padx = 20)
 
street = Entry(root, width = 30)
street.grid(row = 2, column = 1, padx = 20)

city = Entry(root, width = 30)
city.grid(row = 3, column = 1, padx = 20)

state = Entry(root, width = 30)
state.grid(row = 4, column = 1, padx = 20)

zipcode = Entry(root, width = 30)
zipcode.grid(row = 5, column = 1, padx = 20)


# creating the labels for the text boxes, first name
f_name_label = Label(root, text = 'First Name: ')
# place it 
f_name_label.grid(row = 0, column = 0)

l_name_label = Label(root, text = 'Last Name: ')
l_name_label.grid(row = 1, column = 0)

street_label = Label(root, text = 'Street: ')
street_label.grid(row = 2, column = 0)

city_label = Label(root, text = 'City: ')
city_label.grid(row = 3, column = 0)

state_label = Label(root, text = 'State: ')
state_label.grid(row = 4, column = 0)

zipcode_label = Label(root, text='Zipcode: ')
zipcode_label.grid(row=5, column=0)

# Creating Buttons
# Where the text box connects with the submit function 
submit_button = Button(root, text = 'Add Records to DB', command = submit)
submit_button.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

input_query_button = Button(root, text = 'Select Specific Name', command = input_query)
input_query_button.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

# event to open the window -- executes tkinter components
root.mainloop()
