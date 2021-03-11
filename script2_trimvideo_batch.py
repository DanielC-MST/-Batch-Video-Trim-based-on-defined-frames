# Edit：Haodong Chen  Time:2019/12/24 hc373@mst.edu https://scholar.google.com/citations?hl=en&user=WGmYDYwAAAAJ
'''
This script can clip an initial video based on the designed start-end frames obtained from the script1
'''

import cv2

# calculate length of the txt file.
def obtain_txt():
    data = []
    filename = 'train.txt'
    with open(filename, 'r') as f:

        line = f.readline()
        # len(f.readlines())
        while line:
            eachline = line.split()  ###
            read_data = [float(x) for x in eachline[0:7]]  # TopN change to float type
            lable = [int(x) for x in eachline[-1]]  # lable to int
            read_data.append(lable[0])
            # read_data = list(map(float, eachline))
            data.append(read_data)
            line = f.readline()
            length_lines = len(data)
    return data, length_lines


videoCapture = cv2.VideoCapture(r"E:\videos and images\16gestures_arrows\video\16gestures.mp4")  # shi
if __name__ == '__main__':
    data, length_lines = obtain_txt()
    fps = 30
    size = (1920, 1080)

writers = []

# construct video files
for j in range(0, length_lines):
    videoWriter = cv2.VideoWriter(r'E:\videos and images\16gestures_arrows\video\gesture_' + str(j+1) + '.avi',
                                  cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'),
                                  fps, size)
    writers.append(videoWriter)

# clip initial video based on the start and the end frames in the 'train.txt' file
i = 0
while True:
    success, frame = videoCapture.read()
    if success:
        i += 1
        # for j in range(0,2):
        for j in range(length_lines):  #
            i_start = data[j][0]
            i_end = data[j][1]
            if i_start <= i <= i_end:
                writers[j].write(frame)
    else:
        print('end')
        break


