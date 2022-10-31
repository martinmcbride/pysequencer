# Author:  Martin McBride
# Created: 2022-10-17
# Copyright (C) 2022, Martin McBride
# License: MIT

class NameStore:
    
    def __init__(self):   
        self.instrument = 0
        self.function = 0

    def get_instrument_id(self):
        self.instrument += 1
        return self.instrument

    def get_function_id(self):
        self.function += 1
        return self.function

namestore = NameStore()
