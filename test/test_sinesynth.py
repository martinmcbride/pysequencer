import unittest

from instrument import SineSynth, TriSynth
from sequence import Sequence

class TestSineSynth(unittest.TestCase):

    # Test text extent
    def test_default_instrument(self):
        instrument = SineSynth()
        sequence = Sequence(instrument)
        sequence.add_event()
        events = list(sequence)
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0], dict(a=1, b=2, c=3))

if __name__ == '__main__':
    unittest.main()
