# Author:  Martin McBride
# Created:24-06-07
# Copyright (C) 2024, Martin McBride
# License: MIT

class AbstractInstrument:
    """
    Abstract base class for instrument types
    """

    def __init__(self, *extras):
        """
        Set the points for the Pycairo LinearGradient pattern

        Args:
            extras: Additional parameters and defaults, as tuples (name, default) where
                    name is the name as a string and default is the default value
        """
        common_parameters = (("start", 0), ("duration", 1), ("amplitude", 1), ("frequency", 440))
        extras = tuple(extras)
        all_params = common_parameters + extras
        self._arguments = tuple((x[0] for x in all_params))
        self._defaults = {x[0]: x[1] for x in all_params}

    @property
    def arguments(self):
        return self._arguments

    @property
    def defaults(self):
        return self._defaults

    def default(self, param):
        return self._defaults[param]

    def __str__(self):
        params = (f"{p}={self._defaults[p]}" for p in self._arguments)
        param_list = ", ".join(params)
        return f"AbstractInstrument({param_list})"


class Event:

    def __init__(self, instrument, **extras):
        self._instrument = instrument
        self._parameters = dict(instrument.defaults)
        for k, v in extras.items():
            if k in self._parameters:
                self._parameters[k] = v
            else:
                raise ValueError(f"Key {k} not valid for {instrument}")

    def __str__(self):
        params = (f"{p}={self._parameters[p]}" for p in self._parameters)
        param_list = ", ".join(params)
        return f"Event({self._instrument}, {param_list})"


# class Events:
#
#     def __init__(self, instrument):
#         self._instrument = instrument
#         self._defaults = list(instrument.defaults)
#         self._parameters = dict(zip(self._instrument.parameters, range(len(self._instrument.parameters))))
#         self._offset_time = 0
#         self._events = []
#
#     def time(self, new_time):
#         self._offset_time = new_time
#
#     @property
#     def instrument(self):
#         return self._instrument
#
#     @property
#     def events(self):
#         return self._events
#
#     def add_events(self, events):
#         event = list(self._defaults)
#         self._events.extend(events.events)
#
#     def add_event(self, start, duration, amplitude=None, midi=None, **kwargs):
#         event = list(self._defaults)
#         event[0] += start + self._offset_time
#         event[1] = duration
#         if amplitude is not None:
#             event[2] = amplitude
#         if midi is not None:
#             event[3] = midi
#         self._events.append(event)
#
#     def join(self, other):
#         return
#
#
# class Track:
#
#     def __init__(self, instrument, events):
#         self._instrument = instrument
#         self._events = events
#
#     @property
#     def instrument(self):
#         return self._instrument
#
#     @property
#     def events(self):
#         return self._events
#
#     def __str__(self):
#         events = [str(e) for e in self._events.events]
#         return "\r\n".join(events)
#
#
# class Writer:
#
#     def __init__(self, tracks):
#         self._tracks = tracks
#
#     def write(self, filename):
#         pass