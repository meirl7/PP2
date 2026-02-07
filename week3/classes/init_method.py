class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        print(title, author, pages, end='\n')

b = Book("1984", "George Orwell", 328)