import os
from datetime import datetime

def create_directories():
    current_year = datetime.now().year
    parent_dir = str(current_year)
    
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
        print(f"Parent directory '{parent_dir}' created.")
    
    for day in range(1, 26):
        day_dir = f"day-{day}"
        day_path = os.path.join(parent_dir, day_dir)
        
        if not os.path.exists(day_path):
            os.makedirs(day_path)
            print(f"Subdirectory '{day_dir}' created.")
        
        files = ['solution.py', 'ex.txt', 'data.txt']
        
        for file_name in files:
            file_path = os.path.join(day_path, file_name)
            if not os.path.exists(file_path):
                with open(file_path, 'w') as file:
                    file.write("")
                print(f"File '{file_name}' created in '{day_dir}'.")
    
    print("Directory structure and files created successfully!")

create_directories()