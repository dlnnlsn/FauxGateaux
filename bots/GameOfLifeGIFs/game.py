#!/usr/bin/env python3

import sys
import getopt

def writePBM(board, width, height, pixelWidth, pixelHeight, filename):
    with open(filename, 'w') as fout:
            fout.write("P4\n")
            fout.write("{} {}\n".format(width * pixelWidth, height * pixelHeight))
            
    with open(filename, 'ba') as fout:
            for y in range(height):
                row = "".join(map(lambda x: str(int(x)) * pixelWidth, board[y])) \
                    + "0000000"

                vals = bytearray([int(row[8*i:8*(i + 1)], 2) \
                    for i in range((width * pixelWidth - 1)//8 + 1)])

                for i in range(pixelHeight):
                        fout.write(vals)

def nextGeneration(board, width, height):
    newBoard = []
    for y in range(height):
        newBoard += [[False] * width]
        for x in range(width):
            neighbours = 0
            for ny in range(max(y - 1, 0), min(y + 2, height)):
                for nx in range(max(x - 1, 0), min(x + 2, width)):
                    if (x == nx) and (y == ny): continue
                    if board[ny][nx]: neighbours += 1
            if neighbours == 3: newBoard[y][x] = True
            if neighbours == 2: newBoard[y][x] = board[y][x]
    return newBoard

width, height = map(int, input().split())

board = [input() for i in range(height)]
board = [[c == '1' for c in row] for row in board]

frames = 100 
pixelWidth = 10
pixelHeight = 10

options = getopt.getopt(sys.argv[1:], "f:", ["frames=", "pixelWidth=", "pw=", "pixelHeight=", "ph="])

for option, value in options[0]:
    if option in ["-f", "--frames"]:
        frames = int(value)
    if option in ["--pixelWidth", "--pw"]:
        pixelWidth = int(value)
    if option in ["--pixelHeight", "--ph"]:
        pixelHeight = int(value)

nameWidth = len(str(frames - 1))

for f in range(frames):
    filename = "./frames/{:0{}}.pbm".format(f, nameWidth)
    writePBM(board, width, height, pixelWidth, pixelHeight, filename)
    board = nextGeneration(board, width, height)
