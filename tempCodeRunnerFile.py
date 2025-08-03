import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 140)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Try 0 or 1 based on male/female

engine.say("""I am in meeting """)

engine.runAndWait()
