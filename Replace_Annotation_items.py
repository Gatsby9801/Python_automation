import os
import shutil

outfile = "merged_column"
annotation_path = "1"
for file in os.listdir(annotation_path):
    filename, ext = os.path.splitext(file)
    if ext == ".txt":
    	filepath = annotation_path+"/"+file

    	with open(filepath) as fp:
        	line = fp.readline()
        	while line:
	            line_single = list(line.strip())

	            txt_file = outfile+'/'+file
	            if not os.path.exists(txt_file):
	                img_src = annotation_path+"/"+filename+".jpg"
	                img_dst = outfile+"/"+filename+".jpg"
	                shutil.copy(img_src,img_dst)
	                f= open(txt_file,"w+")
	            else:
	                f =  open(txt_file, 'a') 
	                line_single[0]="1"
	                line_single = "".join(line_single)
	                line_single = line_single +"\n"
	                f.write(line_single)
	                line = fp.readline()
