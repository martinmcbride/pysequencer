import unittest

from pysequencer import AbstractInstrument, Event, Events


class TestAbstractInstrument(unittest.TestCase):

    def test_default_instrument(self):
        instrument = AbstractInstrument()
        self.assertEqual(instrument.get_argument("start"), 0)
        self.assertEqual(instrument.get_argument("duration"), 1)
        self.assertEqual(instrument.get_argument("amplitude"), 1)
        self.assertEqual(instrument.get_argument("frequency"), 440)

    def test_modified_instrument(self):
        instrument = AbstractInstrument(duration=2, amplitude=0.5, frequency=600, vibrato=5)
        self.assertEqual(instrument.get_argument("start"), 0)
        self.assertEqual(instrument.get_argument("duration"), 2)
        self.assertEqual(instrument.get_argument("amplitude"), 0.5)
        self.assertEqual(instrument.get_argument("frequency"), 600)
        self.assertEqual(instrument.get_argument("vibrato"), 5)

class TestEvent(unittest.TestCase):

    def test_default_event(self):
        instrument = AbstractInstrument()
        event = Event(instrument)
        self.assertEqual(event.instrument, instrument)
        self.assertEqual(event.get_parameter("start"), 0)
        self.assertEqual(event.get_parameter("duration"), 1)
        self.assertEqual(event.get_parameter("amplitude"), 1)
        self.assertEqual(event.get_parameter("frequency"), 440)

    def test_modified_event(self):
        instrument = AbstractInstrument(duration=2, amplitude=0.5, frequency=600, vibrato=5)
        event = Event(instrument)
        self.assertEqual(event.instrument, instrument)
        self.assertEqual(event.get_parameter("start"), 0)
        self.assertEqual(event.get_parameter("duration"), 2)
        self.assertEqual(event.get_parameter("amplitude"), 0.5)
        self.assertEqual(event.get_parameter("frequency"), 600)
        self.assertEqual(event.get_parameter("vibrato"), 5)

class TestEvents(unittest.TestCase):

    def test_default_events(self):
        events = Events()
        self.assertEqual(len(events), 0)

    def test_add_events(self):
        instrument = AbstractInstrument(vibrato=3)
        events = Events()
        events.add(Event(instrument, start=1))
        events.add(Event(instrument, start=2, vibrato=5))
        self.assertEqual(len(events), 2)

        start_values = [1, 2]
        vibrato_values = [3, 5]
        for i, e in enumerate(events):
            self.assertEqual(e.get_parameter("start"), start_values[i])
            self.assertEqual(e.get_parameter("vibrato"), vibrato_values[i])



if __name__ == '__main__':
    unittest.main()
