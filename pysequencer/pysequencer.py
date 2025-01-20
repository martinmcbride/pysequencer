# Author:  Martin McBride
# Created:24-06-07
# Copyright (C) 2024, Martin McBride
# License: MIT

class AbstractInstrument:
    """
    Abstract base class for instrument types
    """

    def __init__(self, **extras):
        """
        Create AbstractInstrument

        Args:
            extras: Additional parameters and defaults, as named parameters where the value specifies the default
        """
        common_args = dict(start=0, duration=1, amplitude=1, frequency=440)
        self._arguments = common_args | extras

    @property
    def arguments(self):
        return self._arguments

    def get_argument(self, argument):
        return self._arguments[argument]

    def __str__(self):
        params = (f"{p}={self._defaults[p]}" for p, v in self._arguments.items())
        param_list = ", ".join(params)
        return f"AbstractInstrument({param_list})"


class Event:

    def __init__(self, instrument, **extras):
        self._instrument = instrument
        self._parameters = dict(instrument.arguments)
        for k, v in extras.items():
            if k in self._parameters:
                self._parameters[k] = v
            else:
                raise ValueError(f"Key {k} not valid for {instrument}")

    @property
    def instrument(self):
        return self._instrument

    @property
    def parameters(self):
        return self._parameters

    def get_parameter(self, name):
        return self._parameters[name]

    def __str__(self):
        params = (f"{p}={self._parameters[p]}" for p in self._parameters)
        param_list = ", ".join(params)
        return f"Event({self._instrument}, {param_list})"


class Events:

    def __init__(self):
        self._events = []

    def add(self, items):
        if isinstance(items, Event):
            self._events.append(items)
        elif isinstance(items, Events):
            self._events.extend(items)
        else:
            raise TypeError("Events.add require an Event ior Events object")

    def __iter__(self):
        for e in self._events:
            yield e

    def __len__(self):
        return len(self._events)

def delay_events(events, delay):
    pass
