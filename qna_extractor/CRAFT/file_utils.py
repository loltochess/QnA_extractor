# -*- coding: utf-8 -*-
import os
import numpy as np
import cv2
import imgproc

# borrowed from https://github.com/lengstrom/fast-style-transfer/blob/master/src/utils.py
def get_files(img_dir):
    imgs, masks, xmls = list_files(img_dir)
    return imgs, masks, xmls

def list_files(in_path):
    img_files = []
    mask_files = []
    gt_files = []
    for (dirpath, dirnames, filenames) in os.walk(in_path):
        for file in filenames:
            filename, ext = os.path.splitext(file)
            ext = str.lower(ext)
            if ext == '.jpg' or ext == '.jpeg' or ext == '.gif' or ext == '.png' or ext == '.pgm':
                img_files.append(os.path.join(dirpath, file))
            elif ext == '.bmp':
                mask_files.append(os.path.join(dirpath, file))
            elif ext == '.xml' or ext == '.gt' or ext == '.txt':
                gt_files.append(os.path.join(dirpath, file))
            elif ext == '.zip':
                continue
    # img_files.sort()
    # mask_files.sort()
    # gt_files.sort()
    return img_files, mask_files, gt_files

def saveResult(img_file, img, boxes, duplicated, dirname='./result/', verticals=None, texts=None):
        """ save text detection result one by one
        Args:
            img_file (str): image file name
            img (array): raw image context
            boxes (array): array of result file
                Shape: [num_detections, 4] for BB output / [num_detections, 4] for QUAD output
            duplicated : array of duplicated text box
        Return:
            None
        """
        img = np.array(img)

        # make result file list
        filename, file_ext = os.path.splitext(os.path.basename(img_file))


        if not os.path.isdir(dirname):
            os.mkdir(dirname)
        
        
        for i, box in enumerate(boxes):
            if duplicated[i]==False : continue
            poly = np.array(box).astype(np.int32).reshape((-1))
            poly = poly.reshape(-1, 2)
            original_width, original_height=poly[1][0]-poly[0][0], poly[3][1]-poly[0][1]
            poly = poly.reshape(-1,1,2)
            

             # 변환 전 4개의 꼭지점
            #cv2.polylines(img, poly, isClosed=True, color=(0, 0, 255), thickness=2) #[[x1 y1] [x2 y2] [x3 y3] [x4 y4]] -> 좌상 우상 우하 좌하  
 
            #print(original_width, original_height)
             # 원근 변환 행렬 계산
            #width, height = int(original_width*64/original_height), 64  # 새로운 이미지의 너비와 높이
            width,height = original_width, original_height
            new_coords = np.array([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]], dtype=np.float32)
            h, status = cv2.findHomography(poly,new_coords)

             # 이미지 원근 변환 적용
            new_image = cv2.warpPerspective(img, h, (width, height))   
            # 잘라낸 이미지 저장
            cv2.imwrite(f"result/{filename}_{i}.png", new_image)  # 파일 경로를 원하는 저장 경로로 변경하세요
            

