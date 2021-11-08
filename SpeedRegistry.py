import psycopg2
import speedtest
import datetime
import logging
from Database import Database


class SpeedRegistry:
    def __init__(self, databaseInfo: Database):
        self.id = 0
        self.download = 0
        self.upload = 0
        self.utcTime = 0
        self.floatPrecision = 4
        self.databaseInfo = databaseInfo

    def getInternetSpeed(self):
        print('Retrieving speed data...')
        try:
            st = speedtest.Speedtest()
            download = st.download()
            upload = st.upload()
            self.download = round(download, 4)
            self.upload = round(upload, 4)
            self.utcTime = datetime.datetime.now(datetime.timezone.utc)
            print("Download: {0}, Upload: {1}, Time: {2}".format(
                download, upload, self.utcTime))
        except(Exception) as error:
            logging.basicConfig(filename='app.log', level=logging.INFO)
            logging.error('Error occurred ' + str(error))
            print(error)

    def save_to_database(self):
        try:
            conn = psycopg2.connect(
                database=self.databaseInfo.database,
                user=self.databaseInfo.user,
                password=self.databaseInfo.password,
                host=self.databaseInfo.host,
                port=self.databaseInfo.port)
            print("Opened database successfully")

            cur = conn.cursor()
            print("Saving entry to database...")
            sql = """INSERT INTO INTERNETSPEEDDATA (TIME,DOWNLOAD,UPLOAD) VALUES (%s, %s, %s)"""
            cur.execute(sql, (self.utcTime, self.download, self.upload))

            conn.commit()
            print("Entry saved to database!")
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            logging.basicConfig(filename='app.log', level=logging.INFO)
            logging.error('Error occurred ' + str(error))
            print(error)
        finally:
            if conn is not None:
                conn.close()
