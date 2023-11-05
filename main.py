from aplication import Aplication
from data_base import __init__db,Actions
import sqlite3
if __name__ =='__main__':
    with sqlite3.connect('budget.db') as database:
        
        cursor=database.cursor()
        __init__db(cursor)
        database.commit()
        temp=Actions(database)
        main=Aplication(Actions(database))
        main.main()



  