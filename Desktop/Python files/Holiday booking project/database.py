import sqlite3


#create database connection
def connect():
    conn= sqlite3.connect("order.db")
    cur = conn.cursor()
    return conn, cur
    

#Create table#
def create_order_tbl():
    conn,cur= connect()
    cur.execute('''CREATE TABLE IF NOT EXISTS orders(
                orderId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                items TEXT NOT NULL, 
                price FLOAT NOT NULL,
                quantity INTEGER NOT NULL,
                total FLOAT NOT NULL)
                ''')
    conn.commit()
    conn.close()
    
def create_staff_tbl():
    conn,cur = connect()
    cur.execute('''CREATE TABLE IF NOT EXISTS customer(
                no_passengers INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL ,
                itinerary TEXT NOT NULL,
                date_time TEXT NOT NULL)
                ''')
    conn.commit()
    conn.close()
    
    
#inert order                
def insert_order(no_passengers, itinerary, date_time ): 
    conn,cur= connect()
    an_order = (item, unit_price, qty, total_cost)
    cur.execute('''INSERT INTO orders(items,price,quantity,total) VALUES (?, ?, ?, ?)''',  an_order)
    conn.commit()
    conn.close()


def select_all_order():
    conn,cur = connect()
    alist =cur.execute("SELECT * FROM orders")
    print("no_passengers, itinerary, date_time")
    for row in alist:
       print("{}\t\t\t{}\t\t{}\t\t\t{}\t{}".format(row[0],row[1],row[2], row[3], row[4]))
    conn.close()
    
    
         
create_order_tbl() 
           
                
select_all_order()
