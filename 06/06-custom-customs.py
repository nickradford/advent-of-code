#!/usr/bin/env python3

# https://adventofcode.com/2020/day/6
# Given a list of boarding passes, what's the highest ID

with open("06-input.txt") as f:
  answers = set()

  count = 0

  for line in f.readlines():
    if line == "\n":
      count += len(answers)
      answers.clear()
    else:
      for letter in line.rstrip():
        answers.add(letter)

  print("Sum of responses: {}".format(count))


  # Part 2.


with open("06-input.txt") as f:
  group_size = 0
  group_answers = {}
  group_consensus = 0
  for line in f.readlines():
    if line == "\n":
      for key, val in group_answers.items():
        if val == group_size:
          group_consensus += 1

      group_size = 0
      group_answers = {}
    else:
      group_size += 1
      for letter in line.rstrip():
        if letter in group_answers:
          group_answers[letter] += 1
        else:
          group_answers[letter] = 1

  print("Questions where all members of a group answered true: {}".format(group_consensus))