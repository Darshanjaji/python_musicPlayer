import tkinter as tk
import pygame
import os


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")


        pygame.mixer.init()


        self.music_files = []


        self.current_music = None


        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(side=tk.LEFT)


        self.load_music_files()


        for file in self.music_files:
            self.listbox.insert(tk.END, os.path.basename(file))

    def load_music_files(self):
        music_dir = "C:/Users/Rekha/PycharmProjects/MUSIC_PLAYER/music"
        for file in os.listdir(music_dir):
            if file.endswith(".mp3"):
                self.music_files.append(os.path.join(music_dir, file))

    def play_music(self):
        selected_index = self.listbox.curselection()
        if selected_index:

            selected_music = self.music_files[selected_index[0]]

            if self.current_music == selected_music:

                pygame.mixer.music.unpause()
                pygame.mixer.music.play()
            else:

                pygame.mixer.music.load(selected_music)
                pygame.mixer.music.play()
                self.current_music = selected_music

    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_music = None


if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
