import os
from csoundwriter import create_csd
from instrument import SineSynth
from sequence import Sequence

instrument = SineSynth()
seq = Sequence(instrument)

seq.add_event(0, 1, 200, 1)
seq.add_event(1, 1, 500, 0.1)

print(seq)
print(instrument)

create_csd('../scratch/test.csd', [seq], [instrument], ["f 1 0 32768 10 1 1 0 1"])
os.system('csound ../scratch/test.csd')
os.system('aplay ../scratch/test.wav')

