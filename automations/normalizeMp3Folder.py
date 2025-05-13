import os
from pydub import AudioSegment
from pydub.effects import normalize

def normalize_mp3(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3"):
            file_path = os.path.join(folder_path, filename)
            try:
                audio = AudioSegment.from_mp3(file_path)
                normalized_audio = normalize(audio)
                normalized_audio.export(os.path.join(folder_path, "normalized_" + filename), format="mp3")
                print(f"Normalized: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

folder_path = "/Users/rodriguezcanto/Documents/Cds/Facu cds/Facu mix 2" # Replace with the actual path
normalize_mp3(folder_path)