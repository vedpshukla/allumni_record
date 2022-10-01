print('\t\t\t\tKV MALKAPURAM')
print('\t\t\t\t==============\n')
print('\t\t\t\t     Allumni Record')
print('\t\t\t\t     ==========\n')


print("ALLUMNI RECORD\n")
import mysql.connector as p
from tabulate import tabulate
con=p.connect(host="localhost",user="root",passwd="root",database="allumni_record")
cur=con.cursor()
print("........connecting to the database\n")

#time delay code-------------------
import time
time.sleep(2)
print("Database is loading......\n")
time.sleep(1)
print("load successful..\n")

import roll_nos 
d=roll_nos.Z()

#######################################
def add():
        roll=int(input("Roll no.:"))
        if roll not in d:
            name=input("Enter name and gender (like, F/M _NAME_):")
            x=float(input("Enter passout percentage"))
            tot=x*6
            bat=input('Enter Batch(like, 2015-16):')
            query="insert into students values({},'{}',{},{},'{}')".format(roll,name,tot,x,bat)
            cur.execute(query)
            con.commit()
            print("successfully uploaded")
        else:
                print("Roll number already exists")
        z=input("print 0 to continue...any other key to exit:")
        if z=="0":
          show()
        else:
          print("===============end==================")

def search():
    roll=int(input("Enter roll number:"))
    if roll in d:
        time.sleep(1)
        print("scanning database......\n")
        query="select name from students where roll={}".format(roll)
        cur.execute(query)
        res=cur.fetchall()
        print(tabulate(res))
    #time.sleep(1)
        print("load succesful..\n")
        z=input("for more details press 1:")
        if z=="1":
            query="select * from students where roll={}".format(roll)
            cur.execute(query)
            res=cur.fetchall()
            print('\n roll          name         tot  %age  s batch')            
            print(tabulate(res))
    else:
        print("The roll number doesn't exist")
    z=input("print 0 to continue...any other key to exit:")
    if z=="0":
            show()
    else:
            print("===============end==================")
    
def update():
    roll=int(input("Enter roll number:"))

    if roll in d:
        print("Select your option:")
        print('1.Update name\n2.Update percentage')
        print('3.Update batch year')
        x=int(input("Enter your selection:"))
        if x==1:
             name=input("Enter new name:")
             query="update students set name='{}' where roll={}".format(name,roll)
             cur.execute(query)
             con.commit()
             print("successfully updated")
        elif x==2:
             x=float(input("Enter updated passout percentage"))
             query="update students set percentage={} where roll={}".format(x,roll)
             cur.execute(query)
             con.commit()
             print("successfully updated")
        elif x==3:
             bat=input('Enter updated batchyear(like, 2015-16):')
             query="update students set batch='{}' where roll={}".format(bat,roll)
             cur.execute(query)
             con.commit()
             print("successfully updated")
    
        else:
             print("invalid entry")
    else:
             print("Roll number doesn't exist")
    z=input("press 0 to continue...any other key to stop:")
    if z=="0":
                z=(input("Press 1 for main menu and 2 for update menu"))
                if z=="1":
                     show()
                elif z=="2":
                    update()
                else:
                    print("Invalid input\n\t\t\tPROGRAM TERMINATED")

def delete():
    roll=int(input("Enter roll number:"))
    if roll in d:
        z=input("You have selected to delete candidate from the system.To continue press  0:")
        if z=="0":
          query="delete from students where roll={}".format(roll)
          cur.execute(query)
          con.commit()
          print("Candidate deleted")
        else:
            print("program terminated")
    else:
        print("The provided roll number doesn't exist\nTRYAGAIN")
        

def bs():
    bat=input('Enter Batch(like, 2015-16):')
    query="select roll,name,percentage from students where batch='{}'".format(bat)
    cur.execute(query)
    z=cur.fetchall()
    print(tabulate(z))
def custom():
    bat=input('Enter Batch(like, 2015-16):')
    print("\t\t\t\tCUSTOM MENU")
    print("\t\t\t\t*******************")
    print("\t\t1.Show male candidates")
    print("\t\t2.Show female candidates")
    z=input("select your option:")
    if z=="1":
        print("To show candidates with percentage more than 90%,press1")
        print("To show candidates with percentage more than 80% and less than 90%,press2")
        print("To show candidates with percentage below 80%,press3")
        z=input("Enter your choice:")
        
        if z=="1":
                query="select * from m where percentage>=90"
                cur.execute(query)
                z=cur.fetchall()
                print(tabulate(z))
        elif z=="2":
                query="select * from m where percentage>=80 and percentage<90"
                cur.execute(query)
                z=cur.fetchall()
                print(tabulate(z))
        elif z=="3":
                query="select * from m where percentage<80"
                cur.execute(query)
                z=cur.fetchall()
                print(tabulate(z))
        else:
                print("invalid input")
                print("Program terminated")
                
            
    elif z=="2":
        print("To show candidates with percentage more than 90%,press1")
        print("To show candidates with percentage more than 80% and less than 90%,press2")
        print("To show candidates with percentage below 80%,press3")
        z=input("Enter your choice:")
        if z=="1":
                query="select * from f where percentage>=90"
                cur.execute(query)
                z=cur.fetchall()
                print(tabulate(z))
        elif z=="2":
                query="select * from f where percentage>=80 and percentage<90"
                cur.execute(query)
                z=cur.fetchall()
                print(tabulate(z))
        
        elif z=="3":
                query="select * from m where percentage<80"
                cur.execute(query)
                z=cur.fetchall()
                print(tabulate(z))
        else:
                print("invalid input")
                print("Program terminated")
    else:
            print("Invalid input")
def excel():
    query="delete from students"
    cur.execute(query)
    con.commit()
    import Excel
    Excel.a()
    m="insert into m(roll,name,total,batch,percentage) select roll,name,total,batch,percentage from students where name like 'm%'"
    f="insert into f(roll,name,total,batch,percentage) select roll,name,total,batch,percentage from students where name like 'f%'"
    cur.execute(m)
    con.commit()
    cur.execute(f)
    con.commit()
    print("data updated successfully")

#===============================================
#main

def show():
        print('\t\t\t\t\t     Main Menu')
        print('\t\t\t\t\t     --------------\n')
        print('\t\t\t1.Add new candidate\t\t2.Search for already existing candidate\n')
        print('\t\t\t3.Update existing data\t\t4.Delete a candidate\n')
        print('\t\t\t5.Batchwise search\t\t6.Custom\n')
        print('\t\t\t7.Enter bulk data and make changes through excel file')
        x=int(input("Enter your selection:"))
        if x==1:
            add()
        elif x==2:
            search()
        elif x==3:
            update()
        elif x==4:
            delete()
        elif x==5:
            bs()
        elif x==6:
            custom()
        elif x==7:
            excel()
        else:
            print("invalid input")
            start()
    
def start():
    x=(input("Enter admin password to for verification:"))     #Admin pass:123
    if x=="123":
            print("Authorisation granted\n")
            show()

    else:
        print("\nAccess denied\n")
        x=(input("To try again,press y or any other key to end:"))
        if x=="y" or x=="Y":
            start()
        else:
            print("\t\t\tPROGRAM TEMINATED")

start()












