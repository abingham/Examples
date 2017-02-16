from copy import copy
from datetime import datetime, timedelta
import roxar
from roxar.events import Event

# Create event set
event_set1 = project.event_sets.create('Event_Set_12')

events = []

# Create event of PERF type, owner is 'Trajectory' type
# Owner format: [<well name>.<wellbore name>.<trajectory name>]
traj_owner = ['Well_1', 'Well_1', 'Planned Trajectory']
event1 = Event.create(type=roxar.EventType.PERF,
                      date=datetime(2014, 12, 23, 0, 0, 0, 0),
                      owner=traj_owner)
events.append(event1)

# Create event of DATE type
# Owner format: any string
event2 = Event.create(type=roxar.EventType.DATE,
                      date=datetime(2014, 12, 24, 0, 0, 0, 0),
                      owner=['Simulator Model'])
events.append(event2)

# Create event of GCONTROL type, owner is 'Well Group' type
# Owner format: [well group name]
event3 = Event.create(type=roxar.EventType.GCONTROL,
                      date=datetime(2014, 12, 24, 0, 0, 0, 0),
                      owner=['Well Group1'])
events.append(event3)

# Create event of WSTATE type, owner is 'Well' type
# Owner format: [well name]
event4 = Event.create(type=roxar.EventType.WSTATE,
                      date=datetime(2014, 11, 24, 0, 0, 0, 0),
                      owner=['Well_1'])
events.append(event4)

#------------------------------------------
# Copy or duplicate performs same operation

# Copy event
event5 = copy(event4)
# Change date
event5.date = event5.date + timedelta(days=1)
events.append(event5)

# Duplicate
event6 = Event.duplicate(event1)
# Change owner
event6.owner = ['Well_2', 'Well_2', 'Planned Trajectory']
# Change MDSTART, MDEND for PERF event
event6['MDSTART'] = 1456.7
event6['MDEND'] = 1556.7
events.append(event6)

# Set events to event set
event_set1.set_events(events)

#------------------------------------------
# Read events
events = event_set1.get_events()
try:
    # Create event of CPERF type, owner is 'Trajectory' type
    # Owner format 'Well.WellBore.Trajectory' or 'Well..'
    event7 = Event.create(type=roxar.EventType.CPERF,
                          date=datetime(2015, 1, 24, 0, 0, 0, 0),
                          owner=traj_owner)
    events.append(event7)
    # Raises ValueError as cell events are allowed only in Grid event set.
    event_set1.set_events(events)
except ValueError:
    pass
