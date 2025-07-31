# California-Nevada Adjoint Simulations adjoint waveform tomography model (CANVAS)

<a href="https://github.com/sceccode/canvas.git"><img src="https://github.com/sceccode/canvas/wiki/images/canvas_logo.png"></a>

[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
![GitHub repo size](https://img.shields.io/github/repo-size/sceccode/canvas)
[![canvas-ucvm-ci Actions Status](https://github.com/SCECcode/canvas/workflows/canvas-ucvm-ci/badge.svg)](https://github.com/SCECcode/canvas/actions)

California-Nevada Adjoint Simulations adjoint waveform tomography model

This model describes radially anisotropic P- and S-wave speeds for California and Nevada 
based on publicly available broadband data. CANVAS was determined by optimizing the fit 
between observed and synthetic data for moderate-magnitude (Mw 4.5-6.5) earthquakes that 
occurred within its domain. CANVAS effectively predicts waveform fits down to minimum 
periods of 12 seconds.

Doody, C., Rodgers, A., Afanasiev, M., Boehm, C., Krischer, L., Chiang, A., & Simmons, N. (2023). CANVAS: An adjoint waveform tomography model of California and Nevada. Journal of Geophysical Research: Solid Earth, 128(12). https://doi.org/10.1029/2023JB027583

Doody, C. (2023). Dataset for 'CANVAS: An adjoint waveform tomography model of California and Nevada' [Data set]. In Journal of Geophysical Research: Solid Earth (Vol. 128, Number 12). Zenodo. https://doi.org/10.5281/zenodo.8415562

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
 * A right rectangle bounding box, no rotation 


