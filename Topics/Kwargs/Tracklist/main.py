def tracklist(**tracks):
    for musician in tracks:
        print(musician)
        for song in tracks[musician]:
            print(f"ALBUM: {song} TRACK: {tracks[musician][song]}")
