import os
from csoundwriter import create_csd
from instrument import Instrument
from sequence import Sequence

instrument = Instrument()
seq = Sequence(instrument)

seq.add_event(1, 2, 3)
seq.add_event(2, 2, 3)

create_csd('../scratch/test.csd', [seq])
os.system('csound ../scratch/test.csd')
os.system('aplay ../scratch/test.wav')

