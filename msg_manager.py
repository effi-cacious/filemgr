#!/usr/bin/python

""" already import os.path as path"""
#from setup import *

import argparse
from os import path
from debugging import *
from sys import stdout

debug = 0

def parse_script_args(ret="x"):
#  Get parameters and arguments from call to script
#
#  Returns:
#    A list of arguments.

  parser = argparse.ArgumentParser(description="A simple script to parse parameters.", formatter_class=argparse.RawTextHelpFormatter)

  parser.add_argument('MESSAGE', nargs='?',
    help="The message to be stored in the message DB")
  parser.add_argument('-m', '--msgcode', nargs='?', type=int, choices=range(0,6) ,default=0,
    help="Provide a message code:\n0 = general\n1 = error\n2 = warning\n3 = debug\n\n5 = success\nDefault = 0")
  if ret == "h":
    return parser.print_help()

  return parser.parse_args()

if __name__ == "__main__":

  args = parse_script_args()

  usrResponse = False
  # get infos from user
  while not usrResponse == "y":

    if usrResponse == "n":
      argsh = parse_script_args("h")
      print("\n\n{0}\n\n".format(argsh))
      usrCode = input("Please choose a message code (Default: {0} = {1}): ".format(args.msgcode, codeMeaning))
      usrMessage = input("Please change your message here (Default: {0} ): ".format(args.MESSAGE))

      if not usrCode == "" or usrCode in range (0,5,1):
        args.msgcode = int(usrCode)
      if not usrMessage == "":
        args.MESSAGE = usrMessage


    match args.msgcode:
      case 1: codeMeaning="error"
      case 2: codeMeaning="warning"
      case 3: codeMeaning="debug"
      case 4: codeMeaning="success"
      case _: codeMeaning="undefined"

    print_out("Message Code: {0} i.e. {1}".format(args.msgcode, codeMeaning), 9)
    if not args.MESSAGE:
      args.MESSAGE = input("Please type in your message text: \n")
    print_out("Your message:")
    print_out("{0}".format(args.MESSAGE), 9)
    usr = input("Are values correct? (y)es | no\t")

    if usr == "":
      usrResponse = "y"
    else:
      match usr[0].lower():
        case "y": usrResponse = "y"
        case "n": usrResponse = "n"
        case _: usrResponse = False


  # save infos to DB
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

  # get codes from file and increment highest code by one
  codes = []
  codeIdentLen = 5
  lang = "eng"
  linesFromFile = get_lines_from_file(msgDatabase, str(args.msgcode) + "x")
  for line in linesFromFile:
    line = line.split("|")
    codes.append(line[0])

  # get max code and increment by 1
  if not len(codes) == 0:
    maxCode = max(codes)
    maxCode = int(maxCode[-codeIdentLen:len(maxCode)])
    maxCode += 1
  else: maxCode = 1

  while len(str(maxCode)) < codeIdentLen:
    maxCode = "0" + str(maxCode)

  newCode = str(args.msgcode) + "x" + str(maxCode)
  line = newCode + "|" + args.MESSAGE + "|" + lang

  with open(msgDatabase, 'a') as f:
    if f.write(line + "\n"):
      print_out("New code in DB: " + newCode, 5)
    else:
      print_out("Trying to write to Message DB file(" + msgDatabase + "). Please check and try again.")
#    s = set(["c","m","a"])
  exit(0)

 #   usrInput = input("")




  # get codes from file

  # search for string in file


  # print details for user to acknowledge

  # add to file and report back to user

#  linesFromFile = get_lines_from_file(msgDatabase, "3x")

 # print(linesFromFile)


    #debugging("3x00001")
