from tkinter import*
from tkinter import messagebox,ttk
import pymysql 
import time
import os
import tempfile

class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll sysytem")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title=Label(self.root,text="Employee Payroll System",font=("times new roman",30,"bold" ),bg="#262626",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        btn_emp=Button(self.root,text="All Employee's DATA",command=self.employee_frame,font=("times new roman",13),bg="red",fg="black").place(x=1100,y=10,height=30)
        #===========frame1=======================================
        #===============Variables================
        self.var_ID=StringVar()
        self.var_designation=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_hired=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_experience=StringVar()
        self.var_proof_id=StringVar()
        self.var_contact=StringVar()
        self.var_status=StringVar()
        
       


        Frame1=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=70,width=785,height=620)
        title2=Label(Frame1,text="Employee Details",font=("times new roman",20),bg="lightgray",fg="black",anchor="w",padx=10)
        title2.place(x=0,y=0,relwidth=1)

        lbl_code=Label(Frame1,text="Employee ID",font=("times new roman",20),bg="white",fg="black",)
        lbl_code.place(x=10,y=70)
        self.txt_code=Entry(Frame1,font=("times new roman",15),textvariable=self.var_ID,bg="lightyellow",fg="black",)
        self.txt_code.place(x=170,y=74,width=200)
        btn_search=Button(Frame1,text="Search",command=self.search,font=("times new roman",20),bg="lightpink",fg="black",)
        btn_search.place(x=520,y=72,height=30)
       
       #======Row1
        lbl_designation=Label(Frame1,text="Designation",font=("times new roman",20),bg="white",fg="black",)
        lbl_designation.place(x=10,y=120)
        txt_designation=Entry(Frame1,font=("times new roman",15),textvariable=self.var_designation,bg="lightyellow",fg="black",)
        txt_designation.place(x=170,y=125,width=200)
        lbl_dob=Label(Frame1,text="D.O.B",font=("times new roman",20),bg="white",fg="black",)
        lbl_dob.place(x=390,y=120)
        txt_dob=Entry(Frame1,font=("times new roman",15),textvariable=self.var_dob,bg="lightyellow",fg="black",)
        txt_dob.place(x=520,y=125)

       #======Row2
        lbl_Name=Label(Frame1,text="Name",font=("times new roman",20),bg="white",fg="black",)
        lbl_Name.place(x=10,y=170)
        txt_name=Entry(Frame1,font=("times new roman",15),textvariable=self.var_name,bg="lightyellow",fg="black",)
        txt_name.place(x=170,y=175,width=200)
        lbl_doj=Label(Frame1,text="D.O.J",font=("times new roman",20),bg="white",fg="black",)
        lbl_doj.place(x=390,y=170)
        txt_doj=Entry(Frame1,font=("times new roman",15),textvariable=self.var_doj,bg="lightyellow",fg="black",)
        txt_doj.place(x=520,y=175)

       #======Row3
        lbl_age=Label(Frame1,text="Age",font=("times new roman",20),bg="white",fg="black",)
        lbl_age.place(x=10,y=220)
        txt_age=Entry(Frame1,font=("times new roman",15),textvariable=self.var_age,bg="lightyellow",fg="black",)
        txt_age.place(x=170,y=225,width=200)
        lbl_experience=Label(Frame1,text="Experience",font=("times new roman",20),bg="white",fg="black",)
        lbl_experience.place(x=390,y=220)
        txt_experience=Entry(Frame1,font=("times new roman",15),textvariable=self.var_experience,bg="lightyellow",fg="black",)
        txt_experience.place(x=520,y=225)

       #======Row4
        lbl_gender=Label(Frame1,text="Gender",font=("times new roman",20),bg="white",fg="black",)
        lbl_gender.place(x=10,y=270)
        txt_gender=Entry(Frame1,font=("times new roman",15),textvariable=self.var_gender,bg="lightyellow",fg="black",)
        txt_gender.place(x=170,y=275,width=200)
        lbl_proof=Label(Frame1,text="Proof ID",font=("times new roman",20),bg="white",fg="black",)
        lbl_proof.place(x=390,y=270)
        txt_proof=Entry(Frame1,font=("times new roman",15),textvariable=self.var_proof_id,bg="lightyellow",fg="black",)
        txt_proof.place(x=520,y=275)

       #======Row5
        lbl_email=Label(Frame1,text="Email",font=("times new roman",20),bg="white",fg="black",)
        lbl_email.place(x=10,y=320)
        txt_email=Entry(Frame1,font=("times new roman",15),textvariable=self.var_email,bg="lightyellow",fg="black",)
        txt_email.place(x=170,y=325,width=200)
        lbl_contact=Label(Frame1,text="Contact",font=("times new roman",20),bg="white",fg="black",)
        lbl_contact.place(x=390,y=320)
        txt_contact=Entry(Frame1,font=("times new roman",15),textvariable=self.var_contact,bg="lightyellow",fg="black",)
        txt_contact.place(x=520,y=325)

       
       #======Row6
        lbl_hired=Label(Frame1,text="Hired Location",font=("times new roman",18),bg="white",fg="black",)
        lbl_hired.place(x=10,y=372)
        txt_hired=Entry(Frame1,font=("times new roman",15),textvariable=self.var_hired,bg="lightyellow",fg="black",)
        txt_hired.place(x=170,y=375,width=200)
        lbl_status=Label(Frame1,text="Status",font=("times new roman",20),bg="white",fg="black",)
        lbl_status.place(x=390,y=370)
        txt_status=Entry(Frame1,font=("times new roman",15),textvariable=self.var_status,bg="lightyellow",fg="black",)
        txt_status.place(x=520,y=375)

       #======Row7========
        lbl_address=Label(Frame1,text="Address",font=("times new roman",18),bg="white",fg="black",)
        lbl_address.place(x=10,y=422)
        self.txt_address=Text(Frame1,font=("times new roman",15),bg="lightyellow",fg="black",)
        self.txt_address.place(x=170,y=425,width=550,height=150)



        #=========frame2======================================
       #===============Variables================
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_salary=StringVar()
        self.var_t_days=StringVar()
        self.var_absent=StringVar()
        self.var_medical=StringVar()
        self.var_pf=StringVar()
        self.var_convence=StringVar()
        self.var_net_salary=StringVar()
       
       
       
        Frame2=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame2.place(x=800,y=70,width=700,height=300)
        
        title3=Label(Frame2,text="salary calculation",font=("times new roman",20 ),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        
        lb1_month=Label(Frame2,text="Month:",font=("times new roman",18 ),bg="white",fg="black").place(x=10,y=60)
        txt_month=Entry(Frame2,font=("times new roman",15),textvariable=self.var_month,bg="lightyellow",fg="black").place(x=120,y=62,width=100)
        

        lb1_year=Label(Frame2,text="Year:",font=("times new roman",18 ),bg="white",fg="black").place(x=240,y=60)
        txt_year=Entry(Frame2,font=("times new roman",15),textvariable=self.var_year,bg="lightyellow",fg="black").place(x=310,y=60,width=100)

        lb1_salary=Label(Frame2,text="Basic Salary:",font=("times new roman",18 ),bg="white",fg="black").place(x=420,y=60)
        txt_salary=Entry(Frame2,font=("times new roman",15),textvariable=self.var_salary,bg="lightyellow",fg="black").place(x=560,y=60,width=100)

        lb1_days=Label(Frame2,text="Total days:",font=("times new roman",18 ),bg="white",fg="black").place(x=10,y=120)
        txt_days=Entry(Frame2,font=("times new roman",15),textvariable=self.var_t_days,bg="lightyellow",fg="black").place(x=170,y=125,width=100  )

        lb1_absent=Label(Frame2,text="Absent:",font=("times new roman",18 ),bg="white",fg="black").place(x=390,y=120)
        txt_absent=Entry(Frame2,font=("times new roman",15),textvariable=self.var_absent,bg="lightyellow",fg="black").place(x=510,y=125,width=100)

        lb1_medical=Label(Frame2,text="Medical:",font=("times new roman",18 ),bg="white",fg="black").place(x=10,y=150)
        txt_medical=Entry(Frame2,font=("times new roman",15),textvariable=self.var_medical,bg="lightyellow",fg="black").place(x=170,y=155,width=100  )

        lb1_pf=Label(Frame2,text="Pf:",font=("times new roman",18 ),bg="white",fg="black").place(x=400,y=150)
        txt_pf=Entry(Frame2,font=("times new roman",15),textvariable=self.var_pf,bg="lightyellow",fg="black").place(x=510,y=155,width=100)

        lb1_convence=Label(Frame2,text="Convence:",font=("times new roman",18 ),bg="white",fg="black").place(x=10,y=180)
        txt_convence=Entry(Frame2,font=("times new roman",15),textvariable=self.var_convence,bg="lightyellow",fg="black").place(x=170,y=185,width=100  )

        lb1_netsalary=Label(Frame2,text="NetSalary:",font=("times new roman",18 ),bg="white",fg="black").place(x=400,y=180)
        txt_netsalary=Entry(Frame2,font=("times new roman",15),textvariable=self.var_net_salary,bg="lightgray",fg="black").place(x=510,y=185,width=100)

        btn_calculator=Button(Frame2,text="Calculator",command=self.calculator,font=("times new roman",20),bg="orange",fg="black").place(x=100,y=220,height=30,width=120)
        self.btn_save=Button(Frame2,text="Save",command=self.add,font=("times new roman",20),bg="green",fg="white")
        self.btn_save.place(x=250,y=220,height=30,width=120)
        btn_clear=Button(Frame2,text="Clear",command=self.clear,font=("times new roman",20),bg="gray",fg="black").place(x=410,y=220,height=30,width=120)
        
        self.btn_update=Button(Frame2,text="Update",state=DISABLED,command=self.update,font=("times new roman",20),bg="blue",fg="white")
        self.btn_update.place(x=150,y=260,height=30,width=180)
        self.btn_delete=Button(Frame2,text="Delete",state=DISABLED,command=self.delete,font=("times new roman",20),bg="red",fg="black")
        self.btn_delete.place(x=340,y=260,height=30,width=180)


        #=====================frame3==========================
        Frame3=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame3.place(x=800,y=380,width=580,height=310)
     
        sal_Frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        sal_Frame.place(x=10,y=4,width=550,height=280)

        title3=Label(sal_Frame,text="Salary Reciept",font=("times new roman",20 ),bg="lightgray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
      
        sal_Frame2=Frame(sal_Frame,bg="white",bd=2,relief=RIDGE)
        sal_Frame2.place(x=0,y=30,relwidth=1,height=210)  
        self.sample=f'''\t\tCompany Name, XYZ\n\t\tAddress:Xyz,Floor4
-------------------------------------------------------------------------
            Employee ID\t\t : 
            Salary Of\t\t   : Mon-YYYY
            Generated On\t\t: DD-MM-YYYY

--------------------------------------------------------------------------
            Total Days\t\t   : DD
            Total present\t\t: DD
            Total Absent\t\t : DD
            Convence\t\t     : Rs.----
            Medical\t\t      : Rs.----
            PF\t\t           : Rs.----
            Gross Payment\t\t: RS.--------
            Net Salary\t\t   :Rs.--------

-------------------------------------------------------------------------
            This is computer generated slip,not
            required any signature
            '''
        

        Scroll_y=Scrollbar(sal_Frame2,orient=VERTICAL)
        Scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_receipt=Text(sal_Frame2,font=("times new roman",15),bg='lightyellow',yscrollcommand=Scroll_y.set)
        self.txt_salary_receipt.pack(fill=BOTH,expand=1)
        Scroll_y.config(command=self.txt_salary_receipt.yview)
        self.txt_salary_receipt.insert(END,self.sample)
        btn_print=Button(sal_Frame,text="Print",command=self.print,font=("times new roman",20),bg="lightblue",fg="black").place(x=200,y=245,height=30,width=120)

        self.add()
        self.check_connection() 


#=======================================================================================================================================================
    def search(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary where e_id=%s",(self.var_ID.get()))
            row=cur.fetchone()
            #print(rows)
            if row==None:
                messagebox.showerror("error","Invalid ID Try another ID",parent=self.root)
            else:
                 #print(row)
                 self.var_ID.set(row[0])
                 self.var_designation.set(row[1])
                 self.var_name.set(row[2])
                 self.var_age.set(row[3])
                 self.var_gender.set(row[4])
                 self.var_email.set(row[5])
                 self.var_hired.set(row[6])
                 self.var_dob.set(row[7])
                 self.var_doj.set(row[8])
                 self.var_experience.set(row[9]) 
                 self.var_proof_id.set(row[10])
                 self.var_contact.set(row[11])
                 self.var_status.set(row[12])
                 self.txt_address.delete('1.0',END)
                 self.txt_address.insert(END,row[13])
                 
                 

                 self.var_month.set(row[14])
                 self.var_year.set(row[15])
                 self.var_salary.set(row[16])
                 self.var_t_days.set(row[17])
                 self.var_absent.set(row[18])
                 self.var_medical.set(row[19])
                 self.var_pf.set(row[20])
                 self.var_convence.set(row[21])
                 self.var_net_salary.set(row[22])

                 file_=open('Salary_receipt/' + str(row[23]),'r')
                 self.txt_salary_receipt.delete('1.0',END)
                 for i in file_:
                     self.txt_salary_receipt.insert(END,i)
                 file_.close()
                 self.btn_save.config(state=DISABLED)
                 self.btn_update.config(state=NORMAL)
                 self.btn_delete.config(state=NORMAL) 
                 self.txt_code.config(state="readonly")


        except Exception as ex:
                messagebox.showerror("'error",f'error due to:{str(ex)}')            
    
    def clear(self):
            self.btn_save.config(state=NORMAL)
            self.btn_update.config(state=DISABLED)
            self.btn_delete.config(state=DISABLED)
            self.txt_code.config(state=NORMAL)

            self.var_ID.set('')
            self.var_designation.set('')
            self.var_name.set('')
            self.var_age.set('')
            self.var_gender.set('')
            self.var_email.set('')
            self.var_hired.set('')
            self.var_dob.set('')
            self.var_doj.set('')
            self.var_experience.set('')
            self.var_proof_id.set('')
            self.var_contact.set('')
            self.var_status.set('')
            self.txt_address.delete('1.0',END)
            

            self.var_month.set('')
            self.var_year.set('')
            self.var_salary.set('')
            self.var_t_days.set('')
            self.var_absent.set('')
            self.var_medical.set('')
            self.var_pf.set('')
            self.var_convence.set('')
            self.var_net_salary.set('')
            self.txt_salary_receipt.delete('1.0',END)
            self.txt_salary_receipt.insert(END,self.sample)


    def delete(self):
        if self.var_ID.get()=='':
            messagebox.showerror("Error","Employee Id must be required")
        else:    

            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_ID.get()))
                row=cur.fetchone()
                #print(rows)
                if row==True:
                    messagebox.showerror("error","Invalid ID Try another ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?")
                    if op==True: 
                        cur.execute("delete from emp_salary where e_id=%s",(self.var_ID.get())) 
                        con.commit()
                        con.close()  
                        messagebox.showinfo("Delete","Employee Record Deleted Successfully",parent=self.root)
                        self.clear()
            except Exception as ex:
                    messagebox.showerror("'error",f'error due to:{str(ex)}')            
        
        
    def add(self):
         #===============frame1 Variables================
        if self.var_ID.get() == '' or self.var_net_salary.get() == '' or self.var_name.get() == '' :
            messagebox.showerror("Error","Fill all Details are required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_ID.get()))
                row=cur.fetchone()
                #print(rows)
                if row!=None:
                    messagebox.showerror("error","ID has already available in our record,try another ID",parent=self.root)
                else:
                    cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                    
                    self.var_ID.get(),
                    self.var_designation.get(),
                    self.var_name.get(),
                    self.var_age.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_hired.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_experience.get(),
                    self.var_proof_id.get(),
                    self.var_contact.get(),
                    self.var_status.get(),
                    self.txt_address.get('1.0',END),

                    self.var_month.get(),
                    self.var_year.get(),
                    self.var_salary.get(),
                    self.var_t_days.get(),
                    self.var_absent.get(),
                    self.var_medical.get(),
                    self.var_pf.get(),
                    self.var_convence.get(),
                    self.var_net_salary.get(),
                    self.var_ID.get()+".txt"
                    #101.txt
                    )
                    )
                    
                    con.commit()
                    con.close()
                    file_=open('Salary_receipt/' + str(self.var_ID.get()+".txt"),'w')
                    file_.write(self.txt_salary_receipt.get('1.0',END)) 
                    file_.close()         
                    messagebox.showinfo("Successs","Record  added successfully")
            except Exception as ex:
                messagebox.showerror("'error",f'error due to:{str(ex)}')



    def update(self):
         #===============frame1 Variables================
        if self.var_ID.get() == '' or self.var_net_salary.get() == '' or self.var_ID.get() == '' :
            messagebox.showerror("Error","Fill all Details are required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",(self.var_ID.get()))
                row=cur.fetchone()
                #print(rows)
                if row==None:
                    messagebox.showerror("error","Employee ID is Invalid,try again with valid Employe ID",parent=self.root)
                else:
                    cur.execute("UPDATE `emp_salary` SET `designation`=%s,`name`=%s,`var_age`=%s,`gender`=%s,`email`=%s,`hr_location`=%s,`doj`=%s,`dob`=%s,`experience`=%s,`proof_id`=%s,`contact`=%s,`status`=%s,`address`=%s,`month`=%s,`year`=%s,`basic_salary`=%s,`t_days`=%s,`absent_days`=%s,`medical`=%s,`pf`=%s,`convence`=%s,`net_salary`=%s,`salary_receipt`=%s WHERE `e_id`=%s",
                    (
                    
                    self.var_designation.get(),
                    self.var_name.get(),
                    self.var_age.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_hired.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_experience.get(),
                    self.var_proof_id.get(),
                    self.var_contact.get(),
                    self.var_status.get(),
                    self.txt_address.get('1.0',END),


                    self.var_month.get(),
                    self.var_year.get(),
                    self.var_salary.get(),
                    self.var_t_days.get(),
                    self.var_absent.get(),
                    self.var_medical.get(),
                    self.var_pf.get(),
                    self.var_convence.get(),
                    self.var_net_salary.get(),
                    self.var_ID.get()+".txt",
                    self.var_ID.get()
                    #101.txt
                    )
                    )
                    con.commit()
                    con.close()
                    file_=open('Salary_receipt/' + str(self.var_ID.get()+".txt"),'w')
                    file_.write(self.txt_salary_receipt.get('1.0',END)) 
                    file_.close()         
                    messagebox.showinfo("Successs","Record  Updated successfully")
            except Exception as ex:
                messagebox.showerror("'error",f'error due to:{str(ex)}')
            
      #===============frame2 Variables================
    def calculator(self):
        if self.var_month.get()=='' or self.var_year.get()=='' or self.var_absent.get()=='':
            messagebox.showerror('Error','All Fields are required')

        else:
            # self.var_net_salary.set("result")
            # 35000/31==1752
            # 31-10=21*1752
            per_day=int(self.var_salary.get())/int(self.var_t_days.get())
            work_day=int(self.var_t_days.get())-int(self.var_absent.get())
            sal_=per_day*work_day
            deduct=int(self.var_medical.get())+int(self.var_pf.get())
            addtion=int(self.var_convence.get())
            net_sal=sal_ - deduct+addtion
            self.var_net_salary.set(str(round(net_sal,2)))
           #===================UPDATE the receipt====================================
            
            new_sample=f'''\t\tCompany Name, XYZ\n\t\tAddress:Xyz,Floor4
-------------------------------------------------------------------------
            Employee ID\t\t: {self.var_ID.get()}
            Salary Of\t\t: {self.var_month.get()}-{self.var_year.get()}
            Generated On\t\t: {str(time.strftime("%d-%m-%Y"))}

--------------------------------------------------------------------------
            Total Days\t\t: {self.var_t_days.get()}
            Total present\t\t: {str(int(self.var_t_days.get())-int(self.var_absent.get()))}
            Total Absent\t\t:  {self.var_absent.get()}
            Convence\t\t: Rs.{self.var_convence.get()}
            Medical\t\t: Rs.{self.var_medical.get()}
            PF\t\t: Rs.{self.var_pf.get()}
            Gross Payment\t\t: RS.{self.var_salary.get()}
            Net Salary\t\t Rs.{self.var_net_salary.get()}

-------------------------------------------------------------------------
            This is computer generated slip,not
            required any signature
            '''
            self.txt_salary_receipt.delete('1.0',END)
            self.txt_salary_receipt.insert(END,new_sample)

    def check_connection(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            #print(rows)
        except Exception as ex:
            messagebox.showerror("'error",f'error due to:{str(ex)}')


    def show(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            #print(rows)
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert('',END,values=row)
            con.close()    
        except Exception as ex:
            messagebox.showerror("'error",f'error due to:{str(ex)}')



    def employee_frame(self):
        self.root2=Toplevel(self.root)
        self.root2.title("Employee Payroll sysytem")
        self.root2.geometry("1000x500+120+100")
        self.root2.config(bg="white")
        title=Label(self.root2,text="All Employee Details",font=("times new roman",30,"bold" ),bg="#262626",fg="white",anchor="w",padx=10).pack(side=TOP,fill=X)
        self.root2.focus_force()
        
        scrolly=Scrollbar(self.root2,orient=VERTICAL)
        scrollX=Scrollbar(self.root2,orient=HORIZONTAL)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollX.pack(side=BOTTOM,fill=X)
         


        self.employee_tree=ttk.Treeview(self.root2,columns=('e_id', 'designation', 'name', 'var_age', 'gender', 'email', 'hr_location', 'doj', 'dob', 'experience', 'proof_id', 'contact', 'status', 'address', 'month', 'year', 'basic_salary', 't_days', 'absent_days', 'medical', 'pf', 'convence', 'net_salary', 'salary_receipt'),yscrollcommand=scrolly.set,xscrollcommand=scrollX.set)
        self.employee_tree.heading('e_id',text='EID')
        self.employee_tree.heading('designation',text='Designation')
        self.employee_tree.heading('name',text='Name')
        self.employee_tree.heading('var_age',text='Age')
        self.employee_tree.heading('gender',text='Gender')
        self.employee_tree.heading('email',text='Email')
        self.employee_tree.heading('hr_location',text='HR LOC.')
        self.employee_tree.heading('doj',text='D.O.J')
        self.employee_tree.heading('dob',text='D.O.B')
        self.employee_tree.heading('experience',text='Experience')
        self.employee_tree.heading('proof_id',text='Proof_id')
        self.employee_tree.heading('contact',text='Contact')
        self.employee_tree.heading('status',text='Status')
        self.employee_tree.heading('address',text='Address')
        self.employee_tree.heading('month',text='Month')
        self.employee_tree.heading('year',text='Year')
        self.employee_tree.heading('basic_salary',text='Basic Salary')
        self.employee_tree.heading('t_days',text='Days')
        self.employee_tree.heading('absent_days',text='Absent')
        self.employee_tree.heading('medical',text='Medical')
        self.employee_tree.heading('pf',text='PF')
        self.employee_tree.heading('convence',text='Convence')
        self.employee_tree.heading('net_salary',text='Net Salary')
        self.employee_tree.heading('salary_receipt',text='Salary Receipt')

        self.employee_tree['show']='headings'

        self.employee_tree.column('e_id',width=100)
        self.employee_tree.column('designation',width=100)
        self.employee_tree.column('name',width=100)
        self.employee_tree.column('var_age',width=100)
        self.employee_tree.column('gender',width=100)
        self.employee_tree.column('email',width=100)
        self.employee_tree.column('hr_location',width=100)
        self.employee_tree.column('doj',width=100)
        self.employee_tree.column('dob',width=100)
        self.employee_tree.column('experience',width=100)
        self.employee_tree.column('proof_id',width=100)
        self.employee_tree.column('contact',width=100)
        self.employee_tree.column('status',width=100)
        self.employee_tree.column('address',width=500)
        self.employee_tree.column('month',width=100)
        self.employee_tree.column('year',width=100)
        self.employee_tree.column('basic_salary',width=100)
        self.employee_tree.column('t_days',width=100)
        self.employee_tree.column('absent_days',width=100)
        self.employee_tree.column('medical',width=100)
        self.employee_tree.column('pf',width=100)
        self.employee_tree.column('convence',width=100)
        self.employee_tree.column('net_salary',width=100)
        self.employee_tree.column('salary_receipt',width=200)
        scrollX.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1)
        self.show()
        self.root2.mainloop()



    def print(self):
        file_=tempfile.mktemp(".txt")
        open(file_,'w').write(self.txt_salary_receipt.get('1.0',END))
        os.startfile(file_,'print')    

        

root=Tk()
obj=EmployeeSystem(root) 
root.mainloop()        
