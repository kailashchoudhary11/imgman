#!/usr/bin/python3
from PIL import Image
import binascii
import optparse
import codecs
import numpy as np
from bitstring import BitArray 

#beginning with the utility functions

#Reformats rgb value of pixel into hexadecimal
def rgb2hex(r, g, b):
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)
        
#decodes tuple of hex while stripping away the # at the beginning and revealing just rgb values
def hex2rgb(hexcode):
        if hexcode is None:
                return None
        return tuple(codecs.decode(hexcode[1:], 'hex'))
        
def hex2bit(hexcode):
        hexcode = hexcode.replace('#' , '0x')
        bitstring = BitArray(hexcode)
        return  bitstring.bin
        
def bit2hex(bitstring):
        for i in range(4, 20, 4):
            bits = '0'*i

            if(bitstring[:i] == bits):
                return '#000000'
            elif(bitstring[:i] == bits):
                hexcode = hex(int(bitstring, 2))
                hexcode = '#' + '0'*(i%4) + hexcode[2:]
                return hexcode

        if bitstring == '':
            return None
        
        hexcode = hex(int(bitstring, 2))
        hexcode = hexcode.replace('0x' , '#')
        return (hexcode)

#encodes message into byte form and then turns message into binary while ignoring the '0b' value in the beginning
def str2bin(message):
        binary = bin(int(binascii.hexlify(message.encode()), 16))
        return binary[2:]
        
#adds the '0b' back to the binary, transforms it into readable bytes and decodes it into utf-8 to be read as string
def bin2str(binary):
        binary = int(('0b' + binary), 2)
        message = binary.to_bytes((binary.bit_length() + 7) // 8, 'big').decode()
        return message

#replaces last value of the rgb hexcode with the binary digit of the message
def encode(bitstring, digit):
        bitstring = bitstring[:-1] + digit
        return bitstring
                
#looks at the last digit of the rgb hexcode and returns it to be added to binary
def decode(bitstring):
        if bitstring[-1] in ('0', '1'):
                return bitstring[-1]
        else:
                return None
                
def img2bits(filename):
        bitstring = ''
        img = Image.open(filename)
        data = img.getdata()
        for item in data:
                bitstring += hex2bit(rgb2hex(item[0], item[1], item[2]))
        return bitstring
        
def bits2img(bitstring):
        bit = 24
        newData = []
        temp = 0
        
        while(bitstring[temp:bit].format(24)):
                r, g, b = hex2rgb(bit2hex(bitstring[temp:int(bit)]))
                newData.append((r,g,b,255))
                temp = bit
                bit = bit + 24
                
        img = Image.new('RGBA', (300,300))
        img.putdata(newData)
        
        img.save("hidden_img1.jpg", 'PNG')
        return ("Your image has been saved.")
        
def hideImg(filename, filename2):
        img = Image.open(filename)
        binary = img2bits(filename2)
        #adds a breakpoint so we know where to stop
        binary = binary  + '1111111111111110111111111111111011111111111111101111111111111110'
        
        #check if img is available in rgba and convert it just in case
        if img.mode in ('RGBA'):
                img = img.convert('RGBA')
                data = img.getdata()
                
                newData = []
                temp = ''
                digit = 0
                
                #item corresponds to pixels
                for item in data:
                        #if digits is less than the binary length, create a new pixel and using encode method replace with corresponding position in binary value 
                        if(digit < len(binary)):
                                bitstring = encode(hex2bit(rgb2hex(item[0], item[1], item[2])), binary[digit])
                                newpix = bit2hex(bitstring)
                                #if failed just add pixel to the new data
                                if newpix == None:
                                        newData.append(item)
                                #if success change new pixel to rgb and add it to new data
                                else:
                                        r, g, b = hex2rgb(newpix)
                                        newData.append((r,g,b,255))
                                        digit += 1
                        #if we finished the length of the binary then just add back the normal pixels
                        else:
                                newData.append(item)

                # add the new data to the image
                img.putdata(newData)
                img.save(filename, 'PNG')
                return 'COMPLETED!'
                
        else:
                return 'Incorrect image mode, could not hide.'
                
def hide(filename, message):
        img = Image.open(filename)
        binary = str2bin(message)
        #adds a breakpoint so we know where to stop
        binary = binary  + '1111111111111110'
        
        #check if img is available in rgba and convert it just in case
        if img.mode in ('RGBA'):
                img = img.convert('RGBA')
                data = img.getdata()
                
                newData = []
                temp = ''
                digit = 0
                
                #item corresponds to pixels
                for item in data:
                        #if digits is less than the binary length, create a new pixel and using encode method replace with corresponding position in binary value 
                        if(digit < len(binary)):
                                bitstring = encode(hex2bit(rgb2hex(item[0], item[1], item[2])), binary[digit])
                                newpix = bit2hex(bitstring)
                                #if failed just add pixel to the new data
                                if newpix == None:
                                        newData.append(item)
                                #if success change new pixel to rgb and add it to new data
                                else:
                                        r, g, b = hex2rgb(newpix)
                                        newData.append((r,g,b,255))
                                        digit += 1
                        #if we finished the length of the binary then just add back the normal pixels
                        else:
                                newData.append(item)

                # add the new data to the image
                img.putdata(newData)
                img.save(filename, 'PNG')
                return 'COMPLETED!'
                
        else:
                return 'Incorrect image mode, could not hide.'
                
def retrImg(filename):
        img = Image.open(filename)
        binary = ''
        
        if img.mode in ('RGBA'):
                img = img.convert('RGBA')
                data = img.getdata()
                
                for item in data:
                        digit = decode(hex2bit(rgb2hex(item[0], item[1], item[2])))
                        if digit == None:
                                pass
                        else:
                                binary = binary + digit
                                if((binary[-64:]) == '1111111111111110111111111111111011111111111111101111111111111110'):
                                        print('Success!')
                                        return bits2img(binary[:-64])
                                        
                return bits2img(binary)
        else:
                return 'Incorrect image mode, could not retrieve.'
                
def retr(filename):
        img = Image.open(filename)
        binary = ''
        
        if img.mode in ('RGBA'):
                img = img.convert('RGBA')
                data = img.getdata()
                
                for item in data:
                        digit = decode(hex2bit(rgb2hex(item[0], item[1], item[2])))
                        if digit == None:
                                pass
                        else:
                                binary = binary + digit
                                if((binary[-16:]) == '1111111111111110'):
                                        print('Success!')
                                        return bin2str(binary[:-16])
                
                return bin2str(binary)
                
        else:
                return 'Incorrect image mode, could not retrieve.'
                
def Main():
        parser = optparse.OptionParser('usage %prog -e/-d/-i/-u <target file>')
        parser.add_option('-e', dest='hide', type='string', help='target picture path to hide text')
        parser.add_option('-d', dest='retr', type='string', help='target picture path to retrieve text')
        parser.add_option('-i', dest='hideImg', type='string', help='target picture path to hide image in another image')
        parser.add_option('-u', dest='retrImg', type='string', help='target picture path to retrieve image from another image')
        (option, args) = parser.parse_args()

        if(option.hide != None):
            text = input("Enter a message to hide: ")
            print (hide(option.hide, text))
        elif(option.retr != None):
            print (retr(option.retr))
        elif(option.hideImg != None):
            text = input("Enter the image to hide: ")
            print (hideImg(option.hideImg, text))
        elif(option.retrImg != None):
            print (retrImg(option.retrImg))
        else:
            print (parser.usage)
            exit(0)

if __name__ == '__main__':
        Main()