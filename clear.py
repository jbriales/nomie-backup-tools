# Clear duplicates from Dropbox backup
import json

print('Enter the file (and path if needed) for your Nomie backup.')
try:
    fileName = input('> ')
except:
    print('Re-input. Program has fallen back to Python 2.x protocols')
    fileName = raw_input('> ')
file = open(fileName)
dataRaw = file.read()

print('Backing up data.')
backup = open(fileName + '.back', 'w')
backup.write(dataRaw)

data = json.loads(dataRaw)
events = data['events']
cleanedEvents = []
lastId = ''
lastEvent = None
for i in events:
    if not i['_id'] == lastId and not lastId == '':
        cleanedEvents += [lastEvent]
    lastId = i['_id']
    lastEvent = i
cleanedEvents += [lastEvent]

beforeClearCount = len(data['events'])
data['events'] = cleanedEvents
afterClearCount = len(data['events'])

print('Count before clear: ', beforeClearCount)
print('Count after clear: ', afterClearCount)

output = open(fileName, 'w')
output.write(json.dumps(data))
