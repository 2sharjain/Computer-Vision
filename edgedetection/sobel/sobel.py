from PIL import Image
import math


def sobel(imgpath, imgname):
    inputImg = Image.open(imgpath + imgname + ".JPG").convert("L")
    print(inputImg.load)
    width, height = inputImg.size
    mat = inputImg.load()

    sobelx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    sobely = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]

    outputImg = Image.new('L', (width, height))
    sobelMat = outputImg.load()

    for row in range(width-3):
        for col in range(height-3):
            Gx = 0
            Gy = 0
            for i in range(3):
                for j in range(3):
                    val = mat[row+i, col+j]
                    Gx += sobelx[i][j] * val
                    Gy += sobely[i][j] * val

                sobelMat[row+1, col+1] = int(math.sqrt(Gx*Gx + Gy*Gy))

    outputImg.save("./results" + imgname + "-sobel.jpg")


sobel("../Dataset/", 'bolt')
