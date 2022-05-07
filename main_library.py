import json


class Main_library:
    Borrowing_counter = 0
    def __init__(self, list_of_books_in_this_library=[],
                 Borrowing_policy = "", List_of_active_loans=[], add_book =""):
         self.list_of_books_in_this_library = list_of_books_in_this_library
         self.Borrowing_policy = Borrowing_policy
         self.List_of_active_loans = List_of_active_loans
         self.add_book = add_book
 


    def append_to_lib_DB(self, x,filename = "Library_DB.json"):

        # 1. Read file contents
        with open(filename, "r") as file:
            data = json.load(file)
        # 2. Update json object
        data["Library"].append(x.__dict__)
        # 3. rite json file
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    @property
    def Add_Book(self):
        return

    @Add_Book.setter
    def Add_Book(self, value):
            pass

    @property
    def lst_of_registered_users(self):
        return 
    
    @lst_of_registered_users.setter
    def lst_of_registered_users(self, value):
        pass

    def Borrow_book(self,h):

        self.list_of_books_in_this_library.pop(h)


    def Return_a_book(self,h):
        pass

    def Search_For_Book(self, title):
        bookIndex = -1
        for i, book in enumerate(self.list_of_books_in_this_library ):
            if book.title == title:
                bookIndex = i
        return bookIndex


    def Add_or_change_borrowing_policy(self, n):
       # need to override the Restrict a user method
       #  User.Restrict_a_user()
        self.Borrowing_policy = Main_library.Borrowing_counter
        self.Borrowing_policy += 1
        if self.Borrowing_policy == n: # n is going to be a variable which later on is going to let the librarian user to edit the maximum no. of borrows possible for each user
            print("you've been Banned for the excessive usage of loan property")


    def list_of_active_loans(self):
        #  the method will take the popped item from the list and then add it to the list of active loans
        self.List_of_active_loans.append(self.Borrow_book)



    def borrow_book(self,title):
        pass
        # if isinstance(Student,title):
        #     self.list_of_books_in_this_library.pop(title)