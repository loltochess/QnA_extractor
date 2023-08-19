import cv2
import os

from pytube import YouTube
DOWNLOAD_FOLDER = "/yt2frame/videos"
url = "https://www.youtube.com/watch?v=pFKxTlAQiy8"
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download(DOWNLOAD_FOLDER)

filepath = '/content/drive/MyDrive/videos/20만 구독자 기념 준빵조교 Q&A.mp4'
video = cv2.VideoCapture(filepath)

#불러온 비디오 파일의 정보 출력
length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv2.CAP_PROP_FPS)

print("length :", length)
print("width :", width)
print("height :", height)
print("fps :", fps)

#프레임을 저장할 디렉토리를 생성
try:
    if not os.path.exists(filepath[:-4]):
        os.makedirs(filepath[:-4])
except OSError:
    print ('Error: Creating directory. ' +  filepath[:-4])

count = 0

while(video.isOpened()):
    if int(video.get(1)) >= length : break
    ret, image = video.read()
    if(int(video.get(1)) % round(fps) == 0): #앞서 불러온 fps 값을 사용하여 1초마다 추출
        cv2.imwrite(filepath[:-4] + "/frame%d.jpg" % count, image)
        print('Saved frame number :', str(count))
        count += 1
