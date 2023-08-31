#python3.7
#Gui used in project is: Tkinter
#Database used in this project is: SQLite3

#this project is developed by -> Mohd Tahzeeb Khan


"""................................import all the requeired modules and libraries of python3.8.................................................."""
from email import message
import email
from email.policy import EmailPolicy
from os import cpu_count, terminal_size
import os
import time
from tkinter import ttk
import twilio
from twilio.rest import Client
import re
import datetime as dt
import random
from sqlite3.dbapi2 import Connection, Cursor, connect
from tkinter import Button, Canvas, Checkbutton, Frame, Image, IntVar, Menu, Message, OptionMenu, PhotoImage, Place, Radiobutton, StringVar, Tk, Toplevel, font, mainloop
from tkinter.ttk import Entry, Label, LabelFrame, Style, Treeview
import tkinter.messagebox
from tkinter.constants import ANCHOR, BOTH, BOTTOM, BROWSE, CENTER, COMMAND, END, HORIZONTAL, INSERT, LEFT, NW, RAISED, RIGHT, TOP, VERTICAL, W, X, Y
from functools import partial
from typing import Sized, Text
#from PIL import ImageTk, Image
import sqlite3
import tkinter as tk
import smtplib
from email.message import EmailMessage
"""......................................All the Requiered Modules & Librabiers are imported.........................................."""
vv=sqlite3.connect("Covidvaccine.db")



def call():
    ap.destroy()
    start()
    
#.......................................................available vaccine...................................................................

def Available_vaccine():
    co=sqlite3.connect('CovidVaccine.db')#connected to the database called: CovidVaccine.db
    co.execute('''CREATE TABLE IF NOT EXISTS Avaiable_vaccine
    (ID INT NOT NULL, 
    astrazenca INT NOT NULL,
    bharat INT NOT NULL,
    sputnik INT NOT NULL,
    sputnik2 INT NOT NULL,
    drdo INT NOT NULL);''')#creating new table if not present in the database called CovidVaccine.db

    #co.execute("INSERT INTO Avaiable_vaccine (ID, astrazenca, bharat, sputnik, sputnik2, drdo) VALUES(1,0,0,0,0,0)");
    #co.execute("INSERT INTO Avaiable_vaccine (ID, astrazenca, bharat, sputnik, sputnik2, drdo) VALUES(2,0,0,0,0,0)");
    #co.execute("INSERT INTO Avaiable_vaccine (ID, astrazenca, bharat, sputnik, sputnik2, drdo) VALUES(3,0,0,0,0,0)");
    #co.execute("INSERT INTO Avaiable_vaccine (ID, astrazenca, bharat, sputnik, sputnik2, drdo) VALUES(4,0,0,0,0,0)");
    #co.execute("INSERT INTO Avaiable_vaccine (ID, astrazenca, bharat, sputnik, sputnik2, drdo) VALUES(5,0,0,0,0,0)");
    bharatb=bhartakboi.get()#taking values to update
    astra=Astrazenca.get()#taking values to update
    sputI=sputnik.get()#taking values to update
    sputV=sputnikv.get()#taking values to update
    drddo=drdo.get()#taking values to update
    co.execute('''UPDATE Avaiable_vaccine  SET astrazenca=? WHERE ID=1''', (astra,))#updating existing value with the new values
    co.execute('''UPDATE Avaiable_vaccine  SET bharat=? WHERE ID=2''', (bharatb,))#updating existing value with the new values
    co.execute('''UPDATE Avaiable_vaccine  SET sputnik=? WHERE ID=3''', (sputI,))#updating existing value with the new values
    co.execute('''UPDATE Avaiable_vaccine  SET sputnik2=? WHERE ID=4''', (sputV,))#updating existing value with the new values
    co.execute('''UPDATE Avaiable_vaccine  SET drdo=? WHERE ID=5''', (drddo,))#updating existing value with the new values
    #print(bharatb, astra, sputI, sputV, drddo)
    co.commit()#Commiting the changes of CovidVaccine.db
    co.close()#closing the database.

def Available_Beds():#creating new function.
    c=sqlite3.connect('CovidVaccine.db')#connected to the database called: CovidVaccine.db
    c.execute('''CREATE TABLE IF NOT EXISTS Available_beds
    (ID INT NOT NULL PRIMARY KEY, 
    oxygenbed INT NOT NULL,
    vantilatorbed INT NOT NULL,
    normalbed INT NOT NULL);''')##creating new table if not present in the database called CovidVaccine.db
    oxygen_bed=b1.get()#taking values to update
    vantilator_bed=b2.get()#taking values to update
    normal_bed=b3.get()#taking values to update
    
   # c.execute("INSERT INTO Available_beds(ID, oxygenbed, vantilatorbed, normalbed) VALUES(3,0,0,0)");
    c.execute('''UPDATE Available_beds  SET oxygenbed=? WHERE ID=1''',(oxygen_bed,))#Updating existing values with new values
    c.execute("UPDATE Available_beds  SET vantilatorbed=? WHERE ID=2",(vantilator_bed,))#Updating existing values with new values
    c.execute("UPDATE Available_beds  SET normalbed=? WHERE ID=3", (normal_bed,))#Updating existing values with new values
    c.commit()#Commiting all the new changes
    c.close()#closing the database.
   ## print(oxygen_bed, vantilator_bed, normal_bed)#printing all the values to check whether the output is as per the expections.

def update():#function to update vaccine.
   global b1, b2, b3, bhartakboi, Astrazenca, sputnik, sputnikv, drdo#variables for storing value, this variables are declare as Global.
   ava=tkinter.Tk()#creating instance of tkinter
   ava.geometry("825x800")#configration of size of window.
   ava["bg"]= "NavajoWhite2"  #background color configration for window.
   ava.title("Life Care service, Update panel")#configure the title.
   
   oxybed=IntVar()  #declaring local variable to store values for bed.
   vantibed=IntVar()#declaring local variable to store values for bed.
   Norbed=IntVar()#declaring local variable to store values for bed.
   sputnik=IntVar(ava)    #declaring local variable to store values for vaccine
   sputnikv=IntVar(ava)#declaring local variable to store values for vaccine
   bhartakboi=IntVar(ava)#declaring local variable to store values for vaccine
   Astrazenca=IntVar(ava)#declaring local variable to store values for vaccine
   drdo=IntVar(ava)#declaring local variable to store values for vaccine
   
   
   top=Frame(ava, width=750, height= 150, bd= 8, relief="raise")#initializing the frame
   top.place(x=50,y=20)#position for frame
   tkinter.Label(top, text="LifeCare Hospital Service", font=('arial', 38, 'bold')).place(x=75,y=40)#creating labels.
   
   left=Frame(ava, width=350, height= 500, bd= 8, relief="raise")#initailizing frame
   left.place(x=50,y=200)#placing a position
   right=Frame(ava, width=380, height= 500, bd= 8, relief="raise")#initailizing frame
   right.place(x=410,y=200)#placing a position
   
   
   
   #Bed Update
   tkinter.Label(left, text="Beds Available", font=('arial', 20, 'bold')).place(x=70, y=20)#creating new labels
   tkinter.Label(left, text="Oxygen Bed", font=('arial', 15, 'bold')).place(x=20, y=80)#creating new labels
   b1=Entry(left, width=15, textvariable=oxybed)#new entry to input
   b1.place(x=170, y=84)#placing the entry
   tkinter.Label(left, text="Vantilator Bed", font=('arial', 15, 'bold')).place(x=20, y=160)#creating new labels
   b2=Entry(left, width=15, textvariable=vantibed)#new entry to input
   b2.place(x=170, y=164)#placing the entry
   tkinter.Label(left, text="Normal Bed", font=('arial', 15, 'bold')).place(x=20, y=240)#creating new labels
   b3=Entry(left, width=15, textvariable=Norbed)#new entry to input
   b3.place(x=170, y=244)#placing the entry
   
   #Vaccine Update
   tkinter.Label(right, text="Vaccine Available", font=('arial', 20, 'bold')).place(x=70, y=20)#creating new labels
   
   
   tkinter.Label(right, text="Covaxin", font=('arial', 15, 'bold')).place(x=20, y=80)#creating new labels
   Radiobutton(right, text="Available", variable=bhartakboi, value=1).place(x=180, y=80)     #creating radio button
   Radiobutton(right, text="Not-Available",  variable=bhartakboi, value=0).place(x=260, y=80)#creating radio button
   
   tkinter.Label(right, text="Covishield", font=('arial', 15, 'bold')).place(x=20, y=140)#creating new labels
   Radiobutton(right, text="Available", variable=Astrazenca, value=1).place(x=180, y=140)     #creating radio button
   Radiobutton(right, text="Not-Available",  variable=Astrazenca, value=0).place(x=260, y=140)#creating radio button
   
   tkinter.Label(right, text="Sputnik I", font=('arial', 15, 'bold')).place(x=20, y=200)#creating new labels
   Radiobutton(right, text="Available", variable=sputnik, value=1).place(x=180, y=200)     #creating radio button
   Radiobutton(right, text="Not-Available",  variable=sputnik, value=0).place(x=260, y=200)#creating radio button
   
   tkinter.Label(right, text="Sputnik V", font=('arial', 15, 'bold')).place(x=20, y=260)#creating new labels
   Radiobutton(right, text="Available", variable=sputnikv, value=1).place(x=180, y=260)     #creating radio button
   Radiobutton(right, text="Not-Available",  variable=sputnikv, value=0).place(x=260, y=260)#creating radio button
   
   tkinter.Label(right, text="DRDO-D2", font=('arial', 15, 'bold')).place(x=20, y=320)#creating new labels
   Radiobutton(right, text="Available", variable=drdo, value=1).place(x=180, y=320)     #creating radio button
   Radiobutton(right, text="Not-Available",  variable=drdo, value=0).place(x=260, y=320)#creating radio button
   
    
   
   
   
   exitava= tkinter.Button(left, text="Update", command=Available_Beds,height= 1, width= 15, font=1, bg='green', fg='White').place(x=75, y=425)     #creating button.
   exitava= tkinter.Button(right, text="Update",command=Available_vaccine , height= 1, width= 15, font=1, bg='green', fg='White').place(x=75, y=425)#creating button.
   exitava= tkinter.Button(ava, text="Exit", height= 1, width= 59, font=1, command=ava.destroy, bg='Red', fg='White').place(x=50, y=725)#creating button.
   
   ava.mainloop()#looping the tkinter window.
   
    

#....................................................login identification function..........................................................
def logincheck():#login check module
    e_1=user.get() #get the id and password from entry module.
    e_2=passw.get()#get the id and password from entry module.

    idn='tahzeeb'# id and password is hardcoded.
    pa='12345'# id and password is hardcoded.
 
    if(e_1=="") and (e_2==""):#condition if entry is emply.
        tkinter.messagebox.showinfo("Waring","Please Enter Details")#msz to be show when condition ids true.

    elif(e_1==idn and e_2==pa):#if condtion is true.
      
       adminpage()#this module will be run when condition is true.

    else:
        tkinter.messagebox.showinfo("Warning", "Incorrect ID/Password")#show the msz
        ad.destroy()#destroy..... 
#................................................................................................................................







#.........................................................admindashboard....................................................
def adminpage():#admin function
    global ap
    ad.destroy()
    #loginsms()
    con1 = sqlite3.connect('CovidVaccine.db')

    cur1 = con1.cursor()
    cur1.execute('''CREATE TABLE IF NOT EXISTS Registration
    (fullname TEXT NOT NULL, 
     gender TEXT NOT NULL, 
     age INT NOT NULL,
     mobileno INT NOT NULL,
     adharno INT NOT NULL,
     emailid TEXT NOT NULL,
     addres TEXT NOT NULL,
     vaccine TEXT NOT NULL,
     dose TEXT NOT NULL,
     date1 TEXT NOT NULL);''')
    cur1.execute("SELECT * FROM Registration");#Creating new table in the database called as CovidVaccine.db
    

    
    ap=tkinter.Tk()
    ap.geometry("1168x700")
    ap["bg"]='NavajoWhite2'

    ob=IntVar(ap)
    vb=IntVar()
    nco=IntVar()
    razc=IntVar(ap)
    rbbc=IntVar(ap)
    rsup=IntVar(ap)
    rdr=IntVar(ap)
    to= Frame(ap, width=1068, height= 105, bd= 8, relief="raise")
    to.place(x=50,y=25)
    data= Frame(ap, width=1068, height= 410, bd= 8, relief="sunken")
    data.place(x=50, y=200)
    
    labe= tkinter.Label(to, font=('arial', 36, 'bold'), text="LifeCare Hospitals, Vaccination Info").place(x=150, y=12)

    tree_scroll_x=ttk.Scrollbar(data, orient=tk.HORIZONTAL)
    tree_scroll_y=ttk.Scrollbar(data, orient=tk.VERTICAL)
    tree = ttk.Treeview(data, height=18, column=("Name","Gender","Age","Mobile","Adhar","Email","Address","Vaccine","Dose","Date"), xscrollcommand=tree_scroll_x.set, yscrollcommand=tree_scroll_y.set, selectmode='none')
    tree_scroll_x.config(command=tree.xview)
    tree_scroll_y.config(command=tree.yview)
    tree_scroll_x.place(x=200,y=400)
    tree_scroll_y.place(x=15, y=400)
    
    
    
    tree.column("#0", stretch=False, width=1)
    tree.heading("#0", text=".")
    
    tree.column("Name", stretch=False, width=130)
    tree.heading("Name", text="Name")


    tree.column("Gender", stretch=False, width=50)
    tree.heading("Gender", text="Gender")

    tree.column("Age", stretch=False, width=45)
    tree.heading("Age", text="Age")

    tree.column("Mobile", stretch=False, width=100)
    tree.heading("Mobile", text="Mobile No")

    tree.column("Adhar", stretch=False, width=100)
    tree.heading("Adhar", text="Aadhar No")

    tree.column("Email", stretch=False, width=150)
    tree.heading("Email", text="Email Address")

    tree.column("Address", stretch=False, width=120)
    tree.heading("Address", text="Address")

    tree.column("Vaccine", stretch=False, width=150)
    tree.heading("Vaccine", text="Vaccine")

    tree.column("Dose", stretch=False, width=100)
    tree.heading("Dose", text="Doses")
    
    tree.column("Date", stretch=False, width=100)
    tree.heading("Date", text="Vaccination Date")

    tree.place(x=5, y=5)
    



    
    dd = cur1.fetchall()    

    for row in dd:
        
        #print(row) 

        tree.insert("", tkinter.END, values=row)        
   
    con1.close()
    

    exit_buttonap=tkinter.Button(ap, text="Logout", width=50,height=2, bg='red', fg='white', command=call).place(x=50, y= 640)
    update_button=tkinter.Button(ap, text="Update", width=50, height=2 ,bg='blue', fg='white', command=update).place(x=750, y=640)

#............................................................................................................................
    







#................................................Popup msz code...........................................................   
def onclick(nameofp, dateocine):#creating new module with passing two parameter.
    reg.destroy()#destroy
    tkinter.messagebox.showinfo("Lifecare Hospitals" +nameofp, "Your vaccine is booked, please check you Email, & SMS box....\n vaccination date:" +dateocine)#showing the msz.....
    
#................................................................................................................................







#................................................login clear fieldcode...........................................................   
def reset():#reset function.
    user.delete(0, END)  #delete all the data of field.
    passw.delete(0, END)#delete all the data of field.
    return#returning the blank....
#................................................................................................................................




#.............................................admin login setup is here.................................................. 
def admin():
    global user, passw, ad
    m.destroy()
    ad=tkinter.Tk()
    ad.geometry("500x300")
    
   
    adm=StringVar()
    passwo=IntVar()
    tkinter.Label(ad, text="Admin's Login", font=("bold", 30)).place(x=170, y=15)
    tkinter.Label(ad, text="Username:", font=20 ).place(x=100, y=100)
    user=Entry(ad, textvariable=adm)
    user.place(x=250,y=100)
    tkinter.Label(ad, text="Password:", font=14).place(x=100, y=150)
    passw=Entry(ad, textvariable=passwo, show='*')
    passw.place(x=250,y=150)
    reset()
    sumit= tkinter.Button(ad, bg='blue', fg='White', text="Login",  width=15, command=logincheck).place(x=265,y=200)
    sumit= tkinter.Button(ad,bg='green', fg='black', text="Reset", width=15, command=reset).place(x=100,y=200)
    exitreg= tkinter.Button(ad, bg='red', fg='white', text="Exit this Page",width=39, height=2, command=ad.destroy).place(x=100,y=240)
    mainloop()
    
#............................................................................................................................
 









 #.............................................random vaccination date......................................................

def vaccinedate():
    global date, tu, year
    date=random.randrange(1,30)
    #print(date)
    month=random.randrange(7,12)
    #print(month)
    if(month==7):
        tu=('july')
    elif(month==8):
        tu=('august')
    elif(month==9):
        tu=('september')
    elif(month==10):
        tu=('october')
    elif(month==11):
        tu=('november')
    elif(month==12):
        tu=('december')
    year=2021

def loginsms():
    Clienmt=Client(" ", " " )#twillio token and key paste it
    my_no=97#Enter your Mobile No. Here
    my_twiliono=55#Enter your Twilio Mobile no here(you first have to register your self on twillio.com, for more info goto the youtube)
    messagesms=Clienmt.messages('\n Hello Admin \n You Logined IN ')
    Clienmt.messages.create(to=my_no, from_= my_twiliono, body=messagesms)
    return
    
    
#..............................................code for sending SMS to the user..............................................
def sendsms(mono1):
    Clienmt=Client("", "" )#twillio token and key paste it
    my_cell=97#Enter your Mobile No. Here
    my_twilio=55#Enter your Twilio Mobile no here(you first have to register your self on twillio.com, for more info goto the youtube)
    messagesms=Clienmt.messages('Hello User, \n This Project is developed by Mohd Tahzeeb Khan............\n Roll no. 32............Enrollment no:1800760291 \n Subject: Python Programming \n  Subject Teacher: Pallavi Maam \n Session: 2020-21 \n Thank you user to use this covid-19 vaccination software, and please vaccinate your self and be safe from SARcovid-19.......\n Have a nice data')#message to be send
    Clienmt.messages.create(to=my_cell, from_= my_twilio, body=messagesms)#creating and sending msz
    return#return.....
#.............................................................................................................................







#........................................code for sending email to the user..................................................
def emailsend(ema):
   
   
   
   email=" "#Enter your Email address here
   password=" "#Enter lyour Email password Here
   reciever=ema#initailzing the mail
   smtpobj= smtplib.SMTP_SSL('smtp.gmail.com', 465)#config the server and the port no of the mail provider
   smtpobj.login(email, password)#id and password of the mail id from which you want to send the mail
   textmsz="Hello User, \n This Project is developed by Mohd Tahzeeb Khan............\n Roll no. 32............Enrollment no:1800760291 \n Subject: Python Programming \n  Subject Teacher: Pallavi Maam \n Session: 2020-21 \n Thank you user to use this covid-19 vaccination software, and please vaccinate your self and be safe from SARcovid-19.......\n Have a nice day"#msz to be send
   subject="""Lifecare Vaccine registration"""#defining subject for the mail
   smtpobj.sendmail(email, reciever, textmsz, subject)#sending mail
   smtpobj.quit()#closing the mail's object
   return
#................................................................................................................................


#............................................................clear function.................................................
def cleardata():
    entry_1.delete(0, END)
    entry_6.delete(0, END)
    entry_7.delete(0, END)
    entry_4.delete(0, END)
    entry_5.delete(0, END)
    entry_3.delete(0, END)
    
    #print('All fields clear')
#.....................................................................................................................................




#.................................................................About us page..............................................
def aboutus():
    
    
    abt=tkinter.Tk()
    abt.geometry("1200x850")
    abt["bg"]= "black"
    abt_label=tkinter.Label(abt, text="ANJUMAN POLYTECHNIC,", font=('arial', 36, 'bold')).place(x=180, y=50)
    abt_labelngp=tkinter.Label(abt, text="NAGPUR",fg='red', font=('arial', 36, 'bold')).place(x=795, y=50)
    Button_abtexit=tkinter.Button(abt, text="Exit this Application",width=20,bg='brown',fg='white', command=abt.destroy).place(x=1000,y=10)
    abt_labeladd=tkinter.Label(abt, text="Managed By Anjuman HAMI-E-ISLAM", fg='Blue', font=('arial', 15, 'bold')).place(x=430, y=120)    
    abt_labelsub=tkinter.Label(abt, text="SUBMITTED BY:-Mohd Tahzeeb Khan \n Roll No: 30", font=20).place(x=425, y=300)
    abt_labelSubject=tkinter.Label(abt, text="Subject: Programming in Python", font=20).place(x=460, y=250)
    abt_labelsem=tkinter.Label(abt, text="Sixth Semester CO-6-I (I-Scheme)", font=20).place(x=450, y=500)
    abt_labeltecher=tkinter.Label(abt, text="Subject Teacher: Mrs. Pallavi Maam \n Lecturer", font=20).place(x=430, y=400)
    abt_labeltopic=tkinter.Label(abt, text="Topic: Covid19 Vaccine registration System", font=(20)).place(x=400, y=200)

    mainloop()
    
#...............................................................................................................................






#........................................................code for store(insert) user's registed data into database....................................
def storedata():
    vaccinedate()
    dateofvaacine= str(date)+" "+tu+" "+str(year)
    global full_name
    conn=sqlite3.connect('CovidVaccine.db')#connected to the database called: CovidVaccine.db
    conn.execute('''CREATE TABLE IF NOT EXISTS Registration
    (fullname TEXT NOT NULL, 
     gender TEXT NOT NULL, 
     age INT NOT NULL,
     mobileno INT NOT NULL,
     adharno INT NOT NULL,
     emailid TEXT NOT NULL,
     addres TEXT NOT NULL,
     vaccine TEXT NOT NULL,
     dose TEXT NOT NULL,
     date1 TEXT NOT NULL);''')#created table called: Registration
    full_name=entry_1.get()
    identify=gender.get()
    if(identify==1):
        gend='Male'
    elif(identify==0):
        gend='Female'
    else:
        gend='Transgender'
    ag_e= entry_3.get()
    mono=entry_4.get()
    t=str('+91')+" "+str(mono)
    adhno=entry_5.get()
    email_id=entry_6.get()
    add_ress= entry_7.get()
    vaccine=c.get()
    fdo=f_dose.get()
    sdo=s_dose.get()
    tdo=t_dose.get()
    if(fdo==1 and sdo==1 and tdo==1):
        duo='1st Dose, 2 Dose, 3rd Dose'
    elif(fdo==1 and sdo==0 and tdo==0):
        duo='1st Dose'
    elif(fdo==0 and sdo==1 and tdo==0):
        duo='2nd Dose'
    elif(fdo==0 and sdo==0 and tdo==1):
        duo='3rd Dose'
    elif(fdo==1 and sdo==1 and tdo==0):
        duo='1st & 2nd Dose'
    elif(fdo==0 and sdo==1 and tdo==1):
        duo='2nd & 3rd Dose'
    elif(fdo==0 and sdo==0 and tdo==0):
        duo='No dose is seleted'
    dateova=dateofvaacine
    
    
    #print("Name:" +full_name,"\n Age:"+ ag_e,"\n mobile no:" +t,"\n Aadhar No:" +adhno,"\n Email Id:" +email_id, "\n Gender:" +gend,"\n Address:" +add_ress, "\n Vaccine:" +vaccine, "Dose:" +duo, "\n date Of Vaccination:" +dateova)
    conn.execute("INSERT INTO Registration(fullname, gender, age, mobileno, adharno, emailid, addres, vaccine, dose, date1) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (full_name, gend, ag_e, t, adhno, email_id, add_ress, vaccine, duo, dateova));# inserting data in database

    emailsend(email_id)
    #sendsms(t)
    conn.commit()#saving all the changes and updates into the table..............
    conn.close()#close connection with database
    onclick(full_name, dateofvaacine)
#...............................................................................................................................



    

#........................................................User Registration form Setup is Here....................................
def Registrationform():
    vaccinedate()
    global entry_1, entry_3, entry_4, entry_5, entry_7, entry_6, gender, gender1, c, f_dose, s_dose, t_dose,reg, progress
    reg=tkinter.Tk()
    reg.geometry("500x800") #size of widget
    reg["bg"]= "sky blue"  
    reg.title("Vaccine Registration Form")
    
    Fullname=StringVar()
    Email=StringVar()
    gender=IntVar(reg)
    c=tkinter.StringVar(reg)
    age=IntVar()
    var=StringVar()
    mobileno= StringVar()
    adharno=StringVar()
    f_dose=IntVar(reg)
    s_dose=IntVar(reg)
    t_dose=IntVar(reg)
    address=StringVar()
    
  
   

    label_0 = tkinter.Label(reg, text="Vaccine Registration Form", width=25, font=("bold", 20), bg='sky blue', fg='Black')
    label_0.place(x=80, y=53)

    label_1= Label(reg, text="Fullname:", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)

    entry_1=Entry(reg, textvariable=Fullname, width=38)
    entry_1.place(x=240, y=130)

    label_2= Label(reg, text="Gender:", width=20, font=("bold", 10))
    label_2.place(x=80, y=180)
    Radiobutton(reg, text="Male", variable=gender, value=1).place(x=240, y=180)
    Radiobutton(reg, text="Female",  variable=gender, value=0).place(x=320, y=180)
    Radiobutton(reg, text="Trans",  variable=gender, value=2).place(x=410, y=180)


    label_3= Label(reg, text="Age:", width=20, font=("bold", 10))
    label_3.place(x=80, y=230)

    entry_3=Entry(reg, textvariable=age, width=38)
    entry_3.place(x=240, y=230)

    label_4= Label(reg, text="Mobile No:", width=20, font=("bold", 10))
    label_4.place(x=80, y=280)

    label_18= Label(reg, text="+91", width=4, font=("bold", 10)).place(x=240, y=280)
    entry_4=Entry(reg, textvariable=mobileno, width=32)
    entry_4.place(x=275, y=280)

    label_5= Label(reg, text="Aadhar No:", width=20, font=("bold", 10))
    label_5.place(x=80, y=330)

    entry_5=Entry(reg, textvariable=adharno, width=38)
    entry_5.place(x=240, y=330)

    label_6= Label(reg, text="Email Id:", width=20, font=("bold", 10))
    label_6.place(x=80, y=380)

    entry_6=Entry(reg, textvariable=Email, width=38)
    entry_6.place(x=240, y=380)

    label_7= Label(reg, text="Your Address:", width=20, font=("bold", 10))
    label_7.place(x=80, y=420)

    entry_7=Entry(reg, textvariable=address, width=38)
    entry_7.place(x=240, y=420)



    label_8 = Label(reg, text="Vaccine:",width=20,font=("bold", 10))
    label_8.place(x=80,y=470)

    list1 = ['Bharat Boitech Covaxin','Astra zenca Covishield','Sputnik Vaccine I', 'Sputnik Vaccine V', 'DRDO D-2'];

    droplist= OptionMenu(reg, c, *list1)
    droplist.config(width=31)
    c.set("<-Vaccines->") 
    droplist.place(x=240,y=470)

    label_9 = Label(reg, text="Doses:",width=20,font=("bold", 10))
    label_9.place(x=80,y=530)
    
    Checkbutton(reg, text="1st Dose", onvalue=1, offvalue=0, variable=f_dose).place(x=240,y=530)
    Checkbutton(reg, text="2nd Dose", onvalue=1, offvalue=0, variable=s_dose).place(x=320,y=530)
    Checkbutton(reg, text="3rd Dose", onvalue=1, offvalue=0, variable=t_dose).place(x=400,y=530)
    
    lab=Label(reg, text="*After you click submit Button Please wait for 10 seconds for comformation", width=65, font=("bold", 8), background='red')
    lab.place(x=80 ,y=590 )

    Button_submit=tkinter.Button(reg, text="Submit Form",width=20,bg='brown',fg='white', command=storedata).place(x=320,y=630)
    Button_clrscr=tkinter.Button(reg, text="Clear Form",width=20,bg='red',fg='black', command=cleardata).place(x=80,y=630)
    button_exit=tkinter.Button(reg, text="Exit", width=50, bg='blue', fg='white', command=reg.destroy).place(x=90, y= 680)
    
    reg.resizable(False, False)
    reg.mainloop()
#...................................storedata function(use to store user's info in database).........................................



def vaccineshow():
    dd=sqlite3.connect('CovidVaccine.db')
    cont=dd.cursor()
    cont.execute('''CREATE TABLE IF NOT EXISTS Avaiable_vaccine
    (ID INT NOT NULL, 
    astrazenca INT NOT NULL,
    bharat INT NOT NULL,
    sputnik INT NOT NULL,
    sputnik2 INT NOT NULL,
    drdo INT NOT NULL);''')
    cont.execute("SELECT astrazenca FROM Avaiable_vaccine WHERE ID=1");
    check=cont.fetchone()
    if(check==(1,)):
        aczs='Available'
    else:
        aczs='Not-Available'
    
    cont.execute("SELECT bharat FROM Avaiable_vaccine WHERE ID=2");
    checkl=cont.fetchone()
    if(checkl==(1,)):
        bbcs='Available'
    else:
        bbcs='Not-Available'
    
    cont.execute("SELECT sputnik FROM Avaiable_vaccine WHERE ID=3");
    checkn=cont.fetchone()
    if(checkn==(1,)):
        rassainsput='Available'
    else:
        rassainsput='Not-Available'
    
    cont.execute("SELECT drdo FROM Avaiable_vaccine WHERE ID=5");
    checkk=cont.fetchone()
    if(checkk==(1,)):
        ddrr='Available'
    else:
        ddrr='Not-Available'
        

#_________________________________________________Available Vaccines____________________________________________________________________
    vac=Frame(m, width=500, height= 100, bd= 8, bg='black', relief="groove").place(x=150, y=200)
    lab=tkinter.Label(m, text="Available Vaccines", font=('times', 10), fg='White', bg='black').place(x=350, y=210)
    lab=tkinter.Label(m, text="* Bharat Boitech Covaxin", font=('times', 10), fg='White', bg='black').place(x=200, y=230)
    show=tkinter.Label(m, text=bbcs, font=('times', 10), fg='black', bg='white').place(x= 350, y=230)
    lab=tkinter.Label(m, text="* Astra zenca Covishield", font=('times', 10), fg='White', bg='black').place(x=200, y=260)
    show=tkinter.Label(m, text=aczs, font=('times', 10), fg='black', bg='white').place(x= 350, y=260)
    lab=tkinter.Label(m, text="* sputnik I & V", font=('times', 10), fg='White', bg='black').place(x=450, y=230)
    show=tkinter.Label(m, text=rassainsput, font=('times', 10), fg='black', bg='white').place(x= 550, y=230)
    lab=tkinter.Label(m, text="* DRDO- D2", font=('times', 10), fg='White', bg='black').place(x=450, y=260)
    show=tkinter.Label(m, text=ddrr, font=('times', 10), fg='black', bg='white').place(x= 550, y=260)
    dd.commit()
    cont.close()

def bed():
    coo=sqlite3.connect('CovidVaccine.db')
    con=coo.cursor()
    con.execute('''CREATE TABLE IF NOT EXISTS Available_beds
    (ID INT NOT NULL PRIMARY KEY, 
    oxygenbed INT NOT NULL,
    vantilatorbed INT NOT NULL,
    normalbed INT NOT NULL);''')
    con.execute("SELECT oxygenbed FROM Available_beds WHERE ID=1");
    oxybed= con.fetchone()
    con.execute("SELECT vantilatorbed FROM Available_beds WHERE ID=2");
    vantibed=con.fetchone()
    
    con.execute("SELECT normalbed FROM Available_beds WHERE ID=3");
    norbed=con.fetchone()
    to= Frame(m, width=210, height= 130, bd= 8, bg='black', relief="groove")
    to.place(x=300, y=320)
    
    
    a=random.randrange(0, 120)
    b=random.randrange(0, 120)
    c=random.randrange(0, 120)
    
    flab=tkinter.Label(m, text="Available Isolation Beds", font=('times', 10), fg='White', bg='black').place(x=335, y=330)
    flab=tkinter.Label(m, text="* Vantilator's Bed", font=('times', 10), fg='White', bg='black').place(x=325, y=365)
    flab=tkinter.Label(m, text=vantibed, font=('times', 10), fg='black', bg='white').place(x=460, y=365)
    flab=tkinter.Label(m, text="* Oxygen Beds", font=('times', 10), fg='White', bg='black').place(x=325, y=380)
    flab=tkinter.Label(m, text=oxybed, font=('times', 10), fg='black', bg='white').place(x=460, y=380)
    flab=tkinter.Label(m, text="* Covid Normal Beds", font=('times', 10), fg='White', bg='black').place(x=325, y=395)
    flab=tkinter.Label(m, text=norbed, font=('times', 10), fg='black', bg='white').place(x=460, y=395)
    flab=tkinter.Label(m, text="RT-PCR Test", font=('times', 10), fg='White', bg='black').place(x=335, y=420)
    flab=tkinter.Label(m, text="Free", font=('times', 10), fg='black', bg='white').place(x=460, y=420)
    coo.commit()
    coo.close()
#.......................................execution of First function or main will start from this funtion......................................................
def start():
    global m
    
    m=tkinter.Tk()
    m.geometry("800x500")
    m["bg"]= "NavajoWhite2"  
    m.title("Life Care service, UserInterface")
    vaccineshow()
    bed()
    
    tkinter.Label(m, text="LifeCare Hospital Service", font=('arial', 36, 'bold'), bg='NavajoWhite3').place(x=100,y=20)
    tkinter.Label(m, text="Raj Nagar, Nagpur", font=("arial", 15), bg='NavajoWhite3').place(x=330, y=80) 
    tkinter.Label(m, text="ph.no.:7787565  LIC.No.: mpc5846d8\84", bg='NavajoWhite3').place(x=310, y=110)
    tkinter.Label(m, text="lifecarehospitalshelp001@gmail.com", bg='NavajoWhite3').place(x=315, y=130)
    Button= tkinter.Button(m, text="Vaccine Registration",height=1, width=17, font=1, command=Registrationform, fg='green').place(x=540, y=400)
    buttonsignin=tkinter.Button(m, text="Login as Admins", height= 1, width= 17, font=1, command= admin,fg='blue').place(x=540, y=320)
    exitm= tkinter.Button(m, text="Exit", height= 1, width= 17, font=1, command=m.destroy, bg='Red', fg='White').place(x=50, y=400)
    exitm= tkinter.Button(m, text="About Us(Developer)", height= 1, width=17, font=1 , command= aboutus,bg='Green', fg='black').place(x=50, y=320)

    m.resizable(False, False)
    
    
    m.mainloop()


#......................................................function call to start execution of the program..................................
start()


#.....................................................THE END OF THE PROGRAM............................................................
