#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
is210 Section 01 Week 12

Bench marking methods

Works Cited:

    The following Pi calculation functions were sourced from the "Captian
    DeadBones Chronicles" blog posting "Computing Pi With Python".

    http://thelivingpearl.com/2013/05/28/computing-pi-with-python/

    Minor changes were made to conform with lesson plan.

"""

import math
from decimal import *
import time
import sys


def stdlib(depth):
    """
    Calculate Pi using the math.pi from Python standard library

    :param depth:
    :return:
    """
    a = Decimal(1.0)
    b = Decimal(1.0 / math.sqrt(2))
    t = Decimal(1.0) / Decimal(4.0)
    p = Decimal(1.0)

    for i in range(depth):
        at = Decimal((a + b) / 2)
        bt = Decimal(math.sqrt(a * b))
        tt = Decimal(t - p * (a - at) ** 2)
        pt = Decimal(2 * p)

        a = at
        b = bt
        t = tt
        p = pt

    pi = (a + b) ** 2 / (4 * t)

    return str(pi)


def bbp(depth):
    """
    Calculate Pi using the Bailey–Borwein–Plouffe formula
    http://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula

    :param depth:
    :return:
    """
    pi = Decimal(0)
    k = 0
    while k < depth:
        pi += (Decimal(1) / (16 ** k)) * (
            (Decimal(4) / (8 * k + 1)) -
            (Decimal(2) / (8 * k + 4)) -
            (Decimal(1) / (8 * k + 5)) -
            (Decimal(1) / (8 * k + 6))
        )
        k += 1
    return str(pi)


def bellard(depth):
    """
    New school Pi calculation method discovered in 1997 by Fabrice Bellard in
    1997. Usually clocks in 43% faster than the BBP formula.

    http://en.wikipedia.org/wiki/Bellard%27s_formula

    :param depth:
    :return:
    """
    pi = Decimal(0)
    k = 0
    while k < depth:
        pi += (Decimal(-1) ** k / (1024 ** k)) * (
            Decimal(256) / (10 * k + 1) +
            Decimal(1) / (10 * k + 9) -
            Decimal(64) / (10 * k + 3) -
            Decimal(32) / (4 * k + 1) -
            Decimal(4) / (10 * k + 5) -
            Decimal(4) / (10 * k + 7) -
            Decimal(1) / (4 * k + 3)
        )
        k += 1
    pi = pi * 1 / (2 ** 6)
    return str(pi)


def chudnovsky(depth):
    """
    World record holding formula for calculating 5 trillion digits of Pi in
    August 2010. It's a heavy hitter on CPU. This one is about quality over
    quantity.

    http://en.wikipedia.org/wiki/Chudnovsky_algorithm

    :param depth:
    :return:
    """
    pi = Decimal(0)
    k = 0
    while k < depth:
        pi += (Decimal(-1) ** k) * (
            Decimal(math.factorial(6 * k)) /
            (
                (math.factorial(k) ** 3) * (math.factorial(3 * k))
            ) * (13591409 + 545140134 * k) /
            (640320 ** (3 * k))
        )
        k += 1
    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi **= -1
    return pi

class Timer2Class(object):
    """Creates timer class"""

    import timeit
    timer = timeit.default_timer

    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    import time, sys


    def total(self, func, *args, **kwargs):
        """Alternative timer
        Calls and times func(*pargs, **kargs) _reps time and returns
        total time for all runs, with final result."""
        self._reps = kargs.pop('_reps', 1000)
        self.repslist = list(range(_self.reps))
        self.start = self.timer()
        for i in repslist:
            ret = func(*args, **kwargs)
        self.elapsed = self.timer() - self.start
        return (self.elapsed, ret)


    def bestof(self, func, *args, **kwargs):
        """Finds best time
        Runs best-of-N timer to attempt to filter out system load variation,
        and returns total time for all runs, with final results."""
        self._reps = kwargs.pop('_reps', 5)
        self.best = 2 **32
        for i in range(self._reps):
            start = self.timer()
            ret = func(*args, **kwargs)
            elapsed = self.timer() - start
            if elapsed < self.best: self.best = elapsed
        retrn (self.best, ret)


    def bestoftotal(self, func, *args, **kwargs):
        """Runs best-of-totals test, which takes the best among _reps1 runs
        of (the total of _reps runs)"""
        self._reps1 = kwargs.pop('reps1', 5)
        funcname = func.__name__
        for i in range(self._reps1):
            ret = func(*args, **kwargs)
        return funcname,\
               min(self.total(func, *args, **kwargs)
                   for i in range(self.reps1)),\
                   ret

if __name__ == "__main__":

    n = 1000

    for test in (stdlib, bbp, bellard, chudnovsky):
        timer2 = Timer2Class(test, n, _reps1=1, _reps=3)
        print timer2.bestoftotal()
