
from lib.db.db import get_connection
from lib.db.seed import seed_data
from lib.models.author import Author


def setup_and_seed():
    with open("lib/db/schema.sql") as f:
        get_connection().executescript(f.read())
    seed_data()

def test_author_can_save_and_retrieve():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM authors WHERE name = 'Alice'")
    row = cursor.fetchone()
    assert row is not None
    assert row[1] == "Alice"

def test_author_articles():
    author = Author(1, "Alice")
    articles = author.articles()
    assert len(articles) > 0
    assert articles[0].author_id == 1
