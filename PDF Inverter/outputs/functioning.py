# importing necessary functions from module
from pdf2image import convert_from_path
from PIL import Image

def main():
    images = pdftoimage("testfiles/1.pdf")
    convert2pdf(images)


def pdftoimage(filename=None):
# Store Pdf with convert_from_path function
    try:
        if not filename:
            return convert_from_path("testfiles/3.pdf")
        return convert_from_path(filename)
    except:
        raise FileNotFoundError("File Not Found!")
    
    
def convert2pdf(images, path=None, pdfname=''):
    if path == None:
        images[0].save(
            "outputs/" + pdfname, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
        )
    else:
        if not path.endswith('.pdf'):
            images[0].save(
                path + '.pdf', "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
            )
        else:
            images[0].save(
                path + pdfname, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
            )

        
if __name__ == "__main__":
    main()