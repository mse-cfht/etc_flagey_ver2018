MSE Exposure Time Calculator 
============================================================

[![Python: 3.6](https://img.shields.io/badge/Python->3.6-blue.svg)](#)
		
Code developers and contributors:
---------------------------------
The original ETC was written and developed by Nicolas Flagey
(formerly, CFHT, currently, STScI; nflagey@stsci.edu).

Slight code modification and github reporitory building done by
Jen Sobeck (CFHT; sobeck@cfht.hawaii.edu).


Release Notes
------------
* Version 1.0  (2018)
* Version 1.1  (2022)

Requirements
------------
* Python3 (recommended as Python2 is not really supported)
* scipy 
* numpy
* astropy
* bokeh

Installation
------------
To install the package, retrieve the associate git repository and do
the following: 
  
    git clone https://github.com/mse-cfht/etc_flagey_ver2018.git
    cd etc_flagey_ver2018
    python setup.py install


Exposure Time Calculator (ETC)
------------------------------

Description
-----------
The MSE ETC ver2018 has two calculation modes: signal-to-noise (SNR)
and expsoure time. 


The ETC can be run as follows:

    python run_etc.py 


