## Preprocessing
The Preprocessing module uses a pipeline of stanford POS, NER taggers and Wordnet to extract Actors, Groups, Props and Location from the movie script.
It also uses word2vec model for suggesting similar props based on those in the scipt.

Download Stanford NER, POS taggers and adjust model Path in code.

### Run the Preprocessor
Have your movie script in a txt file and chmod `run.sh` to executable.  

> `./run.sh movie-script.txt`
