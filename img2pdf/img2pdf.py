

import img2pdf
from PIL import Image
import os

if __name__ == '__main__':
    # storing image path
    img_path = "D:\\comic\\家庭教师\\第1话\\00001.jpg"

    # storing pdf path
    pdf_path = "D:\\comic\\家庭教师\\第1话\\第一话.pdf"

    # opening image
    image = Image.open(img_path)

    # converting into chunks using img2pdf
    pdf_bytes = img2pdf.convert(image.filename)

    # opening or creating pdf file
    file = open(pdf_path, "wb")

    # writing pdf files with chunks
    file.write(pdf_bytes)

    # closing image file
    image.close()

    # closing pdf file
    file.close()

    # output
    print("Successfully made pdf file")
