# .Astronomy8 Day 0: Python Argparse Tutorial

Python's `argparse` module makes it easy to write user-friendly command-line interfaces. It is the recommended command-line parsing module in the Python standard library.

This repository holds files related to a short `argparse` tutorial
I prepared for the [.Astronomy8 conference](dotastronomy.com/events/eight/).


Installation
------------
`argparse` is part of Python's standard library, meaning you don't need to install anything apart from a basic Python environment!


Basics
------
Command-line arguments are passed to Python programs via `sys.argv`:

    import sys
    print(sys.argv)

The `argparse` module provides a mechanism to define the arguments a program requires and takes care of parsing those out of sys.argv.  Let's start with a simple example:

    import argparse
    parser = argparse.ArgumentParser()
    parser.parse_args()

Running the above example, you will note that `argparse` automatically generates help and usage messages and issues errors when users give the program invalid arguments. 


Positional arguments
--------------------
The first type of arguments `argparse` can parse are positional arguments.
They derive their name from the fact that a program should know what to do
with the arguments based solely on where it appears on the command line.

An example:

    import argparse
    parser = argparse.ArgumentParser(description='Create a new FITS file '
                                                 'containing one extension '
                                                 'from an existing FITS file.')
    parser.add_argument('filename',
                        help='path to a FITS file')
    parser.add_argument('extension', type=int,
                        help='the FITS extension number')
    args = parser.parse_args()
    print(args.filename)


Optional arguments
------------------
Optional arguments allow the user to change behaviour of a program using optional flags or parameters.

An example:

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help='increase verbosity')
    args = parser.parse_args()
    if args.verbosity:
        print('verbose turned on')


Advanced contents of the tutorial
---------------------------------
- Mutually exclusive arguments
- [How does AstroPy add its tools to the command line](https://github.com/astropy/astropy/blob/master/setup.py#L55).
- Demo: add your tools as an executable to the command line using `setup.py`.

Futher reading
--------------
* [A comparison of different command-line parsing libraries](https://realpython.com/blog/python/comparing-python-command-line-parsing-libraries-argparse-docopt-click/)
