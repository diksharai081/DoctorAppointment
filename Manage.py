#!C:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"


import cgi,cgitb
import MySQLdb
db=MySQLdb.connect("localhost","root","","doctorappointment")
cursor=db.cursor()

if cursor:
    """print "Database Connected" """
else:
    print"Database not Connect"

import datetime
import cgi,cgitb
form=cgi.FieldStorage()

flag=form.getvalue("flg")


""" Registration Data Insertion Code """

if flag=='1':
  name=form.getvalue("name")
  """print name"""
  mobile=form.getvalue("mobile")
  """print mobile"""
  email=form.getvalue("email")
  """print name"""
  password=form.getvalue("pass")
  """print password"""
  city=form.getvalue("city")
  """print city"""
  datetime=datetime.datetime.now()
  status="false"
  ins="insert into registration(Reg_Name,Reg_Mobile,Reg_Email,Reg_Password,Reg_City,Reg_Date_Time) values('%s','%s','%s','%s','%s','%s')"%(name,mobile,email,password,city,datetime)
  cursor.execute(ins)
  db.commit()
  ins1="insert into login(Login_Email,Login_Password,Login_Status,Login_Date_Time) values('%s','%s','%s','%s')"%(email,password,status,datetime)
  cursor.execute(ins1)
  db.commit()
  if ins:
    print "<script>window.location.href='Registration.py';alert('Data Insert Successfully !');</script>"
  else:
    print "data not insert"  


""" Registration Data Insertion Code End"""

""" Login  Code Start"""

if flag=='2':
  email=form.getvalue("email")
  print email
  password=form.getvalue("pass")
  print password
  sel="select * from login where Login_Email='%s'"%(email)
  cursor.execute(sel)
  data=cursor.fetchone()
  if data:
    print "<script>window.location.href='Profile.py';alert('Login Success !');</script>"
  else:
    print "<script>window.location.href='Login.py';alert('Login failed !');</script>"
""" Login  Code End"""

""" Contact  Code Start"""

if flag=='3':
  name=form.getvalue("name")
  print name
  email=form.getvalue("email")
  print email
  subject=form.getvalue("subject")
  print subject
  message=form.getvalue("message")
  print message
  datetime=datetime.datetime.now()
  ins3="insert into contact(Contact_Name,Contact_Email,Contact_Subject,Contact_Message,Contact_Date_Time) values('%s','%s','%s','%s','%s')"%(name,email,subject,message,datetime)
  cursor.execute(ins3)
  db.commit()
  print "<script>window.location.href='Contact.py';alert('Thanku ! We will Contact Soon !');</script>"
  
  

""" Contact  Code End"""

""" Appointment  Code Start"""
if flag=='4':
  fname=form.getvalue("fname")
  """print fname"""
  lname=form.getvalue("lname")
  """print lname"""
  service=form.getvalue("service")
  """print service"""
  mobile=form.getvalue("mobile")
  """print mobile"""
  message=form.getvalue("msg")
  """print message"""
  datetime=datetime.datetime.now()
  ins4="insert into appointment(Appoint_Fname,Appoint_Lname,Appoint_Services,Appoint_Mobile,Appoint_Message,Appoint_Date_Time) values('%s','%s','%s','%s','%s','%s')"%(fname,lname,service,mobile,message,datetime)
  cursor.execute(ins4)
  db.commit()
  print "<script>window.location.href='Appointment.py';alert('Appointment Fixed');</script>"
   
""" Appointment  Code End""" 


""" Admin Login Code Start"""

if flag=='5':
  email=form.getvalue("email")
  print email
  password=form.getvalue("password")
  print password
  if email:
    print "<script>window.location.href='Admin/Dashboard.py';alert('Login Success');</script>"  
 
""" Admin Login Code End""" 


""" Add Doctor Code Start""" 

if flag=='6':
  dname=form.getvalue("dname")
  print dname
  dspecial=form.getvalue("dspecial")
  print dspecial
  carea=form.getvalue("carea")
  print carea
  mobile=form.getvalue("mob")
  print mobile
  cname=form.getvalue("cname")
  print cname
  wexp=form.getvalue("wexp")
  print wexp
  address=form.getvalue("address")
  print address
  datetime=datetime.datetime.now()
  ins5="insert into adddoctor(Doctor_Name,Doctor_Spec,Doctor_Area,Doctor_Mob,Doctor_Cname,Doctor_Wexp,Doctor_Address,Doctor_Date_Time) VALUES('%s','%s','%s','%s','%s','%s','%s','%s')"%(dname,dspecial,carea,mobile,cname,wexp,address,datetime)
  cursor.execute(ins5)
  db.commit()
  print "<script>window.location.href='Admin/AddDoctor.py';alert('Doctor Add Successfully');</script>"
   
""" Add Doctor Code End""" 


""" All Doctor Delete Code Start""" 
if flag=='7':
  delid=form.getvalue("delid")
  dell="delete from adddoctor where Doctor_Id='%s'"%(delid)
  cursor.execute(dell)
  db.commit()
  print "<script>window.location.href='Admin/AllDoctor.py';alert('Doctor Data Deleted');</script>" 

""" All Doctor Delete Code End""" 

""" All Appointment Delete Code Start"""
if flag=='8':
  delid=form.getvalue("delid")
  dell="delete from appointment where Appoint_Id='%s'"%(delid)
  cursor.execute(dell)
  db.commit()
  print "<script>window.location.href='Admin/AllAppointment.py';alert('Appointment Data Deleted');</script>"
 
""" All Appointment Delete Code End""" 


""" All Contact Delete Code Start"""
if flag=='9':
  delid=form.getvalue("delid")
  dell="delete from contact where Contact_Id='%s'"%(delid)
  cursor.execute(dell)
  db.commit()
  print "<script>window.location.href='Admin/AllContact.py';alert('Contact Data Deleted');</script>"
 
""" All Contact Delete Code End""" 


""" Logout Code Start"""
if flag=='10':
  print "<script>window.location.href='Admin/index.py';alert('Logout Successfully');</script>"
 
""" Logout Code End""" 


"""Admin Change Password Code Start"""
if flag=='11':
  opass=form.getvalue("opass")
  print opass
  npass=form.getvalue("napss")
  print npass
  cpass=form.getvalue("cpass")  
 
"""Admin Change Password Code End""" 


"""user Feedback Code Start"""
if flag=='12':
  name=form.getvalue("name")
  print name
  mobile=form.getvalue("mobile")
  print mobile
  message=form.getvalue("msg")
  print message
  datetime=datetime.datetime.now()
  ins6="insert into userfeedback(Feed_Name,Feed_Mobile,Feed_Message,Feed_Date_Time) values('%s','%s','%s','%s')"%(name,mobile,message,datetime)
  cursor.execute(ins6)
  db.commit()
  print "<script>window.location.href='Feedback.py';alert('FeedBack is Added !');</script>"
  
  
"""user Feedback Code End"""

 
"""user Logout Code Start"""
if flag=='13':
  print "<script>window.location.href='index.py';alert('Logout Successfully');</script>"
 
"""user Logout Code End""" 


"""user Appointment Book Code Start"""

if flag=='14':
  id=form.getvalue("id")
  print id
  name=form.getvalue("name")
  print name
  mobile=form.getvalue("mobile")
  print mobile
  refer=form.getvalue("refer")
  print refer
  area=form.getvalue("area")
  print area
  aday=form.getvalue("aday")
  print aday
  datetime=datetime.datetime.now()
  ins7="insert into userappointment(Doctor_Id,User_Name,User_Mobile,User_Refer,User_Area,User_Book_Day,User_Date_Time) values('%s','%s','%s','%s','%s','%s','%s')"%(id,name,mobile,refer,area,aday,datetime)
  cursor.execute(ins7)
  db.commit()
  print "<script>window.location.href='Profile.py';alert('Your Appointment is Booked ! Wait for Responce');</script>"  
  
  
 
"""user Appointment Book Code End""" 


"""Admin All user Appointment Book Code Start"""

if flag=='15':
  delid=form.getvalue("id")
  print delid
  dell="delete from userappointment where User_Id='%s'"%(delid)
  cursor.execute(dell)
  db.commit()
  print "<script>window.location.href='Admin/UserAppointment.py';alert('User Appointment Data Deleted');</script>"
    
  
"""Admin All user Appointment Book Code End""" 



