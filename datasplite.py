import os
import cv2

video_url = "E:/save_video/"
data_url = "E:/save_video/dataset/"  # 数据集
video_name = os.listdir(video_url)[:-4]
for i in range(len(video_name)):
    singal_url = video_url + video_name[i]
    write_name = video_name[i][:-4]
    print(singal_url)
    cap = cv2.VideoCapture(singal_url)
    frame_count = 1
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            if frame_count % 25 == 0:
                cv2.imwrite(data_url + write_name + "_%d.jpg" % frame_count, frame)
                print(frame_count)
            frame_count += 1
        else:
            cap.release()
            break