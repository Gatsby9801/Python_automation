import random as rd
import os
from pdf2image import convert_from_path
 
filename = '3_.pdf'
end = 10
start = 5
for i in range(20):   
    images_from_path = convert_from_path(filename, dpi = 96, first_page = start, last_page=end)
    print("pdf converting ...")
    k = 0 
    for page in images_from_path:
        save_dir = "ectracted_image" + "test" + str(k) +".png"
        page.save(save_dir, 'PNG')
        r = rd.randrange(k + 200)            
        k = k + r
    start = start + 5
    end = end + 5
    print(str(i) + "batch complete")



      
 


