from csv2sqlite import convert
import sqlite3
import os

if __name__ == '__main__':
    dbpath = 'profile.db'
    if os.path.exists(dbpath):
        os.remove(dbpath)
    
    for table_name in ( 'bio', 'universities', 'education', 'groups' ):
        table = table_name
        fileobj = 'bio_assignment - %s.csv' % table_name
        convert(fileobj, dbpath, table)
        conn = sqlite3.connect(dbpath)
        c = conn.cursor()
        c.execute('select count(*) from %s' % table);
        row = c.next()
    #assert row[0] == 3, row
