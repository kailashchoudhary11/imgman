## Preamble
* The code is an example of Steganography using images.
* It is a python program that hides information in 'png' pictures.
* Allows for hiding and retrieving of text inside a .PNG picture.

## Working
* It opens the image and analyzes the pixel in hexadecimal.
* If the pixel value blue channel falls in the 0-5 range then 1 bit of info is stored.
* When it is time to retrieve the text it pulls all the blue bits of 1's & 0's.

## Program
* Our main objective is to handle the arguments and whether to store it or retrieve.
* Four operation functions:
    <ol>
        <li>Encode</li>
        <li>Decode</li>
        <li>Hide</li>
        <li>Retr</li>
    </ol>

### You will need the ```Pillow``` module for this code:
* Pillow is built on top of the well-known PIL ( Python Image Library) module.
* It is one of the most important modules for image processing. 

```bash
pip install pillow 
```

## Steganography
* Argument Options: -e Hide a string in an image -d Retrieve a string from an image 
-i Hide an image in another image -u Retrieve an image from another image.
* All arguments options must be followed by an image Filename or Path

<ol>
    <li>Download the file and navigate to the respective folder.</li>
    <li>Run the command "Python Hide,py" followed by the respective commands found above.</li>
    <li>You will be prompted to enter a message or another image filename (for the image include it's extension and its filepath if needed).</li>
    <li>You will have your hidden message!</li>
</ol>

