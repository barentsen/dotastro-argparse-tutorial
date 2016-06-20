from setuptools import setup

setup(name='fitsextract',
      version='1.0',
      packages=['fitsextract'],
      install_requires=['astropy'],
      entry_points={
        'console_scripts': ['fitsextract = fitsextract:fitsextract_main']
        },
      )
