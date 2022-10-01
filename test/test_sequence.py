import unittest
from sequence import Sequence

class TestSequencer(unittest.TestCase):

    # Test text extent
    def test_add_event(self):
        seq = Sequence()
        seq.add_event(a=1, b=2, c=3)
        events = list(seq)
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0], dict(a=1, b=2, c=3))

if __name__ == '__main__':
    unittest.main()
