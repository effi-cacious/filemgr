#!/usr/bin/python

from os import path
debug = False

# Colors for Terminal Output
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

class codes:
  STANDARD = [0,"standard"]
  ERROR = [1, "error"]
  WARNING = [2, "warning"]
  DEBUG = [3, "debug"]
  SUCCESS = [4, "success"]

####
## print color coded message
####
def print_out(msg, code = "unkown"):

  match str(code).lower():
    case "error": msg =  "[" + cols.FAIL + codes.ERROR[1] + cols.ENDC + "] " + str(msg)
    case "1": msg =  "[" + cols.FAIL + codes.ERROR[1] + cols.ENDC + "] " + str(msg)
    case "warning": msg = "[" + cols.WARNING + codes.WARNING[1] + cols.ENDC + "] " + str(msg)
    case "2": msg = "[" + cols.WARNING + codes.WARNING[1] + cols.ENDC + "] " + str(msg)
    case "debug": msg = "[" + cols.OKBLUE + codes.DEBUG[1] + cols.ENDC + "] " + str(msg)
    case "3": msg = "[" + cols.OKBLUE + codes.DEBUG[1] + cols.ENDC + "] " + str(msg)
    case "success": msg = "[" + cols.OKGREEN + codes.SUCCESS[1] + cols.ENDC + "] " + str(msg)
    case "4": msg = "[" + cols.OKGREEN + codes.SUCCESS[1] + cols.ENDC + "] " + str(msg)
    case "system": msg = cols.OKCYAN + str(msg) + cols.ENDC
    case "9": msg = cols.OKCYAN + str(msg) + cols.ENDC
    case _: msg = cols.ENDC + str(msg)

  print(msg)
######

# function to get lines from file
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
# function to print debugging message

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
      print_out("Message could not displayed (1x00000)", 1)
      return 1

  # assuming duplicate codes only exist because of different languages
  # get the language version that is defined in lang
  if (len(linesFromFile) > 1 ):
    for line in linesFromFile:
      if (line[-4:-1] == lang):
        lineAsList = line.split("|")
  else:
    lineAsList = linesFromFile[0].split("|")


  # if the addtional text needs to be added to the text
  if additionalText:
    lineAsList[1] = lineAsList[1] + " : " + additionalText
  match lineAsList[0][0]:
    case 1: lineAsList[1] = lineAsList[1] + "(" + lineAsList[0] + ")"
    case 2: lineAsList[1] = lineAsList[1] + "(" + lineAsList[0] + ")"
    case _: lineAsList[1] = lineAsList[1]

  print_out( lineAsList[1], lineAsList[0][0])
###### debugging
