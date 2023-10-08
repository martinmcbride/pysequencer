# Author:  Martin McBride
# Created: 2022-10-16
# Copyright (C) 2022, Martin McBride
# License: MIT
import pystache

from namestore import namestore


class Instrument:

    def __init__(self, *defs, **kwdefs):
        self._name = "Default instrument"
        self._id = namestore.get_instrument_id()
        self._parameter_names = ("time", "duration", "freq")
        self._initial_values = (0, 1, 440)
        self._parameters = dict()
        self._functions = ()
        self._function_ids = ()
        self._template = ""

    def _update_defaults(self, *defs, **kwdefs):
        if len(self._initial_values)!=len(self._parameter_names):
            raise ValueError(f"{self.name} number of initial values does not equal number of parameters")
        for k, v in zip(self._parameter_names, self._initial_values):
            self._parameters[k] = v
        if len(defs)>=len(self._parameter_names):
            raise ValueError(f"{self.name} number of default values exceeds number of parameters")
        for k, v in kwdefs:
            if k not in self._parameters:
                raise ValueError(f"{self.name} parameter {k} not recognised")
            self._parameters[k] = v

    @property
    def id(self):
        return self._id

    @property
    def parameters(self):
        return self._parameters

    @property
    def defaults(self):
        return self._defaults

    @property
    def name(self):
        return self._name

    @property
    def functions(self):
        function_strings = [pystache.render(s, dict(id=i)) for i, s in zip(self._function_ids, self._functions)]
        return "\n".join(function_strings)

    @property
    def body(self):
        return pystache.render(self._template, dict(id=self._id))

class SineSynth(Instrument):

    def __init__(self, *defs, **kwdefs):
        self._name = "SineSynth"
        self._id = namestore.get_instrument_id()
        self._parameter_names = ("time", "duration", "freq", "volume")
        self._initial_values = (0, 1, 440, 1)
        self._parameters = dict()
        self._update_defaults(self, *defs, **kwdefs)
        self._functions = ("f {{id}} 0 32768 10 1",)
        self._function_ids = (namestore.get_function_id(),)
        self._template =\
"""instr {{id}}
kf mtof p4
a1 oscil 1, kf, 1
a3 adsr .1, .5, 0, 0
a2 = a3 * a1
out a2*p5
endin
"""
