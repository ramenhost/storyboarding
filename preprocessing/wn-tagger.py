import os, json
import helpers
from nltk.corpus import wordnet as wn

def wordnet_optimize(sentence):
  for word in sentence:
    if word[1] in ['NN', 'NNS', 'NNP', 'NNPS'] and word[2] == 'O':
      options = wn.synsets(word[0])
      if len(options) > 4:
        options = options[:4]
      for option in options:
        if option.lexname() == 'noun.artifact':
          word[2] = 'PROP'
          break;
        elif option.lexname() == 'noun.person':
          word[2] = 'PERSON'
          break;
        elif option.lexname() == 'noun.group':
          word[2] = 'GROUP'
          break;
  return sentence

if not os.path.exists('scenes'):
  print('Scenes folder doesn\'t exist :( Run prepare.py first', end='\n')

for filename in sorted(os.listdir('scenes'), key=helpers.natural_keys):
  scenefile = open('scenes/' + filename, 'r+')
  scene = json.load(scenefile)
  processed = [[word[0] for word in sentence] for sentence in scene['processed']]
  for sindex, sentence in enumerate(processed):
    scene['processed'][sindex] = wordnet_optimize(scene['processed'][sindex])
  
  #write to test file for validating
  scenefile.seek(0)
  #scenefile.close()
  #scenefile = open('scenes/' + filename + '-test', 'w')
  json.dump(scene, scenefile, indent=2)
  scenefile.truncate()
  scenefile.close()