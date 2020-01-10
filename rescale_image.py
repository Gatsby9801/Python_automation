import cv2
import numpy as np 
import os 

def resize_image(img_path,factor,out_path):
        img =  cv2.imread(img_path)
        w,h,_ = img.shape
        dim = (int(h/factor) ,int(w/factor))
        
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        cv2.imwrite(out_path,resized)
        print("image saved..")


source = "cropped_1"
for file in os.listdir(source):
    img_file = source+"/"+ file
    factor = 2
    outfile = "test/"+file
    resize_image(img_file,factor,outfile)
