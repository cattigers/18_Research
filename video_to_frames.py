import cv2
from pathlib import Path


def video_to_frames(video_path, result_path):
    print()

    if not result_path.exists():
        result_path.mkdir(parents=True)

    if not video_path.exists():
        print(video_path)
        print("Video does not exist!")
        return

    vidcap = cv2.VideoCapture(str(video_path))

    if not vidcap.isOpened():
        print("Somehow, VideoCapture didn't worked.")
        return

    success, image = vidcap.read()
    count = 0
    while success:
        frame_path = Path("frame%05d.png" % count)
        cv2.imwrite(str(result_path / frame_path), image)
        success, image = vidcap.read()
        count += 1

    print()
    print("Extracted %d frames from %s." % (count, str(video_path)))    
    print("Frames are saved at: %s" % str(result_path))
    print()
    return


if __name__ == "__main__":
    video_list = Path('./video/').glob('**/*.h264')
    video_list = list(map(lambda x: str(x), video_list))
    video_list = sorted(video_list)

    for video in video_list:
        result = Path(video).parts
        result = list(result)
        result[0] = 'result'
        result[-1] = Path(Path(video).stem)
        result = Path(*result)
        print(result)
        print(video)
        video_to_frames(Path(video), Path(result))

    # video_to_frames()