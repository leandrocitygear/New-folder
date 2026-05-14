import pygame
import threading
from pathlib import Path
import random
import time

pygame.mixer.init()

music_folder = Path(__file__).parent / "Assets" / "music"

background_music = [
    music_folder / "fat jon - no way back.mp3",
    music_folder / "MINMI - Who's Theme.mp3",
    music_folder / "Nujabes - Counting Stars.mp3",
    music_folder / "Nujabes - sea of cloud.flac",
    music_folder / "Nujabes - world without words.mp3",
]

current_song = None
music_running = True


def music_loop():
    global current_song

    while music_running:

        chosen_song = random.choice(background_music)


        while chosen_song == current_song and len(background_music) > 1:
            chosen_song = random.choice(background_music)

        current_song = chosen_song

        print(f"Now Playing: {chosen_song.name}")

        pygame.mixer.music.load(str(chosen_song))
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(1)

def play_game_song():
    thread = threading.Thread(
        target=music_loop,
        daemon=True
        )
    thread.start()

def stop_music():
    global music_running

    music_running = False
    pygame.mixer.music.stop()