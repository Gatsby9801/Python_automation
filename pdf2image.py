import os 
import cv2 
from PIL import Image
import PIL
from PDFNetPython import *
# from pdf2image import convert_from_path

entries = os.listdir('pdfs/')
for entry in entries:
     print(entry)
     path = "pdfs/"+ entry
     main(path)

# # convert pdf to image
# def convert_pdf2image(pdf_file):
#     images = convert_from_path(pdf_file,96)
#     for image in images:
#         i = 0
#         path = "extractedimage/" + "image" +  i + ".png"
#         print(path)
#         image.save(path, "PNG", (96,96))
#         i+=1  


def main(input_path):
    json_data = {}
    PDFNet.Initialize("DEMO:2:2F43CEE2D84c95809319B76220D054")
    draw = PDFDraw()
    doc = PDFDoc(input_path)
    doc.InitSecurityHandler()
    page_num = doc.GetPageCount()
    draw.SetDPI(96)
    itr = doc.GetPageIterator()
    for i in range(page_num):
        page = doc.GetPage(i+1)
        out_file = "extracted_image/test%s.png"%i