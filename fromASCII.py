import numpy as np
import scipy.interpolate


def interpol(v1, v2, tt, NxM, logscale=False, rescale=False):
    """Interpolate data with not a regular grid."""
    N = NxM[0]
    M = NxM[1]
    if logscale is True:
        v1i = np.logspace(np.log10(v1.min()), np.log10(v1.max()), N)
        v2i = np.logspace(np.log10(v2.min()), np.log10(v2.max()), M)
    else:
        v1i = np.linspace(v1.min(), v1.max(), N)
        v2i = np.linspace(v2.min(), v2.max(), M)
    ti = scipy.interpolate.griddata((v1, v2), tt,
                                    (v1i[None, :], v2i[:, None]),
                                    method='cubic', rescale=rescale)
    return v1i, v2i, ti


def dataExtract3col(filename, cols=(0, 1, 2), rescale=False):
    """Extract 3 columns from a data file.

    Three columns extraction routine. Getting data ready for contour
    plotting.

    filename: string
    Name of the file with at least four columns.

    cols: Tuple
    Tuple of three int referring to the columns to be read.
    """
    return np.loadtxt(filename, usecols=cols, unpack=True)


def dataExtract2col(filename, cols=(0, 1)):
    """Extract 3 columns from a data file.

    Four columns extraction routine. Getting data ready for contour
    plotting.

    filename: string
    Name of the file with at least four columns.

    cols: tuple
    Tuple of two int referring to the columns to be read.
    """
    return np.loadtxt(filename, usecols=cols, unpack=True)
