"""A program to analyse some movie data.
Find the average budget of the films in our data set, and
identify high budget films that exceed the average budget we calculate."""

MOVIE_TYPE = tuple[str, int]


movies: list[MOVIE_TYPE] = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

new_movie_count: int = int(input("Enter how many new movies you wish to add: "))

for _ in range(new_movie_count):
    name: str = input("Enter new movie name: ").strip().title()
    budget: int = int(input("Enter new movie budget: "))
    new_movie: MOVIE_TYPE = (name, budget)
    movies.append(new_movie)

total_budget: int = 0
counter: int = 0

for name, budget in movies:
    total_budget += budget

average_budget: float = total_budget / len(movies)

print(f"The average budget of all movies is {average_budget:_}")

for name, budget in movies:
    if budget > average_budget:
        print(f"{name} has a budget higher than the average by {budget - average_budget:_}")
        counter += 1

print(f"{counter} movies that have they budget higher than the average")
