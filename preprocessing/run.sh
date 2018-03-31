#!/bin/sh
source setup.sh
echo "Starting Countdown"
python3 prepare.py $1
echo "Firing off"
python3 -W ignore pos-tagger.py
echo "Getting into space"
python3 -W ignore ner-tagger.py
echo "Inbetween the stars"
python3 wn-tagger.py
echo "Just a mile near the planet"
python3 prop-suggest.py
echo "Landing on the surface"
python3 write-out.py
echo "Mission Accomplished!"
open out.txt