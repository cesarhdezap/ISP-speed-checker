from Database import Database
from SpeedRegistry import SpeedRegistry

databaseInfo = Database("", "", "", "", "")

sr = SpeedRegistry(databaseInfo)
sr.getInternetSpeed()
sr.save_to_database()
