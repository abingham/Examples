import roxar

# For every event set in the project, go through and look for spaces
for eset in project.event_sets:
    elist = eset.get_events()
    if len(elist) > 0:
        for index, event in enumerate(elist):
            new_name = [o.replace(" ", "_") for o in event.owner]
            print('Changing from "{}" to "{}"'.format(event.owner, new_name))
            event.owner = new_name
        eset.set_events(elist)

print('All RMS event sets updated')
