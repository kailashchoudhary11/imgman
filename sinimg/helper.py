import img2pdf
from io import BytesIO
import cv2
from PIL import Image, ImageFilter
import re

def blur(img):
    before = Image.open(img)
    ext = re.search("^.*", img)
    print(ext)
    after = before.filter(ImageFilter.BoxBlur(2))
    return BytesIO(after.save("demo.png"))

def color_to_bw(img):
    # originalImage = cv2.imread("media\\images\\topdf\\jocxdgk424i91_aA7wkN6.webp")
    originalImage = cv2.imread(img)
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    
    # cv2.imshow('Original image',originalImage)
    # cv2.imshow('Black white image', blackAndWhiteImage)
    # cv2.imshow('Gray image', grayImage)
    return BytesIO(grayImage)    

def img_to_pdf(img):
    pdf = BytesIO(img2pdf.convert(img))
    return pdf