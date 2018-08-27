# Clear duplicates from Dropbox backup
import json
from icalendar import Calendar, Event
from datetime import datetime, timedelta

def convert(data):
    trackers = data['trackers']
    nameMap = {}
    for i in trackers:
        nameMap[i['_id']] = i['label']

# Support for changing the name of a tracker for a substitute
    substitutes = {}

    events = data['events']
# Event fields: title, startdate, enddate, description, geo
    calendarEvents = []
    corruptedCount = 0
    addedCount = 0
    for i in events:
        elements = i['_id'].split('|')
        # Extract needed data
        try:
            trackername = nameMap[elements[3]]
            # Substitute tracker name if substitute is defined
            try:
                trackername = substitutes[trackername]
            except:
                doNothing = True
            # As Nomie 3 doesn't support spaces in tracker names, substitute with underscores
            trackername = trackername.replace(' ', '_')
            print(trackername)
            # Value should be time in seconds of the event
            # Note there is one single event for timer (at the end of timer)
            event_value = i['value']
            # Currently automatically convert lack of value to 0
            if event_value == None:
                event_value = 0
            raw_timestamp_in_millisecs = elements[2]
            timestamp_in_secs = int(raw_timestamp_in_millisecs) / 1000.0
            # Now build event fields
            # Time stored is that of end
            enddate = datetime.fromtimestamp(timestamp_in_secs)
            # Start date is <value> seconds before the end
            startdate = enddate - timedelta(seconds=event_value)
            description = '#' + trackername + '(' + str(event_value) + ')'
            # Now save geo information without place name
            geo = '["",' + str(i['geo'][0]) + ',' + str(i['geo'][1]) + ']'
            title = '#nomie #' + trackername
            toAdd = {
                    'title': title,
                    'startdate': startdate,
                    'enddate': enddate,
                    'description': description,
                    'geo': geo
                    }
            calendarEvents += [toAdd]
            addedCount += 1
        except:
            corruptedCount += 1
            print("Shoot! This record seems to be corrupted. Try manually adding it or fixing the file.")
            print(i)

    print("Corrupted record count: " + str(corruptedCount))
    print("Events successfully added: " + str(addedCount))

    cal = Calendar()
    for i in calendarEvents:
        event = Event()
        event.add('summary', i['title'])
        event.add('description', i['description'])
        event.add('dtstart', i['startdate'])
        event.add('dtend', i['enddate'])
        event.add('location', i['geo'])
        cal.add_component(event)
    return cal.to_ical()

if __name__ == '__main__':
    print('Enter the file (and path if needed) for your Nomie backup.')
    try:
        fileName = input('> ')
    except:
        print('Re-input. Program has fallen back to Python 2.x protocols')
        fileName = raw_input('> ')
    file = open(fileName)
    dataRaw = file.read()
    data = json.loads(dataRaw)

# Print ical contents
    rawCalendar = convert(data)
    outputFileName = input("File name to write to (e.g. out.ical): ")
    outFile = open(outputFileName, 'wb')
    outFile.write(rawCalendar)
    outFile.close()
