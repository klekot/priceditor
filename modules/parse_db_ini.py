def parse_db_ini(db_ini_file):
    with open(db_ini_file, 'r') as db_ini:
        db_set_arr = [s for s in db_ini.read().split('\n')]
    def_hostname   = db_set_arr[6]
    def_database   = db_set_arr[7]
    def_db_user    = db_set_arr[8]
    def_db_pass    = db_set_arr[9]
    hostname       = db_set_arr[13]
    database       = db_set_arr[14]
    db_user        = db_set_arr[15]
    db_pass        = db_set_arr[16]
    
    return def_hostname, def_database, def_db_user, def_db_pass, \
           hostname, database, db_user, db_pass