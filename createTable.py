import psycopg2


def createTable(conn):
    cur = conn.cursor()
    cur.execute(
        '''CREATE TABLE INTERNETSPEEDDATA
        (ID SERIAL PRIMARY KEY NOT NULL,
        TIME TEXT NOT NULL,
        DOWNLOAD REAL NOT NULL,
        UPLOAD REAL NOT NULL);''')
    print("Table created successfully")
    conn.commit()
    conn.close()
