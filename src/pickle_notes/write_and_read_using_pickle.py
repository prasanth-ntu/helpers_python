# Title         : Write and Read data using pickle
# Date Added    : 25 Jun 2019
# Date Modified : 25 Jun 2019

import pickle as pk
import numpy as np
import os

def write_pickle_data(data, fname):

    pickle_out = open(fname, "wb")
    pk.dump(data, pickle_out)
    pickle_out.close()
    print ('[INFO] : Pickle data written successfully')

def read_pickle_data(fname):
    data_read = pk.load(open(fname, "rb"))
    print ('[INFO] : Pickle data read successfully')
    return data_read

if __name__ == '__main__':
    # Write Pickle data #
    data = {'data1': np.random.randn(10), 'data2': np.random.randn(20), 'data3':np.arange(1,11)}
    fname = os.path.join(os.getcwd(), "data.pickle")
    write_pickle_data(data, fname)

    # Reads pickle data #
    data_read = read_pickle_data(fname)
    print (data_read)
