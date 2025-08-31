# Author:  Martin McBride
# Created: 25-01-31
# Copyright (C) 2025, Martin McBride
# License: MIT

import random

from mido import Message, MetaMessage, MidiFile, MidiTrack, bpm2tempo, second2tick, MAX_PITCHWHEEL

from pysequencer import AbstractInstrument

class MidiInstrument(AbstractInstrument):

    def __init__(self, channel, **extras):
        """
        Create MidiInstrument

        Args:
            channel: The MIDI channel for this instrument
            extras: Additional parameters as keyword parameters, eg echo=0 creates a new instrument parameter called
                    "echo" with default value 0
        """
        super().__init__(extras)
        self._channel = channel

class MidiWriter:

    def __init__(self):
        pass

    def write(self, filename, events):
        notes = [64, 64 + 7, 64 + 12]

        outfile = MidiFile()

        track = MidiTrack()
        outfile.tracks.append(track)

        track.append(Message('program_change', program=12))

        delta = 300
        ticks_per_expr = 20
        for i in range(4):
            note = random.choice(notes)
            track.append(Message('note_on', note=note, velocity=100, time=delta))
            for j in range(delta // ticks_per_expr):
                pitch = MAX_PITCHWHEEL * j * ticks_per_expr // delta
                track.append(Message('pitchwheel', pitch=pitch, time=ticks_per_expr))
            track.append(Message('note_off', note=note, velocity=100, time=0))

        outfile.save(filename)