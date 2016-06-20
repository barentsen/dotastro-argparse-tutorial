import click
from astropy.io import fits


def write_fits_extension(input_fn, extension, output_fn, clobber):
    fits.open(input_fn)[extension].writeto(output_fn, clobber=clobber)


@click.command()
@click.argument('filename', type=click.File('rb'))
@click.argument('extension', type=int)
@click.option('--output', help='Output filename.')
@click.option('--clobber', is_flag=True, envvar='CLOBBER',
              help='Allow the output file to be overwritten')
def fitsextract_main(filename, extension, output, clobber):
    if output is None:
        output = '{}-ext{}.fits'.format(filename.name, extension)
    click.echo('Writing {}'.format(output))
    write_fits_extension(filename, extension, output, clobber)


if __name__ == '__main__':
    fitsextract_main()
