from datetime import datetime
import roxar
from roxar.events import Event

owner=['Well_A']
date1  = datetime(2004, 11, 21, 0, 0, 0, 0)

# Create event set
event_set1 = project.event_sets.create('Event_Set_12')

# Create a couple events
event1 = Event.create(type=roxar.EventType.WSTATE, date=date1, owner=owner)
event2 = Event.create(type=roxar.EventType.GCONTROL, date=date1, owner=['Well Group2'])
event_set1.set_events([event1, event2])

# Get all the events into a list
elist = event_set1.get_events()

print('Number of events in the list:', len(elist))

# Remove specified events from the list
for index, event in enumerate(elist):
    if event.owner == owner and event.date == date1:
        print('Deleting', event.type)
        elist.pop(index)


# Save updated event set
event_set1.set_events(elist)


print('Number of events in the list:', len(event_set1.get_events()))
