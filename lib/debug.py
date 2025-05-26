from lib.db.connection import get_connection
from lib.db.seed import seed_data
from lib.models.author import Author
from lib.models.magazine import Magazine

# Re-seed the data each time
seed_data()

# Examples:
alice = Author.find_by_id(1)
print("Alice's Articles:")
for article in alice.articles():
    print(f" - {article.title} in {article.magazine.name}")

print("\nMagazines Alice has contributed to:")
for mag in alice.magazines():
    print(f" - {mag.name} ({mag.category})")

tech = Magazine.find_by_id(1)
print("\nTech Magazine Contributors:")
for author in tech.contributors():
    print(f" - {author.name}")

print("\nContributing authors (>2 articles):")
for author in tech.contributing_authors():
    print(f" - {author.name}")
