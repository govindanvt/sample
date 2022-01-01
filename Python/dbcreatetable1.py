import sqlite3
c=sqlite3.connect('studenttable.db')
#c.execute('''CREATE TABLE STUDENT(ROLLNO INT NOT NULL,NAME TEXT NOT NULL,AGE INT NOT NULL);''')
#c.execute('''INSERT INTO STUDENT(ROLLNO,NAME,AGE)VALUES(12,'ABHIJITH',26)''');
#c.execute('''INSERT INTO STUDENT(ROLLNO,NAME,AGE)VALUES(13,'HARI',25)''');
#c.execute('''INSERT INTO STUDENT(ROLLNO,NAME,AGE)VALUES(14,'KEETHI',24)''');
#c.execute('''INSERT INTO STUDENT(ROLLNO,NAME,AGE)VALUES(15,'GAYATHRI',21)''');
#c.execute('''INSERT INTO STUDENT(ROLLNO,NAME,AGE)VALUES(16,'JISHNU',24)''');
#c.execute('''INSERT INTO STUDENT(ROLLNO,NAME,AGE)VALUES(17,'RANJITH',35)''');
#c.commit()
cursor=c.execute("SELECT rollno,name,age FROM student")
for row in cursor:
    print("\tRollNo.: ",row[0],"Name: \t\t",row[1],"\tAge: \t",row[2])
#c.execute("UPDATE student SET age=27 WHERE rollno=14")
#c.commit()
#print("Updated Successfully...!")
#c.execute("DELETE from student WHERE rollno=15")
#c.commit()
#print("Deleted Successfully...!")
#c.execute('''INSERT INTO STUDENT(ROLLNO,NAME,AGE)VALUES(?,?,?)''',(10,'GAYATHRI',21));
#c.commit()
#print("Added new field through ")