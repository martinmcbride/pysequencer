# Author:  Martin McBride
# Created: 2022-09-30
# Copyright (C) 2022, Martin McBride
# License: MIT

class Sequence():

    def __init__(self):
        self.events = []

    def add_event(self, **kwargs):
        self.events.append(dict(**kwargs))

    def __iter__(self):
        return iter(self.events)