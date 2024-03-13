import speech_recognition as sr
import pyttsx3
import datetime
import calendar
import pywhatkit
import wikipedia
import pyjokes



listener = sr.Recognizer()
alexa=pyttsx3.init()
voices=alexa.getProperty("voices")                 #Changing voice male to female
alexa.setProperty("voice",voices[1].id)

def talk(text):
    alexa.say(text)            #init speaking
    alexa.runAndWait()


def take_command()
    try:
        with sr.Microphone() as source:
            print('Listening.....')
            voice = listener.listen(source)
            command=listener.recognize_google(voice)
            if "Alexa" in command:

                command=command.replace("Alexa","")
            else:
                print("Sorry! Voice Type Error.Try Again")


    except:

        pass

    return command

def go_alexa():
    command=take_command()

    if "Time" in command:
        Time=datetime.datetime.now().strftime("%H:%M:%p")
        print(Time)
        talk("Current time is"+Time)

    if "Calender" in command:
        cal = calendar.TextCalendar()
        calendar_text = cal.formatyear(year, 2, 1, 1, 3, 3)
        print(calendar_text)
        talk("Here is the calender below"+calendar_text)

    elif "play" in command:
        player=command.replace("play","")

        pywhatkit.playonyt(player)
        talk("Playing" + player)

    elif "tell me about" in command:
        searching=command.replace("tell me about","")

        info=wikipedia.summary(searching,2)
        talk("Here you go" + searching)
        print(info)
    elif "jokes" in command:
        joke=pyjokes.get_joke()
        talk("Alright!"+jokes)

    elif "Date" in command:
        print("Sorry I am an AI based programme!")
    elif "Father" or "Mother" in command:
        print("Sorry I dont have any info on it.But I developed by Amazone")


go_alexa()








