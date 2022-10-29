from io import BytesIO
import cv2
import img2pdf
import numpy

def blur(img):
    
    blurImg = cv2.blur(img,(9,9)) 
    is_success, buffer = cv2.imencode(".png", blurImg)
    io_buf = BytesIO(buffer)
    return io_buf

def color_to_grayscale(img):

    originalImage = img
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    is_success, buffer = cv2.imencode(".png", grayImage)
    io_buf = BytesIO(buffer)
    return io_buf

def img_to_pdf(img):

    is_success, buffer = cv2.imencode(".png", img)
    io_buf = BytesIO(buffer)
    pdf = BytesIO(img2pdf.convert(io_buf))
    return pdf

def clr_to_bw(img):
    
    originalImage = img
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    is_success, buffer = cv2.imencode(".png", blackAndWhiteImage)
    io_buf = BytesIO(buffer)
    return io_buf

def sharp(img):
    kernel = numpy.array([[0,-1,0],[-1,7,-1],[0,-1,0]])
    img_sharp = cv2.filter2D(src=img, ddepth=-1, kernel=kernel )
    is_success, buffer = cv2.imencode(".png", img_sharp)
    io_buf = BytesIO(buffer)
    return io_buf

def resize(img, width=None, height=None):

    if width is None:
        width = img.shape[1] // 2
    if height is None:
        height = width // 4 * 3
    
    originalImage = img
    resizedImage = cv2.resize(originalImage, (width, height))
    issuccess, buffer = cv2.imencode(".png", resizedImage)
    io_buf = BytesIO(buffer)
    return io_buf

def encrypt_image(img, key=123):
    '''
    Expects to get an image that is to be encrypted
    '''
    xor_encrypted_img = cv2.bitwise_xor(img, key)
    is_success, buffer = cv2.imencode(".png", xor_encrypted_img)
    io_buf = BytesIO(buffer)
    return io_buf

def decrypt_image(img, key=123):
    '''
    Expects to get an image that was encrypted earlier
    '''
    xor_decrypted_img = cv2.bitwise_xor(img, key)
    is_success, buffer = cv2.imencode(".png", xor_decrypted_img)
    io_buf = BytesIO(buffer)
    return io_buf
