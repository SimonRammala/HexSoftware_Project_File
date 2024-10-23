import speech_recognition as sr  # Library for speech recognition
import pyttsx3  #  text-to-speech
import pywhatkit  # Library for interacting with YouTube and other online services
import wikipedia  # searching and retrieving Wikipedia articles
import pyjokes  #  retrieving jokes
import datetime  

# Initialize speech recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice for text-to-speech
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)  # Set the voice to the second voice in the list (usually female)

# Function to speak out the given text
def talk(text):
    engine.say(text)  
    engine.runAndWait()  # Run the speech

# Function to listen for and process voice commands
def take_command():
    try:
        # Use the microphone to capture voice input
        with sr.Microphone() as source:
            introduction = "Hello, I am Joe a voice assistant. How can I help you?" 
            print(introduction)  
            voice = listener.listen(source)  # Listen to the source (microphone)
            command = listener.recognize_google(voice)  # Recognize the speech using Google's speech recognition API
            command = command.lower()  

            # If "joe" is detected in the command, remove it
            if 'joe' in command:
                command = command.replace('joe', '')  
                talk(command)  # Optionally speak back the command
    except:
        pass  
    
    return command  # Return the processed command

# Main function to handle the logic for different commands
def run_alexa():
    command = take_command()  # Get the voice command
    print(command)  # Print the command for debugging purposes

    # If the command contains 'play', play a song on YouTube
    if 'play' in command:
        song = command.replace('play', '')  
        talk('playing ' + song)  # Tell the user what song is being played
        pywhatkit.playonyt(song)  

    # If the command contains 'time', tell the current time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')  
        talk('Current time is ' + time)  # Speak the time

    # If the command contains 'date', tell the current date
    elif 'date' in command:   
        date = datetime.datetime.now().strftime('%d:%B:%Y')
        talk('Current date is ' + date)  # Speak the date

    # If the command asks for information about a person (starts with 'who is'), get info from Wikipedia
    elif 'who is' in command:
        person = command.replace('who is', '')  
        try:
            info = wikipedia.summary(person, sentences=2)  # Get a summary of the person from Wikipedia (2 sentences)
            talk(info) 
        except wikipedia.exceptions.DisambiguationError as e:
            talk("The request was too ambiguous. Please be more specific.")  
        except wikipedia.exceptions.PageError:
            talk("I couldn't find anything on that topic.")  # Handle cases where no page is found

    # If the command asks 'what is', get info from Wikipedia
    elif 'what is' in command:
        whatthe = command.replace('what is', '')  
        try:
            info = wikipedia.summary(whatthe, sentences=2)  # Get a summary of the topic from Wikipedia
            talk(info)  
        except wikipedia.exceptions.DisambiguationError as e:
            talk("The request was too ambiguous. Please be more specific.") 
        except wikipedia.exceptions.PageError:
            talk("I couldn't find anything on that topic.")  # Handle cases where no page is found

    # If the command asks 'where is', get info from Wikipedia
    elif 'where is' in command:
        location = command.replace('where is', '') 
        try:
            info = wikipedia.summary(location, sentences=2)  # Get a summary of the location from Wikipedia
            talk(info)  
        except wikipedia.exceptions.DisambiguationError as e:
            talk("The request was too ambiguous. Please be more specific.")  # Handle ambiguous queries
        except wikipedia.exceptions.PageError:
            talk("I couldn't find anything on that topic.")  

    # If the command asks 'when is', get info from Wikipedia
    elif 'when is' in command:
        time = command.replace('when is', '')  # Remove 'when is' to extract the event or time
        try:
            info = wikipedia.summary(time, sentences=2)  
            talk(info)  
        except wikipedia.exceptions.DisambiguationError as e:
            talk("The request was too ambiguous. Please be more specific.")  
        except wikipedia.exceptions.PageError:
            talk("I couldn't find anything on that topic.")  # Handle cases where no page is found

    # If the command contains 'joke', tell a joke
    elif 'joke' in command:
        talk(pyjokes.get_joke())  # Get a random joke from the pyjokes library and speak it

    # If the command contains 'exit', stop the program
    elif 'exit' in command:
        talk('Goodbye!')  
        exit()  

    # If the command is not recognized, ask the user to repeat
    else:
        talk('I did not get that, please say it again.')

while True:
    run_alexa()
