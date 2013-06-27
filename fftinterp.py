#!/usr/bin/env python2

'''2D interpolation using zero-padding in the frequency domain
'''


from numpy import complex64, real, zeros as _zeros
from numpy.fft import fft2, ifft2, fftshift, ifftshift


__author__ = 'Mansour Moufid'
__copyright__ = 'Copyright 2013, Mansour Moufid'
__license__ = 'ISC'
__version__ = '0.1'
__email__ = 'mansourmoufid@gmail.com'
__status__ = 'Development'


def _zeropad2(x, shape):
    '''Pad a two-dimensional NumPy array with zeros along its borders
    to the specified shape.
    '''
    m, n = x.shape
    p, q = shape
    assert p > m
    assert q > n
    tb = (p - m) / 2
    lr = (q - n) / 2
    xpadded = _zeros(shape, dtype=complex64)
    xpadded[tb:tb + m, lr:lr + n] = x
    return xpadded


def interp2(array, factor):
    '''Interpolate a two-dimensional NumPy array by a given factor.
    '''
    reshape = lambda a, (x, y): [int(a * x), int(a * y)]
    newsize = reshape(factor, array.shape)
    nexteven = lambda x: x if (x % 2 == 0) else x + 1
    newsize = map(nexteven, newsize)
    newsize = tuple(newsize)
    fft = fft2(array)
    fft = fftshift(fft)
    fft = _zeropad2(fft, newsize)
    ifft = ifftshift(fft)
    ifft = ifft2(ifft)
    ifft = real(ifft)
    return ifft


if '__main__' in __name__:
    pass