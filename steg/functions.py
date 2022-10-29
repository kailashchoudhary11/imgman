import cv2
import numpy as np
from io import BytesIO
from stegano import lsb, lsbset
from stegano.lsbset import generators


def hide_lsb(img, msg="Demo Message"):
    is_success, buffer = cv2.imencode(".png", img)
    io_buf = BytesIO(buffer)
    hid = lsb.hide(io_buf, msg)
    io_res = BytesIO()
    hid.save(io_res, "PNG")
    decode_img = cv2.imdecode(np.frombuffer(io_res.getbuffer(), np.uint8), -1)
    is_success, buffer = cv2.imencode(".png", decode_img)
    io_buf = BytesIO(buffer)
    return io_buf


def reveal_lsb(img):
    is_success, buffer = cv2.imencode(".png", img)
    io_buf = BytesIO(buffer)
    msg = lsb.reveal(io_buf)
    io_buf = BytesIO(buffer)
    return msg, io_buf


def hide_lsbset(img, msg="LSB SET Test Message"):
    is_success, buffer = cv2.imencode(".png", img)
    io_buf = BytesIO(buffer)
    secret_image = lsbset.hide(io_buf,
                               msg,
                               generators.eratosthenes())
    io_res = BytesIO()
    secret_image.save(io_res, "PNG")
    decode_img = cv2.imdecode(np.frombuffer(io_res.getbuffer(), np.uint8), -1)
    is_success, buffer = cv2.imencode(".png", decode_img)
    io_buf = BytesIO(buffer)
    return io_buf

# Use the same generator for revealing the text

def reveal_lsbset(img):
    is_success, buffer = cv2.imencode(".png", img)
    io_buf = BytesIO(buffer)
    message = lsbset.reveal(io_buf, generators.eratosthenes())
    io_buf = BytesIO(buffer)
    return message, io_buf
