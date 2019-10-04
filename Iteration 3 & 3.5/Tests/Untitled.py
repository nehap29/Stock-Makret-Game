import sqlite3
conn = sqlite3.connect('stock.db')
c = conn.cursor()
username = 'clara'
command = ("SELECT * FROM user_info WHERE username = '"+ username +"'")
c.execute(command)
ID = c.fetchall()
print(ID)
