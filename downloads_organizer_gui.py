import os
import shutil
import tkinter as tk
from tkinter import filedialog

class DownloadsOrganizer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Downloads Organizer")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.select_folder_button = tk.Button(self)
        self.select_folder_button["text"] = "Select Downloads Folder"
        self.select_folder_button["command"] = self.select_folder
        self.select_folder_button.pack(side="top")

        self.organize_button = tk.Button(self)
        self.organize_button["text"] = "Organize Downloads Folder"
        self.organize_button["command"] = self.organize_folder
        self.organize_button.pack(side="top")

        self.quit_button = tk.Button(self, text="Quit", fg="red",
                              command=self.master.destroy)
        self.quit_button.pack(side="bottom")

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()

    def organize_folder(self):
        folders = {
            "Documents": ["doc", "docx", "pdf", "txt", "rtf"],
            "Pictures": ["jpg", "jpeg", "png", "gif", "bmp"],
            "Software": ["exe", "dmg", "pkg", "deb", "rpm"],
            "Music": ["mp3", "wav", "ogg", "wma"],
            "Videos": ["mp4", "avi", "mkv", "mov", "flv"]
        }

        for folder_name in folders.keys():
            folder_path = os.path.join(self.folder_path, folder_name)
            os.makedirs(folder_path, exist_ok=True)

        for filename in os.listdir(self.folder_path):
            if os.path.isfile(os.path.join(self.folder_path, filename)):
                file_extension = filename.split(".")[-1]
                for folder_name, extensions in folders.items():
                    if file_extension in extensions:
                        source_file_path = os.path.join(self.folder_path, filename)
                        destination_folder_path = os.path.join(self.folder_path, folder_name)
                        shutil.move(source_file_path, destination_folder_path)
                        print(f"Moved {filename} to {destination_folder_path}")

        tk.messagebox.showinfo("Downloads Organizer", "Folder organized successfully!")

root = tk.Tk()
app = DownloadsOrganizer(master=root)
app.mainloop()
