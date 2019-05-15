
import img2pdf
import os

if __name__ == '__main__':
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
        except Exception:
            print(root,"处理异常")