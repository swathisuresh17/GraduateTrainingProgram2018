-- ProblemSet<No.00>, july <25> <2018>
-- Submission by <swathi.b.suresh@accenture.com> 

1./*Select the Employee with the top three salary*/

select name, salary from employee where salary>=
   (select max(salary) from employee where salary<
     (select max(salary) from employee where salary<
      (select max(salary) from employee)))order by salary desc;

record count=3

2./*Select the Employee with the least salary*/

select * from employee where salary<=(select min(salary) from employee);

record count=1

3./*Select the Employee who does not have a manager in the department table*/

select e_id,name from employee where managerid not in(select a.e_id  from employee a join dept b on a.name=b.depmanager);

record count=4

4./*Select the Employee who is also a Manager*/

select a.e_id,a.name,a.managerid from employee a join dept b on b.depmanager=a.name;

record count=4

5./*Select the Empolyee who is a Manager and has least salary*/

select e_id,name,min(salary)from employee where salary in(select a.salary from employee a join dept b on a.name=b.depmanager);

record count=1

6./*Select the total number of Employees in Communications departments*/

select count(*) from employee group by dep_id having dep_id='d02';

record count=1

7./*Select the Employee in Finance Department who has the top salary*/

select e_id,max(salary) from employee where salary in(select a.salary from employee a join dept b on a.dep_id=b.dep_id and depname='finance');

record count=1

8./*Select the Employee in product depatment who has the least salary*/

select e_id,min(salary) from employee where salary in(select a.salary from employee a join dept b on a.dep_id=b.dep_id and depname='products');

record count=1

9./*Select the count of Empolyees in Health with maximum salary*/

select count(salary) from employee where salary in (select max(salary) from employee where salary in(select a.salary from employee a join dept b on a.dep_id=b.dep_id and depname='health'));

record count=1

10. /*Select the Employees who report to Natasha Stevens*/

select e_id,name from employee where managerid=(select e_id  from employee a join dept b on a.name=b.depmanager and name='natansha stevens');

record count=2

11./*Display the Employee name,Employee count,Dep name,Dept manager in the Health department*/

select a.name,b.depname,b.depmanager from employee a join dept b on a.dep_id=b.dep_id and depname='health';

record count=6

12./*Display the Department id,Employee ids and Manager ids for the Communications department */

select a.e_id,a.managerid,b.dep_id from employee a join dept b on a.dep_id=b.dep_id and depname='communications';

record count=6

13./*Select the Average Expenses for Each dept with Dept id and Dept name*/

select avg(e.salary),e.dept_id,d.depname from employee e inner join dept d on e.dept_id=d.dept_id group by d.depname order by e.dept_id;

record count=5

14. /*Select the total expense for the department finance*/

select sum(a.salary) from employee  a join dept b on a.dep_id=b.dep_id and depname='finance';

reord count=1

15./*Select the department which spends the least with Dept id and Dept manager name*/

select min(salary),dep_id,depname from(select sum(a.salary)as salary,a.dep_id,b.depname from employee a join dept b on a.dep_id=b.dep_id group by depname);

record count=1

16./*Select the count of Employees in each department*/

select count(e_id),dep_id from employee group by dep_id order by dep_id;

record count=5

17./*Select the count of Employees in each department having salary >10000*/

select count(e_id),dep_id from employee where salary>10000 group by dep_id order by dep_id;

record count=5

18./*Select the total number of Employees in Dept id D04*/

select count(e_id) from employee where dep_id='D04';

record count=2

19./*Select all department details of the Department with Maximum Employees*/

select dep_id,depmanager,max(e_id)from (select b.dep_id,b.depmanager,count(a.e_id)as e_id from dept b join employee a on a.dep_id=b.dep_id group by b.dep_id);

 record count=1
 
 20./*Select the Employees who has Tim Cook as their manager*/
 
 select e_id,name,salary from (select a.e_id as e_id,a.name as name,a.salary as salary from employee a join dept b on a.dep_id=b.dep_id and b.depmanager='tim cook');
 
 record count=0
 
