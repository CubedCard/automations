import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            if event.src_path.endswith('.crdownload') or 'com.brave.Browser' in event.src_path:
                print(f'File {event.src_path} is still downloading.')
            elif event.src_path.endswith('.md'):
                print(f"Notes file created: {event.src_path}")
                file = event.src_path.split('/')[-1]
                subprocess.run(['python3', 'save_notes.py', file])
            else:
                print(f'New file created: {event.src_path}')
                subprocess.run(['python3', 'downloads.py'])

def monitor_downloads():
    path = '/Users/jipderksen/Downloads'
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    monitor_downloads()

