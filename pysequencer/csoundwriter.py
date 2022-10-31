# Author:  Martin McBride
# Created: 2022-10-01
# Copyright (C) 2022, Martin McBride
# License: MIT

import pystache

template = """<CsoundSynthesizer>
<CsOptions>
-o ../scratch/test.wav
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


def create_csd(fname, sequences, instruments):
    csound_script = pystache.render(template, dict(score=sequences, instruments=instruments, functions=[]))

    with open(fname, 'w') as outfile:
        outfile.write(csound_script)
