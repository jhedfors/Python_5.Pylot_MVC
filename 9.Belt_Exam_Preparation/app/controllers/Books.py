from system.core.controller import *

class Books(Controller):
    def __init__(self, action):
        super(Books, self).__init__(action)
        self.load_model('Book')
        self.db = self._app.db
    def books_view(self):
        reviews = self.models['Book'].show_reviews()
        books = self.models['Book'].show_books()
        return self.load_view('Books/books.html', reviews = reviews, books = books)
    def add_book_view(self):
        authors = self.models['Book'].index_authors()
        return self.load_view('Books/add_book.html',authors = authors)
    def add_book_form(self):
        post = request.form
        author_id = post['author_id']
        if not post['new_author'] == '':
            author_id = self.models['Book'].add_author(post['new_author'])
        book_id = self.models['Book'].add_book(post, author_id)
        self.models['Book'].add_review(post,book_id)
        return redirect('/books')
    def book_view(self,id):
        book = self.models['Book'].show_book(id)
        reviews = self.models['Book'].show_reviews_for_book(id)
        return self.load_view('Books/book.html', reviews = reviews, book = book)
    def add_review_form(self):
        book_id = request.form['book_id']
        print book_id
        print 'here'
        print request.form
        self.models['Book'].add_review(request.form, book_id)
        return redirect('/books/'+str(book_id))
    def delete_review(self,review_id,book_id,author_id):
        self.models['Book'].delete_review(review_id,book_id,author_id)
        return redirect('/books/'+str(book_id))
