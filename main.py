#!/usr/bin/python

""" already import os.path as path, argparse"""
from setup import *
from ./lib/db import *

""" import functions # individual functions for this project """
import hashlib
import sqlite3
import dotenv
from os import getenv



if __name__ == "__main__":

  # Load the environment variables from the .env file
  dotenv.load_dotenv()

  """ GETTING DATABASE """
  # Get Database Pointer from .env File
  DATABASE = getenv("DATABASE")
  # Override anything with Argument provided by user
  args = parse_args()
  if args.database:
    DATABASE = args.database

  """ Get Database from user"""
  while not (path.exists(DATABASE)):
    DATABASE = input("Please provide a valid path and name of the database file: ")

  debugging("3x00001", DATABASE)
  """ / GETTING DATABASE """


  exit(0)


""" functions begin """





""" ========== functions end """


def processFiles():

  if getdb(database_name) > 0:
    """ If the database file doesn't exist ask the user to create it """
    msg = "The specified database does not exist or can't be accessed: " + database_name + " Do you want to create it (y)es|no? "
    usr_input = input(msg)
    create_database(database_name) if usr_input[:1].lower() == "y" else exit()
  #end if getdb...

  """ - open databse connection ie. initializing DB """
  conn = create_connection(database_name)
  cnx = conn[0]
  crs = conn[1]

  # Iterate over all of the files in the given folder and subfolders
  for root, dirs, files in os.walk(folder_path):
    for file in files:
      # Calculate the sha256 checksum of the file
      checksum = hashlib.sha256(open(os.path.join(root, file), 'rb').read()).hexdigest()
      with open(os.path.join(root, file), "rb") as f:
        filesize = os.fstat(f.fileno()).st_size


      # Check if the checksum exists in the database
      crs.execute('SELECT * FROM checksums WHERE checksum = ?', (checksum,))
      row = crs.fetchone()

      # If the checksum does not exist in the database, store it
      if row is None:
        crs.execute('INSERT INTO checksums (filename, checksum, is_duplicate, filepath, filesize) VALUES (?, ?, 1, ?, ?)', (file, checksum, os.path.join(root, file), filesize))

      # Otherwise, mark the file as a duplicate
      else:
     #   # Get the index of the existing row
     #   index = row[4]

     #   # Get the list of duplicate files
     #   duplicates = row[5]

     #   # Add the current file to the list of duplicates
     #   duplicates += ", " + file

        # Update the row in the database
     #   crs.execute('UPDATE checksums SET is_duplicate = 1, filepath = ?, index = ?, duplicates = ? WHERE checksum = ?', (os.path.join(root, file), index + 1, duplicates, checksum))
        crs.execute('UPDATE checksums SET is_duplicate = 1, filepath = ? WHERE checksum = ?', (os.path.join(root, file), checksum))
        crs.execute('INSERT INTO checksums (filename, checksum, is_duplicate, filepath, filesize) VALUES (?, ?, 1, ?, ?)', (file, checksum, os.path.join(root, file), filesize))

  # Commit the changes to the database
  cnx.commit()

  # Close the connection to the database
  cnx.close()

  # Print a message indicating that the task is complete
  print("The task is complete.")

def getData ():
  database_name = input("Enter the name of the SQLite database to store the checksums in: ")

  if getdb(database_name) > 0:
    """ If the database file doesn't exist ask the user to create it """
    msg = "The specified database does not exist or can't be accessed: " + database_name + "Aborting..."
    exit()

  """ - open databse connection ie. initializing DB """
  conn = create_connection(database_name)
  cnx = conn[0]
  crs = conn[1]
  crs.execute('SELECT * FROM checksums WHERE checksum = "e6e1513b6dcd023216f5e0a915e9b3b1bcd037bcb9475cc978fb3ed3e3a50253"')
  rows = crs.fetchall()



  for row in rows:
    print("Filename: {} | Filesize: {} | Duplicate: {}".format(row[0], row[1], row[2]))



  # Close the connection to the database
  cnx.close()

def parseArguments():
  """ Check parameters and arguments for script
      - ask for database and folder path if they have not been specified
      - check for sanity ie. do they exist and are they accessible
  """
  db = ""
  folder_path = ""

  # allowed options
  opts = ["-h", "--help",
          "-f", "--folder",
          "-D", "--database"
          ]
  # Get the command line arguments
  args = [arg for arg in sys.argv[1:] if arg.startswith("-")]
  all_args = sys.argv[1:]

  # define Help message
  helpMsg = "Usage: script.py [options]\n"
  helpMsg += "Options:\n"
  helpMsg += "\t-h, --help\tPrint this help message and exit.\n"
  helpMsg += "\t-f FOLDER, --folder=FOLDER\n"
  helpMsg += "\t\tProcess files in this DIRECTORY.\n"
  helpMsg += "\t-D FILE, --DATABASE=FILE\n"
  helpMsg += "\t\tUse this Database FILE."

  # Check if the `-h` option was specified
  if "-h" in args or "--help" in args:
    print("{}".format(helpMsg))
    exit()

  """
  going through options
  """
  # check if the arguments are in the allowed list otherwise
  for arg in args:
    if arg not in opts:
      print("Option: {} not in list.\n\n{}".format(arg,helpMsg))
      exit()


  if "-h" in args or "--help" in args:
    print("{}".format(msg))
    exit()

  # Check if the `c` option was specified
  if "-f" in args or "--folder" in args:
    # Change the current working directory
    folder = all_args[all_args.index("-f") + 1] if "-f" in all_args else all_args[all_args.index("--folder") + 1]
    print("-f option parsing")

  # Check if the `d` option was specified
  if "-D" in args or "--database" in args:
    # Delete the file or directory
    db = all_args[all_args.index("-D") + 1] if "-D" in all_args else all_args[all_args.index("--database") + 1]

  """
  user did not specify parameters
  """
  if not folder_path:
  # Get the parameters from the user
    folder_path = input("Enter the path to the folder to be scanned: ")

  if not db:
    db = input("Enter the name of the SQLite database to store the checksums in: ")

  # ToDo
  # check if the database files exists and can be read/written to
  ret = getdb(db)
  print("db-res: ".format(db))

  # check if the folder_path exists and has files in it

  print("db: {} | folder: {}".format(db,folder_path))

def main ():

  """ parse arguments to script or get info from user at runtime """
  ret = parseArguments()

  print("ret {}".format(ret))



if __name__ == "__main__":
  main()
