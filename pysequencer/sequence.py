# Author:  Martin McBride
# Created: 2022-09-30
# Copyright (C) 2022, Martin McBride
# License: MIT

class Sequence():

    def __init__(self, instrument):
        self.instrument = instrument
        self.events = []

    def add_event(self, *args):
        if len(args) != len(self.instrument.parameters):
            raise ValueError(f"Number of arguments doesn't match number of parameters for {self.instrument.name}")
        self.events.append([self.instrument.id] + list(args))

    @staticmethod
    def _event_to_str(event):
        strings = ["i"] + [str(e) for e in event]
        return " ".join(strings)

    def __iter__(self):
        return iter(self.events)

    def __str__(self):
        return "\n".join(map(Sequence._event_to_str, self.events))
