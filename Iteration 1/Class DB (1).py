import sqlite3

conn = sqlite3.connect('stockmarket.db')

c = conn.cursor()

c.execute('SELECT * FROM user_info')
print(c.fetchone())
