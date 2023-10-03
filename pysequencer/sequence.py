# Author:  Martin McBride
# Created: 2022-09-30
# Copyright (C) 2022, Martin McBride
# License: MIT
from collections.abc import Iterable
from itertools import zip_longest, islice, cycle


class Sequence():

    def __init__(self, instrument):
        self.instrument = instrument
        self._events = []

    def add_event(self, *args):
        if len(args) != len(self.instrument.parameters):
            raise ValueError(f"Number of arguments doesn't match number of parameters for {self.instrument.name}")
        self._events.append([self.instrument.id] + list(args))

    def add_events(self, *args):
        print(args)
        if len(args) != len(self.instrument.parameters):
            raise ValueError(f"Number of arguments doesn't match number of parameters for {self.instrument.name}")
        args_list = [a if isinstance(a, Iterable) else (a,) for a in args]
        sequence_size = max(map(len, args_list))
        print(sequence_size, args_list)
        args_list = [islice(cycle(a), sequence_size) for a in args_list]
        for a in zip_longest(*args_list):
            print(a)
            self.add_event(*a)

    @staticmethod
    def _event_to_str(event):
        strings = ["i"] + [str(e) for e in event]
        return " ".join(strings)

    def __iter__(self):
        return iter(self.events)

    @property
    def events(self):
        return "\n".join(map(Sequence._event_to_str, self._events))
