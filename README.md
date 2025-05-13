# CANVAS

[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

![GitHub repo size](https://img.shields.io/github/repo-size/sceccode/canvas)
[![canvas-ucvm-ci Actions Status](https://github.com/SCECcode/canvas/workflows/canvas-ucvm-ci/badge.svg)](https://github.com/SCECcode/canvas/actions)


California-Nevada Adjoint Simulations (CANVAS) adjoint waveform tomography model describes 
radially anisotropic P- and S-wave speeds for California and Nevada based on publicly 
available broadband data. CANVAS was determined by optimizing the fit between observed and
synthetic data for moderate-magnitude (Mw 4.5-6.5) earthquakes that occurred within its 
domain. CANVAS effectively predicts waveform fits down to minimum periods of 12 seconds.

## Installation

This package is intended to be installed as part of the UCVM framework,
version 25.7 or higher.

## Library

The library ./lib/libcanvas.a may be statically linked into any
user application. Also, if your system supports dynamic linking,
you will also have a ./lib/libcanvas.so file that can be used
for dynamic linking. The header file defining the API is located
in ./include/canvas.h.

## Contact the authors

If you would like to contact the authors regarding this software,
please e-mail software@scec.org. Note this e-mail address should
be used for questions regarding the software itself (e.g. how
do I link the library properly?). Questions regarding the model's
science (e.g. on what paper is the CANVAS based?) should be directed
to the model's authors, located in the AUTHORS file.

## Note

 * (rho = 0.31Vp**0.25), Density is calculated from Gardner’s equation
 * A right rectangle, no rotation 


