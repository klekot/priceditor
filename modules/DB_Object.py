import mysql.connector

class DB_Object():
    def __init__(self, hostname, database, db_user, db_pass):
        self.hostname  = hostname
        self.database  = database
        self.db_user   = db_user
        self.db_pass   = db_pass
    
    def write(self, db_request):
        conn = mysql.connector.connect(host=self.hostname, database=self.database, user=self.db_user, password=self.db_pass)
        cursor = conn.cursor()
        cursor.execute(db_request)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

if __name__ == '__main__':
    hostname   = 'localhost'
    database   = 'poliinfo_bitrix'
    db_user    = 'poliinfo_bitrix'
    db_pass    = 'Y2Gd75q'
    new_text   = 'new!!!!!!!!!!!!!!!'
    item_name  = 'TPW230VSN4X'
    db_request = "update `b_iblock_element` set `DETAIL_TEXT`='%s' where `NAME`='%s'" % (new_text, item_name)
    db = DB_Object(hostname, database, db_user, db_pass)
    db_request = "select `DETAIL_TEXT` from `b_iblock_element`where `NAME` = '%s'" % item_name
    print db.write(db_request)

    