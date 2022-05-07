import json
from main_library import Main_library

main_lib = Main_library() # OBJECT FROM THE MAIN LIBRARY


class User: ## PARENT CLASS
    # CONSTRUCTOR AND INITIALIZER
    def __init__(self, usertype=None, name=None, email=None, id_num=None, legal_age=18, Social_number=None,
                 Allowed_list_of_user_types=[], List_of_already_registered_users=[],
                 List_of_restricted_users=[], Borrowing_policy=None, Loan_period=None, address = None):
        # INSTANCE VARS
        self.user_type = usertype
        self.name = name
        self.email = email
        self.id_num = id_num
        self.legal_age = legal_age
        self._address = address
        self._Social_number = Social_number
        self.Allowed_list_of_user_types = Allowed_list_of_user_types
        self.List_of_already_registered_users = List_of_already_registered_users
        self.List_of_restricted_users = List_of_restricted_users
        self.Borrowing_policy = Borrowing_policy
        self.Loan_period = Loan_period
# METHOD TO ADD THE INPUTS THAT WAS ENTERED DURING THE PROGRAM IN THE JSON FILE NAMED "User_DB.JSON"
    def append_to_DB(self, x, filename="User_DB.json"):
        # 1. Read file contents
        with open(filename, "r") as f:
            data = json.load(f)
        # 2. Update json object
        data["users"].append(x.__dict__)
        # 3. write json file
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

# METHOD TO RETURN THE KEYS INTO A DICTIONARY FORM TO BE STORED INTO TBE JSON FILE
# JSON FILES ONLY USE THE DICTIONARY DATA TYPE AND STORES THEM INTO THE FILE
    def __dict__(self):
        return{
    'name': self.name,
    'ID': self.id_num,
    'email': self.email,
    'type':self.user_type
    }
## METHODS
# USER TYPES THAR ARE ALLOWED TO EXIST IN THE LIBRARY SETTER AND GETTERS
    @property
    def allowed_types(self):
        return self.Allowed_list_of_user_types

    @allowed_types.setter
    def allowed_types(self, value):
        self.Allowed_list_of_user_types.append(value)

# user Type Setter & Getter
    @property
    def get_users_t(self):
        return self.user_type

    @get_users_t.setter
    def get_users_t(self, value):
        self.user_type = value
# A METHOD WHICH RECEIVES INPUT FROM THE USER FROM THE MAIN THEN ADDS THE NAME, ID, OR EMAIL ANYTHING THAT IS USER RELATED TO THE LIST
#  List "List_of_already_registered_users"
    def add_user(self, value):
        self.List_of_already_registered_users.append(value)

# User name setter & Getter
    @property
    def new_users_name(self):
        return self.name

    @new_users_name.setter
    def new_users_name(self, value):
        self.name = value

# user Email Setter & Getter
    @property
    def new_users_email(self):
        return self.email

    @new_users_email.setter
    def new_users_email(self, value):
        self.email = value

# user ID Setter & Getter
    @property
    def new_users_id(self):
        return self.id

    @new_users_id.setter
    def new_users_id(self, value):
        self.id = value
# BORROWING CONDITIONS SETTER, THAT METHOD RECEIVES INPUT FROM THE MAIN FILE AND THE STORES THAT INPUT INSIDE A str FORMAT
# AND THEN DISPLAYS THE LIBRARY CONDITIONS SET BY THE LIBRARIAN OF THE LIBRARY
    def borrowing_conditions(self):
        pass

    @property
    def restricted_user(self):
        return print(self.name+ " has been restricted from the library")

    def loan_period_maximum_value(self, value):
        self.loan_period = value

    @restricted_user.setter
    def restricted_user(self, value):
        if value > self.loan_period_maximum_value(value):
            self.List_of_already_registered_users.pop()
            print(self.name + " Has been banned due to Excessive usage of Loan period")


class Admin(User): ## SUB-CLASS
    def __init__(self, Legal_age="", social_number=""):
        super(Admin, self).__init__(Legal_age, social_number)
        self.Legal_age = Legal_age
# INHERITED METHOD FROM THE CLASS USER, SO THAT WE CAN ASSIGN IT AS A ONE OF THE FUNCTIONS FOR THE ADMIN USER
    def add_user(self, value):
        self.List_of_already_registered_users.append(value)
# ALLOWED TYPES SETTER AND GETTER INHERITED FROM THE PARENT USER
    @property
    def allowed_types(self):
        return self.Allowed_list_of_user_types

    @allowed_types.setter
    def allowed_types(self, value):
        self.Allowed_list_of_user_types.append(value)
# THIS METHOD RECEIVES A CERTAIN USERNAME, ID, OR EMAIL AS AN INPUT FROM THE MAIN THEN REMOVE IT FROM THE LIST "List_of_already_registered_users" AND THEN ADDS IT TO THE LIST "List_of_restricted_users"
    def Remove_user(self, value):
        self.List_of_already_registered_users.pop(value), self.List_of_restricted_users.append(value)

        return

    def library_stats(self):
        #  This function is supposed the latest updates happened in the system
        return self.List_of_already_registered_users[-1], main_lib.list_of_books_in_this_library[-1], \
               main_lib.List_of_active_loans[-1], self.List_of_restricted_users[-1]


class Librarian(Main_library): ## THIS SUB CLASS INHERITS FROM THE PARENT CLASS " MAIN_LIBRARY " WHICH CONTAINS ALL THE LISTS USED INSIDE THESE METHODS INORDER TO STORE BOOK INFO AND BORROWED BOOK INFO
                               #SUBCLASS LIBRARIAN
# BOOK SETTER AND GETTER AND AFTER THE LIBRARIAN ADDS A BOOK TITLE, AUTHOR, ISBN ITS ADDED TO THE LIST "list_of_books_in_this_library" 
    @property
    def Add_Book(self):
        return

    @Add_Book.setter
    def Add_Book(self, value):

        self.add_book = value
        self.list_of_books_in_this_library.append(value)
# THIS METHOD IS USED TO REMOVE A CERTAIN BOOK INSIDE THE LIST "list_of_books_in_this_library"
    def Remove_book(self, h):
        self.list_of_books_in_this_library.pop(h)
#  THIS METHOD RECEIVES A BOOK TITLE AND IRRITATES INSIDE THE LIST "list_of_books_in_this_library" IN A LOOP SEARCHING FOR A MATCH AND IF IT FINDS THE BOOK THEN IT WILL DISPLAY THE BOOK TITLE IS IN THE LIBRARY
    def Search_For_Book(self, title):
        for title in main_lib.list_of_books_in_this_library:
            if title in main_lib.list_of_books_in_this_library:
                print(title + " is in the library")

    def list_of_active_loans(self):
#  the method will take the popped item from the list and then add it to the list of active loans
        self.List_of_active_loans.append(self.Borrow_book)
        print(self.List_of_active_loans)
# THIS METHOD IS INHERITED FORM THE PARENT CLASS AND IT RECEIVES AN INPUT FROM THE USER IN TYPE str THEN DISPLAYS IT TO THE STUDENT/ REGULAR USERS BEFORE BORROWING ANY BOOKS SO THAT THEY CAN READ IT AND KNOW THE LIBRARY CONDITIONS
    def borrowing_policy(self, value):
        print(value)


class Student(User): ##SUB CLASS WHICH RESTRAINT FROM THE PARENT CLASS " User "
 
    def __init__(self, student=""):
        super(Student, self).__init__(student)
# A METHOD THAT CHECKS THE USER TYPE IF IT'S A STUDENT OR NOT, AND IF NOT IT DISPLAYS A MESSAGE TO THE USER 
    def borrow_book(self, title):
        if isinstance(Student, title):
            main_lib.list_of_books_in_this_library.pop(title)
        else:
            print("Invalid user type")
# THIS METHOD RECEIVES A BOOK TITLE AS AN INPUT FROM THE MAIN METHOD THEN ADD IT BACK INSIDE THE LIST THAT CONTAINS THE BOOKS
    def Return_a_book(self, x):
        main_lib.list_of_books_in_this_library.append(x)


class Regular(User): ## SUB-CLASS FROM THE PARENT CLASS " User "
    def __init__(self):
        self.municipality = "cairo"
# SOCIAL NUMBER SETTER AND GETTER 
    @property
    def socialNumber(self):
        return self._Social_number

    @socialNumber.setter
    def socialNumber(self, value):
        self._Social_number = value
# AGE SETTER AND GETTER
    @property
    def age(self):
        return

    @age.setter
    def age(self, value):
        self.legal_age = value
# MUNICIPALITY SETTER AND GETTER
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

# A METHODS WHICH ENSURES THAT THE USER HAS A CREDIT CARD SO THAT ANY PAYMENTS ARE GOING TO BE MADE
    def credit_card_value(self, credit_Value):
        credit_Value = 200
