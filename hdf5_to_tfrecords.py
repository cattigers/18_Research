from pathlib import Path
import numpy as np
import h5py
from np_to_tfrecords import np_to_tfrecords
from words_to_nparray import words_to_nparray

def hdf5_to_np(hdf5):
    h5 = h5py.File(hdf5, 'r')
    data = h5['resnet_v2_101']
    data = data['logits']
    data = np.array(data)
    data = np.squeeze(data, axis=1)
    data = np.squeeze(data, axis=1)

    result = np.zeros((180, 1001), dtype=np.float64)
    result[:data.shape[0], :data.shape[1]] = data

    return result

if __name__ == "__main__":


    hdf5_list = ['./hdf5/model1_%d.h5' % i for i in range (1, 6)]

    hdf5_array = [hdf5_to_np(hdf5) for hdf5 in hdf5_list]
    hdf5_array = np.array(hdf5_array)

    label_array = words_to_nparray()[0][0:5]

    # print(type(hdf5_array))
    # print(type(hdf5_array[0]))
    # print(type(hdf5_array[0][0]))


    # print(type(label_array))
    # print(type(label_array[0]))
    # print(type(label_array[0][0]))

    # exit()

    np_to_tfrecords(hdf5_array, label_array, 'result/tfrecord/model1')

    print(label_array)

    print(len(hdf5_array.shape))
    print(label_array.shape)
    print(label_array[0].shape)

    '''
    hdf5_list = Path('./hdf5').glob('*.h5')
    hdf5_list = sorted(hdf5_list)
    hdf5_list = list(map(lambda x: str(x), hdf5_list))



    for hdf5 in hdf5_list:
        result_path = Path('result/tfrecord/')

        if not result_path.exists():
            result_path.mkdir(parents=True)

        result_path = result_path / Path(hdf5).stem
        
        data = hdf5_to_np(hdf5)
        np_to_tfrecords(data, None, str(result_path))
        '''