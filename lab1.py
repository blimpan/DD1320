import csv


class Drama:

    def __init__(self, a_title, a_rating, some_actors, a_view_rate, a_genre, a_director, a_writer, a_year,
                 a_number_episodes, a_network):
        self.title = a_title
        self.rating = float(a_rating)
        self.actors = some_actors
        self.view_rate = float(a_view_rate)
        self.genre = a_genre
        self.director = a_director
        self.writer = a_writer
        self.year = int(a_year)
        self.num_episodes = int(a_number_episodes)
        self.network = a_network

    def __str__(self):
        return self.title

    def __lt__(self, other):
        if self.rating < other.rating:
            return True
        else:
            return False

    def get_actors(self):
        return self.actors

    def is_older_than(self, another_year):
        return self.year < another_year


def test_function():
    with open("kdrama.csv", encoding="utf-8") as drama_file:

        csv_reader = csv.reader(drama_file)  # reader object used for reading from csv-file
        next(csv_reader)  # skip first row of file containing headers
        data = next(csv_reader)
        first_drama = Drama(*data)

        data = next(csv_reader)
        second_drama = Drama(*data)

    print(first_drama, "-- Rating:", first_drama.rating, "-- Year:", first_drama.year)
    print(second_drama, "-- Rating:", second_drama.rating, "-- Year:", second_drama.year)
    print(first_drama < second_drama)
    print(first_drama.get_actors())
    print(first_drama.is_older_than(second_drama.year))


def get_all_dramas():
    with open("kdrama.csv", encoding="utf-8") as drama_file:

        csv_reader = csv.reader(drama_file)  # reader object used for reading from csv-file
        next(csv_reader)  # skip first row of file containing headers

        drama_list = []

        for line in csv_reader:
            drama_list.append(Drama(*line))

        return drama_list


def search_in_list(drama_list):
    for drama in drama_list:
        a_year = 2021
        a_rating = 8.5
        if drama.year > a_year and drama.rating > a_rating:
            print(drama.title, "has a rating above", a_rating, "and was released after", a_year)


# test_function()
# print(*get_all_dramas())
# search_in_list(get_all_dramas())
