#!/usr/bin/python

def debugging(msg):
  if debug == 1:
    print("{}".format(msg))

def getdb(database_name):
  """ Just a qucik function to check if a database file exists and can be read """
  if os.path.exists(database_name):
    return 0
  # return 1 if the database doesn't exist or can't be accessed
  return 1

def create_connection(db_file):
  """ create a database connection to a SQLite database and return connection and cursor """
  conn = None
  try:
    cnx = sqlite3.connect(db_file)
    crs = cnx.cursor()
    debugging("SQL connection successful: "+sqlite3.version)
  except Error as e:
    debugging(e)
  return [cnx, crs]

def create_database (db_file):
  """ create the db """
  """ - open databse connection ie. initializing DB """
  conn = create_connection(db_file)
  cnx = conn[0]
  crs = conn[1]
  """ - create table in DB """
  debugging("creating table in db")
  # The database does not exist, so create it
  crs.execute('''CREATE TABLE checksums (
    filename TEXT,
    checksum TEXT,
    is_duplicate INTEGER,
    filepath TEXT,
    filesize INTEGER
    )''')
  crs.close()
