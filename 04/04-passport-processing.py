#!/usr/bin/env python3

# https://adventofcode.com/2020/day/4
# Given a batch of passport information, determine which passports are valid

import re

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

color_regex = re.compile("^#[0-9a-f]{6}$")

def height_validator(hgt):
  if hgt.endswith('cm'):
    val = int(hgt.strip('cm'))
    return 150 <= val <= 193
  elif hgt.endswith('in'):
    val = int(hgt.strip('in'))
    return 59 <= val <= 76
  else:
    return False

validators = {
  'byr': lambda year: 1920 <= int(year) <= 2002 ,
  'iyr': lambda year: 2010 <= int(year) <= 2020 ,
  'eyr': lambda year: 2020 <= int(year) <= 2030 ,
  'hgt': height_validator,
  'hcl': lambda color: True if color_regex.match(color) else False ,
  'ecl': lambda color: color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
  'pid': lambda id: True if len(id) == 9 and int(id) else False
}

def parse_line(line, obj):
  assertions = line.strip('\n').split(' ')
  for assertion in assertions:
    prop, val = assertion.split(':')
    obj[prop] = val

def is_valid(passport):
  for field in required_fields:
    if field in passport:
      if validators[field](passport[field]):
        continue
      else:
        return False
    else:
      return False
  return True

with open("04-input.txt") as f:
  lines = f.readlines()

  passport = {}
  valid_count = 0

  for line in lines:
    if line == "\n":
      if is_valid(passport):
        valid_count += 1
      
      passport = {}
    else:
      parse_line(line, passport)

  print("No. of Valid Passports: {}".format(valid_count))