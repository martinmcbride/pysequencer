import unittest

from pysequencer import AbstractInstrument, Event, Events, delay_events


class TestAbstractInstrument(unittest.TestCase):

    def test_str_instrument(self):
        instrument = AbstractInstrument(duration=2, amplitude=0.5, frequency=600, vibrato=5)
        self.assertEqual(str(instrument), "AbstractInstrument(start=0, duration=2, amplitude=0.5, frequency=600, vibrato=5)")

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

    def test_str_event(self):
        instrument = AbstractInstrument(duration=2, amplitude=0.5, frequency=600, vibrato=5)
        event = Event(instrument)
        self.assertEqual(str(event), "Event(AbstractInstrument(start=0, duration=2, amplitude=0.5, frequency=600, vibrato=5), start=0, duration=2, amplitude=0.5, frequency=600, vibrato=5)")

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

    def test_str_events(self):
        events = Events()
        events.add(Event(AbstractInstrument()))
        events.add(Event(AbstractInstrument()))
        events.add(Event(AbstractInstrument()))
        self.assertEqual(str(events), "Events(3 events)")

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

    def test_add_event_lists(self):
        instrument1 = AbstractInstrument(vibrato=3)
        events1 = Events()
        events1.add(Event(instrument1, start=1))
        events1.add(Event(instrument1, start=2, vibrato=5))
        instrument2 = AbstractInstrument(echo=4)
        events2 = Events()
        events2.add(Event(instrument2, start=1))
        events2.add(Event(instrument2, start=2, echo=6))

        events = Events()
        events.add(events1)
        events.add(events2)

        self.assertEqual(len(events), 4)

        start_values = [1, 2, 1, 2]
        vibrato_values = [3, 5, 0, 0]
        instrument_values = [instrument1, instrument1, instrument2, instrument2]
        echo_values = [0, 0, 4, 6]
        for i, e in enumerate(events):
            self.assertEqual(e.instrument, instrument_values[i])
            self.assertEqual(e.get_parameter("start"), start_values[i])
            if e.instrument is instrument1:
                self.assertEqual(e.get_parameter("vibrato"), vibrato_values[i])
            if e.instrument is instrument2:
                self.assertEqual(e.get_parameter("echo"), echo_values[i])

class TestDelayEvents(unittest.TestCase):

    def test_default_events(self):
        instrument = AbstractInstrument(vibrato=3)
        events = Events()
        events.add(Event(instrument, start=1))
        events.add(Event(instrument, start=2, vibrato=5))
        events.add(Event(instrument, start=10, vibrato=2))
        delayed = list(delay_events(events, 20))
        self.assertEqual(len(events), 3)
        self.assertEqual(str(delayed[0]), "Event(AbstractInstrument(start=0, duration=1, amplitude=1, frequency=440, vibrato=3), start=21, duration=1, amplitude=1, frequency=440, vibrato=3)")
        self.assertEqual(str(delayed[1]), "Event(AbstractInstrument(start=0, duration=1, amplitude=1, frequency=440, vibrato=3), start=22, duration=1, amplitude=1, frequency=440, vibrato=5)")
        self.assertEqual(str(delayed[2]), "Event(AbstractInstrument(start=0, duration=1, amplitude=1, frequency=440, vibrato=3), start=30, duration=1, amplitude=1, frequency=440, vibrato=2)")



if __name__ == '__main__':
    unittest.main()
