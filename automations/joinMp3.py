import subprocess

# Create a text file listing the MP3 files to concatenate
with open("concat_list.txt", "w") as f:
    f.write("file 'file1.mp3'\n")
    f.write("file 'file2.mp3'\n")

# Construct the FFmpeg command
command = [
    "ffmpeg",
    "-f", "concat",
    "-safe", "0",
    "-i", "concat_list.txt",
    "-c", "copy",
    "combined_output.mp3"
]

# Execute the FFmpeg command
subprocess.run(command, check=True)