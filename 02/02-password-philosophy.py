#!/usr/bin/env python3

# https://adventofcode.com/2020/day/2
# Given a password policy of [min-max] [character]: password, find how many passwords are valid.

import re

with open("02-input.txt") as f:
  exp = re.compile("(\d+)-(\d+) ([a-zA-Z]): (\w+)")

  def parse_line(line):
    return exp.match(line)

  policies = [parse_line(line).groups() for line in f.readlines()]

  valid_passwords = 0

  for policy in policies:
    minimum, maximum, char, password = policy

    occurrences = password.count(char)

    if int(minimum) <= occurrences <= int(maximum):
      valid_passwords += 1 
  
  print("No. of Valid Passwords: {}".format(valid_passwords))