#!/bin/bash

rm ./frames/*

./randomBoard.py -w 32 -h 32 | ./game.py -f 100 --pw=10 --ph=10
convert -loop 0 -delay 20 ./frames/* image.gif

