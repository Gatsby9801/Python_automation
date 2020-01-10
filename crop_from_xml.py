	
import re
import cv2
import glob
import os
 
data_dir = "extracted _image"
output_dir = "cropped_1"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
print("success")

for file in  os.listdir(data_dir):
	filename,ext = os.path.splitext(file)
	print(filename)
# for pathAndFilename in glob.iglob(os.path.join(data_dir, "*.xml")): 
#     print(pathAndFilename,"d") 
#     print("here")
#     title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    
#     xml_file = data_dir +"/"+title +".xml"
#     content = open(xml_file).read()

#     firstName = re.findall('<width>(.*)</width>', content)
#     filename  = (re.findall('<filename>(.*)</filename>', content))[0]

#     x1 = int ((re.findall('<xmin>(.*)</xmin>', content))[0])
#     y1 = int ((re.findall('<ymin>(.*)</ymin>', content))[0])
#     x2 = int((re.findall('<xmax>(.*)</xmax>', content))[0])
#     y2 = int ((re.findall('<ymax>(.*)</ymax>', content))[0])

#     img_file = data_dir +"/"+filename
#     img = cv2.imread(img_file)
#     print(img.shape)

#     crop_img = img[y1:y2,x1:x2]

#     out_img = output_dir+"/"+filename

#     print(out_img)

#     cv2.imwrite(out_img,crop_img)
