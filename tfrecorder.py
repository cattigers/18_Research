import tensorflow as tf
from pathlib import Path
from PIL import Image
import numpy as np

def record(frame_folder, label_folder, record_path):
    print()
    
    frame_paths = sorted(frame_folder.glob('*.png'))
    frame_names = list(map(lambda x: str(x), frame_paths))

    label_paths = sorted(label_folder.glob('*.txt'))
    label_names = list(map(lambda x: str(x), label_paths))

    print(frame_names)
    print(label_names)

    writer = tf.python.io.TFRecordWriter(str(record_path))

    for image_path in frame_names:
        img = Image.open(image_path)
        print(img)

    writer.close()
    return
