from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
import json
import os
import time
import subprocess
import ctypes
import pyautogui
import msvcrt as m

assistant   =    pyttsx3.init()
voice       =    assistant.getProperty('voices') 
# voice_id   = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
# voice_id   = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"
# voice_id   = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enAU_CatherineM"
voice_id   = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enGB_SusanM"
# voice_id    = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enIN_RaviM"
# voice_id    = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enAU_JamesM"
# voice_id    = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enCA_LindaM"
# voice_id    = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enCA_RichardM"
# voice_id    = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enGB_GeorgeM"
# voice_id    = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enGB_HazelM"
# voice_id    = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enIE_SeanM"
# voice_id    = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enIN_HeeraM"
assistant.setProperty('voice', voice_id)

def speak(audio):
    print("STEM AI:" + audio)
    assistant.say(audio)
    assistant.runAndWait()
def wait():
    m.getch()

def pause():
    speak('i am paused for now. Click any key to resume me')            
    wait() 
    speak('am back now')
    speak('what would you like me to')
    stream.start_stream()
    print('')
    print('Listening')
    print('')

def welcome():
    print('')
    speak('Helloo, am Stem')
    speak('a voice assistant, what can I help you with ')
    print('')
    print("**** LISTENING ******")
    print('')


#read the model
model      = Model("Database\\vosk-model-small-en-us-0.15")
welcome()
recognizer = KaldiRecognizer(model, 16000)
#### other models include : ####
    #model = Model("Database\\vosk-model-en-us-0.22-lgraph") #
    #model = Model("Database\\vosk-model-spk-0.4")


#recognize form the microphone 
mic    = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, frames_per_buffer=8192, rate=16000, input=True, channels=1)
stream.start_stream()

#keep on iterating while reading the input from the mic
while True:

    data = stream.read(4096, exception_on_overflow=False)
    if len(data)==0:
        break
    if recognizer.AcceptWaveform(data): #verifies if the data is valid

        ### The result
        result = recognizer.Result()
        result = json.loads(result)
        if "hello" in result['text']:
            os.system('cls')# This Function will clean any command before execution of this python file
            stream.stop_stream()
            print('STEM AI: ' + result['text'])
            speak("hello ")
            stream.start_stream()
            print("")
            print("Listening.....")
            print("")
        elif 'stop talking' in result['text'] or 'mute' in result['text'] or 'chill' in result['text'] or 'stop listening' in result['text'] or 'don\'t listen' in result['text'] or 'don\'t talk' in result['text']:
            os.system('cls')
            stream.stop_stream()
            speak('Ookay ')
            speak('i am paused for now. Click any key to resume me')            
            wait() 
            speak('am back now')
            speak('what would you like me to')
            stream.start_stream()
            print('')
            print('Listening')
            print('')
            # if 'wake up' in result['text'] or 'stem' in result['text']:
            #     os.system('cls')
            #     stream.stop_stream()
            #     pyautogui.press('enter')
            #     #print('STEM AI: ' + result['text'])                
            #     speak('am back now')
            #     speak('what would you like me to')
            #     stream.start_stream()
            #     print('')
            #     print('Listening')
            #     print('')
        
            
        elif "who are you" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('STEM AI: ' + result['text'])
            speak("I am STEM, a desktop virtual assistant")
            stream.start_stream()
            print("")
            print("Listening.....")
            print("")
        elif "who made you" in result['text'] or "who created you" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('STEM AI: ' + result['text'])
            speak("I was made by Julius kavingo")
            stream.start_stream()
            print("")
            print("Listening.....")
            print("")
        elif "what are you made of" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('STEM AI: ' + result['text'])
            speak("Am just a simple program made up of a bunch of lines of code")
            stream.start_stream()
            print("")
            print("Listening.....")
            print("")
        
        

        elif "microsoft" in result['text'] or "ms word" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('STEM AI: ' + result['text'])
            di = r"C:\\Program Files\\Microsoft Office\\root\\Office16\WINWORD.EXE"   
            os.startfile(di)  
            speak("opening microsoft word")
            pause()
            # speak('What else would you like me to do')
            # stream.start_stream()
            # print('')
            # print('listening ...')
            # print('')

        
            #stream.start_stream()
            
        elif 'minimize the window' in result['text'] or 'minimise the current window' in result['text'] or 'minimize the current window' in result['text'] or 'minimize window' in result['text'] or 'minimise window' in result['text']:
            os.system('cls')
            stream.stop_stream()
            speak('minimizing window')            
            pyautogui.hotkey('win','down','down')
            speak('what would you like me to')
            stream.start_stream()
            print('')
            print('Listening')
            print('')
        elif 'maximize the window' in result['text'] or 'maximise the current window' in result['text'] or 'maximize the current window' in result['text'] or 'maximize window' in result['text'] or 'maximise window' in result['text']:        
            os.system('cls')
            stream.stop_stream()
            speak('maximizing window')
            pyautogui.hotkey('win','up','up')
            speak('what else can i do for you')
            stream.start_stream()
            print('')            
            print('listening')            
            print('') 
        elif 'close window' in result['text'] or 'glass window' in result['text'] or 'cloze window' in result['text'] or 'cloze current window' in result['text'] or 'close current window' in result['text']:
            os.system('cls')
            stream.stop_stream()
            speak('closing current window')
            pyautogui.hotkey('alt', 'f4')
            speak('what else can i do for you')
            stream.start_stream()
            print('')            
            print('listening')            
            print('')            

        elif 'take screenshot' in result['text'] or 'screenshot' in result['text']:
            os.system('cls')
            stream.stop_stream()
            speak('taking a screenshot')
            pyautogui.press('prt sc')
            speak('what else can i do for you')
            stream.start_stream()
            print('')            
            print('listening')            
            print('')
        elif 'open windows explorer' in result['text'] or 'file manager' in result['text'] or 'open file manager' in result['text'] or 'windows explorer' in result['text'] or 'open file explorer' in result['text'] or 'open files' in result['text']  :
            os.system('cls')
            stream.stop_stream()
            speak('opening windows explorer')
            pyautogui.hotkey('win','e')
            speak('what else can i do for you')
            stream.start_stream()
            print('')            
            print('listening')            
            print('')
        
        elif 'open desktop' in result['text']:
            os.system('cls')
            stream.stop_stream()
            speak('opening Desktop window')
            desktop = r"C:\\Users\\Admin\\Desktop"
            os.startfile(desktop)
            speak('what else can i do for you')
            stream.start_stream()
            print('')            
            print('listening')            
            print('')
        elif 'open documents' in result['text']:
            os.system('cls')
            stream.stop_stream()
            speak('opening Documents window')
            desktop = r"C:\\Users\\Admin\\Documents"
            os.startfile(desktop)
            speak('what else can i do for you')
            stream.start_stream()
            print('')            
            print('listening')            
            print('')
        elif 'open downloads' in result['text']:
            os.system('cls')
            stream.stop_stream()
            speak('opening Downloads window')
            desktop = r"C:\\Users\\Admin\\Downloads"
            os.startfile(desktop)
            speak('what else can i do for you')
            stream.start_stream()
            print('')            
            print('listening')            
            print('')


        

        #elif 'minimize' in result['text'] or 'minimise' in result['text']:
            #pyautogui.hotkey('win','down','down')   

        elif 'shut down computer' in result['text'] or 'shut down the computer' in result['text'] or 'computer shut down' in result['text']:
            speak(f"Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')


        elif 'cumputer sleep'  in result['text'] or 'lock screen' in result['text'] or 'lock the screen' in result['text']:
            speak("locking the computer")
            speak("am off for now, thanks for your time")
            ctypes.windll.user32.LockWorkStation()
            exit()


        elif 'exit program' in result['text'] or 'close program' in result['text'] or 'exit asssistant' in result['text']:
            speak("Thanks for giving me your time")
            exit()        
        elif "quit assistant" in result['text'] or "assistant quit" in result['text']:
            speak("Assistant is off. Goodbye")        
            quit()
        elif "bye stem" in result['text'] or 'bye assistant' in result['text']:
            speak("Assistant is off. Goodbye")                   
            quit()        
        elif "buy stem" in result['text'] or 'buy assistant' in result['text']:
            speak("Assistant is off. Goodbye")                   
            quit()               
        elif "see you later" in result['text']:
            speak("Assistant is off. Goodbye")            
            quit()



        elif result['text'] == '':
            os.system('cls')
            stream.stop_stream()
            print('STEM AI: ' + result['text'])
            speak("unable to recognize your voice")            
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        else:
            os.system('cls')
            stream.stop_stream()
            print('STEM AI: ' + result['text'])
            speak("I'm sorry, I can't process that, it's beyond my scope but am still learning.")
            speak('Is there anything else I can help you with?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')










    #else:
    #    txt = recognizer.PartialResult()
    #    print("Listening ### ....")
    #    print(f"This is a Partial Result{txt[14: -3]}")
