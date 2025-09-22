import os
from pydub import AudioSegment

# For copying tags and cover art
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error

# Set your target dBFS (decibels relative to full scale)
TARGET_DBFS = -14.0

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)



folder = "../vienes/NotSoDance1/"  # Change this to your folder path
print("--->:", folder)
print("--->:", os.listdir(folder))

# Create a list of all mp3 files in the folder
mp3_files = [f for f in os.listdir(folder) if f.lower().endswith('.mp3')]
print(f"Found {len(mp3_files)} mp3 files:")
for f in mp3_files:
    print(f"  {f}")

# Optionally, print dBFS for each file before normalization
print("\nOriginal dBFS values:")
for f in mp3_files:
    filepath = os.path.join(folder, f)
    audio = AudioSegment.from_mp3(filepath)
    print(f"{f}: {audio.dBFS:.2f} dBFS")

# Create 'normalized' subfolder if it doesn't exist
normalized_folder = os.path.join(folder, "normalized")
os.makedirs(normalized_folder, exist_ok=True)

for filename in mp3_files:
    print("Processing file:", filename)
    filepath = os.path.join(folder, filename)
    audio = AudioSegment.from_mp3(filepath)
    normalized_audio = match_target_amplitude(audio, TARGET_DBFS)

    normalized_path = os.path.join(normalized_folder, filename)
    normalized_audio.export(normalized_path, format="mp3")

    # Copy tags and cover art using mutagen
    try:
        original = MP3(filepath, ID3=ID3)
        normalized = MP3(normalized_path, ID3=ID3)
        # Remove any tags in the normalized file
        normalized.delete()
        # Copy all tags from original
        normalized.tags = original.tags.copy()
        normalized.save()
        print(f"Normalized {filename} (tags preserved)")
    except Exception as e:
        print(f"Normalized {filename} (tags NOT preserved): {e}")

# Make sure to install pydub and ffmpeg:
# pip install pydub
# brew install ffmpeg  # On Mac
# pip install mutagen