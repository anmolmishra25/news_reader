import requests

# url = ("https://newsapi.org/v2/everything?q=tesla&from=2022-02-25&sortBy=publishedAt&apiKey=4dd63a8e15ab41178117aeb282c4f37f")
# response = requests.get(url)
# print(response.json())
# k = response.json()
# print(k["articles"][0][1])

from newsapi import NewsApiClient
from win32com.client import Dispatch
import json

def let_me_speak(str):
    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)


if(__name__ == "__main__"):
    print("welcome to news bulletin")
    print("Top 10 breaking news")
    let_me_speak("welcome to news bulletin")
    let_me_speak("Top 10 breaking news")
    url = ("https://newsapi.org/v2/top-headlines?country=in&apiKey=4dd63a8e15ab41178117aeb282c4f37f")
    r = requests.get(url)
    y = json.loads(r.text)
    for i in range(1,11):
        print(f"news number {i}     " + y["articles"][i]["title"])
        let_me_speak(f"News number {i}")
        let_me_speak(y["articles"][i]["title"])
    print("Thanks for listening..")
    let_me_speak("Thanks for listening..")
