# Author:  Martin McBride
# Created:24-06-07
# Copyright (C) 2024, Martin McBride
# License: MIT

class Instrument:

    def __init__(self, **kwargs):
        self._parameters = tuple(["start", "duration", "pitch"] + list(kwargs.keys()))
        self._defaults = tuple([0, 1, 440] + list(kwargs.values()))

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


class Channel:

    def __init__(self, instrument):
        self._instrument = instrument
        self._defaults = list(instrument.defaults)
        self._parameters = dict(zip(self._instrument.parameters, range(len(self._instrument.parameters))))
        self._events = []

    def add_event(self, start, duration, pitch=440, **kwargs):
        event = list(self._defaults)
        self._events.append(event)

    @property
    def instrument(self):
        return self._instrument

    def __str__(self):
        events = [str(e) for e in self._events]
        return "\r\n".join(events)

class Player:

    def __init__(self, channels, destination):
        self.channels = channels
        self.destination = destination

    def play(self):
        pass