from event import *


event1 = Event("BRMC", "21 January 2021", "100", "Main hall", "Rock")
event2 = Event("Prodigy", "12 February 2021", "150", "Main Hall", "Rock")
events = [event1, event2]


def add_new_event(event):
    events.append(event)