#!/usr/bin/python

debug = False

from os import path

import argparse



"""Parses the command-line arguments."""
def parse_args():
  """
  Get parameters and arguments from call to script

  Returns:
    A list of arguments.
  """
  parser = argparse.ArgumentParser(description="A simple script to parse parameters.")

#  parser.add_argument('searchstring')           # positional argument
#  parser.add_argument('-v', '--verbose', action='store_true')  # on/off flag
  parser.add_argument('-v', '--verbose',
    help="Set verbosity level: 1 = only warnings, 2 = enable debug messages, 3 = show all messages",
    type=int,
    nargs='?',
    const=1)
  parser.add_argument(
    "-D",
    "--database",
    help="The database file with all responses. Default: debug.txt",
    type=str,
    default="./debug.txt")

  return parser.parse_args()


""" Colors for Terminal Output """
class cols:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

""" GET LINES FROM FILE """
def get_lines_from_file(file_path, string_to_find):
  """
  Gets all lines that include a specific string.

  Args:
    file_path: The path to the text file.
    string_to_find: The string to find.

  Returns:
    A list of strings containing all lines that include the specified string.
  """

  with open(file_path, "r") as file:
    lines = file.readlines()

    lines_that_include_string = []
    for line in lines:
      if string_to_find in line:
        lines_that_include_string.append(line)

  return lines_that_include_string

####
## print color coded message
####
def print_out(msg, code = "undefined"):

  match code[0]:
    case "1":
      print("[{0}ERROR{1}] {3} ({2})".format(cols.FAIL,cols.ENDC, code, msg))
    case "2":
      if (args.verbose > 0):
        print("[{0}WARNING{1}] {3} ({2})".format(cols.WARNING,cols.ENDC, code, msg))
    case "3":
      if (args.verbose > 1):
        print("[{0}DEBUG{1}] {2}".format(cols.OKBLUE,cols.ENDC, msg))
    case "5":
      if (args.verbose > 2):
        print("[{0}SUCCESS{1}] {2}".format(cols.OKGREEN,cols.ENDC, msg))
    case _:
      print("{0}{1}{2}".format(cols.OKCYAN, msg, cols.ENDC))
######

####
## DEBUGGING: show output to user
####
def debugging( debugString, additionalText = "" ,debugDB = "./lib/messages.txt" ):
  """
  Prints output to user.

  Args:
    debugString: code to search for in file to find correct line
    debugDB: database file with all the strings and codes

  Returns:
    Output to terminal

DEBUG CODES

0 = Regular Output, show text
1 = Error, always show code and text
2 = Warning, show code and text when verbose is set
3 = Debug, only text when verbose is set
5 = Success, show text when verbose is set
  """
  lang = "eng"

#  args = parse_args()
#  if args.lang:
#    lang = args.lang

  # check user parameters for sanity and ask user to provide new ones if they fail
  while not (debugString):
    debugString = input("Please provide a string to search for: ")

  while not (path.exists(debugDB)):
    debugDB = input("File does not exist. Please provide a new file: ")

  # get lines from file -- ideally there's is only one
  linesFromFile = get_lines_from_file(debugDB, debugString)

  if not (linesFromFile):
      print("[{0}WARNING{1}] Message could not displayed (2x0000)".format(cols.FAIL,cols.ENDC))
      return 1

  if (len(linesFromFile) > 1 ):
    for line in linesFromFile:
      if (line[-4:-1] == lang):
        lineAsList = line.split("|")
  else:
    lineAsList = linesFromFile[0].split("|")


  # if the addtional text needs to be added to the text
  if additionalText:
    lineAsList[1] = lineAsList[1] + " : " + additionalText

  print_out( lineAsList[1], lineAsList[0])
###### debugging

# always run parse_args automatically on import
args = parse_args()
