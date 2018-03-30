import os, json, sys
import helpers

sys.stdout = open('out.txt', 'w')

if not os.path.exists('scenes'):
  print('Scenes folder doesn\'t exist :( Run prepare.py first', end='\n', file=sys.stderr)

for filename in sorted(os.listdir('scenes'), key=helpers.natural_keys):
  scenename = filename.split('.')[0].upper()
  scenefile = open('scenes/' + filename, 'r+')
  print(scenename + ':')
  scene = json.load(scenefile)
  if not scenename == 'INTRO':
    view = ''
    if scene['meta']['view'] == 'INT':
      view = 'Interior of '
    elif scene['meta']['view'] == 'EXT':
      view = 'Exterior of '
    print('Location: ' + view + scene['meta']['location'], end='\n')
    print('Time: ' + scene['meta']['time'], end='\n')
  print('\nActors needed: ')
  print(', '.join(scene['PERSON']))
  print('\nGroup actors: ')
  print(', '.join(scene['GROUP']))
  print('\nProps needed: ')
  print(', '.join(scene['PROP']))
  print('\nProps we suggest: ')
  print(', '.join(scene['RELATED-PROP']))
  print('\nOrganisations involved: ')
  print(', '.join(scene['ORGANIZATION']))
  print('\n--END OF SCENE--')

print('\n--THE END--\n')