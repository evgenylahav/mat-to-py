"""
tic toc function measuring the time passed from tic to toc
Matlab implementation:
tic;
% do something
elapsed = toc;
"""
import time


def tic() -> float:
    return time.time()


def toc(t: float) -> float:
    return time.time() - t


class Timer(object):
    """ helper class to use as context manager"""
    def __init__(self, name=None):
        self.name = name

    def __enter__(self):
        self.tstart = time.time()

    def __exit__(self, type, value, traceback):
        self.tend = time.time() - self.tstart
        if self.name:
            print('[{}]'.format(self.name))
        print('Elapsed: {}'.format(self.tend))
