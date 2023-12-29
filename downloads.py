import os
import shutil

def organize_downloads(download_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    files = os.listdir(download_folder)

    for file in files:
        print(file)
        file_path = os.path.join(download_folder, file)

        if os.path.isfile(file_path):
            _, extension = os.path.splitext(file)

            extension = extension[1:]

            extension_folder = os.path.join(destination_folder, extension)
            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)

            shutil.move(file_path, os.path.join(extension_folder, file))

if __name__ == "__main__":
    downloads_folder = "/Users/jipderksen/Downloads"
    destination_folder = "/Users/jipderksen/Downloads/files"

    organize_downloads(downloads_folder, destination_folder)
