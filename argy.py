#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="name of the person")
parser.add_argument('-n','--name',metavar='name',default='Word',help='name to greet')
args = parser.parse_args()
print('Hello, ' + args.name + '!')
