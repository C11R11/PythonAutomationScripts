import yt_dlp
import sys
import os

def download_mp3(url):
    ydl_opts = {
        # Audio settings
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        
        # File naming & location
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,  # Ensures it only downloads the video, not the whole radio/list
        
        # Anti-403 Forbidden & Bot detection fixes
        'quiet': False,
        'no_warnings': False,
        'rm_cachedir': True, # Clears cache to prevent old 403 tokens from sticking
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        },
        
        # PRO TIP: Uncomment the line below if you still get 403 errors. 
        # It uses your browser's login session to bypass bot checks.
        'cookiesfrombrowser': ('chrome',), # Options: 'chrome', 'firefox', 'edge', 'safari'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"--- Processing: {url} ---")
            ydl.download([url])
            print("\n✅ Download finished successfully!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n[Suggestion] If you still see '403 Forbidden', try updating the library:")
        print("pip install -U yt-dlp")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
        download_mp3(video_url)
    else:
        print("Usage: python script.py \"URL\"")