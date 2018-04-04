# Clear duplicates from Dropbox backup
import json
from icalendar import Calendar, Event

print('Enter the file (and path if needed) for your Nomie backup.')
try:
    fileName = input('> ')
except:
    print('Re-input. Program has fallen back to Python 2.x protocols')
    fileName = raw_input('> ')
file = open(fileName)
dataRaw = file.read()

data = json.loads(dataRaw)
events = data['events']
calendarEvents = []
for i in events:
    toAdd = None # TODO: Built calendar event
    calendarEvents += [toAdd]

# TODO: Create ical file with events
