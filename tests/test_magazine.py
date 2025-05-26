
from lib.db.db import get_connection
from lib.db.seed import seed_data
from lib.models.magazine import Magazine


def setup_and_seed():
    with open("lib/db/schema.sql") as f:
        get_connection().executescript(f.read())
    seed_data()

def test_magazine_contributors():
    magazine = Magazine(2, "Tech Monthly", "Technology")
    contributors = magazine.contributors()
    assert len(contributors) >= 1
    assert contributors[0].__class__.__name__ == "Author"

def test_magazine_article_titles():
    magazine = Magazine(2, "Tech Monthly", "Technology")
    titles = magazine.article_titles()
    assert "AI Trends" in titles
    assert "Neural Nets" in titles

def test_magazine_contributing_authors():
    magazine = Magazine(2, "Tech Monthly", "Technology")
    contributing_authors = magazine.contributing_authors()
    assert isinstance(contributing_authors, list)
