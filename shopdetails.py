#sqlite

import sqlite3

con=sqlite3.connect('shop.db')
#con.excute('create table customer(customer_id int primary key,name varchar(20),place varchar(20)'))
#
#con.execute("""create table Order_details(order_id int primary key,
# c_id int,
# product varchar(20),
# price int,
# foreign key (c_id) references customer(customer_id))""")

con.execute('insert into customer values(1,"john","ekm")')
con.execute('insert into customer values(2,"smith","tvm")')
con.execute('insert into customer values(3,"smith","kollam")')
con.execute('insert into order_details values(101,1,"laptop","37000")')
con.execute('insert into order_details  values(102,3,"watch","10000")')
con.execute('insert into order_details values(103,1,"mobile","25000")')
con.commit()
print("created two tables successfully")
print("INNER JOIN")
#Reads only matching records based on common field
k=con.execute('select * from customer inner join Order_details on cuzstomer.customer_id=order_details.c_id')
print(k.fetchall())
k=con.execute('select customer_id,product,price from customer inner join Order_details on customer.customer_id=Order_details')
print(k.fetchall())
