import pandas as pd
import sqlite3

# Step 1: Open a connection to the SQLite database
con = sqlite3.connect('bond_movies.db')
cur = con.cursor()

# Step 2: Create the 'movies' table if it doesn't exist
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

# Step 5: Commit the transaction
con.commit()

# Step 6: Close the database connection
con.close()

print("Database populated successfully.")
