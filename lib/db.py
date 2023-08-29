#!/usr/bin/python

def create_connection(db_file):
  """ create a database connection to a SQLite database and return connection and cursor """
  conn = None
  try:
    cnx = sqlite3.connect(db_file)
    crs = cnx.cursor()
    debugging(" "+sqlite3.version)
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
