
--ProblemSet2,september 3 2018
--Submission by<swathi.b.suresh@accenture.com>

/*1.get first name and last name from user and print your full name */

a=raw_input("enter your first name")
b=raw_input("enter your last name")
print("Full Name : %s%s"%(a,b))  

/*2.get ur full name, age as input from user and print first name and last name , age using string slicing*/

a=raw_input("enter your full name ")
b=raw_input("enter your age")
x,y=a.split(" ")
print("first name:%s\n""last name:%s\n" "age:%s\n"%(x,y,b))
if(b>=18):
 print("eligible to vote")
else:
 print("not eligible to vote")
 
/*3.Python program to check whether a year is leap year or not*/
a=raw_input("enter year")
a=int(a)
if(a%4==0):
    if(a%100==0):
        if(a%400==0):
           print("leap year")
        else:
           print("non leap year")
    else:
        print("leap year")
else:
   print("non leap year")     

/*4.program that accepts a sentence and calculate the number of upper case letters and lower case letters*/
s=raw_input("enter year")
upper=0
lower=0
for i in s:
   if(i.isupper()):
      upper=upper+1
   elif(i.islower()):
      lower=lower+1
print("No. of upper case %s"%upper)
print("No. of lower case%s"%lower)

/*5.perform sum of  even numbers*/
a=[1,2,3,4,5,6,7,8]
sum=0
for i in a:
   if(i%2==0):
      sum=sum+i
print("sum=%s"%sum)


a=raw_input("enter number")
x=[]
x=a.split(',')
z=tuple(x)
print(x)
print(z) 


/*6.program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple*/

a=str(raw_input("enter number")) 
x=[]
x=a.split(',')
z=tuple(x)
print(x)
print(z) 
