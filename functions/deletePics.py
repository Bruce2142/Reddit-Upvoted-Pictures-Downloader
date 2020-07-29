import os


def deletePics():
    if(os.path.exists("pics")):
        for picFile in os.listdir("pics"):
            picFilePath = os.path.join("pics", picFile)
            try:
                if os.path.isfile(picFilePath):
                    os.remove(picFilePath)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (picFilePath, e))
