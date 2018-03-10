import re
import sys, os
import json
import nltk

if len(sys.argv) < 2:
  print('Insufficient arguments (python prepare.py script.txt)', file=sys.stderr)
  exit()

#Scene Header Pattern
pattern = '(\b|\W|^)(EXT|INT)(\.|\b|\W)*([\w,\s\']*)(\W)*(\w*)'

if not os.path.exists('scenes'):
  os.mkdir('scenes')

file = open('scenes/intro.json', 'w')
scene_count = 0
scene = dict()
scene['scene_no'] = scene_count
raw_scene = ''

with open(sys.argv[1], 'r') as scriptfile:
  for line in scriptfile:
    #Skip for lines without word
    if not re.search('\w', line):
      continue

    #New scene start
    header = re.search(pattern, line)
    if header:
      scene['raw'] = nltk.sent_tokenize(raw_scene)
      raw_scene = ''
      if not scene == None:
        json.dump(scene, file, indent=2)
        file.close()
        file = open('scenes/scene' + str(scene_count+1) + '.json', 'w')
      scene = dict()
      scene_count += 1
      scene['scene_no'] = scene_count
      scene['meta'] = dict()
      scene['meta']['view'] = header.group(2)
      scene['meta']['location'] = header.group(4)
      scene['meta']['time'] = header.group(6)

    #Append to current scene
    else:
      raw_scene += line.lstrip().replace('\n', ' ')

scene['raw'] = nltk.sent_tokenize(raw_scene)
json.dump(scene, file, indent=2)
file.close()