import keyboard
from recording import record_audio,save_recording
from s2t import s2t

frames = []
while True:
    if keyboard.is_pressed('esc'):
        print("esc-ing")
        break
    elif keyboard.is_pressed("ctrl + shift + /"): #recording audio
        frames=record_audio(frames)
    else:
        if len(frames)>0:
            save_recording(frames)
            text=s2t("output.wav")
            print(text)
        # saving function of the audio
            frames = []