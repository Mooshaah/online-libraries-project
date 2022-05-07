from All_users import *
from Credit_card import *
Credit = credit_Card()
class online_national_library(Main_library,credit_Card,Regular):
    def __int__(self):
        self.Legal_age = 18
    @property
    def age(self):
        return

    @age.setter
    def age(self, value):
        if value >= self.Legal_age:
            print("age verified welcome to the Online National library")
        else:
            print("your age doesn't meet the requirements set by the library")

    @property
    def social_no(self):
        return self.Social_number
    @social_no.setter
    def social_no(self, value):
        self.Social_number = value


    def add_user(self,social_no):
        if not isinstance(social_no, Regular):
            print("This user meets the library requirements and has been added to the library data base")
        else:
            print("User can't be added")


    def borrowBook(self, book):
        if Credit.available_credit >= 20:
            print("you can borrow a book")
            self.list_of_books_in_this_library.append(book)
        else:
            print("you should have credit balance in your credit card")
