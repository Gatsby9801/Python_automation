#get input as foldername  and creates yolo format data annotation
import numpy as np
import cv2
import MTM
from MTM import matchTemplates, drawBoxesOnRGB 
import os
import argparse
import matplotlib.pyplot as plt

input_dir = "/home/younesh/Desktop/Python_automation/dir"

def coordinatesToFile(hits, image, ih ,iw):
    coordinates = hits['BBox']
    newimagename = os.path.splitext(str(image))[0]
    newfilename = newimagename + ".txt"
    loop = len(hits.index)
    c  = 0
    file = open("class.txt", "w")
    file.write(str(c))
    for i in range(loop):
        x1, y1, w, h = coordinates[i]
        dw = 1. / iw
        dh = 1. / ih
        x = float((x1 + (x1+w))/ 2.0)
        y = float((y1 + (y1+h))/ 2.0)
        x = round(x * dw, 4)
        w = round(w * dw, 4)
        y = round(y * dh, 4)
        h = round(h * dh, 4)



        data = str(c) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) + "\n"
        file = open(newfilename, "a+")
        file.write(data)


    print(hits, newfilename)


def TemplateMmatching(tarImg, hostImg, thres):
    
    target = cv2.cvtColor(tarImg,cv2.COLOR_BGR2GRAY)
    listTarget = [('target', target)]
    host = cv2.cvtColor(hostImg,cv2.COLOR_BGR2GRAY)
    for i,angle in enumerate([90,180]):
        rotated = np.rot90(target, k=i+1) # NB: rotate not good here, turns into float!
        listTarget.append((str('target'), rotated))
    hits = matchTemplates(listTarget, host, score_threshold = thres, method=cv2.TM_CCOEFF_NORMED, maxOverlap=0)
    return hits

images = os.listdir(input_dir)
print(images)
for image in images:
    imagefile = input_dir + "/" + image
    host = cv2.imread(imagefile)
    img = cv2.cvtColor(host,cv2.COLOR_BGR2GRAY)
    h, w = img.shape
    plt.imshow(host)
    plt.show()
    thres = float(input("enter threshold:"))
    tar = cv2.imread("/home/younesh/Desktop/projects/TemplateMatching/tar007.png")
    
    hits = TemplateMmatching(tar, host, thres)# thresh = 0.326
    print(hits)
    Overlay = drawBoxesOnRGB(host, hits, showLabel=True)
    plt.imshow(Overlay)
    plt.show()
    conform = input("should we write the data to the file?(y/n)")
    if(conform == "y"):
        coordinatesToFile(hits, image, h, w)    
    while(conform == "n"):
        thres = float(input("enter threshold:"))
        hits = TemplateMmatching(tar, host, thres)# thresh = 0.326
        Overlay = drawBoxesOnRGB(host, hits, showLabel=True)
        plt.imshow(Overlay)
        plt.show()
        conform = input("should we write the data to the file?(y/n)")
        if(conform == "y"):
            coordinatesToFile(hits, image, h ,w)
        
        


            






