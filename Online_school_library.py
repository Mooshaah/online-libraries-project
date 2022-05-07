from All_users import *

class online_school_library(Main_library,Student):

    def add_user(self, value):
         if not isinstance(value,Regular):
             self.List_of_already_registered_users.append(value)



    def Borrow_book(self, user):
        if isinstance(user, Student):
            self.list_of_books_in_this_library.pop(user)
