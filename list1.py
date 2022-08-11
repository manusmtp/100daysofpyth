#!/usr/bin/env python3

with open('README.MD','r') as p:
    data = p.read()

listdata =  data.split()
 
print("printing the file in reverse")
try:

   while(len(listdata) >= 0):
       print(listdata.pop().upper(),end=" ")

except:
    print("")


