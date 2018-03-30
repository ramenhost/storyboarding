import os, json
import helpers
from nltk.corpus import gutenberg as gb
from gensim.models import Word2Vec

w2v = Word2Vec(gb.sents())

if not os.path.exists('scenes'):
  print('Scenes folder doesn\'t exist :( Run prepare.py first', end='\n')

for filename in sorted(os.listdir('scenes'), key=helpers.natural_keys):
  scenefile = open('scenes/' + filename, 'r+')
  scene = json.load(scenefile)
  scene['RELATED-PROP'] = list()
  for prop in scene['PROP']:
    try:
      for suggestion in w2v.most_similar(prop, topn=3):
        if suggestion[1] > 0.89 and suggestion not in scene['PROP'] and suggestion not in scene['RELATED-PROP']:
          scene['RELATED-PROP'].append(suggestion[0])
    except KeyError:
      continue
  #write to test file for validating
  scenefile.seek(0)
  #scenefile.close()
  #scenefile = open('scenes/' + filename + '-test', 'w')
  json.dump(scene, scenefile, indent=2)
  scenefile.truncate()
  scenefile.close()