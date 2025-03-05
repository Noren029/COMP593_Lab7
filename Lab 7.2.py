import sqlite3

# Step 1: Open a connection to the database
con = sqlite3.connect('bond_movies.db')
cur = con.cursor()

# Step 2: Query the database for movies released before 1980
query = """
SELECT Year, Movie, Bond
FROM movies
WHERE Year < 1980
ORDER BY Year ASC
"""
cur.execute(query)

# Step 3: Fetch all results
movies_before_1980 = cur.fetchall()

# Step 4: Print each result in the desired format
print("Pre-1980 Bond Movies:")
for movie in movies_before_1980:
    year, title, bond = movie
    print(f"In {year} this movie was release and the actor was {bond} and the movie tittle is {title}.")

# Step 5: Close the database connection
con.close()
