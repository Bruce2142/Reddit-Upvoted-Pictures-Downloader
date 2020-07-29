from random import shuffle

from functions.getUser import getUser
from functions.getPicsUrls import getPicsUrls
from functions.deletePics import deletePics
from functions.downloadPics import downloadPics


user = getUser()
randomOrderInput = input(
    "Dowload in random order? (y/n): ").strip().lower()

urls = getPicsUrls(user)

if(randomOrderInput == "y"):
    shuffle(urls)

deletePics()

downloadPics(urls)
print("Pics Downloaded!")
