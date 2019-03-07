from gtts import gTTS
import os

sentence = """
Bring that ass back like a boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Never give a motherfuck
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Bring that ass back like a boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Bring that ass back like a boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
Boom boom boom boom
"""

speech = gTTS(text = sentence, lang = 'en', slow = False)
speech.save('welcome.mp3')
os.system('welcome.mp3')