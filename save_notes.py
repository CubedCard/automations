import os
import sys
import shutil
from datetime import date

def save_note(download_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    file = sys.argv[1]
    print(file)

    file_path = os.path.join(download_folder, file)

    if os.path.isfile(file_path):
        date_folder = os.path.join(destination_folder, date.today().strftime('%B %d, %Y'))

        if not os.path.exists(date_folder):
            os.makedirs(date_folder)

        shutil.move(file_path, os.path.join(date_folder, file))

if __name__ == "__main__":
    downloads_folder = "/Users/jipderksen/Downloads"
    destination_folder = "/Users/jipderksen/Downloads/files/notes"

    save_note(downloads_folder, destination_folder)
