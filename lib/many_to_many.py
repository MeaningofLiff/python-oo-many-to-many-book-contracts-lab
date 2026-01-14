class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("title must be a string")
        if value.strip() == "":
            raise Exception("title must not be empty")
        self._title = value

    def contracts(self):
        return [c for c in Contract.all if c.book is self]

    def authors(self):
        authors = []
        for c in self.contracts():
            if c.author not in authors:
                authors.append(c.author)
        return authors


class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("name must be a string")
        if value.strip() == "":
            raise Exception("name must not be empty")
        self._name = value

    def contracts(self):
        return [c for c in Contract.all if c.author is self]

    def books(self):
        books = []
        for c in self.contracts():
            if c.book not in books:
                books.append(c.book)
        return books

    # ✅ REQUIRED BY TESTS
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    # (Optional alias to match the wording in your prompt)
    def sign_contracts(self, book, date, royalties):
        return self.sign_contract(book, date, royalties)

    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an instance of Author")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be an instance of Book")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        if value.strip() == "":
            raise Exception("date must not be empty")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be an integer")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        if not isinstance(date, str):
            raise Exception("date must be a string")
        return [c for c in cls.all if c.date == date]
 