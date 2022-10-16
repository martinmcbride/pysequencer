import os
from csoundwriter import create_csd

create_csd('test.csd')
os.system('csound test.csd')
os.system('aplay test.wav')

