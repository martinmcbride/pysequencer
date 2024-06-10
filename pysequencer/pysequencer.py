# Author:  Martin McBride
# Created:24-06-07
# Copyright (C) 2024, Martin McBride
# License: MIT

class Instrument:

    def __init__(self):
        self._parameters = tuple(["time", "duration", "midi", "volume"])
        self._defaults = tuple([0, 1, 1, 440])

    def play(self, channel, destination):
        pass

    @property
    def parameters(self):
        return self._parameters

    @property
    def defaults(self):
        return self._defaults

    def __str__(self):
        params = (f"{p}={v}" for p, v in zip(self._parameters, self._defaults))
        return ", ".join(params)


class Events:

    def __init__(self, instrument, start_time):
        self._instrument = instrument
        self._defaults = list(instrument.defaults)
        self._parameters = dict(zip(self._instrument.parameters, range(len(self._instrument.parameters))))
        self.start_time = start_time
        self._events = []

    @property
    def instrument(self):
        return self._instrument

    @property
    def events(self):
        return self._events

    def add_events(self, events):
        event = list(self._defaults)
        self._events.extend(events.events)

    def add_event(self, start, duration, midi=60, volume=1, **kwargs):
        event = list(self._defaults)
        event[0] += self.start_time
        self._events.append(event)

    def join(self, other):
        return


class Channel:

    def __init__(self, instrument, events):
        self._instrument = instrument
        self._events = events

    @property
    def instrument(self):
        return self._instrument

    @property
    def events(self):
        return self._events

    def __str__(self):
        events = [str(e) for e in self._events.events]
        return "\r\n".join(events)
