import pandas as pd
import sqlite3

# Step 1: Open a connection to the SQLite database (it will create the database if it doesn't exist)
con = sqlite3.connect('bond_movies.db')
cur = con.cursor()

# Step 2: Create the 'movies' table if it doesn't already exist
create_table_query = """
CREATE TABLE IF NOT EXISTS movies (
    Year INTEGER,
    Movie TEXT,
    Bond TEXT,
    Avg_User_IMDB REAL)
"""
cur.execute(create_table_query)

# Step 3: Load data from the CSV file into a Pandas DataFrame
bond_df = pd.read_csv('jamesbond.csv')

# Step 4: Insert data from the DataFrame into the database
for row in bond_df.itertuples(index=False):
    cur.execute('''
        INSERT INTO movies (Year, Movie, Bond, Avg_User_IMDB)
        VALUES (?, ?, ?, ?)
    ''', (row.Year, row.Movie, row.Bond, row.Avg_User_IMDB))

# Step 5: Commit the transaction to save the data
con.commit()

# Step 6: Query the database for movies released before 1980
query = """
SELECT Year, Movie, Bond
FROM movies
WHERE Year < 1980
ORDER BY Year ASC
"""
cur.execute(query)

# Step 7: Fetch all results from the query
movies_before_1980 = cur.fetchall()

# Step 8: Print each result in the desired format
print("Pre-1980 Bond Movies:")
for movie in movies_before_1980:
    year, title, bond = movie
    print(f"In {year} {bond} starred in {title}.")

# Step 9: Close the database connection
con.close()

