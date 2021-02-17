from PIL import Image
import math


def prewitt(imgpath, imgname):
    inputImg = Image.open(imgpath + imgname + ".JPG").convert("L")
    print(inputImg.load)
    width, height = inputImg.size
    mat = inputImg.load()

    prewittx = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
    prewitty = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]

    outputImg = Image.new('L', (width, height))
    prewittMat = outputImg.load()

    for row in range(width-2):
        for col in range(height-2):
            Gx = 0
            Gy = 0
            for i in range(2):
                for j in range(2):
                    val = mat[row+i, col+j]
                    Gx += prewittx[i][j] * val
                    Gy += prewitty[i][j] * val

                prewittMat[row+1, col+1] = int(math.sqrt(Gx*Gx + Gy*Gy))

    outputImg.save("./results/" + imgname + "-prewitt.jpg")


prewitt("../Dataset/", 'bolt')
