<Problem set 03> Sep 10,2018
 Submitted by swathi.b.suresh

/*1.Given the following dictionary:
      inventory = {
                   'gold' : 500,
                   'pouch' : ['flint', 'twine', 'gemstone'],
                   'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
                }
       Try to do the followings:
       i)Add a key to inventory called 'pocket'.
       ii)Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
       iii).sort()the items in the list stored under the 'backpack' key.
       iv)Then .remove('dagger') from the list of items stored under the 'backpack' key.
       v)Add 50 to the number stored under the 'gold' key.*/
def sort_backpack():
    inventory['backpack'].sort()
    print("sorted list%s"%inventory['backpack'])
def delete():
    # del inventory['backpack'][2]
   inventory['backpack'].pop(2)
   print("after deletion%s"%inventory['backpack'])	
def add_element():
    inventory['gold']=[500,50]
    print("after adding value to the key gold%s"%inventory)
inventory = {
                   'gold' : 500,
                   'pouch' : ['flint', 'twine', 'gemstone'],
                   'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
                }
				
inventory['pocket']=['seashell', 'strange berry' ,'lint']
print("new inventory%s"%inventory)
sort_backpack()
delete()
add_element()

/*2.create a student details dictionary having {'student1':[marks1,marks2, marks3],'student2':[marks1,marks2,marks3]}
      #i)Create the dictionary as mentioned above
       #ii) need to perform total and average of the marks for each student*/
def sum_stu():
   sum_s={}
   for k,v in student_details.iteritems():
       sum_s[k]=sum(v)
   print("total mark%s"%sum_s)
def avg():
   avg_s={}
   for k,v in student_details.iteritems():
       avg_s[k]=sum(v)/len(v)
   print("average mark%s"%avg_s)
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
avg()
