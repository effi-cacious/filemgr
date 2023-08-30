#!/usr/bin/python

""" already import os.path as path"""
#from setup import *

import argparse

def parse_script_args():
#  Get parameters and arguments from call to script
#
#  Returns:
#    A list of arguments.

  parser = argparse.ArgumentParser(description="A simple script to parse parameters.", formatter_class=argparse.RawTextHelpFormatter)

  parser.add_argument('MESSAGE', nargs='?',
    help="The message to be stored in the message DB")
  parser.add_argument('-m', '--msgcode', nargs='?', type=int, choices=range(0,6) ,default=0,
    help="Provide a message code:\n0 = general\n1 = error\n2 = warning\n3 = debug\n\n5 = success\nDefault = 0")
  return parser.parse_args()

if __name__ == "__main__":

  args = parse_script_args()

  usrResponse = False
  # get infos from user
  while not usrResponse:

    match args.msgcode:
      case 1: codeMeaning="error"
      case 2: codeMeaning="warning"
      case 3: codeMeaning="debug"
      case 4: codeMeaning="success"
      case _: codeMeaning="undefined"

    print("Message Code: {0} i.e. {1}".format(args.msgcode, codeMeaning))
    if not args.MESSAGE:
      args.MESSAGE = input("Please type in your message text: \n")
    print("Your message:\n{0}".format(args.MESSAGE))
    usr = input("Are values correct? (y)es | no")

    if usr[0].lower() == "y":
      usrResponse = True

    s = set(["c","m","a"])

    usrInput = input("")


  # save infos to DB


  exit (0)
  #if args.code:
  #  usrCode = 1


#  msgDatabase = "./lib/messages.txt"
#
#  # check if file exists
#  if (path.exists(msgDatabase)):
#    try:
#      with open(msgDatabase, 'a') as f:
#          # file opened for writing. write to it here
#        debugging("5x00001")
#        pass
#    except IOError as x:
#      print_out ("error {0}.{1}".format(x.errno, x.strerror))
#  else:
#    debugging("1x00001")

  #  Get string from user
  while not usrCode:
    usrCode = input("Please provide a code: ")

  print("code: {0}".format(usrCode))

  exit(0)
  # check if the user provided a string with the script call
  # if not, get the code from the user as input

  # get codes from file
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
