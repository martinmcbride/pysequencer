# Author:  Martin McBride
# Created: 2022-10-16
# Copyright (C) 2022, Martin McBride
# License: MIT
import pystache

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
    # "time", "duration", "volume", "midi"
    #   p2       p3          p4       p5
    def __init__(self):
        CSoundInstrument.__init__(self)

        self._id = self.get_instrument_id()
        self._functions = ("f {{id}} 0 32768 10 1",)
        self._function_ids = (self.get_function_id(),)
        self._template =\
"""instr {{id}}
kf mtof p5
a1 oscil 1, kf, 1
a3 adsr .05, .2, 0.3, 0.05
a2 = a3 * a1
out a2*p4
endin
"""
