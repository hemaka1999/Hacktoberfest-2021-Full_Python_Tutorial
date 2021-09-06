import pyglet

audio = pyglet.media.load("audio.wav")
x=audio.duration
print(x)

audio.play()