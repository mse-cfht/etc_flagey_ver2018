#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='etc_flagey_2018',
      version='1.0.1',
      description='MSE Exposure Time Calculator (ETC) ver2018',
      author='Nicolas Flagey, Jennifer Sobeck',
      author_email='nflagey@stsci.edu',
      url='https://github.com/mse-cfht/etc_flagey_ver2018',
      packages=find_packages(exclude=["tests"]),
      requires=['numpy','astropy','scipy','bokeh'],
      include_package_data=True,
)


