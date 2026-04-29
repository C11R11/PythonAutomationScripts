docker run -it -v $(pwd)/downloads:/music \
  pndurette/zotify:latest \
  --username "cristianrodriguezcanto@gmail.com" --password "g46ytd72" \
  --output "/music" \
  https://open.spotify.com/playlist/5LyZZywTQ3orJ4y1tSlNJU