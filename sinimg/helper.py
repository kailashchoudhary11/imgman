from io import BytesIO
import cv2
import img2pdf

def blur(img):
    img = cv2.imread(img)
    blurImg = cv2.blur(img,(3,3)) 
    is_success, buffer = cv2.imencode(".jpg", blurImg)
    io_buf = BytesIO(buffer)
    return io_buf

def color_to_grayscale(img):
    originalImage = cv2.imread(img)
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    is_success, buffer = cv2.imencode(".jpg", grayImage)
    io_buf = BytesIO(buffer)
    return io_buf

def img_to_pdf(img):
    pdf = BytesIO(img2pdf.convert(img))
    return pdf