
import img2pdf
import os
import shutil
from PyPDF2 import PdfFileReader, PdfFileWriter,PdfFileMerger

def changeToPDF(sourcePath,rootPath):
    newPath = rootPath
    for root, dirs, files in os.walk(sourcePath):
        try:
            if (files):
                print(root, files)
                os.chdir(root)
                ls = root.split("\\")
                name = ls[-1] + ".pdf"
                # os.remove(os.path.join(root,name))
                with open(name,"ab") as f:
                    f.write(img2pdf.convert(files))
                print(os.path.join(root,name))
                shutil.copyfile(os.path.join(root,name),os.path.join(newPath,name))
        except Exception:
            print(root,"处理异常")

def getFileNames(filepath='',filelist_out=[]):
    path_list = os.listdir(filepath)
    path_list.sort(key=lambda x:int(x[1:-5]))
    for filename in path_list:
        filelist_out.append(os.path.join(filepath, filename))
    return filelist_out;

def mergePDF(filepath='',output_filename='out.pdf',import_bookmarks=False):
    filelist = getFileNames(filepath)
    merger = PdfFileMerger()
    os.chdir(filepath)
    for filename in filelist:
        short_filename = os.path.basename(os.path.splitext(filename)[0])
        pdf = PdfFileReader(open(filename,'rb'))
        pageNums = pdf.getNumPages()
        merger.append(pdf,short_filename,None,import_bookmarks)
    with open(output_filename, 'wb') as fout:
        merger.write(fout)
    merger.close()


if __name__ == '__main__':
    changeToPDF("D:\\comic\\鸭子的天空\\第1卷","D:\\comic\\鸭子的天空\\pdf")