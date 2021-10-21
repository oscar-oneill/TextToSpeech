from urllib import request
import json
import pyttsx3

url = "https://api.reddit.com/r/cscareerquestions/new?limit=1"
r = request.urlopen(url)
data = r.read()
jsonData = json.loads(data)
children = jsonData['data']['children']

class Post:
    def __init__(self, subreddit, author, title, selftext) -> None:
        self.subreddit = subreddit
        self.author = author        
        self.title = title
        self.selftext = selftext

    def __str__(self) -> str:
        return f"Subreddit: {self.subreddit}, Author: {self.author}\n Title: {self.title}\n Text: {self.selftext}"

posts = []

for x in children:
    subreddit = x['data']['subreddit']
    author = x['data']['author']
    title = x['data']['title']
    selftext = x['data']['selftext']
    post = Post(subreddit, author, title, selftext)
    posts.append(post)

print(f"{len(posts)} post(s) returned...")

for post in posts:
    print(post)
    pyttsx3.speak("Subreddit")
    pyttsx3.speak(post.subreddit)
    pyttsx3.speak("Author")
    pyttsx3.speak(post.author)
    pyttsx3.speak("Title")
    pyttsx3.speak(post.title)
    pyttsx3.speak("Text")
    pyttsx3.speak(post.selftext)