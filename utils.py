import numpy as np
import cv2 as cv

def frame_diff(prev_frame, cur_frame, next_frame):
    diff_frames1 = cv.absdiff(next_frame, cur_frame)
    # Absolute difference between current frame and previous frame
    diff_frames2 = cv.absdiff(cur_frame, prev_frame)
    # Return the result of bitwise 'AND' between the above two resultant images
    #gives better result than simple substraction
    return cv.bitwise_and(diff_frames1, diff_frames2)

def get_frame(cap):
    ret, frame = cap.read()
    # Resize the image if convolution made the tracking area smaller
    '''frame = cv.resize(frame, None, fx=1,
        fy=1, interpolation=cv.INTER_AREA)'''
    return frame

#finds and draws contours over pixels if greater than threshold
def construct_contours(frame, contour_threshold):
    #frame = cv.dilate(frame, (1,1), iterations=1)
    contours, hierarchy = cv.findContours(frame, cv.RETR_TREE, 
                                           cv.CHAIN_APPROX_SIMPLE)
    detections=[]
    for contour in contours:
      if cv.contourArea(contour) < contour_threshold:
        continue
      (x, y, w, h) = cv.boundingRect(contour)
      #cv.rectangle(frame, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2)
      detections.append([x,y,w,h])
    
    return detections

#applying blur 
def prepare_frames(frames,kernel):
    result = []
    for frame in frames:
        result.append(cv.GaussianBlur(frame, kernel, 0))
    return result[0], result[1], result[2]