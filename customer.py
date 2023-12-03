from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer")
        self.root.geometry("1320x580+230+220")
        # ==============================variables ===============================
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()

        # =================================title ===================================
        lbl_title = Label(self.root, text ="ADD CUSTOMER DETAILS", font = ("arial", 18, "bold"), bg ="black", fg = "gold", bd = 4, relief = RIDGE)
        lbl_title.place(x = 0, y=0, width = 1320, height = 50)

        # ================================logo ====================================
        img2 = Image.open(r"images/logohotel.png")
        img2 = img2.resize((100,40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        lblimg = Label(self.root, image=self.photoimg2, bd= 0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)


        # =====================================labelFrame ============================
        labelframeleft = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "Customer Details",font = ("arial", 12, "bold") ,padx = 2, ) # Khoang cach giua text  bd
        labelframeleft.place(x =5, y = 50, width = 425, height = 490)

        #================================== labels and entrys =================================
        # custRef
        lbl_cust_ref = Label(labelframeleft, text = "Customer Reference",font = ("arial", 12, "bold"), padx = 2, pady=6 )
        lbl_cust_ref.grid(row = 0, column=0, stick = W)
        entry_ref = ttk.Entry(labelframeleft,textvariable= self.var_ref, width= 27, font = ("arial", 13, "bold"), state = "readonly") #không cho sửa
        entry_ref.grid(row = 0, column= 1)

        # custName
        cname = Label(labelframeleft, text = "Customer Name: ",font = ("arial", 12, "bold"), padx = 2, pady=6 )
        cname.grid(row = 1, column=0, stick = W) 
        txtcname = ttk.Entry(labelframeleft,textvariable = self.var_cust_name, width= 27, font = ("arial", 13, "bold"))
        txtcname.grid(row = 1, column= 1)

        # motherName
        lblmname = Label(labelframeleft, text = "Mother Name",font = ("arial", 12, "bold"), padx = 2, pady=6 )
        lblmname.grid(row = 2, column=0, stick = W)
        txtmname= ttk.Entry(labelframeleft,textvariable = self.var_mother, width= 27, font = ("arial", 13, "bold"))
        txtmname.grid(row = 2, column= 1)

        # Gender Combobox
        label_gender = Label(labelframeleft, text = "Gender",font = ("arial", 12, "bold"), padx = 2, pady=6 )
        label_gender.grid(row = 3, column=0, stick = W)

        combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_gender, font = ("arial", 12, "bold"), width = 25, state = "readonly")
        combo_gender["value"] = ("Male", "Female", " Other")
        combo_gender.current(0)
        combo_gender.grid(row = 3, column=1)
 
        # postcode
        lbl_post_code = Label(labelframeleft, text = "PostCode:",font = ("arial", 12, "bold"), padx = 2, pady=6 )
        lbl_post_code.grid(row = 4, column=0, stick = W)
        txtPostCode = ttk.Entry(labelframeleft,textvariable = self.var_post, width= 27, font = ("arial", 13, "bold"))
        txtPostCode.grid(row = 4, column= 1)


        # mobile number
        lblMobile = Label(labelframeleft, text = "Mobile Number:",font = ("arial", 12, "bold"), padx = 2, pady=6 )
        lblMobile.grid(row = 5,column=0, stick = W)
        txtMobile = ttk.Entry(labelframeleft,textvariable = self.var_mobile, width= 27, font = ("arial", 13, "bold"))
        txtMobile.grid(row = 5, column= 1)


        # email
        lblEmail = Label(labelframeleft, text = "Email",font = ("arial", 12, "bold"), padx = 2, pady=6 )
        lblEmail.grid(row = 6, column=0, stick = W)
        txtEmail = ttk.Entry(labelframeleft,textvariable = self.var_email, width= 27, font = ("arial", 13, "bold"))
        txtEmail.grid(row = 6, column= 1)


        # nationality
        lbl_Nationality = Label(labelframeleft, text = "Nationality: ",font = ("arial", 12, "bold"), padx = 2, pady=6 )
        lbl_Nationality.grid(row = 7, column=0, stick = W)

        combo_Nationality = ttk.Combobox(labelframeleft,textvariable= self.var_nationality, font = ("arial", 12, "bold"), width = 25, state = "readonly")
        combo_Nationality["value"] = ("Indian", "American", "British", "Vietnamese", "American", "Vietnamese")
        combo_Nationality.current(0)
        combo_Nationality.grid(row = 7, column=1)
        
        
        #idproof type combobox
        lbl_IdProof = Label(labelframeleft, text = "Id Proof Type: ",font = ("arial", 12, "bold"), padx = 2, pady=6 )
        lbl_IdProof.grid(row = 8, column=0, stick = W)

        combo_id = ttk.Combobox(labelframeleft,textvariable= self.var_id_proof, font = ("arial", 12, "bold"), width = 25, state = "readonly")
        combo_id["value"] = ("AdharCard", "DrivingLicense", "PassPort")
        combo_id.current(0)
        combo_id.grid(row = 8, column=1)

        # id number
        lblIdNumber = Label(labelframeleft, text = "Id Number: ",  font = ("arial", 12, "bold"), padx = 2, pady=6 )
        lblIdNumber.grid(row = 9, column=0, stick = W)
        txtIdNumber = ttk.Entry(labelframeleft,textvariable = self.var_id_number, width= 27, font = ("arial", 13, "bold"))
        txtIdNumber.grid(row = 9, column= 1)

        # address
        lblAddress = Label(labelframeleft, text = "Adress:",font = ("arial", 12, "bold"), padx = 2, pady=6 )
        lblAddress.grid(row = 10, column=0, stick = W)
        txtAddress = ttk.Entry(labelframeleft,textvariable = self.var_address, width= 27, font = ("arial", 13, "bold"))
        txtAddress.grid(row = 10, column= 1)

        #=======================================btns ====================================
        btn_frame = Frame(labelframeleft, bd = 2, relief = RIDGE)
        btn_frame.place(x = 0, y = 400, width = 412, height = 39)

        btnAdd = Button(btn_frame, command = self.add_data, text = "Add", font = ("arial", 12, "bold"), bg = "black", fg = "gold", width = 9)
        btnAdd.grid(row = 0 , column = 0, padx = 1)

        btnUpdate = Button(btn_frame, command= self.update, text = "Update", font = ("arial", 12, "bold"), bg = "black", fg = "gold", width = 9)
        btnUpdate.grid(row = 0 , column = 1, padx = 1)

        btnDelete = Button(btn_frame, command = self.mDelete ,  text = "Delete", font = ("arial", 12, "bold"), bg = "black", fg = "gold", width = 9)
        btnDelete.grid(row = 0 , column = 2, padx = 1)

        btnReset = Button(btn_frame, command= self.reset, text = "Reset", font = ("arial", 12, "bold"), bg = "black", fg = "gold", width = 9)
        btnReset.grid(row = 0 , column = 3, padx = 1)

        #================================== label frame search system ===========================
        Table_Frame = LabelFrame(self.root, bd = 2, relief = RIDGE, text = "View Details And Search System",font = ("arial", 12, "bold") ,padx = 2, )
        Table_Frame.place(x =435, y = 50, width = 880, height = 490)

        lblSearchBy = Label(Table_Frame, font = ("arial", 12, "bold"), text = "Search By", bg = "red", fg ="white")
        lblSearchBy.grid(row =0, column = 0, stick = W, padx = 2)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame, textvariable= self.search_var, font = ("arial", 12, "bold"), width = 25, state = "readonly")
        combo_Search["value"] = ("Mobile", "Customer Reference")
        combo_Search.current(0)
        combo_Search.grid(row = 0, column=1, padx = 2)
        
        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable= self.txt_search, width= 27, font = ("arial", 13, "bold"))
        txtSearch.grid(row = 0, column= 2, padx = 2)

        btnSearch = Button(Table_Frame, text = "Search", command=self.search, font = ("arial", 12, "bold"), bg = "black", fg = "gold", width = 10)
        btnSearch.grid(row = 0 , column = 3, padx = 1)

        btnShowAll = Button(Table_Frame, text = "Show All", command= self.fetch_data, font = ("arial", 12, "bold"), bg = "black", fg = "gold", width = 10)
        btnShowAll.grid(row = 0 , column = 4, padx = 1) 

        # ====================Show data Table =========================
        details_table = Frame(Table_Frame, bd = 2, relief = RIDGE)
        details_table.place(x = 0, y = 50, width = 860, height = 350)

        scroll_x = ttk.Scrollbar(details_table, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient = VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, columns=("ref", "name", "mother", "gender", "post", "mobile", "email", 
                                                                       "nationality", "idproof", "idnumber", "address"),
                                                                        xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        scroll_x.pack(side = BOTTOM, fill = X) 
        scroll_y.pack(side = RIGHT, fill = Y) 

        scroll_x.config(command =  self.Cust_Details_Table.xview)
        scroll_y.config(command =  self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref", text = "Refer No")
        self.Cust_Details_Table.heading("name", text = "Name")
        self.Cust_Details_Table.heading("mother", text = "Mother Name")
        self.Cust_Details_Table.heading("gender", text = "Gender")
        self.Cust_Details_Table.heading("post", text = "PostCode")
        self.Cust_Details_Table.heading("mobile", text = "Mobile")
        self.Cust_Details_Table.heading("email", text = "Email")
        self.Cust_Details_Table.heading("nationality", text = "Nationality")
        self.Cust_Details_Table.heading("idproof", text = "Id Proof")
        self.Cust_Details_Table.heading("idnumber", text = "Id Number")
        self.Cust_Details_Table.heading("address", text = "Address")

        self.Cust_Details_Table["show"] = "headings"
        # dieu chinh kich co cot
        self.Cust_Details_Table.column("ref", width=100)
        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("mother", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("post", width=100)
        self.Cust_Details_Table.column("mobile", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("idproof", width=100)
        self.Cust_Details_Table.column("idnumber", width=100)
        self.Cust_Details_Table.column("address", width=100)

        self.Cust_Details_Table.pack(fill = BOTH, expand = 1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
                messagebox.showerror("Error", "All fields are required", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="belieber2004",
                database="management")
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

    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost", username = " root", password = "belieber2004", database = "management")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows: 
                self.Cust_Details_Table.insert("", END, values = i)
            conn.commit()
        conn.close()

    def get_cursor(self, event =""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]

        if row: 
            self.var_ref.set(row[0])
            self.var_cust_name.set(row[1])
            self.var_mother.set(row[2])
            self.var_gender.set(row[3])
            self.var_post.set(row[4])
            self.var_mobile.set(row[5])
            self.var_email.set(row[6])
            self.var_nationality.set(row[7])
            self.var_id_proof.set(row[8])
            self.var_id_number.set(row[9])
            self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent = self.root)
        else: 
            conn = mysql.connector.connect(host = "localhost", username = " root", password = "belieber2004", database = "management")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set  Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s, Email=%s,Nationality=%s,Idproof=%s, idnumber=%s, Address=%s where Ref=%s",(
                                                                                                    self.var_cust_name.get(),
                                                                                                    self.var_mother.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_post.get(), 
                                                                                                    self.var_mobile.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_nationality.get(),
                                                                                                    self.var_id_proof.get(),
                                                                                                    self.var_id_number.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_ref.get()
                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Customer details has been updated successfully", parent = self.root)
        



    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer", parent = self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host = "localhost", username = " root", password = "belieber2004", database = "management")
            my_cursor = conn.cursor()
            query = "Delete from customer where Ref=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
        else: 
            if not mDelete:
                return 
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set(""), 
  
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        # Hàm search 
    def search(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="belieber2004", database="management")
            my_cursor = conn.cursor()

            search_by = self.search_var.get()
            # Map the user-friendly search option to the actual database column name
            column_map = {
                "Customer Reference": "Ref",
                "Mobile": "Mobile"
            }
            db_column = column_map.get(search_by, "Ref")  # Default to "Ref" if not found

            search_value = self.txt_search.get()
            query = f"SELECT * FROM customer WHERE `{db_column}` LIKE %s"
            my_cursor.execute(query, ('%' + search_value + '%',))

            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for i in rows:
                    self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("SQL Error", f"An error occurred: {err}", parent=self.root)




    
    

            





if __name__ == "__main__":

    root = Tk()
    obj  = Cust_Win(root)
    root.mainloop()
