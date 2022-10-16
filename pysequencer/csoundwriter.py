# Author:  Martin McBride
# Created: 2022-10-01
# Copyright (C) 2022, Martin McBride
# License: MIT

import pystache

_template = """<CsoundSynthesizer>
<CsOptions>
-odac
</CsOptions>
<CsInstruments>
sr = 44100
ksmps = 32
nchnls = 2
0dbfs  = 1
instr 1
a1 oscil 1, p4, 1
a3 adsr .1, .5, 0, 0
a2 = a3 * a1
out a2
endin

</CsInstruments>
<CsScore>
; sine wave.
f 1 0 32768 10 1

i 1 0 1 440 1
i 1 1 1 880 1
e
</CsScore>
</CsoundSynthesizer>
"""


def create_csd(fname):
    csound_script = pystache.render(_template, {})

    with open(fname, 'w') as outfile:
        outfile.write(csound_script)
