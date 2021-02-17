from PIL import Image
import math


def roberts(imgpath, imgname):
    inputImg = Image.open(imgpath + imgname + ".JPG").convert("L")
    print(inputImg.load)
    width, height = inputImg.size
    mat = inputImg.load()

    robertsx = [[1,0],[0,-1]]
    robertsy = [[0,1],[-1,0]]

    outputImg = Image.new('L', (width, height))
    robertsMat = outputImg.load()

    for row in range(width-2):
        for col in range(height-2):
            Gx = 0
            Gy = 0
            for i in range(2):
                for j in range(2):
                    val = mat[row+i, col+j]
                    Gx += robertsx[i][j] * val
                    Gy += robertsy[i][j] * val

                robertsMat[row+1, col+1] = int(math.sqrt(Gx*Gx + Gy*Gy))

    outputImg.save("./results/" + imgname + "-roberts.jpg")


roberts("../Dataset/", 'bolt')
