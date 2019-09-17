#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Haydar with instructor help"


import sys
import argparse

def to_upper(string):
    return string.upper()
def to_lower(string):
    return string.lower()
def to_title(string):
    return string.title()


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(description='Perform transformation on input text.')
    parser.add_argument('-u','--upper', action='store_true', help='convert text to uppercase')
    parser.add_argument('-l','--lower', action='store_true', help='convert text to lowercase')
    parser.add_argument('-t','--title', action='store_true', help='convert text to titlecase')
    parser.add_argument('text', help='text to be manipulated')
    return parser

def main(args):
    """Implementation of echo"""
    text = args.text
    if args.upper:
        text = to_upper(text)
    if args.lower:
        text = to_lower(text)
    if args.title:
        text = to_title(text)
    return text


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    result = main(args)
    print(result)
