"""
import tkinter modules
"""
from tkinter import Tk, PhotoImage, Label, Entry, Checkbutton,  Button
#from tkinter import Canvas
import os
import mysql.connector
#from cv2 import cv2

os.system('clear')
serviceApp=Tk()


def get_info():
    """
    get Database information
    """
    database_conn = mysql.connector.connect(host ="localhost",
                                     user = "root",
                                     password = "karthi123",
                                     db ="students")
    cursor = database_conn.cursor()
    savequery = "select * from student"
    try:
        cursor.execute(savequery)
        myresult = cursor.fetchall()
        res=[]
        for student_detail in myresult:
            res.append(student_detail[1])
        print("Query Excecuted successfully")
        nameLabel.config(text=res[0])
    except: # pylint: disable=W0702
        database_conn.rollback()
        print("Error occured")


#titleLogo = PhotoImage(file = "/Users/karthi/ServiceAPP/logo.gif")
backgroundImage = PhotoImage(file = "/Users/karthi/ServiceAPP/backgound.png")

serviceApp.title('AK Mobile Service Shop')
#serviceApp.iconbitmap("/Users/karthi/ServiceAPP/icon.icns")
#C = Canvas( bg="blue", height=1000, width=950)
serviceApp.geometry("1000x950")


serviceApp.columnconfigure(0, weight=1)
serviceApp.columnconfigure(1, weight=3)
serviceApp.columnconfigure(2, weight=3)
serviceApp.columnconfigure(3, weight=20)
serviceApp.columnconfigure(4, weight=20)
#serviceApp.rowconfigure(0, weight=1)
#serviceApp.rowconfigure(1, weight=3)
#serviceApp.rowconfigure(2, weight=1)
#serviceApp.rowconfigure(3, weight=3)
#serviceApp.rowconfigure(4, weight=3)

backgroundLabel = Label(serviceApp, image=backgroundImage)
backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)


#rightSideLogo = Label(serviceApp, image=titleLogo, width=50)
#rightSideLogo.grid(row=0, column=0)

#relief - "flat", "raised", "sunken", "ridge", "solid", and "groove".
myLabel = Label(serviceApp, text="AK Mobile Service Shop",
background="black", foreground="white", width=30, height=2, borderwidth=2, relief="raised")
myLabel.grid(row=0, column=1, padx=20, pady=40, columnspan=3)

currentDate = Label(serviceApp, text="Date", background="green",
foreground="white", width=20, height=2, borderwidth=2, relief="raised")
currentDate.grid(row=1,column=0, padx=2, pady=10)

currentDateInput = Entry(serviceApp, background="white", foreground="black")
currentDateInput.grid(row=1,column=1, sticky='W')

BillNumber = Label(serviceApp, text="Bill No.", background="green",
foreground="white", width=20, height=2, borderwidth=2, relief="raised")
BillNumber.grid(row=1,column=2, padx=2, pady=10, sticky='W', columnspan=1)

BillNumberInput = Entry(serviceApp, background="white", foreground="black")
BillNumberInput.grid(row=1,column=3, sticky='W', columnspan=2)

customerName = Label(serviceApp, text="Enter Customer Name",
background="green", foreground="white", width=20, height=2, borderwidth=2, relief="raised")
customerName.grid(row=2,column=0, padx=2, pady=10)

customerNameInput = Entry(serviceApp, background="white", foreground="black")
customerNameInput.grid(row=2,column=1,sticky='W')

webCam = Label(serviceApp, text="Webcame", background="green",
foreground="white", width=20, height=2, borderwidth=2, relief="raised")
webCam.grid(row=2, rowspan=2, column=2, padx=2, pady=10)

productName = Label(serviceApp, text="Enter Product Name", background="green",
foreground="white", width=20, height=2, borderwidth=2, relief="raised")
productName.grid(row=3,column=0, padx=2, pady=10)

productNameInput = Entry(serviceApp, background="white", foreground="black")
productNameInput.grid(row=3,column=1,sticky='W')

ModelName = Label(serviceApp, text="Enter Model Name", background="green",
foreground="white", width=20, height=2, borderwidth=2, relief="raised")
ModelName.grid(row=4,column=0, padx=2, pady=10)

ModelNameInput = Entry(serviceApp, background="white", foreground="black")
ModelNameInput.grid(row=4,column=1,sticky='W')

issueType = Label(serviceApp, text="Enter Issue", background="green",
foreground="white", width=20, height=2, borderwidth=2, relief="raised")
issueType.grid(row=5,column=0, padx=2, pady=10)

issueTypeInput = Entry(serviceApp, background="white", foreground="black")
issueTypeInput.grid(row=5,column=1,sticky='W', pady=40)

BATTERYSTATUS = 0
BACKCASESTATUS = 1

isWithBattery = Checkbutton(text='Battery', variable=BATTERYSTATUS, onvalue=1,
offvalue=0, background="#7aaebf" )
isWithBattery.grid(row=6, column=1, columnspan=2, sticky='W', pady=40)

isWithBackCase = Checkbutton(text='BackCase', variable=BACKCASESTATUS, onvalue=1,
offvalue=0, background="#7aaebf")
isWithBackCase.grid(row=6, column=2, columnspan=2, pady=40)

delivaryDate = Label(serviceApp, text="Enter Issue", background="green",
foreground="white", width=20, height=2, borderwidth=2, relief="raised")
delivaryDate.grid(row=7,column=0)

delivaryDateInput = Entry(serviceApp, background="white", foreground="black")
delivaryDateInput.grid(row=7,column=1)

returnDate = Label(serviceApp, text="Enter Issue", background="green", foreground="white",
width=20, height=2, borderwidth=2, relief="raised")
returnDate.grid(row=7,column=2)

returnDateInput = Entry(serviceApp, background="white", foreground="black")
returnDateInput.grid(row=7,column=3)

saveButton = Button(serviceApp, text="Save", command=get_info, width=20, height=2)
saveButton.grid(row=8, column=2, pady=40)

nameLabel = Label(serviceApp, text='', width=30, height=2)
nameLabel.grid(row=9, column=1, pady=30)

serviceApp.mainloop()
