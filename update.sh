#!/bin/bash

cd /home/pi/FauxGateaux/

bot=$1
shift

if [[ $bot == "random" ]]; then
    bot=$(ls -d ./bots/*/ | shuf -n 1)
else
    bot="./bots/$bot/"
fi

cd $bot

if [ -f update.sh ]; then
    ./update.sh $@
elif [ -f update.py ]; then
    ./update.py $@
fi

cd /home/pi/FauxGateaux

if [ -f "$bot/image.png" ]; then
    ./tweet.py -i "$bot/image.png" < "$bot/status.txt"
elif [ -f "$bot/image.gif" ]; then
    ./tweet.py -i "$bot/image.gif" < "$bot/status.txt"
else
    ./tweet.py < "$bot/status.txt"
fi
