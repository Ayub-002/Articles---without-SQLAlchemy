from lib.db import get_connection
from lib.models.article import Article

class Magazine:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self.name, self.category))
            self.id = cursor.lastrowid
        else:
            cursor.execute("UPDATE magazines SET name=?, category=? WHERE id=?", (self.name, self.category, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category FROM magazines")
        magazines = [Magazine(id=row[0], name=row[1], category=row[2]) for row in cursor.fetchall()]
        conn.close()
        return magazines

    def articles(self):
        return Article.find_by_magazine(self)

    def contributors(self):
        return list({article.author() for article in self.articles()})

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        return [author for author in self.contributors() if len([a for a in author.articles() if a.magazine().id == self.id]) > 2]
