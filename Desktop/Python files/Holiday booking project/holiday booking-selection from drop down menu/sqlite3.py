
#1. Import the library
import sqlite3


#2 . Get a connection to DB
conn = sqlite3.connect("customer.db")
cur = conn.cursor()

#3Use the Cursor to execute SQL queries
#4. Close the connection when done
def create_user_table():
    cur.execute('''CREATE TABLE IF NOT EXISTS user(
                    userId INT,
                    firstname TEXT,
                    lastname TEXT,
                    phonenumber TEXT,
                    email TEXT);'''
                    )
    conn.commit()
    conn.close


#3Use the Cursor to execute SQL queries
#4. Close the connection when done    
def insert_order():
    cur.execute("""INSERT INTO user(userid, firstname, lastname, phonenumber, email)
                VALUES('002', 'Mary', 'Collins', '07456111111', '01@gmail.co.uk');""")
    
    user2 = ('004', 'Ben', 'Lane', '222222222222', '02@gmail.co.uk')
    cur.execute("INSERT INTO user VALUES(?, ?, ?, ?,?);", user2)
    conn.commit()
    conn.close

#3Use the Cursor to execute SQL queries
#4. Close the connection when done    
def select_user():
    cur.execute("SELECT * FROM user;")
    result = cur.fetchall()
    print(result)


    
create_user_table()
insert_order()
select_user()
