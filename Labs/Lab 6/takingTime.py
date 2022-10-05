from songlist import Song
import timeit

all_songs = []
with open("unique_tracks.txt", "r", encoding="utf-8") as track_file:
    for row in track_file:
        data = row.strip().split("<SEP>")
        all_songs.append(Song(*data))


def linear_search(the_list, key):
    for item in the_list:
        if item.track_id == key:
            return True
    return False


def binary_search(the_list, the_key):
    low = 0
    high = len(the_list)-1
    while high - low >= 0:
        mid_index = (high + low) // 2
        mid_element = the_list[mid_index]
        if mid_element == the_key:
            return mid_element
        elif the_key < mid_element:
            high = mid_index-1
        elif mid_element < the_key:
            low = mid_index+1
    return None


def hash_search(the_dict, the_key):
    return the_key in the_dict


def linear_timer():
    n = 1000*1000
    sliced_list = all_songs[0:n]
    last_index = len(sliced_list) - 1
    last_element = sliced_list[last_index]

    print("Taking time (linear)!")
    linear_time = timeit.timeit(stmt=lambda: linear_search(sliced_list, last_element.track_id), number=10000)
    print("Linear search took:", round(linear_time, 4), "seconds")


def binary_timer():
    print("Sorting...")
    n = 1000*1000
    sliced_list = all_songs[0:n]
    sorted_list = sorted(sliced_list)
    last_index = len(sorted_list) - 1
    last_element = sorted_list[last_index]

    print("Taking time (binary)!")
    binary_time = timeit.timeit(stmt=lambda: binary_search(sorted_list, last_element), number=10000)
    print("Binary search took:", round(binary_time, 4), "seconds")


def hash_timer():
    track_dict = {}
    print("Sorting...")
    n = 1000*1000
    sliced_list = all_songs[0:n]
    last_index = len(sliced_list) - 1
    last_element = sliced_list[last_index]
    for song in sliced_list:
        track_dict[song.track_id] = song

    print("Taking time (hash)!")
    hash_time = timeit.timeit(stmt=lambda: hash_search(track_dict, last_element.track_id), number=10000)
    print("Hash search took:", round(hash_time, 4), "seconds")


if __name__ == "__main__":
    # linear_timer()
    #binary_timer()
    # hash_timer()
    pass
