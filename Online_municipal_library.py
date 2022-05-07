from All_users import *
from Credit_card import *
class online_municipal_library(Main_library,Regular,credit_Card):

    def add_user(self,municipality):

        if  not isinstance(municipality,Regular):
           print("This user lives in the same municipality")
        else:
            print("User is not in the same municipality")

    def add_to_municipal_DB(self, y, filename="Library_DB.json"):

        s = "{\"Online Municipal Library\":[\n"
        with open(filename, 'w') as file:
            s += json.dumps(y.__dict__, indent=4)
            s += "\n]}"
            file.write(s)

    def Borrow_book(self,h, filename = "Municipal.json"):
        if self.available_credit >= 20:

            self.list_of_books_in_this_library.pop(h)
        else:
            print("your credit card is empty, please put some cash and try again")