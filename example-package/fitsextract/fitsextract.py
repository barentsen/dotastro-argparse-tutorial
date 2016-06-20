"""Demonstrates the creation of a command-line tool using argparse.
"""
import argparse
from astropy.io import fits


def write_fits_extension(input_fn, extension, output_fn, clobber=False):
    """Writes a single extension from a FITS file to a new FITS file."""
    fits.open(input_fn)[extension].writeto(output_fn, clobber=clobber)


def fitsextract_main():
    """Defines the fitsextract command-line tool using argparse."""
    parser = argparse.ArgumentParser(description='Create a new FITS file '
                                                 'containing one extension '
                                                 'from an existing FITS file.')
    parser.add_argument('filename',
                        help='path to a FITS file')
    parser.add_argument('extension', type=int,
                        help='the FITS extension number')
    parser.add_argument('-o', '--output', metavar='FILENAME', default=None,
                        help='Output filename')
    parser.add_argument('-c', '--clobber', action='store_true',
                        help='Overwrite the output file if it already exists')
    # Add a --verbose and --quiet option, but don't allow both at the same time
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', action='store_true')
    group.add_argument('-q', '--quiet', action='store_true')
    args = parser.parse_args()

    if args.output is None:
        output_fn = '{}-ext{}.fits'.format(args.filename, args.extension)
    else:
        output_fn = args.output

    if args.verbose:
        print('Opening {}#{}'.format(args.filename, args.extension))
    if not args.quiet:
        print('Writing {}'.format(output_fn))

    write_fits_extension(input_fn=args.filename,
                         extension=args.extension,
                         output_fn=output_fn,
                         clobber=args.clobber)

if __name__ == '__main__':
    fitsextract_main()
