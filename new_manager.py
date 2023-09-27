#!/usr/bin/python

#### Description ####
# take all the files from the source device and calculate session size
# check target device if there is enough space to copy all files
# if not all files can be copied try to copy as many folders as possible
# copy or move files
# add file info to DB
# update session and device tables at the end
#### /desc ####


# importing custom functions
from debugging import *
from functions import *

# importing sys libs
import dotenv
from os import getenv

# argparse

## program call
# filemgr.py [OPTIONS] SOURCE TARGET

## OPTIONS
#
# -D/ --database ARG    pointer to database file, the default is ./files.sqlite
# -m/ --move    move files to target i.e. delete from source after successful copy
# -k/ --keep-duplicates write duplicates instead of linking them - especially useful if the first copy is on a different target device
#                       default behavior is to link duplicates or create a text file with a pointer to the first copy of the file

## Parameters
#
# SOURCE: path from which to copy files from
# TARGET: path to which to copy files to


# setting default options
DATABASE = "./files.sqlite"
VERBOSE = 0
MOVE = 0
KEEPDUPLICATES = 0
# import .env parameters




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
# file db: DB with infos for file in TARGET

# get file DB from user or config

#  res=None
#  db=None
#  while not (res):
#    DATABASE = DATABASE if not db else db
#    usrInput = input("Do you want to use this database: " + cols.OKBLUE + DATABASE + cols.ENDC + "(y)es, no ")
#    usrInput = str(usrInput[0]).lower()
#    match usrInput:
#      case "y":
#          print_out("yay")
#          res = 1
#      case _:
#          db = input("Please provide a valid database file: ")

# test if file DB exists or needs to be created

## create file DB if necessary

### create tables in file DB

### table checksums
# |id|checksum|date added|
# checksum: string sha256
# date added: date time
#
dbCreate = {} # initalizing dict

dbCreate['checksums'] = 'CREATE TABLE "checksums" ( \
"id" INTEGER UNIQUE, \
"checksum" TEXT NOT NULL, \
"date_added" INTEGER DEFAULT 0, \
PRIMARY KEY("id" AUTOINCREMENT) \
 );'


### table file info
# |id|checksum_id|file name|file path|mime type id|file size|duplicate|duplicate id|target device id|session id|
# file name: string with extension
# file path: string, relative path
# file size: int in Byte
# duplicate: int 0=False, 1=True
# checksum id: foreign key
# mime-type id: foreign key
# session id: foreign key
# target device id: foreign key
#
dbCreate['file_info'] = 'CREATE TABLE "file_info" ( \
  "id" INTEGER UNIQUE, \
  "file_name" TEXT NOT NULL, \
  "file_path" TEXT NOT NULL, \
  "file_size" INTEGER DEFAULT 0, \
  "duplicate" INTEGER DEFAULT 0, \
  "fk_checksums" INTEGER, \
  "fk_devices" INTEGER, \
  "fk_mime-types" INTEGER, \
  "fk_sessions" INTEGER, \
  PRIMARY KEY("id" AUTOINCREMENT) \
 );'
### table device
# |id|device serial|space used|size|space free|
# device serial: string
# space used: int in MByte
# size: int in MByte
# space free: int in MByte

dbCreate['devices'] = 'CREATE TABLE "devices" (\
  "id" INTEGER UNIQUE,\
  "dev_serial" TEXT NOT NULL,\
  "size" INTEGER DEFAULT 0,\
  "space_used" INTEGER DEFAULT 0,\
  "space_free" INTEGER DEFAULT 0,\
  PRIMARY KEY("id" AUTOINCREMENT)\
 );'

### table MIME type
# |id|type name|type category|
# type name: string
# type category: string

dbCreate['mime_types'] = 'CREATE TABLE "mime_types" (\
  "id" INTEGER UNIQUE,\
  "name" TEXT UNIQUE,\
  "category" TEXT,\
  PRIMARY KEY("id" AUTOINCREMENT)\
 );'

### table sessions
# |id|start|ended|source device id|target device id|size|size copied|size freeed|
# start: date time
# ended: date time
# source device id: foreign key
# size: int in MByte
# size copied: int in MByte
# size freeed: int in MByte
# length: int in seconds
# user: foreign key

dbCreate['sessions'] = 'CREATE TABLE "sessions" (\
  "id" INTEGER UNIQUE,\
  "starting_time" INTEGER DEFAULT 0,\
  "ending_time" INTEGER DEFAULT 0,\
  "size_copied" INTEGER DEFAULT 0,\
  "size_freed" INTEGER DEFAULT 0,\
  "length" INTEGER DEFAULT 0,\
  "fk_users" INTEGER,\
  "fk_devices" INTEGER,\
  PRIMARY KEY("id" AUTOINCREMENT)\
 );'

### table user
# |id|name|
# name: string

dbCreate['users'] = 'CREATE TABLE "users" (\
  "id" INTEGER UNIQUE,\
  "username" TEXT UNIQUE,\
  "email" TEXT,\
  "password" TEXT,\
  PRIMARY KEY("id" AUTOINCREMENT)\
 );'

print(dbCreate['users'])
### test file DB for write and read operations

#---------#

# get file path from user or argparse

# check if file path exists and can be accessed

#---------#

# get current user by whoami or other means

# calculate session size via du -h of source path

# estimate session length and display to user - that can be used to display a percentage as well

# if more than one target is specified get all free space and compare session size to that

# advice user that not all files can be copied if the session size is larger than the target free space

# add session info to DB

## table device (if it is not in DB)
## serial no
## size in Mbyte
## space used in MByte
## space free in MByte

## table session
## - start time
## - end time
## - source device id
## - size = 0
## - size copied = 0
## - size freeed = 0
## - length = 0
## - user id

#---------#

# get all files in file path

# loop over files

## get file name, file path without root path, file size, MIME type

## get checksum of file

## check if checksum is already in DB

### NO: copy file to target

### NO: create checksum of copied file

### NO: Checksum Match: delete file from source if mode is move

### NO: add infos to DB,
### table checksum:
### - checksum
### - datetime

### table file info
### - file name
### - file path
### - file size in Byte
### - checksum id
### - device id
### - duplicate = 0
### - mime type id
### - session id of current session
### - target device id

### table device id (if doesn't exist):
### - device serial

### table mime type (if mime type new:
### - name
### - category

### table session
### - increment size
### - increment size copied/freeed

###--------###

### YES: do not copy to target

### TRUE: add info DB

### table file info
### - file name
### - file path
### - file size in Byte
### - duplicate = 1
### - checksum id
### - device id
### - mime type id
### - session id of current session
### - target device id

### table device id (if doesn't exist):
### - device serial

### table session
### - increment size
### - increment size copied/freeed

###--------###
##--------##
#--------#


# close session by updating table session
## - ended
## - length

# print summary
