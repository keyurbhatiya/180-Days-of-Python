# *66.** File Organizer (auto-sort files into folders by extension)


import os
import shutil

# Map extensions to folder names
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css"]
}

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    dest_folder = os.path.join(folder_path, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    moved = True
                    print(f"Moved {filename} to {folder}/")
                    break
            
            if not moved:
                other_folder = os.path.join(folder_path, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"Moved {filename} to Others/")

# 👇 Example Usage
if __name__ == "__main__":
    folder_to_sort = input("Enter path of the folder to organize: ")
    organize_folder(folder_to_sort)
    print("✅ Folder organized successfully!")