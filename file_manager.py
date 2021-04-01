import os
from os import path
from shutil import move

sample = {
    "Programming Files": set([".ipynb", ".py", ".java", ".cs", ".js", ".vsix", ".jar", ".R"]),
    "Compressed": set([".zip", ".rar", ".arj", ".gz", ".sit", ".sitx", ".sea", ".ace", ".bz2", ".7z"]),
    "Applications": set([".exe", ".msi"]),
    "Pictures":  set([".jpeg", ".jpg", ".png", ".gif", ".tiff", ".raw", ".webp", ".jfif", ".ico", ".psd", ".svg", ".ai"]),
    "Videos":  set([".mp4", ".webm", ".mkv", ".MPG", ".MP2", ".MPEG", ".MPE", ".MPV", ".OGG", ".M4P", ".M4V", ".WMV", ".MOV", ".QT", ".FLV", ".SWF", ".AVCHD", ".avi", ".mpg", ".mpe", ".mpeg", ".asf", ".wmv", ".mov", ".qt", ".rm"]),
    "Documents": set([".txt", ".pdf", ".doc", ".xlsx", ".pdf", ".ppt", ".pps", ".docx", ".pptx", ".csv"]),
    "Music":  set([".mp3", ".wav", ".wma", ".mpa", ".ram", ".ra", ".aac", ".aif", ".m4a", ".tsa"]),
    "Other": set([])
}


def create_folders(folder):
    try:
        os.mkdir(folder)
        print(f"{folder:} Folder Created.")
    except OSError:
        print(f"{folder:} Folder Already Exists")
        

def choose_folder(ext):
    for item in sample.items():
        if(ext in item[1]):
            res = item[0]
            return res    
    return "Other"

def start():
    for each in os.listdir():
        if each != os.path.basename(__file__) and each[0] != '.' and os.path.isfile(each):
            try:
                ext = path.splitext(each)
                folder = choose_folder(ext[1])
                create_folders(folder)
                move(each, folder)
            except KeyError as e:
                print(e)
                print("Failed to move ", each)
            except:
                print("Failed to move ", each)


def main():
    start()
    print("\nProgram executed succesfully!")


if __name__ == '__main__': main()