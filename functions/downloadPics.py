import csv
import os
import requests


def downloadPics(pics):
    ignoreImageUrlsList = list(csv.reader(
        open("data/ignorePics.csv", newline="")))
    ignoreImageList = [requests.get(
        imgUrl[0]).content for imgUrl in ignoreImageUrlsList]
    removedPicCount = 0

    if(not os.path.exists("pics")):
        os.mkdir("pics")

    for i in range(len(pics)):
        print("\rSaving Picture " + str(i + 1) + "/" + str(len(pics)), end="")
        imgData = requests.get(pics[i]).content
        successfulPicDownload = downloadPic(
            imgData, ignoreImageList, i - removedPicCount)
        if(not successfulPicDownload):
            removedPicCount += 1
    print("\r")


def downloadPic(imgData, ignoreImageList, imageNumber):
    for ignoreImage in ignoreImageList:
        if(imgData == ignoreImage):
            return(False)
    open("pics/" + str(imageNumber) + ".jpg", 'wb').write(imgData)
    return(True)
