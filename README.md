# Reddit Upvoted Pictured Downloader
## What does it do?
This app downloads your upvoted pictures from Reddit. For example, if you have a meme account where you upvote all your favorite memes, you can use this app to download all of them. Keep in mind, Reddit only remembers your 1000 most recently upvoted posts. This app can't get around that. 

## How to use?
1. Make a reddit app (this will allow this app to communicate with Reddit's API on your behalf)
   1. Go to [reddit](https://old.reddit.com/) (this links to old reddit. IDK how to find these settings on new reddit)
   2. preferences -> apps -> create app
   3. Give it a name like "Download Upvoted Pictures"
   4. Select Script
   5. Put a dummy website for redirect uri like "https://www.google.com" or something
   6. You'll need to take note of you personal use script and secret
2. Run `refreshPics.py`
3. You'll be prompted to input your username, password, personal use script, and secret.
4. It'll also ask you if you want your pictures downloaded in a random order. Otherwise, they'll be downloaded in chronological order from newest to oldest.

## Advanced
If there are any pictures you want it to ignore, just put the urls in `ignorePics.csv`. By default, the removed picture placeholder pictures for i.imgur.com and i.redd.it are in there. 