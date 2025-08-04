books = [
    {"title": "Harry Potter", "tags": "magic wizard school fantasy"},
    {"title": "The Hobbit", "tags": "fantasy dragon journey"},
    {"title": "Sherlock Holmes", "tags": "mystery crime detective"},
    {"title": "Pride and Prejudice", "tags": "romance classic love"},
    {"title": "The Da Vinci Code", "tags": "mystery thriller secret"},
    {"title": "Percy Jackson", "tags": "mythology hero adventure"}
]
user_input = input("What types of books do you like? ").strip().lower()
user_tags = set(user_input.split())

recommendations = []
for book in books:
    book_tags = set(book["tags"].split())
    score = len(user_tags.intersection(book_tags))
    recommendations.append((book["title"], score))

recommendations.sort(key=lambda x: x[1], reverse=True)
print("\n📚 Recommended Books:")
for title, score in recommendations[:3]:
    if score > 0:
        print(f"- {title} (Matched Tags: {score})")

