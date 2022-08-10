#!/usr/bin/env python3

import argparse
from datetime import datetime


now = datetime.now()
hour = int(now.strftime("%H"))
parser = argparse.ArgumentParser(description="name of the person")
parser.add_argument('-n','--name',metavar='name',default='Word',help='name to greet')
args = parser.parse_args()
if args.name != "Word":
    if hour >= 12 :
        print("Good Afternoon "+ args.name)
    elif hour >= 15:
        print("Good Evening "+ args.name)
    elif hour >= 19:
        print("Good Night "+ args.name)
    else: 
        print("Good Morning "+ args.name)

    
    
