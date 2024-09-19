import yt_dlp
import sys

def download_video(url, output_path='/Users/jipderksen/Desktop'):
    ydl_opts = {'outtmpl': output_path + '/%(title)s.%(ext)s'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = sys.argv[1]
    download_video(video_url)

