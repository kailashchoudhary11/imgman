from io import BytesIO
import cv2
import img2pdf

def blur(img):
    img = cv2.imread(img)
    blurImg = cv2.blur(img,(9,9)) 
    # blurImg = cv2.GaussianBlur(img, (11, 11), cv2.BORDER_DEFAULT)
    is_success, buffer = cv2.imencode(".png", blurImg)
    io_buf = BytesIO(buffer)
    return io_buf

def color_to_grayscale(img):
    originalImage = cv2.imread(img)
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    is_success, buffer = cv2.imencode(".png", grayImage)
    io_buf = BytesIO(buffer)
    return io_buf

def img_to_pdf(img):
    pdf = BytesIO(img2pdf.convert(img))
    return pdf

def clr_to_bw(img):
    originalImage = cv2.imread(img)
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    is_success, buffer = cv2.imencode(".png", blackAndWhiteImage)
    io_buf = BytesIO(buffer)
    return io_buf