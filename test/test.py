import os
from csoundwriter import create_csd
from instrument import SineSynth
from sequence import Sequence

instrument = SineSynth()
seq = Sequence(instrument)

seq.add_events([0, 1, 2, 4, 5, 6], 1, [60, 62, 63], 1)

create_csd('../scratch/test.csd', [seq.events], [instrument.body], [instrument.functions])
os.system('csound ../scratch/test.csd')
os.system('aplay ../scratch/test.wav')

