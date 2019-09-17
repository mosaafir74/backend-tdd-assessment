#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess

# Your test case class goes here

class TestEcho(unittest.TestCase):
    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)
    def test_upper(self):
        # TODO Write a unit test that asserts that upper get stored inside of the namespace returned from parser.parse_args when either "-u" or "--upper" arguments are passed.
        self.assertEquals(echo.to_upper('hello'),'HELLO')
    def test_lower(self):
        # TODO Write a unit test that asserts that lower get stored inside of the namespace returned from parser.parse_args when either "-l" or "--lower" arguments are passed.
        self.assertEquals(echo.to_lower('Hello'),'hello')
    def test_title(self):
        # TODO Write a unit test that asserts that title get stored inside of the namespace returned from parser.parse_args when either "-t" or "--title" arguments are passed.
        self.assertEquals(echo.to_title('hello'),'Hello')
    def test_all(self):
        result = echo.to_upper('heLLo!')
        result = echo.to_lower(result)
        result = echo.to_title(result)
        self.assertEquals(result,'Hello!')
    def test_no_arguments(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        self.assertEquals(stdout,'hello\n')

if __name__ == '__main__':
    unittest.main()
