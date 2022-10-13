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

    def get_genre(self):
        return self.genre


class DictHash:
    def __init__(self):
        self.dict = {}

    def store(self, key, data):
        self.dict[key] = data

    def search(self, key):
        try:
            return self.dict[key]
        except KeyError:
            return False


if __name__ == "__main__":
    my_dict_hash = DictHash()
    with open("kdrama.csv", "r", encoding="utf-8") as drama_file:
        csv_reader = csv.reader(drama_file)  # reader object used for reading from csv-file
        next(csv_reader)  # skip header
        for i in range(10):
            row = next(csv_reader)
            my_dict_hash.store(row[0], Drama(*row))
    print(my_dict_hash.search("The King: Eternal Monarch"))
    print(my_dict_hash.search("Namn som inte finns med"))
