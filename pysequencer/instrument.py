# Author:  Martin McBride
# Created: 2022-10-16
# Copyright (C) 2022, Martin McBride
# License: MIT

from dataclasses import dataclass

@dataclass
class Instrument:

    name = None
    id = None
    parameters = None
    functions = None
    template = None

    def __post_init__(self):
        self.name = "Default instrument"
        self.id = 1
        self.parameters = ["time", "duration", "midi"]

class SineSynth(Instrument):

    def __post_init__(self):
        self.name = "Default instrument"
        self.id = 1
        self.parameters = ["time", "duration", "midi"]
