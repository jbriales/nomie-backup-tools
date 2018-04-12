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

trackers = data['trackers']
nameMap = {}
for i in trackers:
    nameMap[i['_id']] = i['label']

events = data['events']
# Event fields: title, startdate, enddate, description, geo
calendarEvents = []
for i in events:
    elements = i['_id'].split('|')
    # Extract needed data
    try:
        trackername = nameMap[elements[3]]
        print(trackername)
        value = i['value']
        if value == None:
            value = 0
        # Now build event fields
        startdate = int(elements[2])
        enddate = startdate
        description = '#' + trackername + '(' + str(value) + ')'
        geo = i['geo']
        title = '#nomie #' + trackername
        toAdd = {
                'title': title,
                'startdate': startdate,
                'enddate': enddate,
                'description': description,
                'geo': geo
                }
        calendarEvents += [toAdd]
    except:
        print("Shoot! This record seems to be corrupted. Try manually adding it or fixing the file.")
        print(i)

cal = Calendar()
for i in events:
    event = Event()
    event.add('summary', i['description'])
    event.add('dtstart', i['startdate'])
    event.add('dtend', i['enddate'])
    event.add('location', i['geo'])
    cal.add_component(event)

# Print ical contents
print(cal.to_ical())
