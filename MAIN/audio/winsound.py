import winsound
# x=winsound.PlaySound('audio.wav',winsound.SND_FILENAME)
# print(x)
freq = 2500 # Set frequency To 2500 Hertz
dur = 1000 # Set duration To 1000 ms == 1 second
winsound.Beep(freq,dur)
