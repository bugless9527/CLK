#提取目录下所有图片,更改尺寸后保存到另一目录
from PIL import Image
import os.path
import glob
def convertjpg(jpgfile,outdir,width=500):
    img=Image.open(jpgfile)
    wid=img.size[0]
    hei=img.size[1]
    height=500*hei//wid
    try:

        new_img=img.resize((width,height),Image.BILINEAR)   
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)

for jpgfile in glob.glob("./img/*.jpg"):
    convertjpg(jpgfile,"./output")

