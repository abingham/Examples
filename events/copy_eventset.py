import roxar

# Create event set
esname1 = 'Events_Set1'
event_set1 = project.event_sets[esname1]

# Duplicate event set
escopy1 = 'Events_Set1B'
event_set1_copy1 = project.event_sets.duplicate(existing_name=esname1,
                                                new_name=escopy1)

# Create and add events
escopy2 = 'Events_Set1C'
event_set1_copy2 = project.event_sets.create(escopy2)
event_set1_copy2.set_shared(event_set1.shared)
events = event_set1.get_events()
if events:
    event_set1_copy2.set_events(events)

    # Output some info about the operation
    types = [event.type for event in events]
    unique_types = list(set(types))
    print("{} events created with unique types {}".\
        format(len(events), unique_types))
