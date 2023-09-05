#!/usr/bin/python

import argparse

def parse_script_args():
#  Get parameters and arguments from call to script
#
#  Returns:
#    A list of arguments.

  parser = argparse.ArgumentParser(description="A simple script to parse parameters.", formatter_class=argparse.RawTextHelpFormatter)

  parser.add_argument('msgCode', nargs='?', type=int, choices=range(0,6) ,default=0,
    help="Provide a message code:\n0 = general\n1 = error\n2 = warning\n3 = debug\n\n5 = success\nDefault = 0")
  return parser.parse_args()

#### Start Script
if __name__ == "__main__":

  args = parse_script_args()
  args.msgCode
