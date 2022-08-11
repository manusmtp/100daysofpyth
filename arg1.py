#!/usr/bin/env python3

import argparse


def get_parse():
    """ get command-line arguments  """
    parser = argparse.ArgumentParser(description="manipulate the args",formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-pos','-p',metavar='int',type=str,help='enter a number')
    parser.parse_args()



if __name__ == '__main__':
    get_parse()
