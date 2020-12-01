#!/usr/bin/env python3

# https://adventofcode.com/2020/day/1
# Find the 2 numbers which add up to 2020, then calculate their product

with open('01-input.txt') as f:
  values = [int(value) for value in f.readlines()]

  values.sort()

  iterations = 0

  found_2 = False
  factors_2 = []

  found_3 = False
  factors_3 = []

  for i in range(len(values) - 1, 1, -1):
    for j in range(len(values)):
      a = values[i]
      b = values[j]
      iterations += 1

      if (a + b == 2020):
        found_2 = True
        factors_2 = [a, b]
        break
    else:
      continue
    
    if found_2:
      break

  for i in range(len(values) - 1, 1, -1):
    for j in range(len(values)):
      for k in range(len(values)):
        a = values[i]
        b = values[j]
        c = values[k]
        iterations += 1

        if (a + b + c == 2020):
          found_3 = True
          factors_3 = [a, b, c]
          break
      else:
        continue
      
      if found_3:
        break

print("Find the product of the two numbers whose sum is 2020:")
# print("Iterations: {}".format(iterations))
print("Factors: {}, {}".format(factors_2[0], factors_2[1]))
print("Product: {}".format(factors_2[0] * factors_2[1]))

print("\n")
print("Find the product of the three numbers whose sum is 2020:")
# print("Iterations: {}".format(iterations))
print("Factors: {}, {}, {}".format(factors_3[0], factors_3[1], factors_3[2]))
print("Product: {}".format(factors_3[0] * factors_3[1] * factors_3[2]))