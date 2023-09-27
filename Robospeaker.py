import win32com.client as wincom
if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Pinki")

    speaker = wincom.Dispatch("SAPI.SpVoice")
    while True:
        x = input("Enter what you want me to speak (or 'q' to quit): ")
        if x.lower() == "q":
            speaker.Speak("Bye Bye, my friend.")
            break

        speaker.Speak(x)
