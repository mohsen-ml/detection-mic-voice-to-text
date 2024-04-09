import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    microphone_list = sr.Microphone.list_microphone_names()
    print("Available microphones:", microphone_list)  # Debugging statement
    # Check name of the microphone
    microphone_name = "Microphone (CH321)"
    try:
        mic_index = microphone_list.index(microphone_name)
    except ValueError:
        print("Microphone not found in the list.")
        return
    
    with sr.Microphone(device_index=mic_index) as source:
        recognizer.adjust_for_ambient_noise(source, 1)
        print("Speak something in Persian...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="fa-IR") # Set language to Persian (fa-IR)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results. Check your internet connection.")
        print("Error:", e)

if __name__ == "__main__":
    recognize_speech()