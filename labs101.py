# Record Audio
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=5)
    r.dynamic_energy_threshold = True
    print("Say something!")
    audio = r.listen(source)

# speech recognition using Google speech Recognition
try: 
    # for testing purposes , we' re just using the default API KEY")'
    # to use another API key, use r.recognize_google(audio,key="GOOGLE_SPEECH_RECOGNITION_API_KEY") 
    # instead of 'r.recognise_google(audio)'
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
     print("Google speech Recognition could not understand audio")
except sr.RequestError as e:
     print("could not request results from Google speech Recognition service; {0}".format(e))
