source ../demucs-env/bin/activate;

#spotdl download https://open.spotify.com/playlist/3bko4nsuJSTMtlZ8JEaDdv?si=3549b71bb19140b4

spotdl download "https://api.spotify.com/v1/playlists/5LyZZywTQ3orJ4y1tSlNJU" \
--cookie-file cookies.txt \
--format mp3 \
--bitrate 256k \
--m3u "DENON_SET"