import requests
import json
                               ------------+
def speak(str):                            | 
    from win32com.client import Dispatch   |   
    speak = Dispatch("SAPI.SpVoice")       | # This is a SPEAKER which convert our text into Speech
    speak.Speak(str)                       |
                               ------------+
    
if __name__ == '__main__':
    api_key = input("Enter your api key\n> ")
    speak("Fetching today's latest news...Let's begin")
    urll = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    
    req = requests.get(urll).text # Getting the content of the specified link in the text Format
    news_list = json.loads(req)   # loads() method can be used to parse a valid JSON string and convert it into a Python 
    art = news_list['articles']   # Accessing the articles
    for article in art:
        print(article["title"])   # Printing the titles
        speak(article["title"])
        ur = (article["url"])     # It will gives us the url of the latest article  
        print(f"For More {ur}")
        speak("Rolling to next....Listen Carefully")
    speak("Thanks for Listening....")
