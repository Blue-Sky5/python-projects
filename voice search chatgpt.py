import openai
import pyttsx3
import speech_recognition as sr
import time

openai.api_key = ":)"

#tts engine
engine = pyttsx3.init()
voice = engine.getProperty('voices')


#stt engine
def speech_to_text(file):
    stt_instance = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio = stt_instance.record(source)
    try:
        return stt_instance.recognize_google(audio)
    except:
        print("something went wrong in the transcription process")

def Chat_GPT_Responce(query):
    responce = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = query,
        max_tokens = 4000,
        n = 1,
        stop = None,
        #temprature = 0.5,
    )
    return responce["choices"][0]["text"]

def text_to_speech(input):
    engine.say(input)
    engine.runAndWait()


def main():
    while True:
        engine.say("say hello and ask your question ! i will do my best to answer ")
        engine.runAndWait()

        print("Say the word hello to start Assistance ...")
        with sr.Microphone() as source:
            stt_instance = sr.Recognizer()
            audio = stt_instance.listen(source)
            try:
                transcription = stt_instance.recognize_google(audio)
                if transcription.lower() == "exit":
                    break
                if transcription.lower() == "hello":
                    # record the query
                    filename = "input.wav"
                    print("say your question ... ")
                    with sr.Microphone() as source:
                        stt_instance = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = stt_instance.listen(source,phrase_time_limit=None,timeout= None)
                        with open(filename,"wb") as f:
                            f.write(audio.get_wav_data())

                    # fetching transcription
                    text = speech_to_text(filename)
                    if text:
                        print(f"you said:{text}")

                        # response from openai
                        response = Chat_GPT_Responce(text)
                        print(f"chatgpt said :{response}")

                        # speak the response
                        text_to_speech(response)
            except Exception as e:
                print(f"An exception occurred by following message : {e}")



if __name__ == "__main__":
    main()
