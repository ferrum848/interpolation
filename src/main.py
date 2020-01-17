import cv2, os
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

'''
x = np.linspace(120, 1850, num=2).astype(int)
y = np.linspace(950, 1000, num=2).astype(int)
f = interp1d(y, x)

#xnew = np.linspace(120, 1850, num=43).astype(int)
ynew = np.linspace(950, 1000, num=43).astype(int)
print(ynew)
print(f(ynew).astype(int))
test = np.linspace(120, 1850, num=43).astype(int)
print(test)
plt.plot(test, ynew, 'o', f(ynew), ynew, '-')
plt.show()


vidcap = cv2.VideoCapture('1.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("result/frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  count += 1


def lin_interpolation(bbox_start, start_frame, bbox_end, end_frame):
    count_of_frames = end_frame - start_frame
    #x = np.linspace(bbox_start[0], bbox_end[0], num=2).astype(int)
    #y = np.linspace(bbox_start[1], bbox_end[1], num=2).astype(int)
    #f = interp1d(y, x)
    x_all =  np.linspace(bbox_start[0], bbox_end[0], num = count_of_frames).astype(int)
    y_all = np.linspace(bbox_start[1], bbox_end[1], num=count_of_frames).astype(int)
    #x_all = f(y_all).astype(int)
    return list(zip(x_all, y_all))


start_tl_point = (1850, 1000)
end_tl_point = (120, 950)
start_br_point = (2320, 1350)
end_br_point = (1500, 1650)
start_frame = 180
end_frame = 225

list_of_points1 = lin_interpolation(start_tl_point, start_frame, end_tl_point, end_frame)
list_of_points2 = lin_interpolation(start_br_point, start_frame, end_br_point, end_frame)

test_frames = []
for i in range(start_frame, end_frame):
    test_frames.append('frame{}.jpg'.format(i))
print(test_frames)
print(len(test_frames))

sch = 0
for frame in test_frames:
    image = cv2.imread('result/' + frame)
    image_rect = cv2.rectangle(image, list_of_points1[sch], list_of_points2[sch], (0, 0, 255), 3)
    cv2.imwrite('test/res_' + frame, image_rect)
    sch += 1


#start_tl_point = (2350, 1050)
#end_tl_point = (400, 1000)
#start_br_point = (2800, 1350)
#end_br_point = (1950, 1850)
#start_frame = 95
#end_frame = 140


start_tl_point = (2350, 1050)
end_tl_point = (2155, 1045)
start_br_point = (2800, 1350)
end_br_point = (2723, 1395)
start_frame = 95
end_frame = 101


list_of_points_tl = lin_interpolation(start_tl_point, start_frame, end_tl_point, end_frame)
list_of_points_br = lin_interpolation(start_br_point, start_frame, end_br_point, end_frame)
print(list_of_points_tl)
print(list_of_points_br)

test_frames = []
for i in range(start_frame, end_frame):
    test_frames.append('frame{}.jpg'.format(i))
print(test_frames)
print(len(test_frames))

sch = 0
for frame in test_frames:
    image = cv2.imread('result/' + frame)
    image_rect = cv2.rectangle(image, list_of_points_tl[sch], list_of_points_br[sch], (0, 0, 255), 3)
    cv2.imwrite('test/res_' + frame, image_rect)
    sch += 1
'''
#image = cv2.imread('frame40.jpg')
#image_rect = cv2.rectangle(image, (300, 550), (970, 950), (0, 255, 255), 3)
#cv2.imwrite('1.jpg', image_rect)



def lin_interpolation(bbox_start, start_frame, bbox_end, end_frame):
    count_of_frames = end_frame - start_frame
    x_all_tl =  np.linspace(bbox_start[0][0], bbox_end[0][0], num = count_of_frames).astype(int)
    y_all_tl = np.linspace(bbox_start[0][1], bbox_end[0][1], num=count_of_frames).astype(int)
    x_all_br = np.linspace(bbox_start[1][0], bbox_end[1][0], num = count_of_frames).astype(int)
    y_all_br = np.linspace(bbox_start[1][1], bbox_end[1][1], num = count_of_frames).astype(int)
    all_tl = list(zip(x_all_tl, y_all_tl))
    all_br = list(zip(x_all_br, y_all_br))
    return list(zip(all_tl, all_br))


start_tl_point = (300, 550)
end_tl_point = (1050, 500)
start_br_point = (970, 950)
end_br_point = (1300, 650)
start_frame = 40
end_frame = 61

start_points = (start_tl_point, start_br_point)
end_points = (end_tl_point, end_br_point)
all_points = lin_interpolation(start_points, start_frame, end_points, end_frame)
print(all_points)

test_frames = []
for i in range(start_frame, end_frame):
    test_frames.append('frame{}.jpg'.format(i))
sch = 0
for frame in test_frames:
    image = cv2.imread('result2/' + frame)
    image_rect = cv2.rectangle(image, all_points[sch][0], all_points[sch][1], (0, 0, 255), 3)
    cv2.imwrite('test2/res_' + frame, image_rect)
    sch += 1
