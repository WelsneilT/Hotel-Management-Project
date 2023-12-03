from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Room Booking")
        self.root.geometry("1320x580+230+220")

        #================================ variables=================
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        # =================================title ===================================
        lbl_title = Label(self.root, text ="ROOMBOOKING DETAILS", font = ("arial", 18, "bold"), bg ="black", fg = "gold", bd = 4, relief = RIDGE)
        lbl_title.place(x = 0, y=0, width = 1320, height = 50)

        # ================================logo ====================================
        img2 = Image.open(r"images/logohotel.png")
        img2 = img2.resize((100,40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        lblimg = Label(self.root, image=self.photoimg2, bd= 0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        # =====================================labelFrame ============================
        labelframeleft = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "RoomBooking Details",font = ("arial", 12, "bold") ,padx = 2, ) # Khoang cach giua text  bd
        labelframeleft.place(x =5, y = 50, width = 425, height = 490)

        #================================== labels and entrys =================================
        # Customer Contact
        lbl_cust_contact = Label(labelframeleft, text = "Customer Contact",font = ("arial", 12, "bold"), padx = 2, pady=6 )
        lbl_cust_contact.grid(row = 0, column=0, stick = W)
        entry_contact = ttk.Entry(labelframeleft, textvariable=self.var_contact, width= 20, font = ("arial", 13, "bold"))
        entry_contact.grid(row = 0, column= 1, sticky = W)

        #Fetch data button
        btnFetchData = Button(labelframeleft, command = self.Fetch_contact, text = "Fetch Data", font = ("arial", 10, "bold"), bg = "black", fg = "gold", width = 8)
        btnFetchData.place(x=345, y = 4)

        # Check_in Date
        check_in_date = Label(labelframeleft, text = "Check_in Date: ",font = ("arial", 12, "bold"), padx = 2, pady=6 )
        check_in_date.grid(row = 1, column=0, stick = W) 
        txtCheck_in_date = ttk.Entry(labelframeleft, textvariable=self.var_checkin, width= 27, font = ("arial", 13, "bold"))
        txtCheck_in_date.grid(row = 1, column= 1)

        # Check_out Date
        check_out_date = Label(labelframeleft, text = "Check_out Date: ",font = ("arial", 12, "bold"), padx = 2, pady=6 )
        check_out_date.grid(row = 2, column=0, stick = W) 
        txtCheck_out_date = ttk.Entry(labelframeleft, textvariable = self.var_checkout, width= 27, font = ("arial", 13, "bold"))
        txtCheck_out_date.grid(row = 2, column= 1)

        # Room Type
        label_RoomType = Label(labelframeleft, text = "Room Type:",font = ("arial", 12, "bold"), padx = 2, pady=6 )
        label_RoomType.grid(row = 3, column=0, stick = W)

        combo_RoomType = ttk.Combobox(labelframeleft, textvariable = self.var_roomtype, font = ("arial", 12, "bold"), width = 25, state = "readonly")
        combo_RoomType["value"] = ("Single", "Double", "Luxary")
        combo_RoomType.current(0)
        combo_RoomType.grid(row = 3, column=1)

        #Available Room
        lblAvailableRoom = Label(labelframeleft, text = "Available Room",font = ("arial", 12, "bold"), padx = 2, pady=6 )
        lblAvailableRoom.grid(row = 4, column=0, stick = W) 
        txtRoomAvailable = ttk.Entry(labelframeleft, textvariable=self.var_roomavailable, width= 27, font = ("arial", 13, "bold"))
        txtRoomAvailable.grid(row = 4, column= 1)

        #Meal
        lblMeal = Label(labelframeleft, text = "Meal: ",font = ("arial", 12, "bold"), padx = 2, pady=6 )
        lblMeal.grid(row = 5, column=0, stick = W) 
        txtMeal = ttk.Entry(labelframeleft, textvariable=self.var_meal, width= 27, font = ("arial", 13, "bold"))
        txtMeal.grid(row = 5, column= 1)

        #Number of Days
        lblNoOfDays = Label(labelframeleft, text = "No of Days: ",font = ("arial", 12, "bold"), padx = 2, pady=6 )
        lblNoOfDays.grid(row = 6, column=0, stick = W) 
        txtNoOfDays = ttk.Entry(labelframeleft, textvariable = self.var_noofdays, width= 27, font = ("arial", 13, "bold"))
        txtNoOfDays.grid(row = 6, column= 1)

        #Paid Tax
        lblNoOfDays = Label(labelframeleft, text = "Paid Tax: ",font = ("arial", 12, "bold"), padx = 2, pady=6 )
        lblNoOfDays.grid(row = 7, column=0, stick = W) 
        txtNoOfDays = ttk.Entry(labelframeleft, textvariable=self.var_paidtax, width= 27, font = ("arial", 13, "bold"))
        txtNoOfDays.grid(row = 7, column= 1)

        #Sub Total
        lblNoOfDays = Label(labelframeleft, text = "Sub Total: ",font = ("arial", 12, "bold"), padx = 2, pady=6 )
        lblNoOfDays.grid(row = 8, column=0, stick = W) 
        txtNoOfDays = ttk.Entry(labelframeleft, textvariable=self.var_actualtotal, width= 27, font = ("arial", 13, "bold"))
        txtNoOfDays.grid(row = 8, column= 1)

        #Total Cost
        lblIdNumber = Label(labelframeleft, text = "Total Cost: ",font = ("arial", 12, "bold"), padx = 2, pady=6 )
        lblIdNumber.grid(row = 9, column=0, stick = W) 
        txtIdNumber = ttk.Entry(labelframeleft, textvariable=self.var_total, width= 27, font = ("arial", 13, "bold"))
        txtIdNumber.grid(row = 9, column= 1)
        
        #===================================Bill Button===========================
        btnBill = Button(labelframeleft,  text = "Bill", font = ("arial", 12, "bold"), bg = "black", fg = "gold", width = 9)
        btnBill.grid(row = 10 , column = 0, padx = 1, sticky = W)

        #=============================================btns===========================
        btn_frame = Frame(labelframeleft, bd = 2, relief = RIDGE)
        btn_frame.place(x = 0, y = 400, width = 412, height = 39)

        btnAdd = Button(btn_frame,  text = "Add", font = ("arial", 12, "bold"), bg = "black", fg = "gold", width = 9)
        btnAdd.grid(row = 0 , column = 0, padx = 1)

        btnUpdate = Button(btn_frame, text = "Update", font = ("arial", 12, "bold"), bg = "black", fg = "gold", width = 9)
        btnUpdate.grid(row = 0 , column = 1, padx = 1)

        btnDelete = Button(btn_frame,   text = "Delete", font = ("arial", 12, "bold"), bg = "black", fg = "gold", width = 9)
        btnDelete.grid(row = 0 , column = 2, padx = 1)

        btnReset = Button(btn_frame,  text = "Reset", font = ("arial", 12, "bold"), bg = "black", fg = "gold", width = 9)
        btnReset.grid(row = 0 , column = 3, padx = 1)

        #================================= Rightside ===============================================
        img3 = Image.open(r"images/bed.jpg")
        img3 = img3.resize((550,300), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        lblimg = Label(self.root, image=self.photoimg3, bd= 0, relief=RIDGE)
        lblimg.place(x=750, y=55, width=550, height=300)

        #================================== label frame search system ===========================
        Table_Frame = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "View Details And Search System",font = ("arial", 12, "bold") ,padx = 2, )
        Table_Frame.place(x =435, y = 280, width = 870, height = 260)

        lblSearchBy = Label(Table_Frame, font = ("arial", 12, "bold"), text = "Search By", bg = "red", fg ="white")
        lblSearchBy.grid(row =0, column = 0, stick = W, padx = 2)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame, textvariable= self.search_var, font = ("arial", 12, "bold"), width = 25, state = "readonly")
        combo_Search["value"] = ("Contact", "Room")
        combo_Search.current(0)
        combo_Search.grid(row = 0, column=1, padx = 2)
        
        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable= self.txt_search, width= 27, font = ("arial", 13, "bold"))
        txtSearch.grid(row = 0, column= 2, padx = 2)

        btnSearch = Button(Table_Frame, text = "Search",  font = ("arial", 12, "bold"), bg = "black", fg = "gold", width = 10)
        btnSearch.grid(row = 0 , column = 3, padx = 1)

        btnShowAll = Button(Table_Frame, text = "Show All", font = ("arial", 12, "bold"), bg = "black", fg = "gold", width = 10)
        btnShowAll.grid(row = 0 , column = 4, padx = 1)

        # ====================Show data Table =========================
        details_table = Frame(Table_Frame, bd = 2, relief = RIDGE)
        details_table.place(x = 0, y = 50, width = 870, height = 180)

        scroll_x = ttk.Scrollbar(details_table, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient = VERTICAL)

        self.room_table = ttk.Treeview(details_table, columns=("contact", "checkinDate", "checkoutDate", "roomtype", "roomavailable", "meal", "noOfdays"),
                                                                        xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        scroll_x.pack(side = BOTTOM, fill = X) 
        scroll_y.pack(side = RIGHT, fill = Y) 

        scroll_x.config(command =  self.room_table.xview)
        scroll_y.config(command =  self.room_table.yview)

        self.room_table.heading("contact", text = "Contact")
        self.room_table.heading("checkinDate", text = "Check-in")
        self.room_table.heading("checkoutDate", text = "Check-out")
        self.room_table.heading("roomtype", text = "Room Type")
        self.room_table.heading("roomavailable", text = "Room No")
        self.room_table.heading("meal", text = "Meal")
        self.room_table.heading("noOfdays", text = "NoOfDays")
        

        self.room_table["show"] = "headings"
        # dieu chinh kich co cot
        self.room_table.column("contact", width=100)
        self.room_table.column("checkinDate", width=100)
        self.room_table.column("checkoutDate", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noOfdays", width=100)


        self.room_table.pack(fill = BOTH, expand = 1)

    def add_data(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
                messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost", username = "root", password = "belieber2004", database = "management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_ref.get(),
                                                                                                    self.var_cust_name.get(),
                                                                                                    self.var_mother.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_post.get(), 
                                                                                                    self.var_mobile.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_nationality.get(),
                                                                                                    self.var_id_proof.get(),
                                                                                                    self.var_id_number.get(),
                                                                                                    self.var_address.get()
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Some thing went wrong: {str(es)}",parent=self.root)

    # ============================== All data fetch ==========================================
    def Fetch_contact(self):
        if self.var_contact.get()== "":
            messagebox.showerror("Error", "Please enter Contact Number")
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="belieber2004",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error", "This number Not Found", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4, relief=RIDGE,padx=2) 
                showDataframe.place(x=450,y=55,width=300,height=180)
                
                lblName=Label(showDataframe, text="Name:", font=("arial", 12, "bold")) 
                lblName.place(x=0,y=0) 

                lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=0)

                #=========================== Gender ===============================
                conn=mysql.connector.connect(host="localhost", username="root", password="belieber2004",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe, text="Gender:", font=("arial", 12, "bold")) 
                lblGender.place(x=0,y=30) 

                lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=30)

                #=============================== Email ===============================
                conn=mysql.connector.connect(host="localhost", username="root", password="belieber2004",database="management")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe, text="Email:", font=("arial", 12, "bold")) 
                lblGender.place(x=0,y=60) 

                lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=60)

                #================================== Nationality ======================================
                conn=mysql.connector.connect(host="localhost", username="root", password="belieber2004",database="management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe, text="Nationality:", font=("arial", 12, "bold")) 
                lblGender.place(x=0,y=90) 

                lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=90)

                #================================= Address =========================================
                conn=mysql.connector.connect(host="localhost", username="root", password="belieber2004",database="management")
                my_cursor=conn.cursor()
                query=("select address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query, value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe, text="Address:", font=("arial", 12, "bold")) 
                lblGender.place(x=0,y=120) 

                lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=120)



        

if __name__ == "__main__":
    root = Tk()
    obj  = Roombooking(root)
    root.mainloop()