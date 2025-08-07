import unittest
from monitor import vitals_ok, vitals_status

class MonitorTest(unittest.TestCase):
    def test_temperature_out_of_range(self):
        self.assertFalse(vitals_ok(103, 70, 95))  # High temp
        self.assertFalse(vitals_ok(94, 70, 95))   # Low temp

    def test_pulse_rate_out_of_range(self):
        self.assertFalse(vitals_ok(98, 101, 95))  # High pulse
        self.assertFalse(vitals_ok(98, 59, 95))   # Low pulse

    def test_spo2_out_of_range(self):
        self.assertFalse(vitals_ok(98, 70, 89))   # Low SpO2

    def test_all_vitals_ok(self):
        self.assertTrue(vitals_ok(98.6, 72, 98))

    def test_vitals_status_messages(self):
        self.assertEqual(vitals_status(103, 70, 95), (False, 'Temperature critical!'))
        self.assertEqual(vitals_status(98, 101, 95), (False, 'Pulse Rate is out of range!'))
        self.assertEqual(vitals_status(98, 70, 89), (False, 'Oxygen Saturation out of range!'))
        self.assertEqual(vitals_status(98.6, 72, 98), (True, 'All vitals normal.'))

if __name__ == '__main__':
    unittest.main()
