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
  linesFromFile = get_lines_from_file(msgDatabase, "1x00001")
  print(linesFromFile)

  # search for string in file

  # get largest number and increment by 1

  # get text for message from user

  # print details for user to acknowledge

  # add to file and report back to user

#  linesFromFile = get_lines_from_file(msgDatabase, "3x")

 # print(linesFromFile)


    #debugging("3x00001")
