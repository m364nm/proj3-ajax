import unittest
import calculate

def run_test(control_dist):
    test = calculate.calc(control_dist)
    if test == -1:
        return -1
    start = test[0].format("MM.DD.YYYY HH:mm")
    finish = test[1].format("MM.DD.YYYY HH:mm")
    return [start, finish]

class TestBrevetCalculator(unittest.TestCase):

    ## This tests the opening_times function, without special cases
    def test_opening_times(self):
        self.assertEqual(calculate.get_opening_time(0), '00:00')
        self.assertEqual(calculate.get_opening_time(1), '00:02')
        self.assertEqual(calculate.get_opening_time(200), '05:53')
        self.assertEqual(calculate.get_opening_time(400), '12:08')
        self.assertEqual(calculate.get_opening_time(599), '18:46')
        self.assertEqual(calculate.get_opening_time(600), '18:48')
        self.assertEqual(calculate.get_opening_time(601), '18:50')
        self.assertEqual(calculate.get_opening_time(999), '33:03')
        self.assertEqual(calculate.get_opening_time(1000), '33:05')

    ## This tests the closing_times function, without special cases
    def test_closing_times(self):
        self.assertEqual(calculate.get_closing_time(0), '01:00')
        self.assertEqual(calculate.get_closing_time(1), '00:04')
        self.assertEqual(calculate.get_closing_time(200), '13:20')
        self.assertEqual(calculate.get_closing_time(400), '26:40')
        self.assertEqual(calculate.get_closing_time(599), '39:56')
        self.assertEqual(calculate.get_closing_time(600), '40:00')
        self.assertEqual(calculate.get_closing_time(601), '40:05')
        self.assertEqual(calculate.get_closing_time(999), '74:55')
        self.assertEqual(calculate.get_closing_time(1000), '75:00')

####
#   The following tests are verifying the calc function in calculate.py with
#   special cases
####

    def test_brevet_200(self):
        calculate.brevet = 200
        times = run_test(0)
        self.assertEqual(times[0], "01.01.2000 00:00")
        self.assertEqual(times[1], "01.01.2000 01:00")

        times = run_test(1)
        self.assertEqual(times[0], "01.01.2000 00:02")
        self.assertEqual(times[1], "01.01.2000 00:04")

        times = run_test(199)
        self.assertEqual(times[0], "01.01.2000 05:51")
        self.assertEqual(times[1], "01.01.2000 13:16")

        times = run_test(200)
        self.assertEqual(times[0], "01.01.2000 05:53")
        self.assertEqual(times[1], "01.01.2000 13:30")

        times = run_test(201)
        self.assertEqual(times[0], "01.01.2000 05:53")
        self.assertEqual(times[1], "01.01.2000 13:30")

        times = run_test(221)
        self.assertEqual(times, -1)

    def test_brevet_300(self):
        calculate.brevet = 300

        times = run_test(200)
        self.assertEqual(times[0], "01.01.2000 05:53")
        self.assertEqual(times[1], "01.01.2000 13:20")

        times = run_test(299)
        self.assertEqual(times[0], "01.01.2000 08:59")
        self.assertEqual(times[1], "01.01.2000 19:56")

        times = run_test(300)
        self.assertEqual(times[0], "01.01.2000 09:00")
        self.assertEqual(times[1], "01.01.2000 20:00")

        times = run_test(301)
        self.assertEqual(times[0], "01.01.2000 09:00")
        self.assertEqual(times[1], "01.01.2000 20:00")

        times = run_test(331)
        self.assertEqual(times, -1)

    def test_brevet_400(self):
        calculate.brevet = 400

        times = run_test(300)
        self.assertEqual(times[0], "01.01.2000 09:00")
        self.assertEqual(times[1], "01.01.2000 20:00")

        times = run_test(399)
        self.assertEqual(times[0], "01.01.2000 12:06")
        self.assertEqual(times[1], "01.02.2000 02:36")

        times = run_test(400)
        self.assertEqual(times[0], "01.01.2000 12:08")
        self.assertEqual(times[1], "01.02.2000 03:00")

        times = run_test(440)
        self.assertEqual(times[0], "01.01.2000 12:08")
        self.assertEqual(times[1], "01.02.2000 03:00")

        times = run_test(441)
        self.assertEqual(times, -1)

    def test_brevet_600(self):
        calculate.brevet = 600

        times = run_test(400)
        self.assertEqual(times[0], "01.01.2000 12:08")
        self.assertEqual(times[1], "01.02.2000 02:40")

        times = run_test(599)
        self.assertEqual(times[0], "01.01.2000 18:46")
        self.assertEqual(times[1], "01.02.2000 15:56")

        times = run_test(600)
        self.assertEqual(times[0], "01.01.2000 18:48")
        self.assertEqual(times[1], "01.02.2000 16:00")

        times = run_test(660)
        self.assertEqual(times[0], "01.01.2000 18:48")
        self.assertEqual(times[1], "01.02.2000 16:00")

        times = run_test(661)
        self.assertEqual(times, -1)

    def test_brevet_1000(self):
        calculate.brevet = 1000

        times = run_test(600)
        self.assertEqual(times[0], "01.01.2000 18:48")
        self.assertEqual(times[1], "01.02.2000 16:00")

        times = run_test(999)
        self.assertEqual(times[0], "01.02.2000 09:03")
        self.assertEqual(times[1], "01.04.2000 02:55")

        times = run_test(1000)
        self.assertEqual(times[0], "01.02.2000 09:05")
        self.assertEqual(times[1], "01.04.2000 03:00")

        times = run_test(1100)
        self.assertEqual(times[0], "01.02.2000 09:05")
        self.assertEqual(times[1], "01.04.2000 03:00")

        times = run_test(1101)
        self.assertEqual(times, -1)


if __name__ == '__main__':
    unittest.main()
