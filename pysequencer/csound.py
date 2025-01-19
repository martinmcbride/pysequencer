import pystache

template = """<CsoundSynthesizer>
<CsOptions>
-t {{tempo}}
-o {{sound_file}}
</CsOptions>
<CsInstruments>
sr = 44100
ksmps = 32
nchnls = 1
0dbfs  = 1
{{#instruments}}
{{.}}
{{/instruments}}
</CsInstruments>
<CsScore>
{{#functions}}
{{.}}
{{/functions}}
{{#score}}
{{.}}
{{/score}}
e
</CsScore>
</CsoundSynthesizer>
"""

class CSoundPlayer:

    def __init__(self, script_file, channels, tempo):
        self.instrument_id = 0
        self.function_id = 0
        self.script_file = script_file
        self.channels = channels
        self.tempo = tempo

    def get_instrument_id(self):
        self.instrument_id += 1
        return self.instrument_id

    def get_function_id(self):
        self.function_id += 1
        return self.function_id

    def event_to_str(self, events, id):
        print("**", events)
        strings = ["i", f"{id}"] + [str(e) for e in events]
        return " ".join(strings)

    def create_csd(self):
        events = []
        instruments = []
        functions = []
        for channel in self.channels:
            print(">>", channel.events)
            for e in channel.events.events:
                events.append(self.event_to_str(e, channel.instrument.id))
            instruments.append(channel.instrument.body)
            functions.append(channel.instrument.functions)
        print("events", events)
        print("instruments", instruments)
        print("functions", functions)
        csound_script = pystache.render(template, dict(score=events,
                                                       instruments=instruments,
                                                       functions=functions,
                                                       tempo=self.tempo,
                                                       sound_file=self.script_file + ".wav"
                                                       ))

        with open(self.script_file + ".csd", 'w') as outfile:
            outfile.write(csound_script)
