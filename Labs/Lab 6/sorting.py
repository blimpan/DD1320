# metoderna för sortering av data togs från Linda Kanns föreläsninganteckningar.

from songlist import Song
import timeit


def bubbelsortera(data):
    n = len(data)
    bytt = True
    while bytt:
        bytt = False
        for i in range(n - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                bytt = True
    return data


def quicksort(data):
    sista = len(data) - 1
    return qsort(data, 0, sista)


def qsort(data, low, high):
    pivotindex = (low + high) // 2
    # flytta pivot till kanten
    data[pivotindex], data[high] = data[high], data[pivotindex]

    # damerna först med avseende på pivotdata
    pivotmid = partitionera(data, low - 1, high, data[high])

    # flytta tillbaka pivot
    data[pivotmid], data[high] = data[high], data[pivotmid]

    if pivotmid - low > 1:
        qsort(data, low, pivotmid - 1)
    if high - pivotmid > 1:
        qsort(data, pivotmid + 1, high)
    return data


def partitionera(data, v, h, pivot):
    while True:
        v = v + 1
        while data[v] < pivot:
            v = v + 1
        h = h - 1
        while h != 0 and data[h] > pivot:
            h = h - 1
        data[v], data[h] = data[h], data[v]
        if v >= h:
            break
    data[v], data[h] = data[h], data[v]
    return v


if __name__ == "__main__":
    all_songs = []
    with open("unique_tracks.txt", "r", encoding="utf-8") as track_file:
        for row in track_file:
            data = row.strip().split("<SEP>")
            all_songs.append(Song(*data))
    n = 100000
    sliced_list = all_songs[0:n]

    print("N:", n)
    print("Taking time (bubblesort)!")
    sorting_time = timeit.timeit(stmt=lambda: bubbelsortera(sliced_list), number=1)
    print("Sorting took:", round(sorting_time, 4), "seconds")

    print("Taking time (quicksort)!")
    sorting_time = timeit.timeit(stmt=lambda: quicksort(sliced_list), number=1)
    print("Sorting took:", round(sorting_time, 4), "seconds")