import os
import shutil

file_types_key: dict = {
    "1.Audio & Video": ["mp3", "wav", "mp4"],
    "2.Pictures": ["png", "jpg", "jpeg", "ico", "webp"],
    "3.Executables & Installers": ["exe", "msi"],
    "4.Spreadsheets": ["csv", "xlsx"],
    "5.Zips": ["zip"]
}

file_types: dict = {
    "1.Audio & Video": [],
    "2.Pictures": [],
    "3.Executables & Installers": [],
    "4.Spreadsheets": [],
    "5.Zips": []
}

directory: str = ""
# directory: str = "C:/Users/jason/OneDrive/Desktop/Test"

class File():
    def __init__(self, name: str, file_type: str) -> None:
        self.name: str= name
        self.file_type: str = file_type
        self.sys_name: str = f"{name}.{file_type}"

files: list[File] = []   

def create_file(name: str) -> None:
    extension: str = name.split(".")[-1]
    file_name: str = name[0:-len(extension)-1]
    file = File(file_name, extension)
    files.append(file)

def open_folder() -> None:
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                create_file(entry.name)

def organize_files(files: list[File]) -> None:
    for file in files:
        for k, v in file_types_key.items():
            if file.file_type in v:
                file_types[k].append(file.sys_name)

def make_dir(file_types: list[File]) -> None:
    for k, _ in file_types.items():
        try: 
            os.mkdir(f"{directory}/{k}")
        except FileExistsError:
            print("Folder already exists")

def move_files(file_types: list[File]) -> None:
    for k, v in file_types.items():
        for file in v:
            try:
                shutil.move(f"{directory}/{file}", f"{directory}/{k}")
            except shutil.Error as e:
                print(e)

def main() -> None:
    open_folder()
    organize_files(files)
    make_dir(file_types)
    move_files(file_types)