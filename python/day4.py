<Problem set 04> Sep 6,2018
Submitted by swathi.b.suresh>

/*1.You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
alison heck => Alison Heck
Given a full name, your task is to capitalize the name appropriately.
Input Format:-
A single line of input containing the full name, S .
Constraints:-
* 0<len(S)<1000
* The string consists of alphanumeric characters and spaces.*/

s=raw_input("enter your name:")
s1=s.split()[0]
s2=s.split()[1]
print(s1)
print(s2)
if(s1[0].islower() or s2[0].islower()):
    new_str1=s1[0].upper()
    new_str2=s2[0].upper()
    my_str=new_str1+s1[1:]+new_str2+s2[1:]
    c=''.join(my_str)
    print(c)
elif(name[0].isdigit()):
    print(s)

/*2.You have a record of  students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer  followed by the names and marks for students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.
Input Format:-
The first line contains the integer N, the number of students. The next  lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.
Constraints:-
* 2<=N<=10
* 0<=MARKS<=100*/

def sum_stu():
   sum_s={}
   for k,v in student_details.iteritems():
       sum_s[k]=sum(v)
   print("total mark%s"%sum_s)
def avg(new):
   avg_s={}
   k1=new
   for k,v in student_details.iteritems():
       if(k==k1):
         print(float(sum(v)/len(v)))
         #print("average mark%s"%avg_s[k])
student_details={}	
std_count=raw_input("enter no student")			
for i in range(int(std_count)):
   name=raw_input("enter student name")
   sub_count=raw_input("enter no of subject")
   student_marklist=[]
   for j in range(int(sub_count)):
      j=j+1
      v=input("enter marks of subject"+str(j)+":")		
      student_marklist.append(v)
   student_details[name]=student_marklist
	
print(student_details)
sum_stu()
new=raw_input("enter name to find avg")
avg(new)

/*3.Exceptions
----------
Errors detected during execution are called exceptions.*/

def div(a,b):
    try:
      c=a/b
      print(c)
    except Exception as error:
      print(error)
	
count_num=raw_input("enter number of count:")
count_num=int(count_num)
for i in (range(count_num)):
    print(i)
    a=raw_input("enter a number:")
    b=raw_input("enter a number:")
    try:
       div(int(a),int(b))
    except:
	   print("please enter valid number")
    
i+=1

/*4.Initialize your list and read in the value of  followed by  lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format:-
The first line contains an integer, n , denoting the number of commands. 
Each line i of the n  subsequent lines contains one of the commands described above.

Constraints:-
* The elements added to the list must be integers.*/

dict={}
l=[]
n=input("enter no of command:")
for i in range(n):
    a=raw_input()
    l1=a.split(" ")
    dict[i]=l1
print dict
for i in range(n):
	if(dict[i][0]=="insert"):
		l.insert(int(dict[i][1]),int(dict[i][2]))
	elif(dict[i][0]=="print"):
		print l
	elif(dict[i][0]=="remove"):
		l.remove(int(dict[i][1]))
	elif(dict[i][0]=="append"):
		l.append(int(dict[i][1]))
	elif(dict[i][0]=="sort"):
		l.sort()
	elif(dict[i][0]=="pop"):
		l.pop(len(l)-1)
	elif(dict[i][0]=="reverse"):
		l.reverse()
