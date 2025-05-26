# lib/models/author.py
from lib.db import get_connection

class Author:
    def __init__(self, name, email, id=None):
        self.id = id
        self.name = name
        self.email = email

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO authors (name, email) VALUES (?, ?)", (self.name, self.email)
        )
        conn.commit()
        self.id = cursor.lastrowid

    def articles(self):
        from lib.models.article import Article
        return Article.find_by_author(self)

    def magazines(self):
        return list({article.magazine() for article in self.articles()})
