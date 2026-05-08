import sounddevice
import soundfile
import threading


def song():
    data, fs  = soundfile.read('Guess_Num_Game/Nujabes - sea of cloud.flac')

    sounddevice.play(data, fs)
    sounddevice.wait()

def play_game_song():
    thread = threading.Thread(target=song)
    thread.start()