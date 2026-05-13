import sounddevice
import soundfile
import threading


def song():
    data, fs  = soundfile.read('Assets/music/Nujabes - sea of cloud.flac')

    sounddevice.play(data, fs)
    sounddevice.wait()

def play_game_song():
    thread = threading.Thread(target=song)
    thread.start()