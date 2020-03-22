import time
from pygame import mixer


def play(soundfile, duration_secs=1000000):
    """Play a soundfile for a predetermined duration"""

    mixer.init()
    mixer.music.load(soundfile)
    mixer.music.play()
    time.sleep(duration_secs)
    mixer.music.stop()
    mixer.quit()


# Play for a determined period
play('test.mp3', 5)
