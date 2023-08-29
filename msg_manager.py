#!/usr/bin/python

""" already import os.path as path, argparse"""
from setup import *



if __name__ == "__main__":



  msgDatabase = "./lib/messages.txt"

  # check if file exists
  if (path.exists(msgDatabase)):
    try:
      with open(msgDatabase, 'a') as f:
          # file opened for writing. write to it here
        debugging("5x00001")
        pass
    except IOError as x:
      print_out ("error {0}.{1}".format(x.errno, x.strerror))
  else:
    debugging("1x00001")

  #  Get string from user

  # check if the user provided a string with the script call
  # if not, get the code from the user as input
  
  get codes from file 
  codes = []
  linesFromFile = get_lines_from_file(msgDatabase, "1x")
  for line in linesFromFile:
    line = line.split("|")
    codes.append(line[0])

  # get max code and increment by 1
  maxCode = max(codes)
  maxCode = int(maxCode[-5:len(maxCode)])
  maxCode += 1
  print_out("Found line: " + str(maxCode))

  # search for string in file

  # get largest number and increment by 1

  # get text for message from user

  # print details for user to acknowledge

  # add to file and report back to user

#  linesFromFile = get_lines_from_file(msgDatabase, "3x")

 # print(linesFromFile)


    #debugging("3x00001")
