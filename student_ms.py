from tkinter import *
from tkinter import ttk

class StudentMs:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x600+0+0")
        title=Label(self.root,text="Student Management System",font=("Times new roman",18,"bold"),bg="green",fg="white")
        title.pack(side=TOP,fill=X)

        #StringVar() instance
        self.roll_no=StringVar()
        self.name=StringVar()
        self.emai=StringVar()
        self.gender=StringVar()
        self.contact=StringVar()
        self.dob=StringVar()
        


        #First Frame in Main Window
        manage_frame=Frame(self.root,bg="plum1",bd=2,relief=RIDGE)
        manage_frame.place(x=20,y=80,width=400,height=580)

        #Widgets in manage_frame
        manage_title=Label(manage_frame,text="Manage Students",bg="plum1",font=("times ",18,"bold"))
        manage_title.grid(row=0,column=1,columnspan=4,pady=20)
        roll_no_label=Label(manage_frame,text="Roll_No:",bg="plum1",fg="red",font=("times ",14,"bold"))
        roll_no_label.grid(row=1,column=0,columnspan=2,pady=10,sticky="W")
        roll_no_txt=Entry(manage_frame,font=("times",18))
        roll_no_txt.grid(row=1,column=2,columnspan=2,pady=10,sticky="W")
        name_label=Label(manage_frame,text="Name:",bg="plum1",fg="red",font=("Times new roman",14,"bold"))
        name_label.grid(row=2,column=0,columnspan=2,pady=10,sticky=W)
        name_txt=Entry(manage_frame,font=("times",18))
        name_txt.grid(row=2,column=2,columnspan=2,pady=10,sticky="W")
        email_label=Label(manage_frame,text="Email:",bg="plum1",fg="red",font=("times ",14,"bold"))
        email_label.grid(row=3,column=0,columnspan=2,pady=10,sticky=W)
        email_txt=Entry(manage_frame,font=("times",18))
        email_txt.grid(row=3,column=2,columnspan=2,pady=10,sticky="W")
        gender_label=Label(manage_frame,text="Gender:",bg="plum1",fg="red",font=("times ",14,"bold"))
        gender_label.grid(row=4,column=0,columnspan=2,pady=10,sticky=W)
        combo_gender=ttk.Combobox(manage_frame,font=("times",18),state='readonly')
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=2,columnspan=2,pady=10,sticky="W")
        contact_no_label=Label(manage_frame,text="Contact No:",bg="plum1",fg="red",font=("times ",14,"bold"))
        contact_no_label.grid(row=5,column=0,columnspan=2,pady=10,sticky=W)
        contact_no_txt=Entry(manage_frame,font=("times",18))
        contact_no_txt.grid(row=5,column=2,columnspan=2,pady=10,sticky="W")
        dob_label=Label(manage_frame,text="D.O.B:",bg="plum1",fg="red",font=("times ",14,"bold"))
        dob_label.grid(row=6,column=0,columnspan=2,pady=10,sticky=W)
        dob_txt=Entry(manage_frame,font=("times",18))
        dob_txt.grid(row=6,column=2,columnspan=2,pady=10,sticky="W")
        address_label=Label(manage_frame,text="Address:",bg="plum1",fg="red",font=("times ",14,"bold"))
        address_label.grid(row=7,column=0,columnspan=2,pady=10,sticky=W)
        self.address_txt=Text(manage_frame,width=24,height=4,font=("",14))
        self.address_txt.grid(row=7,column=2,columnspan=2,pady=10,sticky="W")

        #Button Frame
        btn_frame=Frame(manage_frame,bg="plum1")
        btn_frame.place(x=10,y=500,width=380,height=60)

        #Buttons
        add_btn=Button(btn_frame,text="Add",bg="plum1",activeforeground="red",font=("times ",16,"bold"))
        add_btn.grid(row=0,column=0,pady=10,padx=4)
        update_btn=Button(btn_frame,text="Update",bg="plum1",activeforeground="red",font=("times ",16,"bold"))
        update_btn.grid(row=0,column=1,pady=10,padx=4)
        delete_btn=Button(btn_frame,text="Delete",bg="plum1",activeforeground="red",font=("times ",16,"bold"))
        delete_btn.grid(row=0,column=2,pady=10,padx=4)
        clear_btn=Button(btn_frame,text="Clear",bg="plum1",activeforeground="red",font=("times ",16,"bold"))
        clear_btn.grid(row=0,column=3,pady=10,padx=4)



        #Second Frame in Main Window
        detail_frame=Frame(self.root,bg="powder blue",bd=2,relief=RIDGE)
        detail_frame.place(x=470,y=80,width=820,height=580)

        #Widgets in detail_frame
        search_label=Label(detail_frame,text="Search By",bg="powder blue",activeforeground="red",font=("times ",18,"bold"))
        search_label.grid(row=0,column=0,pady=10,padx=2)
        combo_serach=ttk.Combobox(detail_frame,font=("times ",18,"bold"),state='readonly')
        combo_serach['values']=("roll_no","name","email","contact_no")
        combo_serach.grid(row=0,column=1,pady=10,padx=2)
        search_txt=Entry(detail_frame,font=("times ",18,"bold"))
        search_txt.grid(row=0,column=2,pady=10,padx=2)
        search_btn=Button(detail_frame,text="Search",bg="powder blue",activeforeground="red",font=("times ",14,"bold"))
        search_btn.grid(row=0,column=3,pady=10,padx=2)
        show_all_btn=Button(detail_frame,text="Show All",bg="powder blue",activeforeground="red",font=("times ",14,"bold"))
        show_all_btn.grid(row=0,column=4,pady=10,padx=2)

        #Table Frame
        table_frame=Frame(detail_frame,bg="white",bd=2,relief=RIDGE)
        table_frame.place(x=10,y=60,width=800,height=500)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("roll_no","name","email","gender","contact_no","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("roll_no",text="Roll_no")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("contact_no",text="Contact")
        self.student_table.heading("dob",text="D.O.B")
        self.student_table.heading("address",text="Address")

        self.student_table['show']='headings'

        self.student_table.column("roll_no",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("contact_no",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("address",width=150)

        self.student_table.pack(fill=BOTH,expand=1)



root=Tk()
obj=StudentMs(root)
root.mainloop()
