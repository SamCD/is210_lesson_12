==========================================
IS 210: Software Application Programming I
==========================================
------------
Homework #12
------------

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Available: 2014-11-10T09:00:00-0400
:Due-Date: 2014-11-17T09:00:00-0400

Overview
========

This week, we learn about benchmarking Python programming techniques. Just
because your code works doesn't mean it is the optimal solution. Sometimes
you have to evaluate two or more solution to the same problem and decide
which works better for your purposes.

Pi Are Round
============

The task assignments this week are built around the material covered in the
text reading. You will create a benchmark class based on the examples show in
the ``timer2.py`` of reading assignment.

Task 01: Create the Benchmark Class
-----------------------------------

In this exercise you'll be creating a class object to handle benchmark
testing of the provided Pi calculation formulas.

Specifications
^^^^^^^^^^^^^^

#.  Open ``pi_r_round.py``.

#.  Create a class named ``Timer2Class``.

#.  Define a public *class attribute* named ``timer``. The ``timeit`` module's
    ``default_timer`` property to provide you the correct timer function.

#.  Create a class constructor function. Have it accept the following arguments:

    #.  ``func``

    #.  ``*args``

    #.  ``**kwargs``

    These arguments should be assigned to class attributes of the same name.

Task 02: Adapt the ``total`` Function Into Class Method
-------------------------------------------------------

Study how the author coded his ``def total``. Adapt it to work within the
``Timer2Class`` object.

Specifications
^^^^^^^^^^^^^^

#.  Create a public class method named ``total``.

#.  Adapt the text's example to work within the class as a method.

#.  Return the elapsed time and the evaluated function's return value.

Task 03: Adapt the ``bestof`` Function Into Class Method
--------------------------------------------------------

Now port over the code for the ``bestof`` function and modify it to work as a
method of the ``Timer2Class`` object.

Specifications
^^^^^^^^^^^^^^

#.  Create a public class method named ``bestof``.

#.  Adapt the text's example to work within the class as a method.

#.  Return the elapsed time and the evaluated function's return value.

Task 04: Adapt the ``bestoftotal`` Function Into Class Method
-------------------------------------------------------------

Adapt the ``bestoftotal`` example code from the text to use inside your
``Timer2Class``.

Specifications
^^^^^^^^^^^^^^

#.  Create a public class method named ``bestoftotal``.

#.  Adapt the text's example to work within the class as a method.

#.  Return the evaluated function name, elapsed time and the evaluated
    function's return value.

.. tip::

    You can retrieve the name of a function object using the ``func.__name__``
    built-in method.


Task 05: Main Program Execution
-------------------------------

Use the ``if __name__ == "__main__":`` technique to instantiate the
``Timer2Class`` object and consume the four Pi functions for benchmark
performance evaluation.

Specifications
^^^^^^^^^^^^^^

#.  Append the following code to the end of your program file.

.. code-block:: python

    if __name__ == "__main__":

        n = 1000

        for test in (stdlib, bbp, bellard, chudnovsky):
            timer2 = Timer2Class(test, n, _reps1=1, _reps=3)
            print timer2.bestoftotal()

#.  Example output of your program should look like:

.. code-block:: console

    $ python pi_r_round.py
    ('stdlib', (0.20364809036254883, '3.141592653589793127002456641'))
    ('bbp', (0.3437209129333496, '3.141592653589793238462643381'))
    ('bellard', (0.7685971260070801, '3.141592653589793238462643383'))
    ('chudnovsky', (23.97059988975525, Decimal('3.141592653589793238462643384')))


Submission
==========

Code should be submitted to `GitHub`_ by means of opening a pull request.

As-of Lesson 02, each student will have a branch named after his or her
`GitHub`_ username. Pull requests should be made against the branch that
matches your `GitHub`_ username. Pull requests made against other branches will
be closed.  This work flow mimics the steps you took to open a pull request
against the ``pull`` branch in Lesson 01.

For a refresher on how to open a pull request, please see homework instructions
in Lesson 01. It is recommended that you run PyLint locally after each file
is edited in order to reduce the number of errors found in testing.

In order to receive full credit you must complete the assignment as-instructed
and without any violations (reported in the build status). There will be
automated tests for this assignment to provide early feedback on program code.

When you have completed this assignment, please post the link to your
pull request in the body of the assignment on Blackboard in order to receive
credit.

.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
