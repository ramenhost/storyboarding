#!/bin/sh
echo "Starting Preprocessor"
python prepare.py $1
echo "Starting POS Tagger"
python pos-tagger.py
echo "Starting NER Tagger"
python ner-tagger.py
echo "Starting Wordnet for NER"
python wn-tagger.py