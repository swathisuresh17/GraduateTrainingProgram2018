<Problem set 08> Sep 10,2018
 Submitted by swathi.b.suresh


/*1.you need to install sqlite3 python module first 
Write a Script where establish a connection to db
Write a DDL to create a table (columns: Name, Rollno, Subject1, Subject2, Subject3)
insert 5 rows with values
Do a count() the table
update query to modify existing records
delete the table
finally drop table */
 


import sqlite3
conn=sqlite3.connect('sample2.db')
c=conn.cursor()	
data=[('prithi','2013pec181',87,98,66),('swathi','2013pec182',77,87,89),('kirthi','2013pec183',89,98,78)]
obj=Stud()
obj.Create(c)
obj.Insert(data,c)
n='swathi'
obj.Update(c,88,n)
obj.Select(c)
