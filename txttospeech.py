import gtts
import playsound
# this converts text to speech...
text = input("Type something here!!")
sound = gtts.gTTS(text, lang="en") # u can change the lang...
sound.save("Shv.mp3")
playsound.playsound("shv.mp3")