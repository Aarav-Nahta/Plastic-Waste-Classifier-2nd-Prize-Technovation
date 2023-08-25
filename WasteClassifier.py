#By - CDR4 
'''
TOPIC - A homemaker just learnded the impact of plastic help her to navigate
through the house indetify recyclable plastic and non recyclable waste via helper 
'''


#-------------Importing Modules-------------

#Importing Tkinter module as tk 
import tkinter as tk 
from tkinter import messagebox
#Importing Os module
import os 


#------------Functions(BACKEND)---------


#Points Will be 0 For new user
points = 0

#Function For Writing file 
def writeFile(name, data):
    filew = open(name, 'w+') #using w
    filew.write(data)
    filew.close()

#Function for Reading th existing file
def readFile(name):
    if os.path.isfile(name):
        filer = open(name, 'r+')
        filer.seek(0, os.SEEK_SET)
        strp = filer.read()
        return int(strp)
    else:
        writeFile(name, '0')
        return 0
#Points Var will be now the points inside the file 
points = readFile('point.txt')




#loop
points += 4     

#If file is not present the new file will be created with the name point.txt
writeFile('point.txt', str(points))


#DATABSE FOR ITEMS AND CITIES 


# Database of common items and their recyclability status
plastic_items = {
        "plastic bottle": "recyclable",
        "plastic bag": "non-recyclable",
        "plastic container": "recyclable",
        "newspaper":"non-recyclable",
        "glass":"non-recyclable",
        "cloths":"non-recyclable",
        "Cans":"recyclable",
        "Garbage":"non-recyclable",
        "polyethene":"non-recyclable",
        #more items can be added in this database 
    
}
# Database of Cities and Dumpsturs Loacation status

city = {
        "mumbai": '''Thane, Kandivali, Bandra, 
        Andheri, ChurchGate ''',
        "delhi": '''Gazipur, Tikri Kalan,
          Karol Bagh''',
        "indore": "Bhicholi",
        "banglore":"Main Street 90ft road",
        "chennai":"Dumpstur Hub road"
        #more items can be added in this database
}

#Function for checking item with database
def identify_plastic(item):
    return plastic_items.get(item.lower(), "unknown")


#Function for checking Cities with database
def indentify_city(area):
    return city.get(area.lower(),"unknown")

#this function is for Checking the recyclability of the item
def check_plastic():
    item = item_entry.get()
    recyclability = identify_plastic(item)
    if recyclability == "unknown":
        result_label.config(text="Sorry, I couldn't identify the item.")
    else:
        result_label.config(text=f"The {item} is {recyclability}.")

#this function is for Fetching Location of the Dumpstur inside a city
def check_dumpsturs():
    area = area_entry.get()
    dumpsturs = indentify_city(area)
    if dumpsturs == "unknown":
        result_label_city.config(text="Sorry, I couldn't identify the City.")
    else:
        result_label_city.config(text=f"In {area} dumpsturs are in {dumpsturs}.")

#Functin for Exit Button || Terminating the program
def exit_app():
    window.destroy()




# ------ GUI DESIGN (FrontEnd) --------


# Creating the main window
window = tk.Tk()
window.title("Plastic Waste Sorting Assistant")
window.geometry("400x400+10+20")

# Creating and placing widgets
label = tk.Label(window, text="Enter the type of plastic item you have:")
label.pack(pady=10)

item_entry = tk.Entry(window)
item_entry.pack(pady=5)

check_button = tk.Button(window, text="Check", command=check_plastic)
check_button.pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

label = tk.Label(window, text="Enter Your location for your near by dumpsturs:")
label.pack(pady=10)

area_entry = tk.Entry(window)
area_entry.pack(pady=5)

check_button_city = tk.Button(window, text="Check For Dumpsturs", command=check_dumpsturs)
check_button_city.pack(pady=5)

result_label_city = tk.Label(window, text="")
result_label_city.pack(pady=5)

exit_button = tk.Button(window, text="Exit", command=exit_app)
exit_button.pack(pady=10)

label_points = tk.Label(window, text=f"Total Points : {points}")
label_points.pack(pady=10)


# Start the main event loop
window.mainloop()