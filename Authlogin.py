import sqlite3
conn = sqlite3.connect('main.db') 
cursour = conn.cursor()
    
cursour.execute("CREATE TABLE IF NOT EXISTS login(username VARCHAR, password VARCHAR)")

cursour.execute("INSERT INTO login VALUES('Admin', 'tennis')")
conn.commit()
def singup():
    
    cursour.execute('CREATE TABLE IF NOT EXISTS malli(name TEXT)')
    
singup()