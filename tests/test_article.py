
from lib.models.article import Article
from lib.db.seed import seed_data


def setup():
    seed_data()

def test_find_articles_by_author():
    articles = Article.find_by_author_id(1)  # Alice
    assert any(a.title == "AI and You" for a in articles)

def test_find_articles_by_magazine():
    articles = Article.find_by_magazine_id(1)
    titles = [a.title for a in articles]
    assert "5G Myths" in titles
