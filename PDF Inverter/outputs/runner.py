import sys
from PIL import Image, ImageChops
from functioning import pdftoimage, convert2pdf

def main():
    # Checking for errors
    if len(sys.argv) != 2:
        filename = input("Enter the file's name : ")
    else:
        filename = sys.argv[1]
        
    images = pdftoimage(filename)
    
    if not images:
        raise FileNotFoundError("File not found")
    
    invimages = invertimages(images)
    
    convert2pdf(invimages)
    


def get_images(filename):
    return pdftoimage(filename)


def invertimages(images):
    invimages = []
    for image in images:
        # Passing the image object to invert()
        invimages.append(ImageChops.invert(image))
    return invimages


if __name__ == "__main__":
    main()