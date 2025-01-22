# Author:  Martin McBride
# Created:24-06-07
# Copyright (C) 2024, Martin McBride
# License: MIT
from collections.abc import Iterable
from typing import Union, Self


class AbstractInstrument:
    """
    Abstract base class for instrument types
    """

    def __init__(self, **extras):
        """
        Create AbstractInstrument

        Args:
            extras: Additional parameters as keyword parameters, eg echo=0 creates a new instrument parameter called
                    "echo" with default value 0
        """
        common_args = dict(start=0, duration=1, amplitude=1, frequency=440)
        self._arguments = common_args | extras

    @property
    def arguments(self) -> dict:
        """
        Arguments property

        Returns:
            A dictionary listing each argument and its default value as key:value pairs.
        """
        return self._arguments

    def get_argument(self, name: str) -> any:
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        return self._arguments[name]

    def __str__(self) -> str:
        params = (f"{p}={self._arguments[p]}" for p, v in self._arguments.items())
        param_list = ", ".join(params)
        return f"AbstractInstrument({param_list})"


class Event:

    def __init__(self, instrument: AbstractInstrument, **extras):
        if not isinstance(instrument, AbstractInstrument):
            raise TypeError("instrument must be an AbstractInstrument")

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
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        return self._parameters[name]

    def __str__(self):
        params = (f"{p}={self._parameters[p]}" for p in self._parameters)
        param_list = ", ".join(list(params))
        return f"Event({self._instrument}, {param_list})"


class Events:

    def __init__(self):
        self._events = []

    def add(self, item: Event | Self):
        if isinstance(item, Event):
            self._events.append(item)
        elif isinstance(item, Events):
            self._events.extend(item)
        else:
            raise TypeError("item must be an Event or Events object")

    def __iter__(self):
        for e in self._events:
            yield e

    def __len__(self):
        return len(self._events)

    def __str__(self) -> str:
        return f"Events({len(self._events)} events)"


def delay_events(events: Iterable[Event], delay: float):
    for e in events:
        parameters = dict(e.parameters)
        parameters["start"] = parameters["start"] + delay
        yield Event(e.instrument, **parameters)
