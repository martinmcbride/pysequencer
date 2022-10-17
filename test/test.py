import os
from csoundwriter import create_csd
from instrument import Instrument
from sequence import Sequence

instrument = Instrument()
seq = Sequence(instrument)

seq.add_event(0, 1, 200)
seq.add_event(1, 1, 500)

create_csd('../scratch/test.csd', [seq])
os.system('csound ../scratch/test.csd')
os.system('aplay ../scratch/test.wav')

