-- ProblemSet<No.00>, july <31> <2018>
-- Submission by <swathi.b.suresh@accenture.com> 


1./*List full details of all hotels.*/

select h.hotelno,h.name,h.city,r.roomsno,r.type,r.price from hotel h join rooms r on r.hotelno=h.hotelno;

  record count=(12)

2./*List full details of all hotels in New York.*/

select h.hotelno,h.name,h.city,r.roomsno,r.type,r.price from hotel h join rooms r on r.hotelno=h.hotelno and city='newyork'; 

record count=(4)

3./*List the names and cities of all guests, ordered according to their cities.*/

select gname,city from guest order by city; 

record count=(6)

4./*List all details for non-smoking rooms in ascending order of price.*/

select h.hotelno,h.name,h.city,r.price,r.roomsno from hotel h join rooms r on r.hotelno=h.hotelno where r.type='n' order by price; 
 
 record count=(8)

5./*List the number of hotels there are.*/

select count(*) as "Number Of Hotels" from hotel; 

record count=(1)

6./*List the cities in which guests live. Each city should be listed only once*/

select distinct(city) from guest;

record count=(4)

7./*List the average price of a room.*/

select avg(price) as "Average Price Of a Room" from rooms; 

record count=(1)
 
8./*List hotel names, their room numbers, and the type of that room.List the hotel names, booking dates, and room numbers for all hotels in New York.*/

select h.name,r.roomsno,r.type from hotel h join rooms r on r.hotelno=h.hotelno;

record count=(12)
 
 9./*List the hotel names, booking dates, and room numbers for all hotels in New York.*/

select name,date_from,date_to,roomsno from hotel  join book  on book.hotelno=hotel.hotelno where city='newyork';

record count=(3)

10./*What is the number of bookings that started in the month of September?*/

SELECT count(*) FROM book where date_from between '1999-09-01' and '1999-09-30';

record count=(1)

11./*List the names and cities of guests who began a stay in New York in August.*/

select g.gname,g.city from guest g join book b on g.guestno=b.guestno join hotel h on h.hotelno=b.hotelno where  h.city='newyork'  and b.date_from between '1999-08-01' and '1999-08-31' ;

record count=(2) 

12./*List the hotel names and room numbers of any hotel rooms that have not been booked.*/

select h.name,r.roomsno from rooms r join hotel h on h.hotelno=r.hotelno where roomsno not in (select roomsno from book);
record count=(5)

13./*List the hotel name and city of the hotel with the highest priced room.*/

select h.name,h.city from hotel h join rooms r  on h.hotelno=r.hotelno where price=(select max(price) from rooms) 

record count=(1)

14./*List hotel names, room numbers, cities, and prices for hotels that have rooms with prices lower than the lowest priced room in a Boston hotel.*/

select a.city,a.name,b.roomsno,b.price from hotel a   inner join rooms b on a.hotelno=b.hotelno where price< (select min(r.price)  from rooms r join hotel h on h.hotelno=r.hotelno where h.city='boston') ;
record count=(2)

15./*List the average price of a room grouped by city.*/

select avg(r.price) from rooms r join hotel h on h.hotelno=r.hotelno group by city;

record count=(3)
 
