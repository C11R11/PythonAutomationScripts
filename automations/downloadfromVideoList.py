import yt_dlp
import os

# List your YouTube URLs here
video_urls = [
    "https://music.youtube.com/watch?v=w1eN8vyVFIM"
    # Add more URLs...
]

def download_for_denon(urls):
    ydl_opts = {
        'format': 'bestaudio/best',
        # Post-processors handle the conversion and metadata
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320', # High quality for club play
            },
            {
                'key': 'FFmpegMetadata',
                'add_metadata': True,
            },
            {
                'key': 'EmbedThumbnail',
            },
        ],
        # Denon Hardware Compatibility: Force ID3v2.3 via FFmpeg arguments
        'postprocessor_args': [
            '-id3v2_version', '3',
            '-write_id3v1', '1',
        ],
        'writethumbnail': True,
        'outtmpl': '%(title)s.%(ext)s', # Keeps filenames clean
        
        # Bypassing the 429 Error / Bot Detection
        'quiet': False,
        'no_warnings': False,
        'source_address': '0.0.0.0', # Forces IPv4 (helps bypass blocks)
        # Uncomment the line below if you keep getting 429 errors:
        # 'cookies_from_browser': 'safari', 
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)

if __name__ == "__main__":
    download_for_denon(video_urls)