import requests


def getPicsUrls(user):
    headers = getHeaders(user)
    urls = getUrls(user["username"], headers)
    pics = [url for url in urls if url.endswith(
        ".png") or url.endswith(".jpg")]
    return pics


def getHeaders(user):
    clientAuth = requests.auth.HTTPBasicAuth(
        user["personalUseScript"], user["secret"])
    postData = {"grant_type": "password",
                "username": user["username"], "password": user["password"]}
    userAgent = "Reddit-Upvoted-Pictures-Downloader/1.0 (https://github.com/Bruce2142/Reddit-Upvoted-Pictures-Downloader)"
    headers = {"User-Agent": userAgent}
    token = requests.post("https://www.reddit.com/api/v1/access_token",
                          auth=clientAuth, data=postData, headers=headers).json()
    headers = {"Authorization": token['token_type'] + " " +
               token['access_token'], "User-Agent": userAgent}
    return headers


def getUrls(username, headers):
    urls = []
    response = requests.get(
        "https://oauth.reddit.com/user/" + username + "/upvoted?limit=1", headers=headers).json()
    urls.append(response['data']['children'][0]['data']['url'])
    while response['data']['after'] is not None:
        response = requests.get("https://oauth.reddit.com/user/" + username + "/upvoted?limit=100&after=" +
                                response['data']['after'], headers=headers).json()
        for item in response['data']['children']:
            urls.append(item['data']['url'])
    return urls
