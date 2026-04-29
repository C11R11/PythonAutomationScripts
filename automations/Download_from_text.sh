import yt_dlp
import os

# Configuration
INPUT_FILE = "songs.txt"
COOKIES_BROWSER = "safari" # Crucial to avoid 429 errors

def download_official_audio():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        return

    with open(INPUT_FILE, "r") as f:
        queries = [line.strip() for line in f if line.strip()]

    ydl_opts = {
        # 'ytmsearch1:' forces the first result from the "Music" category specifically
        'default_search': 'ytmsearch',
        'format': 'bestaudio/best',
        
        # FILTER: Ignore results over 10 minutes (likely DJ sets/docs)
        'match_filter': yt_dlp.utils.match_filter_func("duration < 600"),

        'postprocessors': [
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '320'},
            {'key': 'FFmpegMetadata', 'add_metadata': True},
            {'key': 'EmbedThumbnail'}
        ],
        
        # Denon Compatibility Force
        'postprocessor_args': ['-id3v2_version', '3', '-write_id3v1', '1'],
        
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        'cookies_from_browser': COOKIES_BROWSER,
        'impersonate': 'chrome',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for query in queries:
            # We add " (Official Audio)" to the search string to prioritize label releases
            refined_query = f"{query} (Official Audio)"
            print(f"\n--- Targeted Search: {refined_query} ---")
            try:
                # Use ytmsearch1 to pull from the 'Songs' shelf on YTM
                ydl.download([f"ytmsearch1:{refined_query}"])
            except Exception as e:
                print(f"Failed: {e}")

if __name__ == "__main__":
    download_official_audio()