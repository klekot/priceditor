import mysql.connector
from _codecs import encode

class DB_Object():
    def __init__(self, hostname, database, db_user, db_pass):
        self.hostname  = hostname
        self.database  = database
        self.db_user   = db_user
        self.db_pass   = db_pass
    
    def fetchone(self, db_request):
        conn = mysql.connector.connect(host=self.hostname, database=self.database, user=self.db_user, password=self.db_pass)
        cursor = conn.cursor()
        cursor.execute(db_request)
        result = cursor.fetchone()
        return result
        cursor.close()
        conn.close()

if __name__ == '__main__':
    hostname   = 'localhost'
    database   = 'poliinfo_bitrix'
    db_user    = 'poliinfo_bitrix'
    db_pass    = 'Y2Gd75q'
    db_request = "select * from `b_iblock_element`where `NAME` = 'TPW230VSN4X'"
    db = DB_Object(hostname, database, db_user, db_pass)
    print db.fetchone(db_request)

    