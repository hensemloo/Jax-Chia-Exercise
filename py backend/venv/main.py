from fastapi import FastAPI, Body


app = FastAPI()

BOOKS = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"title": "1984", "author": "George Orwell"},
    {"title": "Pride and Prejudice", "author": "Jane Austen"},
]

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/books/{book_title}")
async def get_books(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
    return "book not found"

@app.get("/books")
async def get_book_by_query(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold(): 
            books_to_return.append(book)

            return books_to_return

@app.get("/books/")
async def get_books_by_query(author: str, title: str = None):
    books_to_return = []
    for book in BOOKS:
        if author and book.get("author").casefold() == author.casefold():
            books_to_return.append(book)
        elif title and book.get("title").casefold() == title.casefold():
            books_to_return.append(book)

    return books_to_return

@app.get("/books/")
async def get_book_by_query(author: str, published_year: int):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold() and \
           book.get("published_year") == published_year:
            books_to_return.append(book)
    return books_to_return

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return {"message": "Book created successfully"}