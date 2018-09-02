## Preprocessing
The Preprocessing module uses a pipeline of stanford POS, NER taggers and Wordnet to extract Actors, Groups, Props and Location from the movie script.
It also uses word2vec model for suggesting similar props based on those in the scipt.

Download Stanford NER, POS taggers and adjust model Path in code.

### Run the Preprocessor
Have your movie script in a txt file and chmod `run.sh` to executable.  

> `./run.sh movie-script.txt`

### Implementation
**Input:** Raw movie script.  
**Output:** Actors, Groups, Props and Location for each scene.  
The raw script is seperated into scenes using regex and each scene is saved under a folder. Then a POS tagger is made to run through all the scenes, followed by a NER tagger. The NER tagger will identify the person names and locations in the script. Then wordnet is used to identify the groups and props in the script.   
For suggestion of props that are not mentioned in the script but are relevant to the scene, a word2vec model is used so that those words that are near to the ones mentioned in the script are suggested. Again the suggestions are made sure that they are props using wordnet.
