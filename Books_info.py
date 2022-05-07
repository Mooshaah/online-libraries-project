class Book:
## CLASS BOOK THAT CONTAINS ALL THE NESSASRY INSTANCE VARS FOR NEEDED FOR THE BOOKS DETAILS, AND CONTAINS THE LIST OF BORROWERS THAT BORROWED A BOOK 
    def __init__(self, title= "", authors= "", ISBN= "", noOfCps=1, noOfCpsBorrowed=0, physOrOnline=0, loanPeriod=30,
                 list_of_borrowers=[]):
        self._title = title
        self._authors = authors
        self._ISBN = ISBN
        self._noOfCps = noOfCps
        self._noOfCpsBorrowed = noOfCpsBorrowed
        self._physOrOnline = physOrOnline
        self._loanPeriod = loanPeriod
        self.list_of_borrowers = list_of_borrowers


    # setters

    def title(self, title):
        self._title = title


    def authors(self, authors):
        self._authors = authors


    def ISBN(self, ISBN):
        self._ISBN = ISBN


    def noOfCps(self, noOfCps):
        self._noOfCps = noOfCps


    def noOfCpsBorrowed(self, noOfCpsBorrowed):
        self._noOfCpsBorrowed = noOfCpsBorrowed


    def physOrOnline(self, physOrOnline):
        self._physOrOnline = physOrOnline


    def loanPeriod(self, loanPeriod):
        self._loanPeriod = loanPeriod



    def __eq__(self, other):
        if isinstance(other, type(self)):
            if self.ISBN == other.ISBN:
                return True
            elif (self.title == other.title) and (self.authors == other.authors):
                return True
            else:
                return False
        else:
            return False

    def __repr__(self):
        return f'Book Details are:\n' \
               f'Title: {self.title}\n' \
               f'Authors: {self.authors}\n' \
               f'ISBN: {self.ISBN}\n' \
               f'Total number of copies: {self.noOfCps}\n' \
               f'{"This book is available as a hard copy only" if (self.physOrOnline == 0) else None}' \
               f'{"This book is available as an online copy only" if (self.physOrOnline == 1) else None}' \
               f'{"This book is available as a hard copy as well as online" if (self.physOrOnline == 2) else None}' \
               f'\nLoan duration for this book is: {self.loanPeriod}\n'
