#!/usr/bin/env python3

import os ,signal
import time

def pTime():

    try:
      #h,m,s = time.localtime().tm_hour,time.localtime().tm_min,time.localtime().tm_sec
      clear = lambda: os.system('clear')
      while 1:
        clear()
        print(f"HOUR:: "+ str(time.localtime().tm_hour)+"\nMINUTE:: "+str(time.localtime().tm_min) + "\nSECONDS:: "+str(time.localtime().tm_sec) )
    except KeyboardInterrupt:
         for line in os.popen("ps ax | grep maincheck.py  | grep -v grep"):
            fields = line.split()
             
            # extracting Process ID from the output
            pid = fields[0]
             
            # terminating process
            os.kill(int(pid), signal.SIGKILL) 


if __name__ == '__main__':
    pTime()
