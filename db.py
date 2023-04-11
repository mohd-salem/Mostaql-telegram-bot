from data import * 
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor() 
# c.execute('''CREATE TABLE JOBS(title TEXT,budget TEXT)''')

c.execute('''SELECT title FROM JOBS ORDER BY ROWID DESC''')
result = c.fetchone()[0] 
if (result != title):
    c.execute('''INSERT INTO JOBS VALUES(?,?)''',(title, budget))
    conn.commit()
    new_record = True
    print('new record inserted')
    

else:
    print('No new records')
    new_record = False
  
c.execute('''SELECT title FROM JOBS ORDER BY ROWID DESC''')
lastresult = c.fetchone()[0]
print(lastresult)