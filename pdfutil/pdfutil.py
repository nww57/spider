
import img2pdf
import os
import shutil

def changeToPDF():
    newPath = "D:\\comic\\家庭教师\\pdf"
    for root, dirs, files in os.walk("D:\\comic\\家庭教师"):
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


if __name__ == '__main__':
    changeToPDF()