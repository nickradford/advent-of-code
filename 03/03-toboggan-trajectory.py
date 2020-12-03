#!/usr/bin/env python3

# https://adventofcode.com/2020/day/3
# With the map repeating to the right infinitely, calculate the number of trees encountered for a given slope (3, 1) (right, down) 

import math

def calculate_trees_for_slope(slope, grid):
  x, y = slope

  width = len(grid[0]) - 1

  posX, posY = 0, 0

  tree_encounters = 0

  for i in range(0, len(grid), y):
    obj = grid[i][posX % width]
    if obj == "#":
      tree_encounters += 1
    posX += x
    posY += y
  
  return tree_encounters


with open("03-input.txt") as f:
  grid = f.readlines()
  slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
  ]
  
  trees_in_slopes = [calculate_trees_for_slope(slope, grid) for slope in slopes]

  tree_encounters = math.prod(trees_in_slopes)
  
  print("No. of Trees Encountered: {}".format(tree_encounters))

