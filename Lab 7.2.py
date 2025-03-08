import sqlite3

def get_pre_1980_bond_movies(db_path):
    """Fetches Bond movies released before 1980 from the database."""
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    
    query = """
    SELECT Year, Movie, Bond
    FROM movies
    WHERE Year < 1980
    ORDER BY Year ASC
    """
    cur.execute(query)
    movies = cur.fetchall()
    
    con.close()
    return movies

def main():
    db_path = 'bond_movies.db'
    movies = get_pre_1980_bond_movies(db_path)
    
    print("Pre-1980 Bond Movies:")
    for year, title, bond in movies:
        print(f"In {year}, the movie '{title}' was released, starring {bond} as James Bond.")

if __name__ == "__main__":
    main()

