import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Parash")
    command = pyttsx3.init()  # Initialize the text-to-speech engine
    while True:
        x = input("Enter what you want me to speak (type 'q' to quit): ")
        if x.lower() == "q":
            command.say("bye bye")
            command.runAndWait()
            break
        command.say(x)  # Speak the input text
        command.runAndWait()  # Wait until speaking is complete
