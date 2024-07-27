# Author:  Martin McBride
# Created:24-07-25
# Copyright (C) 2024, Martin McBride
# License: MIT
from midiutil.MidiFile import MIDIFile
from pysequencer import Instrument


class MidiInstrument(Instrument):

    def __init__(self, program_number, track):
        super().__init__()
        self._program_number = program_number
        self._track = track

    def play_events(self, midi_file, events):
        # Default parameters "time", "duration", "volume", "midi"
        print(events.events)
        for event in events.events:
            midi_file.addNote(self._track, 0, event[3], event[0], event[1], event[2])


class MidiWriter:

    def __init__(self, tracks):
        self._tracks = tracks

    def write(self, filename):
        midifile = MIDIFile(2)  # One track
        midifile.addTempo(0, 0, 60)
        for track in self._tracks:
            track.instrument.play_events(midifile, track.events)

        with open(filename, "wb") as output_file:
            midifile.writeFile(output_file)
