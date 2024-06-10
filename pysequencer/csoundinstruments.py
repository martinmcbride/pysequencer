# Author:  Martin McBride
# Created: 2022-10-16
# Copyright (C) 2022, Martin McBride
# License: MIT
import pystache

from namestore import namestore
from pysequencer import Instrument


class CSoundInstrument(Instrument):
    instrument_id = 0
    function_id = 0

    def __init__(self):
        Instrument.__init__(self)
        self._id = self.get_instrument_id()
        self._functions = ()
        self._function_ids = ()
        self._template = ""

    def get_instrument_id(self):
        CSoundInstrument.instrument_id += 1
        return CSoundInstrument.instrument_id

    def get_function_id(self):
        CSoundInstrument.function_id += 1
        return CSoundInstrument.function_id

    @property
    def id(self):
        return self._id

    @property
    def functions(self):
        function_strings = [pystache.render(s, dict(id=i)) for i, s in zip(self._function_ids, self._functions)]
        return "\n".join(function_strings)

    @property
    def body(self):
        return pystache.render(self._template, dict(id=self._id))

class SineSynth(CSoundInstrument):

    def __init__(self):
        CSoundInstrument.__init__(self)

        self._id = namestore.get_instrument_id()
        self._functions = ("f {{id}} 0 32768 10 1",)
        self._function_ids = (namestore.get_function_id(),)
        self._template =\
"""instr {{id}}
kf mtof p4
a1 oscil 1, kf, 1
a3 adsr .05, .2, 0.3, 0.05
a2 = a3 * a1
out a2*p5
endin
"""

class TriSynth(CSoundInstrument):

    def __init__(self, *defs, **kwdefs):
        self._name = "TriSynth"
        self._id = namestore.get_instrument_id()
        self._parameter_names = ("time", "duration", "midi", "volume")
        self._initial_values = (0, 1, 440, 1)
        self._parameters = dict()
        self._update_defaults(self, *defs, **kwdefs)
        self._functions = ("f {{id}} 0 32768 10 1 0.5 0.3 0.25 0.2 0.167 0.14 0.125 .111",)
        self._function_ids = (namestore.get_function_id(),)
        self._template =\
"""instr {{id}}
kf mtof p4
kfactor line 1.005, p3, 1.03
a1 oscil 1, kf, 1
a2 oscil 1, kf*kfactor, 1
a3 oscil 1, kf/kfactor, 1
aenv adsr .01, .2, 0.3, 0.05
aout = aenv * (a1 + a2 + a3) /3
out aout*p5
endin
"""
