# scripts/run_queries.py

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.seed import seed_data

def run_queries():
    seed_data()

    # Query 1: All articles by Alice
    alice = Author.find_by_id(1)
    print(f"\nArticles by {alice.name}:")
    for article in alice.articles():
        print(f" - {article.title}")

    # Query 2: Magazines Bob has contributed to
    bob = Author.find_by_id(2)
    print(f"\nMagazines contributed by {bob.name}:")
    for mag in bob.magazines():
        print(f" - {mag.name} ({mag.category})")

    # Query 3: Contributors to Tech Monthly
    tech = Magazine.find_by_name("Tech Monthly")
    print(f"\nContributors to {tech.name}:")
    for author in tech.contributors():
        print(f" - {author.name}")

if __name__ == "__main__":
    run_queries()
