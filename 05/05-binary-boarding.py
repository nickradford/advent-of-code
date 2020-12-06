#!/usr/bin/env python3

# https://adventofcode.com/2020/day/5
# Given a list of boarding passes, what's the highest ID
import math

row_cache = {}
col_cache = {}


with open("05-input.txt") as f:
  rows = list(range(0, 128))
  cols = list(range(0, 8))

  parsed_passes = []
  highest_seat_id = [0]
  print(rows, cols)

  for boarding_pass in f.readlines():
    row_info = boarding_pass[:7]
    col_info = boarding_pass[7:]

    row_start, row_end = 0, 127
    col_start, col_end = 0, 7

    row_number = -1
    col_number = -1

    if row_info in row_cache:
      print("Found Row: {} = {}".format(row_info, row_cache[row_info]))
      row_number = row_cache[row_info]
    else:
      for i, val in enumerate(row_info):
        if i == 6:
          row_number = (row_start if val == "F" else row_end)
        else:
          if val == "F":
            row_end = math.floor((row_start + row_end) / 2)
          elif val == "B":
            row_start = math.floor((row_start + row_end) / 2) + 1

      # row_cache[row_info] = row_number
    
    if col_info in col_cache:
      print("Found Col: {} = {}".format(col_info, col_cache[col_info]))
      col_number = col_cache[col_info]
    else:
      for i, val in enumerate(col_info):
        if i == 2:
          col_number = col_start if val == "L" else col_end
        else:
          if val == "L":
            col_end = math.floor((col_start + col_end) / 2)
          elif val == "R":
            col_start = math.floor((col_start + col_end) / 2) + 1
      
      # col_cache[col_info] = col_number
    

    seat_id = (row_number * 8 )+ col_number
    # print("ID: {}, Row: {}, Col: {}".format(seat_id, row_number, col_number))

    if seat_id > highest_seat_id[0]:
      highest_seat_id = [seat_id, row_number, col_number]

    parsed_passes.append([seat_id, row_number, col_number])
  
  parsed_passes.sort(key=lambda id: id[0])

  prev = 0
  found = 0
  for seat_id, row, col in parsed_passes:
    if seat_id - prev == 2:
      found = seat_id - 1
      break
    prev = seat_id
  
  print("My Seat ID: {}".format(found))