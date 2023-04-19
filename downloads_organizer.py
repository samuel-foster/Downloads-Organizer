import os
import shutil

# set the path of your Downloads folder
downloads_path = "C:/Users/samue/Downloads"

# create a dictionary of file types and their corresponding folders
folders = {
    "Documents": ["doc", "docx", "pdf", "txt", "rtf", "pptx", "odt", "csv"],
    "Pictures": ["jpg", "jpeg", "png", "gif", "bmp"],
    "Software": ["exe", "dmg", "pkg", "deb", "rpm"],
    "Music": ["mp3", "wav", "ogg", "wma"],
    "Videos": ["mp4", "avi", "mkv", "mov", "flv"]
}

# create the subfolders in the Downloads folder
for folder_name in folders.keys():
    folder_path = os.path.join(downloads_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)

# loop through the files in the Downloads folder and move them to their respective subfolders
for filename in os.listdir(downloads_path):
    if os.path.isfile(os.path.join(downloads_path, filename)):
        file_extension = filename.split(".")[-1]
        for folder_name, extensions in folders.items():
            if file_extension in extensions:
                source_file_path = os.path.join(downloads_path, filename)
                destination_folder_path = os.path.join(downloads_path, folder_name)
                shutil.move(source_file_path, destination_folder_path)
                print(f"Moved {filename} to {destination_folder_path}")
