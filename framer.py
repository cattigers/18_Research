import cv2
from pathlib import Path


def extract(video_path, result_path):
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
