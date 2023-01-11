from gtts import gTTS


def string_to_speak_ru(string):
    text_val = string
    language = 'ru'
    obj = gTTS(text=text_val, lang=language, slow=False)
    obj.save('speak.mp3')



def string_to_speak_en(string):
    text_val = string
    language = 'en'
    obj = gTTS(text=text_val, lang=language, slow=False)
    obj.save('speak.mp3')


