import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Assalam o alikum sir, I am your assistant AI of ubaid ur rehman. How may I help you?")

# Function to take voice command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-PK')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

# Function to fetch weather updates
def getWeatherUpdates():
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Karachi"
    complete_url = f"{base_url}appid={api_key}&q={city_name}"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        weather_data = data["main"]
        temperature = round(weather_data["temp"] - 273.15, 2)  # Convert temperature to Celsius
        humidity = weather_data["humidity"]
        description = data["weather"][0]["description"]
        speak(f"The current temperature in {city_name} is {temperature} degrees Celsius with {description}.")
        speak(f"The humidity level is {humidity}%.")
    else:
        speak("Weather data not found for the specified city.")

# Function to fetch news updates
def getNewsUpdates():
    news_api_key = "YOUR_NEWS_API_KEY"
    news_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}"
    response = requests.get(news_url)
    data = response.json()
    if data["status"] == "ok":
        articles = data["articles"]
        speak("Here are the latest news headlines:")
        for article in articles:
            speak(article["title"])
    else:
        speak("Failed to fetch news updates.")

# Function to integrate Fitbit API
def getFitbitData():
    # Your Fitbit API integration code here
    pass

# Function to integrate Google Fit API
def getGoogleFitData():
    # Your Google Fit API integration code here
    pass

# Function to integrate HealthGraph API
def getHealthGraphData():
    # Your HealthGraph API integration code here
    pass

# Function to integrate Alpha Vantage API
def getStockData():
    # Your Alpha Vantage API integration code here
    pass

# Function to integrate Yahoo Finance API
def getYahooFinanceData():
    # Your Yahoo Finance API integration code here
    pass

# Function to integrate IEX Cloud API
def getIEXCloudData():
    # Your IEX Cloud API integration code here
    pass

# Function to integrate Google Maps API
def getGoogleMapsData():
    # Your Google Maps API integration code here
    pass

# Function to integrate Google Calendar API
def getGoogleCalendarData():
    # Your Google Calendar API integration code here
    pass

# Function to integrate Outlook Calendar API
def getOutlookCalendarData():
    # Your Outlook Calendar API integration code here
    pass

# Main function
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'weather updates' in query:
            getWeatherUpdates()  # Call the function to get weather updates

        elif 'news updates' in query:
            getNewsUpdates()  # Call the function to get news updates

        # Add more conditions to integrate other APIs as required

        elif 'exit' in query:
            speak("Goodbye!")
            break
