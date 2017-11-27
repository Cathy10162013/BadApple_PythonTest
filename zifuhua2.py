
from PIL import Image
from sys import argv
import os

IMGPATH = os.getcwd()+'\\pictures\\'
WIDTH = 160
HEIGHT = 60
# OUTPUT = os.getcwd()+'\\zifuhua.txt'
IMGNUM = sum([len(x) for _, _, x in os.walk(os.path.dirname(IMGPATH+'img0.png'))])   # get the num of pictures
TXTPATH = os.getcwd()+'\\text\\'
ascii_char = list("$*+. ")   

def get_char(r,b,g,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126*r+0.7152*g+0.0722*b)
    unit = (256.0+1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    x = 0
    while x< IMGNUM:
        f = open(TXTPATH+'txt'+str(x)+'.txt','w')
        im = Image.open(IMGPATH+'img'+str(x)+'.png')
        im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
        txt = ""
        for i in range(HEIGHT):
            for j in range(WIDTH):
                txt += get_char(*im.getpixel((j,i)))
            txt += '\n'
        print('finish %d',x)
        f.write(txt)
        x = x+1
        f.close()
