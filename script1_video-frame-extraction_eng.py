# Edit：Haodong Chen  Time:2019/12/24 hc373@mst.edu https://scholar.google.com/citations?hl=en&user=WGmYDYwAAAAJ

'''
    This script is designed for the video frame extraction and save into on the txt file (key frames).
    Input is the video including more than one gestures, the output will be start and the end frames of these gestures
    fps is 30 frames/second, size is 1920*1080,
    The result will be saved in a txt file named as 'Train.txt' where the first column shows the start frames,
    the second one represents the end frames.Remember put a done txt file in another folder otherwise the frame
    information of two videos might be in a same txt file.
    Just change the video path, use backspace to pause and record a frame. After several times, you can write some key
    frames for yourself for the final review.

'''

import cv2

# ————————input video———————————
video_path = r"test.mp4"
video_capture = cv2.VideoCapture(video_path)

# read the fps,  size
fps = video_capture.get(cv2.CAP_PROP_FPS)
size = (video_capture.get(cv2.CAP_PROP_FRAME_WIDTH), video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("fps: {}\nsize: {}".format(fps, size))

# read the number of frames
total = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
print("[INFO] {} total frames in video".format(total))

# set the start frame
frameToStart = 1
video_capture.set(cv2.CAP_PROP_POS_FRAMES, frameToStart)

# display the video
timesof = 0
current_frame = frameToStart
while True:
    success, frame = video_capture.read()
    if success == False:
        break
    # image size
    h, w = frame.shape[:2]  # channels
    size = (int(w * 0.5), int(h * 0.5))
    frame = cv2.resize(frame, size)
    # --------keyboard control---------------
    # read the value of keyboard
    key = cv2.waitKey(25) & 0xff
    # stop by space bar and record the frame
    with open('train.txt', 'a') as f:  # open an train.txt, if there is no file, create one
        if key == ord(" "):
            cv2.waitKey(0)
            now_seconds = str(current_frame - 1)  # / fps % 60q
            f.write(now_seconds + "\t")
            timesof += 1
            print(timesof)
            if timesof % 2 == 0:
                f.write('\n')
        # 'q' button can drop out
        if key == ord("q"):
            break
    # show the frames and calculation
    now_seconds = int(current_frame)  # / fps % 60q
    now_minutes = int(current_frame)  # / fps / 60
    total_second = int(total)  # / fps % 60
    total_minutes = int(total)  # / fps / 60
    #   { <label> : <filling> <aligned）> <width> <,> <.accuracy> <style>}.
    Time_now_vs_total = "Time:{:>02}|{:0>2}".format(now_seconds, total_second)

    cv2.putText(frame, Time_now_vs_total, (300, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
    cv2.imshow("frame", frame)
    #
    current_frame += 1
print(timesof % 2)
video_capture.release()
