#!/usr/bin/env python3

import sys
import getopt
import random

width = 24
height = 24
prob = 0.375

options = getopt.getopt(sys.argv[1:], "w:h:p:", ["width=", "height=", "prob="])

for option, value in options[0]:
    if option in ["-w", "--width"]:
        width = int(value)
    if option in ["-h", "--height"]:
        height = int(value)
    if option in ["-p", "--prob"]:
        prob = float(value)

print("{} {}".format(width, height))

for y in range(height):
    print("".join("1" if random.random() < prob else "0" for x in range(width)))

