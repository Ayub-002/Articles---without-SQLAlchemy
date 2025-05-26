from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed_data():
    author1 = Author(name="Alice Smith", email="alice@example.com")
    author1.save()
    author2 = Author(name="Bob Jones", email="bob@example.com")
    author2.save()

    mag1 = Magazine(name="Tech Weekly", category="Technology")
    mag1.save()
    mag2 = Magazine(name="Health Today", category="Health")
    mag2.save()

    a1 = Article(title="Tech Trends", content="AI and more", author_id=author1.id, magazine_id=mag1.id)
    a2 = Article(title="Health Tips", content="Drink water", author_id=author1.id, magazine_id=mag2.id)
    a3 = Article(title="Cybersecurity", content="Stay safe", author_id=author2.id, magazine_id=mag1.id)
    for a in [a1, a2, a3]:
        a.save()
