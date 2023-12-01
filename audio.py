import winsound


sound = ('a.wav')

flags = winsound.SND_FILENAME | winsound.SND_NOWAIT

winsound.PlaySound(sound, flags)
