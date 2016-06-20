import argparse
from astropy.io import fits

def write_fits_extension(input_fn, extension, output_fn, clobber):
    fits.open(input_fn)[extension].writeto(output_fn, clobber=clobber)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Writes a FITS extension to a new file')
    parser.add_argument('filename', help='FITS filename')
    parser.add_argument('extension', help='Extension number', type=int)
    parser.add_argument('-o', '--output', default=None,
                        metavar='FILENAME',
                        help='Output filename')
    parser.add_argument('-c', '--clobber',
                        action='store_true',
                        help='Allow the output file to be overwritten')
    args = parser.parse_args()

    if args.output is None:
        output_fn = '{}-ext{}.fits'.format(args.filename, args.extension)
    else:
        output_fn = args.output  # Whatever the user wanted

    print('Writing ' + output_fn)
    write_fits_extension(input_fn=args.filename,
                         extension=args.extension,
                         output_fn=output_fn,
                         clobber=args.clobber)

