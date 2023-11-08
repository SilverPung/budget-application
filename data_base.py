import sqlite3 
def __init__db(db_cursor):
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS categories( id INTEGER PIMARY KEY , name TEXT)''')
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS items(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT,
                       category_id INTEGER,
                       date TEXT,
                    amount REAL,
                       FOREIGN KEY (category_id) REFERENCES categories(id))''')
class Actions:
    def __init__(self,connection) -> None:
        self.connection=connection
        self.cursor=connection.cursor()
    def add_item(self,name:str,category:str,date:str,value:int):
        category_id=int(self.add_or_get_category(category))
        self.cursor.execute('INSERT INTO items VALUES(null,?,?,?,?)',(name.capitalize(),category_id,date,value))
    def add_or_get_category(self,name):
        self.cursor.execute('SELECT id FROM categories WHERE name=?',(name.capitalize(),))
        category_id=self.cursor.fetchone()
        if category_id==None:
            self.cursor.execute('SELECT COUNT(id) FROM categories')
            count=self.cursor.fetchone()[0]+1
            self.cursor.execute('INSERT INTO categories VALUES(?,?)',(count,name.capitalize()))
            self.connection.commit()
            return count
        category_id=category_id[0]
        return category_id
    def delete_item(self,id):
        self.cursor.execute('DELETE FROM items WHERE id=?',(id,))
    def list_items(self):
        return(self.cursor.execute('SELECT * from items'))
    def stats(self):
        self.cursor.execute('SELECT SUM(amount) from items')
        return self.cursor.fetchone()