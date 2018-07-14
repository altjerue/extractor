import numpy as np
import h5py as h5


def hdf5ExtractScalar(h5file, dsets, group=None):
    """Extract data from an HDF5 data file.


    h5file: string
    File name.

    dsets: strings
    scalar datasets names
    """

    h5f = h5.File(h5file, 'r')
    if group is None:
        if type(dsets) is list:
            v = []
            for i in range(0, len(dsets)):
                v.append(h5f[dsets[i]][0])
            v = np.array(v)
            v = v.squeeze()
        else:
            v = h5f[dsets][0]
    else:
        if type(dsets) is list:
            v = []
            for i in range(0, len(dsets)):
                v.append(h5f[group][dsets[i]][0])
            v = np.array(v)
            v = v.squeeze()
        else:
            v = h5f[group][dsets][0]
    h5f.close()
    return v


def hdf5Extract1D(h5file, dsets, group=None):
    """Extract data from an HDF5 data file.

    h5file: string
    File name.

    ds1,ds2: strings
    1D data set names
    """
    h5f = h5.File(h5file, 'r')
    if group is None:
        if type(dsets) is list:
            v = []
            for i in range(0, len(dsets)):
                v.append(h5f[dsets[i]][:])
            v = np.array(v)
            v = v.squeeze()
        else:
            v = h5f[dsets][:]
    else:
        if type(dsets) is list:
            v = []
            for i in range(0, len(dsets)):
                v.append(h5f[group][dsets[i]][:])
            v = np.array(v)
            v = v.squeeze()
        else:
            v = h5f[group][dsets][:]
    h5f.close()
    return v


def hdf5Extract2D(h5file, dsets, group=None):
    """Extract data from an HDF5 data file.

    h5file: string
    File name.

    dsets: string or array of strings
    2D data set names
    """
    h5f = h5.File(h5file, 'r')
    if group is None:
        if type(dsets) is list:
            v = []
            for i in range(0, len(dsets)):
                v.append(h5f[dsets[i]][:, :])
            v = np.array(v)
            v = v.squeeze()
        else:
            v = h5f[dsets][:, :]
    else:
        if type(dsets) is list:
            v = []
            for i in range(0, len(dsets)):
                v.append(h5f[group][dsets[i]][:, :])
            v = np.array(v)
            v = v.squeeze()
        else:
            v = h5f[group][dsets][:, :]
    h5f.close()
    return v


def hdf5Extract3D(h5file, dsets, group=None):
    """Extract data from an HDF5 data file.

    h5file: string
    File name.

    dsets: strings or array of strings
    3D data set names
    """
    h5f = h5.File(h5file, 'r')
    if group is None:
        if type(dsets) is list:
            v = []
            for i in range(0, len(dsets)):
                v.append(h5f[dsets[i]][:, :, :])
        else:
            v = h5f[dsets][:, :, :]
    else:
        if type(dsets) is list:
            v = []
            for i in range(0, len(dsets)):
                v.append(h5f[group][dsets[i]][:, :, :])
        else:
            v = h5f[group][dsets][:, :, :]
    h5f.close()
    return v


def hdf5Extract4D(h5file, dsets, group=None):
    """Extract data from an HDF5 data file.

    h5file: string
    File name.

    dsets: strings or array of strings
    3D data set names
    """
    h5f = h5.File(h5file, 'r')
    if group is None:
        if type(dsets) is list:
            v = []
            for i in range(0, len(dsets)):
                v.append(h5f[dsets[i]][:, :, :, :])
        else:
            v = h5f[dsets][:, :, :, :]
    else:
        if type(dsets) is list:
            v = []
            for i in range(0, len(dsets)):
                v.append(h5f[group][dsets[i]][:, :, :, :])
        else:
            v = h5f[group][dsets][:, :, :, :]
    h5f.close()
    return v
