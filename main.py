from pathlib import Path
import framer
import tfrecorder

def main(file_names, name, video_path, label_path, result_path):
    frame_path = result_path / Path('frame')
    record_path = result_path / Path('record')
    print("Extracting frames from video...")

    for file_name in file_names:
        print(str(name / file_name))
        
        video_file = video_path / name / file_name
        label_file = label_path / name / Path(file_name.stem)
        frame_folder = frame_path / name / Path(file_name.stem)
        record_file = record_path / name / Path(file_name.stem + '.tfrecord')
        framer.extract(video_file, frame_folder)
        #print("Making TFRecords from frames...")
        #tfrecorder.record(frame_path, record_path)
    print("DONE!")


if __name__ == '__main__':
    # constants
    base = Path('./')
    video_path = base / Path('video')
    label_path = base / Path('label')
    result_path = base / Path('result')

    print("Running data preset...")

    for folder in sorted(video_path.glob('*')):

        if not folder.is_dir():
            print("%s is not a directory!" % str(folder))
            continue
        
        print(folder)

        file_names = folder.glob('*.h264')
        file_names = list(map(lambda x: Path(x.name), file_names))
        file_names = sorted(file_names)
        # print("base folder: %s, video folder: %s, label folder: %s, result path: %s" % (base, video_path, label_path, result_path))
        main(file_names, Path(folder.name), video_path, label_path, result_path)