
from system.core.model import Model

class Book(Model):
    def __init__(self):
        super(Book, self).__init__()

    def show_reviews(self):
        query = "SELECT books.id AS book_id, books.title, reviews.star_rating, users.id AS user_id, users.name, reviews.review, reviews.created_at from reviews LEFT JOIN users ON users.id = reviews.user_id LEFT JOIN books ON books.id = reviews.book_id ORDER BY reviews.created_at DESC LIMIT 3"
        values = {}
        return self.db.query_db(query,values)
    def show_reviews_for_book(self, book_id):
        query = "SELECT books.id AS book_id, books.author_id, books.title, reviews.star_rating, users.id AS user_id, users.name, reviews.id AS review_id, reviews.review, reviews.created_at from reviews LEFT JOIN users ON users.id = reviews.user_id LEFT JOIN books ON books.id = reviews.book_id LEFT JOIN authors ON authors.id= books.author_id  WHERE books.id = :book_id ORDER BY reviews.created_at"
        values = {'book_id':book_id}
        return self.db.query_db(query,values)
    def show_reviewed_titles(self,id):
        query = "SELECT DISTINCT title, books.id FROM books LEFT JOIN reviews ON reviews.book_id = books.id LEFT JOIN users on users.id = reviews.user_id WHERE user_id = :user_id"
        values = {'user_id': id}
        return self.db.query_db(query,values)
    def show_books(self):
        query = "SELECT books.id, books.title from books"
        all_books = self.db.query_db(query)
        top_reviews = self.show_reviews()
        other_books = []
        for book in all_books:
            in_top_reviews = False
            for review in top_reviews:
                if review['book_id'] == book['id']:
                    in_top_reviews = True
            if in_top_reviews == False:
                other_books.append(book)
        return other_books
    def show_book(self, id):
        query = "SELECT books.id, books.title, authors.name as author from books LEFT JOIN authors ON authors.id = books.author_id WHERE books.id = :book_id"
        values = {'book_id':id}
        return self.db.query_db(query,values)
    def add_book(self, post, author_id):
        query = "INSERT INTO books (author_id, title, created_at, modified_at) VALUES (:author_id,:title,now(), now())"
        values = {'author_id':author_id,'title':post['title']}
        return self.db.query_db(query,values)
    def add_author(self, new_author):
        query = "INSERT INTO authors (name, created_at, modified_at) VALUES (:name, now(), now())"
        values = {'name':new_author}
        return self.db.query_db(query,values)
    def delete_review(self,review_id,book_id,author_id):
        query = "DELETE FROM reviews WHERE id = :review_id"
        values = {'review_id':review_id}
        return self.db.query_db(query,values)
    def add_review(self,post,book_id):
        # # print post
        # print book_id
        query = "INSERT INTO reviews (user_id, book_id, review, star_rating, created_at, modified_at) VALUES (:user_id, :book_id, :review, :star_rating, now(), now())"
        values = {'user_id' :post['user_id'],'book_id' :book_id,'review':post['review'],'star_rating':post['star_rating']}
        return self.db.query_db(query,values)
    def index_authors(self):
        query = "SELECT id, name FROM authors"
        return self.db.query_db(query)
