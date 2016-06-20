import argparse
from astropy.io import fits

def write_fits_extension(input_fn, extension, output_fn):
    fits.open(input_fn)[extension].writeto(output_fn)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Writes a FITS extension to a new file')
    parser.add_argument('filename', help='FITS filename')
    parser.add_argument('extension', help='Extension number', type=int)
    args = parser.parse_args()

    output_fn = '{}-ext{}.fits'.format(args.filename, args.extension)
    write_fits_extension(input_fn=args.filename,
                         extension=args.extension,
                         output_fn=output_fn)

