#!/usr/bin/env python2

'''FFTresize resizes images using zero-padding in the frequency
domain.
'''

from numpy import zeros as _zeros

from avena import image, utils
from . import fftinterp


__author__ = 'Mansour Moufid'
__copyright__ = 'Copyright 2013, 2014, Mansour Moufid'
__license__ = 'ISC'
__version__ = '0.4.5'
__email__ = 'mansourmoufid@gmail.com'
__status__ = 'Development'


def resize(filename, factor=1.5):
    '''Resize an image by zero-padding in the frequency domain.

    Return the filename of the resized image.
    '''
    img = image.read(filename)
    nchannels = utils.depth(img)
    if nchannels == 1:
        new = fftinterp.interp2(img, factor)
    else:
        new = None
        for i in range(nchannels):
            rgb = img[:, :, i]
            newrgb = fftinterp.interp2(rgb, factor)
            if new is None:
                newsize = list(newrgb.shape)
                newsize.append(nchannels)
                new = _zeros(tuple(newsize))
            new[:, :, i] = newrgb
    return image.save(new, filename, random=True)


if '__main__' in __name__:
    pass
