def tracklist(**tracks):
    for musician, value in tracks.items():
        print(musician)
        for song, track in tracks[musician].items():
            print(f"ALBUM: {song} TRACK: {track}")
