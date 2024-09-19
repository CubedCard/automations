import ssl
from pytube import YouTube
import sys
import traceback

def download_video(url, output_path='/Users/jipderksen/Downloads'):
    try:
        yt = YouTube(url, on_progress_callback=progress_function)
        stream = yt.streams.get_highest_resolution()
        print("Downloading:", yt.title)
        stream.download(output_path)
        print("Download completed successfully!")
    except Exception as e:
        print("Error:", e)
        traceback.print_exc()

def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"Download progress: {percentage:.2f}%")

if __name__ == "__main__":
    # Ignore SSL certificate verification
    ssl._create_default_https_context = ssl._create_unverified_context

    video_url = sys.argv[1]
    download_video(video_url)
