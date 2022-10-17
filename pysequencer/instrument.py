# Author:  Martin McBride
# Created: 2022-10-16
# Copyright (C) 2022, Martin McBride
# License: MIT
import pystache

from namestore import namestore


class Instrument:

    def __init__(self):
        self._name = "Default instrument"
        self._id = namestore.get_instrument()
        self._parameters = ["time", "duration", "midi"]
        self._functions = []
        self._template = ""

    @property
    def id(self):
        return self._id

    @property
    def parameters(self):
        return self._parameters

    @property
    def name(self):
        return self._name

    def __str__(self):
        return pystache.render(self._template, dict(id=self._id))

class SineSynth(Instrument):

    def __init__(self):
        self._name = "SineSynth"
        self._id = namestore.get_instrument()
        self._parameters = ["time", "duration", "midi", "volume"]
        self._functions = []
        self._template =\
"""instr {{id}}
a1 oscil 1, p4, 1
a3 adsr .1, .5, 0, 0
a2 = a3 * a1
out a2*p5
endin
"""
