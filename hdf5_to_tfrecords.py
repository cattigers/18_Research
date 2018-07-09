from pathlib import Path
from np_to_tfrecords import np_to_tfrecords
import numpy as np
import h5py

def hdf5_to_np(hdf5):
    h5 = h5py.File(hdf5, 'r')
    data = h5['resnet_v2_101']
    data = data['logits']
    data = np.array(data)
    data = np.squeeze(data, axis=1)
    data = np.squeeze(data, axis=1)
    return data

if __name__ == "__main__":
    hdf5_list = Path('./hdf5').glob('*.h5')
    hdf5_list = sorted(hdf5_list)
    hdf5_list = list(map(lambda x: str(x), hdf5_list))

    for hdf5 in hdf5_list:
        result_path = Path('result/tfrecord/' + hdf5[5:-3])
        if not result_path.exists():
            result_path.mkdir(parents=True)
        data = hdf5_to_np(hdf5)
        np_to_tfrecords(data, None, 'result/tfrecord/' + hdf5[5:-3])

    print(hdf5_list)