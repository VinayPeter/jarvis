import speech_recognition as sr
import win32com.client
import random
import webbrowser
import datetime
from jikanpy import Jikan, JikanException
import jokes
# import nltk
# from nltk.tokenize import word_tokenize, sent_tokenize
# from nltk.tag import pos_tag
# from nltk.sentiment import SentimentIntensityAnalyzer
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('vader_lexicon')
speaker= win32com.client.Dispatch("SAPI.Spvoice")

# todo: add more greetings
greetings = [
    "Greetings, sir. How may I assist you today?",
    "Ah, there you are sir. I've been eagerly awaiting your command.",
    "Welcome back sir. I stand ready to serve.",]
greeting0 = random.choice(greetings)
print(greeting0)
speaker.Speak(greeting0)
 #listening to the voice FUNCTION
 # todo: modify the try except(the response)
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        audio= r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said:{query}")
            return query
        except Exception as e:
            print("Recognizing")
            print("sorry sire")
            query = "sorry sir, some error occured"
            return query

import jokes

def say_joke(category):
    category = 'programming'
    joke_index = 2
    joke = jokes.get_joke(category=category, index=joke_index)
    print(f"{category.capitalize()} Joke #{joke_index}: {joke}")

# category = 'programming'
# say_joke(category

# List of shutdown dailogs
shutdown_phrases = [
    "As you wish, shutting down Jarvis.",
    "Understood, powering down Jarvis now.",
    "Very well, Jarvis signing off.",
    "Acknowledged, shutting down operations.",
]
def shutdown_jarvis():
    shutdown_message = random.choice(shutdown_phrases)
    speaker.Speak(shutdown_message)

#anime function
def get_anime_info(anime_name):
    try:
        jikan = Jikan()
        anime_search = jikan.search("anime", anime_name)
        if anime_search['results']:
            anime_id = anime_search['results'][0]['mal_id']
            anime = jikan.anime(anime_id)
            return anime['title'], anime['type'], anime['episodes'], anime['score'], anime['synopsis']
        else:
            print(f"Anime '{anime_name}' not found.")
            return None
    except JikanException as e:
        print(f"Error: {e}")
        return None

if __name__== '  main  ':
    print("JARVIS")

while True:
    # text = takecommand()
    # # Tokenization
    # tokens = word_tokenize(text)
    # print("Tokens:", tokens)
    # # Part-of-Speech Tagging
    # tagged_tokens = pos_tag(tokens)
    # print("POS Tags:", tagged_tokens)
    # # Sentence Segmentation
    # sentences = sent_tokenize(text)
    # print("Sentences:", sentences)
    # # Sentiment Analysis
    # sid = SentimentIntensityAnalyzer()
    # sentiment_scores = sid.polarity_scores(text)
    # print("Sentiment Scores:", sentiment_scores)
    print("listening....")
    say = takecommand()
    # todo: add more links as you like
    sites = [["youtube", "https://youtube.com"],["wikipedia","https://wikipedia.com"],["google","https://google.com"]]
    for site in sites:
        if f"open {site[0]}".lower() in say.lower():
            say= f"opening {site[0]} sir..."
            webbrowser.open(site[1])
    speaker.Speak(say)
    #work on the joke
    # if "joke" in say:
    #     speaker.Speak("as you wish sir")
    #     speaker.Speak("do you have any specific topic, you can name it sir or else i have a good one for you!!!")
    #     speaker.Speak(jokes)
    if "time" in say:
        time= datetime.datetime.now().strftime("%H:%M")
        print(time)
        say= f"the current time is {time}"
        speaker.Speak(say)
# todo: work on the shutting down problem
    elif say.lower() == "shutdown":
        confirm = ("Are you sure you want to shut down Jarvis? (yes/no): ")
        speaker.Speak(confirm)
        lconfirm= takecommand()
        if lconfirm.lower() == "yes":
            shutdown_jarvis()
            break
        elif lconfirm.lower() == "no":
            speaker.Speak("shutdown cancel")
    if "anime" in say.lower():
        speaker.Speak("Sure, which anime would you like to know about?")
        anime_name = takecommand()
        if anime_name:
            anime_info = get_anime_info(anime_name)
            if anime_info:
                title, anime_type, episodes, score, synopsis = anime_info
                speaker.Speak(f"Title: {title}")
                speaker.Speak(f"Type: {anime_type}")
                speaker.Speak(f"Episodes: {episodes}")
                speaker.Speak(f"Score: {score}")
                speaker.Speak(f"Synopsis: {synopsis}")
            else:
                speaker.Speak("Anime data not found.")
        else:
            speaker.Speak("Sorry, I didn't catch the anime name. Please try again.")

    else:
        print("Command not recognized...")
        speaker.Speak("Command not recognized...")

