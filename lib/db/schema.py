def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS authors (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        email TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS articles (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT,
                        content TEXT,
                        author_id INTEGER,
                        magazine_id INTEGER,
                        FOREIGN KEY (author_id) REFERENCES authors(id),
                        FOREIGN KEY (magazine_id) REFERENCES magazines(id))''')
    # Ensure other necessary tables are also created
    conn.commit()
