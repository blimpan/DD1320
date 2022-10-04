from songlist import Song
import timeit

all_songs = []
with open("unique_tracks.txt", "r", encoding="utf-8") as track_file:
    for row in track_file:
        data = row.strip().split("<SEP>")
        all_songs.append(Song(*data))


def linear_search(the_list, key):
    for item in the_list:
        if item.title == key:
            return True
    return False



if __name__ == "__main__":
    print("Taking time!")
    n = 250000
    sliced_list = all_songs[0:n]
    last_index = len(sliced_list)-1
    last_title = sliced_list[last_index].title

    linear_time = timeit.timeit(stmt=lambda: linear_search(sliced_list, last_title), number=10000)
    print("Linear search took:", round(linear_time, 4), "seconds")

