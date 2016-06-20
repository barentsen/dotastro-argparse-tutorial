import click
from astropy.io import fits


@click.command()
@click.argument('input_fn', type=click.File('rb'))
@click.argument('extension', type=int)
@click.option('--output_fn', help='Output filename.')
@click.option('--clobber', is_flag=True, envvar='CLOBBER',
              help='Allow the output file to be overwritten')
def fitsextract(input_fn, extension, output_fn=None, clobber=False):
    if output_fn is None:
        output_fn = '{}-ext{}.fits'.format(input_fn.name, extension)
    click.echo('Writing {}'.format(output_fn))
    fits.open(input_fn)[extension].writeto(output_fn, clobber=clobber)


if __name__ == '__main__':
    fitsextract()
