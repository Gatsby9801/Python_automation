import os
import sys
import shutil
#classes = ["0","1"]
classes = ["0","1","2","3","4","5","6"]
for cls in classes:
    if not os.path.exists(cls):
        os.makedirs(cls)
annotation_path = "rescaled_1"
for file in os.listdir(annotation_path):
    filename, ext = os.path.splitext(file)
    if ext == ".txt":
        filepath = annotation_path+"/"+file

        with open(filepath) as fp:
            line = fp.readline()
            while line:
                line_single = list(line.strip())

                txt_file = line_single[0]+'/'+file
                if not os.path.exists(txt_file):
                    img_src = annotation_path+"/"+filename+".jpg"
                    img_dst = line_single[0]+"/"+filename+".jpg"
                    shutil.copy(img_src,img_dst)
                    f= open(txt_file,"w+")
                else:
                    f =  open(txt_file, 'a') 
                    line_single[0]="0"
                    line_single = "".join(line_single)
                    line_single = line_single +"\n"
                    f.write(line_single)
                    line = fp.readline()
            
