#!C:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb
form=cgi.FieldStorage()

a=form.getvalue("id")

b=form.getvalue("opass")
c=form.getvalue("npass")
d=form.getvalue("cpass")

import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","","docterappointment")
cursor=db.cursor()

sel="select * from admin where id='%s'"%(a)
cursor.execute(sel)
data=cursor.fetchone()

if data[2]==b:
  if c==d:
    up="update admin set password='%s' where id='%s'"%(c,a)
    cursor.execute(up)
    db.commit()
    print "<script>window.location.href='dashboard.py';alert('password change');</script>"
  else:
    print "new and confirm not match"
else:
  print "old pass not match"

  

  
  

