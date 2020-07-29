import json
import os


def getUser():
    if(os.path.exists("data/user.json")):
        jsonFile = open("data/user.json", "r")
        user = json.loads(jsonFile.read())
        jsonFile.close()
    else:
        user = {"username": "", "password": "",
                "personalUseScript": "", "secret": ""}
    for i in user:
        if(not user[i]):
            user[i] = input("Input your " + i + ": ").strip()
        else:
            while True:
                isCorrectValue = input(
                    "Is your " + i + " \"" + user[i] + "\"? (y/n): ").strip().lower()
                if(isCorrectValue == "y"):
                    break
                elif(isCorrectValue == "n"):
                    user[i] = input("Input your " + i + ": ").strip()
                    break
                else:
                    print("Sorry, I didn't understand that. ", end="")
    jsonFile = open("data/user.json", "w")
    json.dump(user, jsonFile)
    jsonFile.close()
    return user
