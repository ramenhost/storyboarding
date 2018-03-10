import os
import json
import helpers
from nltk.tag.stanford import StanfordNERTagger

if not os.path.exists('scenes'):
  print('Scenes folder doesn\'t exist :( Run prepare.py first', end='\n')

ner_tagger = StanfordNERTagger(r'english.all.3class.distsim.crf.ser.gz')

for filename in sorted(os.listdir('scenes'), key=helpers.natural_keys):
  scenefile = open('scenes/' + filename, 'r+')
  scene = json.load(scenefile)
  processed = [[word[0] for word in sentence] for sentence in scene['processed']]
  ner_tags = ner_tagger.tag_sents(processed)
  for sindex, sentence in enumerate(ner_tags):
    for windex, word in enumerate(sentence):
      scene['processed'][sindex][windex].append(ner_tags[sindex][windex][1])
  scenefile.seek(0)
  json.dump(scene, scenefile, indent=2)
  scenefile.truncate()
  scenefile.close()
