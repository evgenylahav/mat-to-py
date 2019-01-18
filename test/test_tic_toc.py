import unittest, time
from src.tic_toc import tic, toc, Timer


class TestTicToc(unittest.TestCase):
    def test_tic_toc(self):
        pause = 2
        t = tic()
        time.sleep(pause)
        elapsed = toc(t)

        self.assertAlmostEqual(elapsed, pause, places=1)

    def test_helper_class(self):
        pause = 2
        timer = Timer('foo_stuff')
        with timer:
            time.sleep(pause)

        self.assertAlmostEqual(timer.tend, pause, places=1)

