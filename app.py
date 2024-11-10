import sqlite3



# Create a connection to a new database (or connect to an existing one)
conn = sqlite3.connect('movies.db')

# Create a cursor object+
cursor = conn.cursor()



# Create the movies table
cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT NOT NULL,

    director TEXT,

    year INTEGER,

    rating FLOAT
               
    genre TEXT
)
''')


# Insert a single movie using string formatting (UNSAFE - vulnerable to SQL injection)

movie = ('The Bee Movie', 'Steve Hickner, Simon J. Smith', 2007, 6.1)

cursor.execute(f'''

INSERT INTO movies (title, director, year, rating)

VALUES ('{movie[0]}', '{movie[1]}', {movie[2]}, {movie[3]})

''')


# Insert a single movie using a parameterized query (SAFE)

cursor.execute('''

INSERT INTO movies (title, director, year, rating)

VALUES (?, ?, ?, ?)

''', ('The Peanuts Movie', 'Steve Martino', 2015, 7))



# List of movies to insert

movies = [

    ('Shrek', 'Andrew Adamson & Vicky Jenson', 2001, 7.9),

    ('Puss in Boots: The Last Wish', 'Joel Crawford', 2022, 7.8),

    ('Megamind', ' Tom McGrath', 2010, 7.3),

    ('The Princess and The Frog', 'John Musker & Ron Clements', 2009, 7.1)

]



# Insert multiple movies

cursor.executemany('''

INSERT INTO movies (title, director, year, rating)

VALUES (?, ?, ?, ?)

''', movies)

# Select all movies

cursor.execute('SELECT * FROM movies')

all_movies = cursor.fetchall()

print("All movies:")

for movie in all_movies:

    print(movie)



# Select movies after 2000

cursor.execute('SELECT title, year FROM movies WHERE year > 2000')

recent_movies = cursor.fetchall()

print("\nMovies after 2000:")

for movie in recent_movies:

    print(f"{movie[0]} ({movie[1]})")



# Select average rating

cursor.execute('SELECT AVG(rating) FROM movies')

avg_rating = cursor.fetchone()[0]

print(f"\nAverage rating: {avg_rating:.2f}")



conn.close()