#!/usr/bin/python

#### Description ####
# take all the files from the source device and calculate session size
# check target device if there is enough space to copy all files
# if not all files can be copied try to copy as many folders as possible
# copy or move files
# add file info to DB
# update session and device tables at the end
#### /desc ####


# import debugging

# argparse

# Source: path from which to copy files from
# Target: path to which to copy files to
# Mode: copy (default) or move ie. deleting files after succesful copy from source
# file db: DB with infos for file in TARGET

# get file DB from user or config

# test if file DB exists or needs to be created

## create file DB if necessary

### create tables in file DB

### table checksum
# |id|checksum|date added|
# checksum: string sha256
# date added: date time

### table file info
# |id|checksum_id|file name|file path|mime type id|file size|duplicate|duplicate id|target device id|session id|
# checksum id: foreign key
# file name: string with extension
# file path: string, relative path
# mime-type id: foreign key
# file size: int in Byte
# duplicate: int 0=False, 1=True
# duplicate id: foreign key
# target device id: foreign key
# session id: foreign key

### table device
# |id|device serial|space used|size|space free|
# device serial: string
# space used: int in MByte
# size: int in MByte
# space free: int in MByte

### table MIME type
# |id|type name|type category|
# type name: string
# type category: string

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

### table user
# |id|name|
# name: string

### test file DB for write and read operations

#---------#

# get file path from user or argparse

# check if file path exists and can be accessed

#---------#

# get current user by whoamior other means

# calculate session size via du -h of source path

# estimate session length and display to user

# if more than one target is specified get all free space and compare session size to that

# advice user that not all files can be copied if the session size is larger than the target free space

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

### table mime type (if mime type new:
### - name
### - category

### table device id (if doesn't exist):
### - device serial

### table session
### - increment size
### - increment size copied/freeed

### table file info
### - file name
### - file path
### - device id
### - duplicate = FALSE
### - mime type
### - file size
### - target device id
### -

###--------###

### YES: do not copy to target

### YES: check if file name already exists

#### TRUE: add info DB - file path path, device id, mark as duplicate, duplicate id from already existing file
