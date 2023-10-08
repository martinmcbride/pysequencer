# Author:  Martin McBride
# Created: 2022-10-01
# Copyright (C) 2022, Martin McBride
# License: MIT

import pystache

template = """<CsoundSynthesizer>
<CsOptions>
-t {{tempo}}
-o {{sound_file}}
</CsOptions>
<CsInstruments>
sr = 44100
ksmps = 32
nchnls = 2
0dbfs  = 1
{{#instruments}}
{{.}}
{{/instruments}}
</CsInstruments>
<CsScore>
; sine wave.
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


def create_csd(script_file, sequences, instruments, functions, tempo, sound_file):
    csound_script = pystache.render(template, dict(score=sequences,
                                                   instruments=instruments,
                                                   functions=functions,
                                                   tempo=tempo,
                                                   sound_file=sound_file
                                                   ))

    with open(script_file, 'w') as outfile:
        outfile.write(csound_script)
