import pandas as pd
import sqlite3

def create_movies_table(con):
    """Creates the 'movies' table if it does not exist."""
    cur = con.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS movies (
        Year INTEGER,
        Movie TEXT,
        Bond TEXT,
        Avg_User_IMDB REAL)
    """
    cur.execute(create_table_query)
    con.commit()

def load_data_into_db(con, csv_file):
    """Loads data from a CSV file into the SQLite database."""
    bond_df = pd.read_csv(csv_file)
    cur = con.cursor()
    for row in bond_df.itertuples(index=False):
        cur.execute('''
            INSERT INTO movies (Year, Movie, Bond, Avg_User_IMDB)
            VALUES (?, ?, ?, ?)
        ''', (row.Year, row.Movie, row.Bond, row.Avg_User_IMDB))
    con.commit()

def main():
    db_path = 'bond_movies.db'
    csv_file = 'jamesbond.csv'
    
    con = sqlite3.connect(db_path)
    create_movies_table(con)
    load_data_into_db(con, csv_file)
    
    print(pd.read_sql_query('SELECT * FROM movies', con))
    
    con.close()

if __name__ == "__main__":
    main()



print("Database populated successfully.")
