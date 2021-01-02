"Front camera access"
from tkinter import Tk, Canvas, Label, Entry, Button, Checkbutton, IntVar
#import time
from cv2 import cv2
from PIL import Image, ImageTk
import mysql.connector


class App:
    "Class for tkinter window"
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.window.geometry("2040x2040")

        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(video_source)

        self.my_label = Label(self.window, text="AK Mobile Service Shop", background="black",
                        foreground="white", width=30, height=3, borderwidth=2, relief="raised")
        self.my_label.grid(row=0, column=1, padx=20, pady=40, columnspan=3, sticky='NEWS')

        self.search_button = Button(self.window, text='Search Customer',
                                foreground='black', width=30,
                                height=3,
                                borderwidth=2,
                                relief="raised",
                                font=("Times New Roman", 15),
                                command=self.search_window)
        self.search_button.grid(row=0, column=4, padx=20, pady=40, sticky='NEWS')

        self.current_date = Label(self.window, text="Date", background="green",
        foreground="white", width=20, height=2, relief="raised", font=("Times New Roman", 15))
        self.current_date.grid(row=1, column=0, sticky='NEW', padx=2, pady=0)

        self.current_date_input = Entry(self.window, background="white",
                                    foreground="black", width=20)
        self.current_date_input.grid(row=1,column=1, sticky='NEW', padx=0, pady=0, ipady=6)

        # Create a canvas that can fit the above video source size
        self.photo_booth = Canvas(self.window, width = 350, height = 350)
        self.photo_booth.grid(row=1,column=2, rowspan=3, columnspan=3, padx=0, pady=0)

        #cv_img = cv2.cvtColor(cv2.imread("/Users/karthi/ServiceAPP/frame-12-12-2020-21-48-41.png"),
        #cv2.COLOR_BGR2RGB)
        #height, width, test = cv_img.shape

        self.front_side_image = Canvas(self.window, width = 350, height = 350)
        self.front_side_image.grid(row=1,column=5,columnspan=3, rowspan=3, padx=0, pady=0)

        self.back_side_image = Canvas(self.window, width = 350, height = 350)
        self.back_side_image.grid(row=1,column=9,columnspan=3, rowspan=3, padx=0, pady=0)

        #photo = ImageTk.PhotoImage(image = Image.fromarray(cv_img))
        #img = PhotoImage(file="/Users/karthi/ServiceAPP/frame-12-12-2020-21-00-22.png")
        #self.canvasFront.create_image(0, 0, image=photo)

        #self.canvasBack = Canvas(self.window, width = 50, height = 50)
        #self.canvasBack.grid(row=1,column=7, padx=0, pady=0)

        self.bill_number_label = Label(self.window, text="Bill No.", background="green",
                                    foreground="white", width=20, height=2, relief="raised",
                                    font=("Times New Roman", 15))
        self.bill_number_label.grid(row=2, column=0, sticky='NEW', padx=5, pady=0)

        self.bill_number_value = Entry(self.window, background="white",
                                    foreground="black", width=20)
        self.bill_number_value.grid(row=2, column=1, sticky='NEW', padx=0, pady=0, ipady=6)

        self.customer_name_label = Label(self.window, text="Enter Customer Name",
                                    background="green", foreground="white", width=20, height=2,
                                    relief="raised", font=("Times New Roman", 15))
        self.customer_name_label.grid(row=3,column=0, sticky='NEW', padx=5, pady=0)

        self.customer_name_value = Entry(self.window, background="white", foreground="black",
                                    width=20)
        self.customer_name_value.grid(row=3,column=1, sticky='NEW', padx=0, pady=0, ipady=6)

        self.product_name = Label(self.window, text="Enter Product Name", background="green",
                            foreground="white", width=20, height=2,
                            relief="raised", font=("Times New Roman", 15))
        self.product_name.grid(row=4, column=0, sticky='NEW', padx=5, pady=0)

        self.product_name_value = Entry(self.window, background="white",
                                    foreground="black", width=20)
        self.product_name_value.grid(row=4, column=1, sticky='NEW', padx=0, pady=0, ipady=6)

        self.snapshot_button_screen = Button(self.window, text="Screen Snapshot",
                                        background="green", foreground="black", width=20, height=2,
                                        relief="raised", font=("Times New Roman", 15),
                                        command=lambda: self.snapshot(1))
        self.snapshot_button_screen.grid(row=4, column=3, sticky='NW', padx=0, pady=5, ipady=6)

        self.snapshot_button_backcover = Button(self.window, text="Back Cover Snapshot",
                                            background="green", foreground="black", width=20,
                                            height=2, relief="raised",
                                            font=("Times New Roman", 15),
                                            command=lambda: self.snapshot(2))
        self.snapshot_button_backcover.grid(row=4, column=4, sticky='NE', padx=0, pady=5, ipady=6)

        self.model_name = Label(self.window, text="Enter Model Name", background="green",
                            foreground="white", width=20, height=2, relief="raised",
                            font=("Times New Roman", 15))
        self.model_name.grid(row=5,column=0, sticky='EW', padx=5, pady=50)

        self.model_name_value = Entry(self.window, background="white", foreground="black")
        self.model_name_value.grid(row=5, column=1, sticky='EW', padx=0, pady=50, ipady=6)

        self.battery_status  = IntVar()
        self.backcase_status = IntVar()

        self.is_with_battery = Checkbutton(self.window, text='BATTERY', background="#7aaebf",
                                variable=self.battery_status,
                                relief="raised",
                                font=("Times New Roman", 15))
        self.is_with_battery.grid(row=5, column=2, sticky='EW', pady=40, padx=15, ipady=6)

        self.is_with_backcase = Checkbutton(self.window, text='BACK CASE',
                                    variable=self.backcase_status,
                                    background="#7aaebf", relief="raised",
                                    font=("Times New Roman", 15))
        self.is_with_backcase.grid(row=5, column=3, sticky='EW', pady=40, padx=15, ipady=6)

        self.issue_type = Label(self.window, text="Enter Issue", background="green",
                            foreground="white", width=20, height=2, relief="raised",
                            font=("Times New Roman", 15))
        self.issue_type.grid(row=6, column=0, padx=5, pady=35)

        self.issue_type_input = Entry(self.window, background="white", foreground="black")
        self.issue_type_input.grid(row=6, column=1, sticky='EW', padx=0, pady=35, ipady=6)

        self.delivery_date = Label(self.window, text="Delivery Date", background="green",
                                foreground="white", width=20, height=2, relief="raised",
                                font=("Times New Roman", 15))
        self.delivery_date.grid(row=6, column=2, padx=5, pady=30)

        self.delivery_date_value = Entry(self.window, background="white", foreground="black")
        self.delivery_date_value.grid(row=6, column=3, sticky='EW', padx=0, pady=30, ipady=6)

        self.return_date = Label(self.window, text="Return Date", background="green",
                            foreground="white", width=20, height=2, relief="raised",
                            font=("Times New Roman", 15))
        self.return_date.grid(row=6, column=4, padx=5, pady=30)

        self.return_date_value = Entry(self.window, background="white", foreground="black")
        self.return_date_value.grid(row=6, column=5, sticky='EW', padx=0, pady=30, ipady=6)

        self.save_button = Button(self.window, text="Save", background="green", foreground="black",
                            width=20, height=2, command=self.save_info,
                            font=("Times New Roman", 15))
        self.save_button.grid(row=7, column=2, sticky='EW', padx=0, pady=25, ipady=6)

        #After it is called once, the update method will be automatically
        #called every delay milliseconds
        self.delay = 15
        self.update()

        self.window.mainloop()

    def update(self):
        "Get a frame from the video source"
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
            self.photo_booth.create_image(0, 0, image = self.photo)

        self.window.after(self.delay, self.update)

    def snapshot(self, flip):
        "Get a frame from the video source"
        ret, frame = self.vid.get_frame()
        #self.side = flip
        print(flip)

        if ret:
            #self.front_side_image.create_image(0,0,image='/Users/karthi/ServiceAPP/'+img)
            #cv_img = cv2.cvtColor(
            #cv2.imread('/Users/karthi/ServiceAPP/frame-12-12-2020-21-48-41.png'),
            #cv2.COLOR_BGR2RGB)
            #photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
            if flip == 1:
                cv2.imwrite("FrontSideframe_" + self.bill_number_value.get() + ".png",
                cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
                self.front_image = ImageTk.PhotoImage(image = Image.fromarray(frame))
                self.front_side_image.create_image(0,0,image=self.front_image)
                self.front_image_name = "FrontSideFrame_" + self.bill_number_value.get() + ".png"
            if flip == 2:
                cv2.imwrite("BackSideFrame_" + self.bill_number_value.get() + ".png",
                cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
                self.back_image = ImageTk.PhotoImage(image = Image.fromarray(frame))
                self.back_side_image.create_image(0,0,image=self.back_image)
                self.back_image_name = "BackSideFrame_" + self.bill_number_value.get() + ".png"

    def search_window(self):
        """
        Quit Save Window
        Open Search Window
        """
        #self.window.quit()
        #self.window.after_cancel()
        self.vid.__del__()
        self.window.destroy()
        Search(Tk(), "Tkinter and OpenCV")

    def save_info(self):
        """
        Save information in Database
        """
        database_conn = mysql.connector.connect(host ="localhost",
                                                user = "root",
                                                password = "karthi123",
                                                db ="customerinfo")
        print("Battery, Backcase", self.is_with_backcase.getint, self.is_with_battery.getint)
        try:
            cursor = database_conn.cursor()
            cursor.execute("INSERT INTO Customer (Name, Bill_Numer, \
            registered_date, Product_Name, Model_Name, Issue_Description, \
            Promised_Delivery_Date, Actual_Delivery_Date,\
            Battery, Backcase, Front_image, Back_image )\
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
            self.customer_name_value.get(), self.bill_number_value.get(),
            self.current_date_input.get(), self.product_name_value.get(),
            self.model_name_value.get(), self.issue_type_input.get(),
            self.delivery_date_value.get(), self.return_date_value.get(),
            self.battery_status.get(), self.backcase_status.get(),
            self.back_image_name, self.front_image_name
            )
            )
            database_conn.commit()
            print("Query Excecuted successfully",
            self.customer_name_value.get(), self.bill_number_value.get(),
            self.current_date_input.get(), self.product_name_value.get(),
            self.model_name_value.get(), self.issue_type_input.get(),
            self.delivery_date_value.get(), self.return_date_value.get(),
            self.battery_status.get(), self.backcase_status.get(),
            self.back_image_name, self.front_image_name)
        except TypeError as db_error:
            database_conn.rollback()
            print("Error occured", db_error)

        #value = self.current_date_input.get()
        #print("Value of current date: ")
        #print(value)

class MyVideoCapture:
    "Video capturing functionalities"
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

    def get_frame(self):
        "get frame"
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

class Search:
    "Class for tkinter window"
    def __init__(self, window, window_title):
        self.swindow = window
        self.swindow.title(window_title)
        self.swindow.geometry("2040x2040")

        self.my_label = Label(self.swindow, text="AK Mobile Service Shop", background="black",
                        foreground="white", width=40, height=3, borderwidth=2, relief="raised")
        self.my_label.grid(row=0, column=3, padx=20, pady=10, columnspan=3)

        self.show_bill_number = Label(self.swindow, text="Bill Number: ", background="black",
                                    foreground="white", width=40, height=2,
                                    font=("Times New Roman", 15))
        self.show_bill_number.grid(row=1, column=0, padx=2, pady=5, sticky='EW')

        self.show_current_date = Label(self.swindow, text="Registered Date: ", background="black",
        foreground="white", width=40, height=2, font=("Times New Roman", 15))
        self.show_current_date.grid(row=2, column=0, padx=2, pady=5, sticky='EW')

        self.show_customer_name = Label(self.swindow, text="Enter Customer Name: ",
                                    background="black", foreground="white", width=40, height=2,
                                    font=("Times New Roman", 15))
        self.show_customer_name.grid(row=3,column=0, padx=2, pady=5, sticky='EW')

        self.show_product_name = Label(self.swindow, text="Enter Product Name", background="black",
                            foreground="white", width=40, height=2,
                            relief="raised", font=("Times New Roman", 15))
        self.show_product_name.grid(row=4, column=0, padx=2, pady=10, sticky='NEWS')

        self.show_model_name = Label(self.swindow, text="Enter Model Name", background="black",
                            foreground="white", width=40, height=2,
                            font=("Times New Roman", 15))
        self.show_model_name.grid(row=5, column=0, padx=2, pady=10, sticky='NEWS')

        self.show_issue_type = Label(self.swindow, text="Enter Issue: ", background="black",
                            foreground="white", width=40, height=2,
                            font=("Times New Roman", 15))
        self.show_issue_type.grid(row=6, column=0, padx=2, pady=10, sticky='NEWS')

        self.show_delivery_date = Label(self.swindow, text="Delivery Date: ", background="black",
                                foreground="white", width=40, height=2,
                                font=("Times New Roman", 15))
        self.show_delivery_date.grid(row=7, column=0, padx=2, pady=10, sticky='NEWS')

        self.show_return_date = Label(self.swindow, text="Return Date: ", background="black",
                                foreground="white", width=40, height=2,
                                font=("Times New Roman", 15))
        self.show_return_date.grid(row=8, column=0, padx=2, pady=10, sticky='NEWS')

        self.show_is_with_battery = Label(self.swindow, text='Battery Status', background="black",
                                foreground="white", width=40, height=2,
                                font=("Times New Roman", 15))
        self.show_is_with_battery.grid(row=9, column=0, padx=2, pady=10, sticky='NEWS')

        self.show_is_with_backcase = Label(self.swindow, text='Backcase Status', background="black",
                                foreground="white", width=40, height=2,
                                font=("Times New Roman", 15))
        self.show_is_with_backcase.grid(row=10, column=0, padx=2, pady=10, sticky='NEWS')

        self.show_front_side_image = Canvas(self.swindow, width = 350, height = 350)
        self.show_front_side_image.grid(row=1, column=2, columnspan=3, rowspan=3, padx=2, pady=10)

        self.show_back_side_image = Canvas(self.swindow, width = 350, height = 350)
        self.show_back_side_image.grid(row=5, column=2, columnspan=3, rowspan=3, padx=2, pady=10)

        self.get_info()

        self.swindow.mainloop()

    def get_info(self):
        """
        get information from database
        """
        database_conn = mysql.connector.connect(host ="localhost",
                                                user = "root",
                                                password = "karthi123",
                                                db ="customerinfo")
        cursor = database_conn.cursor()
        selectquery = "select * from Customer"
        try:
            cursor.execute(selectquery)
            customer_info = cursor.fetchall()

            for info in customer_info:
                self.show_bill_number.config(text="Bill Number: {}".format(info[2]))
                self.show_current_date.config(text="Registered Date: {}".format(info[3]))
                self.show_customer_name.config(text="Customer Name: {}".format(info[1]))
                self.show_product_name.config(text="Product Name: {}".format(info[4]))
                self.show_model_name.config(text="Model Name: {}".format(info[5]))
                self.show_issue_type.config(text="Issue Type: {}".format(info[6]))
                self.show_delivery_date.config(text="Delivery Date: {}".format(info[7]))
                self.show_return_date.config(text="Return Date: {}".format(info[8]))
                self.show_front_image=info[12]
                self.show_back_image=info[11]
                if(info[9]) == 1:
                    battery = 'Yes'
                else:
                    battery = 'No'
                self.show_is_with_battery.config(text="Battery Status: "+battery)
                if(info[10]) == 1:
                    backcase = 'Yes'
                else:
                    backcase = 'No'
                self.show_is_with_backcase.config(text="Backcase Status: "+backcase)
                if self.show_front_image is not None:
                    self.cv_img_front = cv2.cvtColor(
                    cv2.imread("/Users/karthi/ServiceAPP/"+self.show_front_image),
                    cv2.COLOR_BGR2RGB)
                    self.photo_front = ImageTk.PhotoImage(
                        image = Image.fromarray(self.cv_img_front)
                        )
                    print(self.photo_front, self.show_front_image)
                    self.show_front_side_image.create_image(0,0,image=self.photo_front)
                
                if self.show_back_image is not None:
                    self.cv_img_back = cv2.cvtColor(
                    cv2.imread("/Users/karthi/ServiceAPP/"+self.show_back_image),
                    cv2.COLOR_BGR2RGB)
                    self.photo_back = ImageTk.PhotoImage(
                        image = Image.fromarray(self.cv_img_back)
                        )
                    print(self.photo_back, self.show_back_image)
                    self.show_back_side_image.create_image(0,0,image=self.photo_back)


        except TypeError as image_error:
            database_conn.rollback()
            print(image_error)

App(Tk(), "Tkinter and OpenCV", 0)
#Search(Tk(), "Tkinter and OpenCV")

#Create Table Customer(ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(100) NOT NULL,
#Bill_Numer INT NOT NULL PRIMARY KEY, registered_date VARCHAR(30),
#Product_Name VARCHAR(100) NOT NULL, Model_Name VARCHAR(100) NOT NULL,
#Issue_Description VARCHAR(300) NOT NULL, Promised_Delivery_Date VARCHAR(20),
#Actual_Delivery_Date VARCHAR(30), Battery INT(1), Backcase INT(1),
#Front_image VARCHAR(50), Back_image VARCHAR(50) )
#cursor.execute("INSERT INTO Customer (Name, Bill_Numer,\
#                registered_date, Product_Name, Model_Name, Issue_Description, \
#                Promised_Delivery_Date, Actual_Delivery_Date, Battery, Backcase, \
#                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
#                (self.customer_name_value.get(), self.bill_number_value.get(),
#                self.current_date_input.get(), self.product_name_value.get(),
#                self.model_name_value.get(), self.issue_type_input.get(),
#                self.return_date_value.get(), self.is_with_battery,
#                self.is_with_backcase)
#                )
#            database_conn.commit()
#            print("Query Excecuted successfully",
#            self.customer_name_value.get(), self.bill_number_value.get(),
#            self.current_date_input.get(), self.product_name_value.get(),
#            self.model_name_value.get(), self.issue_type_input.get(),
#            self.return_date_value.get(), self.is_with_battery,
#            self.is_with_backcase)
