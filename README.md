# -Batch-Video-Trim-based-on-defined-frames
# Python 3.6-3.8
# Opencv 4.1.2
The script 1 can let users extract starta-end frames by press the backspace on keyboard by go through the video in the code. Then the key frames will be saved in the txt file.
As shown below, the left number is current frame, the right number is the number of total frames of this video. 

![4](https://user-images.githubusercontent.com/61817794/110737186-83e7b000-81f2-11eb-9f41-9c8b3b41c3c1.PNG)
![5](https://user-images.githubusercontent.com/61817794/110737195-86e2a080-81f2-11eb-8510-940efaae535d.PNG)

When push backspace on the keyboard, the current frame will be saved in an txt file,'train.txt'. From the first frame, Every two adjacent frames will be a group: 1-2, 3-4, 5-6 ......... Then the txt file will be like as follows:

![image](https://user-images.githubusercontent.com/61817794/110737575-39b2fe80-81f3-11eb-8266-fc16463e6d59.png)


The script 2 can trim the initial video into multiple clips (shown as follows) based on the key frames in the txt file.


![image](https://user-images.githubusercontent.com/61817794/110737533-2869f200-81f3-11eb-99a4-6d64d68472c6.png)

Reference:
1.	“Design of a Real-Time Human-Robot Collaboration System Operated by Dynamic Gestures,” H. Chen, M. C. Leu, W. Tao and Z. Yin, Proceedings of the ASME 2020 International Mechanical Engineering Congress and Exposition (IMECE 2020), November 13-19, 2020, Portland, OR.
https://asmedigitalcollection.asme.org/IMECE/proceedings-abstract/IMECE2020/84492/V02BT02A051/1099004

2.	“Dynamic Gesture Design and Recognition for Human-Robot Collaboration with Convolutional Neural Networks,” H. Chen, W. Tao, M. C. Leu, and Z. Yin, Proceedings of the 2020 International Symposium on Flexible Automation (ISFA 2020), Jul. 5-9, 2020, Chicago, IL.
https://asmedigitalcollection.asme.org/ISFA/proceedings-abstract/ISFA2020/83617/V001T09A001/1087346
