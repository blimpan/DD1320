class Song:
    def __init__(self, a_track_id, a_duration, an_artist, a_title):
        self.track_id = a_track_id
        self.duration = a_duration
        self.artist = an_artist
        self.title = a_title

    def __lt__(self, other):
        return other.artist > self.artist

    def __str__(self):
        return self.title + " by " + self.artist

if __name__ == "__main__":
    songs = []
    with open("unique_tracks.txt", "r", encoding="utf-8") as track_file:
        for row in track_file:
            data = row.strip().split("<SEP>")
            songs.append(Song(*data))

    print(len(songs))
    print(songs[0])
    print(songs[-1])
