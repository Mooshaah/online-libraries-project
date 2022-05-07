'''
## Assignment 2 inheritance, polymorphism ,and files
# written by Mohamed Medhat Elshaarawy
# GitHub username: Moshaah
'''
import warnings
from All_users import *
from Books_info import Book
from Online_municipal_library import online_municipal_library
from Online_national_library import online_national_library
from Online_school_library import online_school_library

# objects used to use the classes 
main_lib = Main_library()
municipal = online_municipal_library()
online_school_lib = online_school_library()
regular = Regular()
student  = Student()
national = online_national_library()
admin = Admin()
librarian = Librarian()
book = Book()
user = User()
user_file = "User_DB.json"
library_file = "Library_DB.json"
#  The whole program will get excuted inside the while loop so when the user finish using a certian function, the program will go back to the main menu
while True:

    main_menu = int(input(print("==========================================================\n" # Library main menu
                                "             Welcome to the Libraries Main-Menu           \n"
                                "==========================================================\n"
                                "1)Online School Library\n"
                                "2)Online Municipal Library\n"
                                "3)Online National Library\n"
                                "==========================================================\n")))
    if main_menu == int(1):
        menu = int(input(print("==========================================================\n" # school menu
                           "               Welcome to the Online School Library       \n"
                           "==========================================================\n"
                           " Choose the user type \n"
                           "1) Admin \n"
                           "2) Librarian \n"
                           "3) Student\n"
                           "==========================================================\n")))
        if menu == 1:
            # admin menu
            admin_choice =int(input(print("============================================================================\n"
                                      "                            Welcome to the Admin user Menu            \n"
                                      "=============================================================================\n"
                                      "1) Add a User\n"
                                      "2) Remove a user\n"
                                      "3) Get library stats\n"
                                      "=============================================================================\n")))

            if admin_choice == 1:
                name= input("Enter the name of the user that you want to add : ")
                type = str(input("Enter the new user type: "))
                id_no = input("Enter the new user id: ")
                email = input("Enter the new user email: ")
                # User info setter
                admin.List_of_already_registered_users.append(name)
                admin.List_of_already_registered_users.append(type)
                admin.List_of_already_registered_users.append(id_no)
                admin.List_of_already_registered_users.append(email)

                all_data = admin.List_of_already_registered_users.adduser(name, type, id_no, email)
                # school_user_data = user(name, typ, id_num, email)

                with open(user_file,'r')as openfile:
                    for data in admin.List_of_already_registered_users:
                        json.dumps(data.__dict__(),all_data)

            elif admin_choice == 2:
                address = input("Enter the name of the user that you want to remove")
                user_deletion = admin.Remove_user(address)
                print(user_deletion)
            elif admin_choice == 3:
                stats = admin.library_stats()
                print(stats)
        elif menu == 2:
            librarian_choice = int(input(print("==========================================================\n"
                                               "               Welcome to the Librarian user Menu         \n"
                                               "==========================================================\n"
                                               "1) Add a book \n" 
                                               "2) Remove a book\n"
                                               "3) search for a book \n"
                                               "4) View Active loans \n"
                                               "5) Set maximum loan period duration\n"
                                               "6) Set the borrowing policy\n"
                                               "==========================================================\n")))

            if librarian_choice == 1:
                n = int(input("Enter how many books you want to Add? "))
                for i in range(n): # after the librarian user decides how many books he wants to add the loop irotates according to the number of the book he want to add
                    title = input("Enter the name of the Book that you want to add")
                    authors = input("Enter the Author name")
                    ISBN = int(input("Enter the ISBN number of the book"))
                    no_of_copies = int(input("Enter the number of copies available at the library"))
                    no_of_copies_borrowed = int(input("Enter the nuber of copies that are loaned at the moment"))
                    physOrOnline = str(input("Enter the type of the book whether if it's available as a PHYSICAL or ONLINE"))
                # settin the books info
                    school_bookTitle = book.title(title)
                    school_bookAuthor = book.authors(authors)
                    school_book_ISBN = book.ISBN(ISBN)
                    school_book_copies = book.noOfCps(no_of_copies)
                    school_borrowed_copies = book.noOfCpsBorrowed(no_of_copies_borrowed)
                    school_book_Type = book.physOrOnline(physOrOnline)
                # appending the books info inside the list "list_of_books_in_this_library"
                    school_appended_book_title = main_lib.list_of_books_in_this_library.append(school_bookTitle)
                    school_appended_book_author = main_lib.list_of_books_in_this_library.append(school_bookAuthor)
                    school_appended_book_ISBN = main_lib.list_of_books_in_this_library.append(school_book_ISBN)
                    school_appended_book_no_of_copies = main_lib.list_of_books_in_this_library.append(school_book_copies)
                    school_appended_book_borrowed_copies = main_lib.list_of_books_in_this_library.append(school_borrowed_copies)
                    school_appended_book_type = main_lib.list_of_books_in_this_library.append(school_book_Type)
                # adding all the variables of the appended books inside one variable so we can use it to dump the books info inside the JSON file
                    all_of_appended_books = school_appended_book_title, school_appended_book_author, school_appended_book_ISBN, school_appended_book_no_of_copies, school_appended_book_borrowed_copies,school_appended_book_type

            elif librarian_choice == 2: # Removed books
                n = int(input("Enter the number of books you want to remove")) # after the librarian user decides how many books he wants to add the loop irotates according to the number of the book he want to add
                for i in range(n):
                    title = input("Enter the name of the Book that you want to add")
                    authors = input("Enter the Author name")
                    ISBN = int(input("Enter the ISBN number of the book"))
                    no_of_copies = int(input("Enter the number of copies available at the library"))
                    no_of_copies_borrowed = int(input("Enter the nuber of copies that are loaned at the moment"))
                    physOrOnline = str(input("Enter the type of the book whether if it's available as a PHYSICAL or ONLINE"))
                # settin the books info
                    school_BookTitle = book.title(title)
                    school_BookAuthor = book.authors(authors)
                    school_Book_ISBN = book.ISBN(ISBN)
                    school_book_copies = book.noOfCps(no_of_copies)
                    school_borrowed_copies = book.noOfCpsBorrowed(no_of_copies_borrowed)
                    school_book_Type = book.physOrOnline(physOrOnline)
                # appending the books info inside the list "list_of_books_in_this_library"
                    school_removed_book_title = main_lib.list_of_books_in_this_library.pop(school_BookTitle)
                    school_removed_book_author = main_lib.list_of_books_in_this_library.pop(school_BookAuthor)
                    school_removed_book_ISBN = main_lib.list_of_books_in_this_library.pop(school_Book_ISBN)
                    school_removed_book_no_of_copies = main_lib.list_of_books_in_this_library.pop(school_book_copies)
                    school_removed_book_borrowed_copies = main_lib.list_of_books_in_this_library.pop(school_borrowed_copies)
                    school_removed_book_type = main_lib.list_of_books_in_this_library.pop(school_book_Type)
                # adding all the variables of the appended books inside one variable so we can use it to dump the books info inside the JSON file, and removw the user
                    all_of_removed_books = school_removed_book_title, school_removed_book_author, school_removed_book_ISBN, school_removed_book_no_of_copies, school_removed_book_borrowed_copies,school_removed_book_type
            elif librarian_choice == 3:
                Book_title = input("Enter the name of the book you're searching for")
                Book_search_engine = librarian.Search_For_Book(Book_title)
                print(Book_search_engine)


            elif librarian_choice == 4:
                active_loans = librarian.list_of_active_loans() # pritning the list which contains the current active loans to the librarian user
                print(active_loans)
                loaned_Books = active_loans

            elif librarian_choice == 5: # this option is used to set a maximum number of days the users are allowed to borrow a certian book for, and if they exceed that period they librarian user will add them to the list of resrticted uesrs
                maximum_borrowing_period = input("Enter the maximum number of days the users are allowed to borrow a certain book")
                borrow_limit = user.loan_period_maximum_value(maximum_borrowing_period)
                print("the borrow limit has been set successfully")
            elif librarian_choice == 6 : # takes an input from the librarian user to set the rules for the library inside a str
                policy = input("Enter the rules you want to be set for the library borrowing policy")
                print("The borrowing policy has successfully been set")
        elif menu == 3:
            student_choice = int(input(print("==========================================================\n"
                                         "              Welcome to the Student user Menu            \n"
                                         "==========================================================\n"
                                       "1) Borrow a book \n"
                                       "2) Return a book \n"
                                       "3) Extend loan period\n"
                                         "==========================================================\n")))
            if student_choice == 1:
                user_type_checker = input("Enter your user type to authenticate wehtere if you're eligible for this functionality or not: ")
                if user_type_checker == "student" or "Student": # checking for the borrower if it's a student or not and if not the program is going to display a warning message 
                    book = input("Enter the name of the Book that you want to Borrow")
                    online_school_lib.Borrow_book(book)
                else:
                    warnings.warn("Sorry, but your user type isn't eligible for this functionality") # Dislays a warning if the condition above isn't met

            elif student_choice == 2:
                address = input("Enter the name of the Book that you want to return")
                retuning_Book = student.Return_a_book(address)
                print(retuning_Book)
            elif student_choice == 3:
                # a function for the student user if he wants to extend the deadline of a book he borrowed (optional) 
                address = input("Enter the amount of days that you want to extend the due date to")
                loan_extension_request = user.loan_period_maximum_value(address)

    elif main_menu == 2:
        menu = int(input(print("==========================================================\n"
                               "            Welcome to the Online Municipal Library       \n"
                               "==========================================================\n"
                               " Choose the user type \n"
                               "1) Admin \n"
                               "2) Librarian \n"
                               "3) user\n"
                               "==========================================================\n")))
        if menu == 1:
            admin_choice = int(input(print("==========================================================\n"
                                       "                Welcome to the Admin user Menu            \n"
                                       "==========================================================\n"
                                       "1) Add a User\n"
                                       "2) Remove a user\n"
                                       "3) Get library stats\n"
                                       "==========================================================\n")))

            if admin_choice == 1:
            # setting the new user info
                municipal_name = input("Enter the name of the user that you want to add to the library : ")
                municipal_id = input("Enter the NewUser ID : ")
                municipal_type = input("Enter the NewUser Type : ")
                municipal_email = input("Enter NewUser Email : ")
                municipal_user_address = input("Enter the new-user address : ")
                municipal.add_user(municipal_user_address)
            #adding the new user info to the list "List_of_already_registered_users"
                j = admin.List_of_already_registered_users.append(municipal_name)
                k = admin.List_of_already_registered_users.append(municipal_id)
                l = admin.List_of_already_registered_users.append(municipal_type)
                z = admin.List_of_already_registered_users.append(municipal_user_address)
                all_municipal_added_users = j, k, l ,z
                print("The New-User has been added")
            
            elif admin_choice == 2:
            # ENTERING THE INFO OF THE USER THAT THE ADMIN WANT TO REMOVE FROM THE SYSTEM 
                municipal_deleted_account_name = input("Enter the name of the user that you want to remove")
                municipal_del_type = input("Enter the Type of the user you want to remove : ")
                municipal_del_id = input("Enter the ID of the user that you want to remove ")
                municipal_del_email = input("Enter the Email of the user that you want to remove : ")
                municipal_del_social_n = int(input("Please enter the Social-Number of the user that you want to remove"))
                user_deletion = admin.Remove_user(municipal_deleted_account_name)
            # STORING THE REMOVED USER INFO INSIDE VARIABLES
                municipal_usr_del_acc_name = admin.List_of_already_registered_users.pop(municipal_deleted_account_name)
                municipal_usr_del_acc_type = admin.List_of_already_registered_users.pop(municipal_del_type)
                municipal_usr_del_acc_id =admin.List_of_already_registered_users.pop(municipal_del_id)
                municipal_usr_del_acc_name_email = admin.List_of_already_registered_users.pop(municipal_del_email)
                municipal_usr_del_acc_name_social_n = admin.List_of_already_registered_users.pop(municipal_del_social_n)
            #  STORING THE VARIABLED OF THE REMOVED USER INSIDE A NEW VARIABLE WHICH LATER ON CAN BE USED TO DUMP THESE INFP INSIDE THE SYSTEM DB SO, THE USER GET REMOVED
                municipal_all_national_del = municipal_usr_del_acc_name, municipal_usr_del_acc_type, municipal_usr_del_acc_id, municipal_usr_del_acc_name_email, municipal_usr_del_acc_name_social_n
            elif admin_choice == 3:
                stats = admin.library_stats()
                print(stats)


        elif menu == 2:
            librarian_choice = int(input(print("==========================================================\n"
                                               "             Welcome to the Librarian user Menu           \n"
                                               "==========================================================\n"
                                               "1) Add a book \n"
                                               "2) Remove a book\n"
                                               "3) search for a book \n"
                                               "4) Active loans \n"
                                               "5) Set maximum loan period duration\n"
                                               "==========================================================\n")))

            if librarian_choice == 1:
                n = int(input("Enter the number of books the you're going to add")) # after the librarian user decides how many books he wants to add the loop irotates according to the number of the book he want to add
                for i in range(n): 
                # settin the books info
                    title = input("Enter the name of the Book that you want to add")
                    authors = input("Enter the Author name")
                    ISBN = int(input("Enter the ISBN number of the book"))
                    no_of_copies = int(input("Enter the number of copies available at the library"))
                    no_of_copies_borrowed = int(input("Enter the nuber of copies that are loaned at the moment"))
                    physOrOnline = str(input("Enter the type of the book whether if it's available as a PHYSICAL or ONLINE"))
                # STORING THE INPUT INSIDE THE CREATED METHODS
                    BookTitle = book.title(title)
                    BookAuthor = book.authors(authors)
                    Book_ISBN = book.ISBN(ISBN)
                    book_copies = book.noOfCps(no_of_copies)
                    borrowed_copies = book.noOfCpsBorrowed(no_of_copies_borrowed)
                    book_Type = book.physOrOnline(physOrOnline)
                # ADDING THE BOOK INFO TO THE LIST " list_of_books_in_this_library " 
                    appended_book_title = main_lib.list_of_books_in_this_library.append(BookTitle)
                    appended_book_author = main_lib.list_of_books_in_this_library.append(BookAuthor)
                    appended_book_ISBN = main_lib.list_of_books_in_this_library.append(Book_ISBN)
                    appended_book_no_of_copies = main_lib.list_of_books_in_this_library.append(book_copies)
                    appended_book_borrowed_copies = main_lib.list_of_books_in_this_library.append(borrowed_copies)
                    appended_book_type = main_lib.list_of_books_in_this_library.appended(book_Type)
                # ADDING ALL THE VARIABLES THAT CONTAINS ALL THE BOOK INFO THAT WAS ADDED TO THE LIST, WHICH LATER ON IS GOING TO BE USED IN DUMPING THE BOK INFO INSIDE THE JSON FILE 
                    all_of_appended_books = appended_book_title, appended_book_author, appended_book_ISBN, appended_book_no_of_copies, appended_book_borrowed_copies,appended_book_type

            elif librarian_choice == 2:
                n = int(input("Enter the number of books you want to remove")) # after the librarian user decides how many books he wants to add the loop irotates according to the number of the book he want to add
                for i in range(n):
            # ENTERING the REMOVED books info
                    municipal_title = input("Enter the name of the Book that you want to add")
                    municipal_authors = input("Enter the Author name")
                    municipal_ISBN = int(input("Enter the ISBN number of the book"))
                    municipal_no_of_copies = int(input("Enter the number of copies available at the library"))
                    municipal_no_of_copies_borrowed = int(input("Enter the nuber of copies that are loaned at the moment"))
                    municipal_physOrOnline = str(input("Enter the type of the book whether if it's available as a PHYSICAL or ONLINE"))
            # ENTERING THE REMOVED INFO INSIDE THE METHODS CREATED IN ORDER TO REMOVE THE BOOKS 
                    municipal_BookTitle = book.title(municipal_title)
                    municipal_BookAuthor = book.authors(municipal_authors)
                    municipal_Book_ISBN = book.ISBN(municipal_ISBN)
                    municipal_book_copies = book.noOfCps(municipal_no_of_copies)
                    municipal_borrowed_copies = book.noOfCpsBorrowed(municipal_no_of_copies_borrowed)
                    municipal_book_Type = book.physOrOnline(municipal_physOrOnline)
            # ADDING THE BOOK INFO TO THE LIST " list_of_books_in_this_library "
                    municipal_removed_book_title = main_lib.list_of_books_in_this_library.pop(municipal_BookTitle)
                    municipal_removed_book_author = main_lib.list_of_books_in_this_library.pop(municipal_BookAuthor)
                    municipal_removed_book_ISBN = main_lib.list_of_books_in_this_library.pop(municipal_Book_ISBN)
                    municipal_removed_book_no_of_copies = main_lib.list_of_books_in_this_library.pop(municipal_book_copies)
                    municipal_removed_book_borrowed_copies = main_lib.list_of_books_in_this_library.pop(municipal_borrowed_copies)
                    municipal_removed_book_type = main_lib.list_of_books_in_this_library.pop(municipal_book_Type)
                            # ADDING ALL THE VARIABLES THAT CONTAINS ALL THE BOOK INFO THAT WAS ADDED TO THE LIST, WHICH LATER ON IS GOING TO BE USED IN DUMPING THE BOK INFO INSIDE THE JSON FILE 
                    all_of_removed_books = municipal_removed_book_title, municipal_removed_book_author, municipal_removed_book_ISBN, municipal_removed_book_no_of_copies,municipal_removed_book_borrowed_copies,municipal_removed_book_type
            elif librarian_choice == 3:
            # ENTERING THE NAME OF THE BOOKS THE LIBRARIAN USER IS SEARCHING FOR
                book_searched_for = input("Enter the name of the book you're searching for")
                Book_search_engine = librarian.Search_For_Book(book_searched_for)
                print(Book_search_engine)


            elif librarian_choice == 4:
            # DISPLAYING THE LIST THAT CONTAINS THE CURRENT ACTIVE LOANS
                active_loans = librarian.list_of_active_loans()
                print(active_loans)

            elif librarian_choice == 5:

                max_no_of_loan_period = input("Enter the maximum number of days the users are allowed to borrow a certain book")
                borrow_limit = user.loan_period_maximum_value(max_no_of_loan_period)
                print("the borrow limit has been set successfully")

        elif menu == 3:
            regular_choice = int(input(print("==========================================================\n"
                                         "              Welcome to the Regular user Menu            \n"
                                         "==========================================================\n"
                                         "1) Borrow a book \n"
                                         "2) Return a book \n"
                                         "3) Extend loan period\n"
                                         "==========================================================\n")))
            if regular_choice == 1: 
                book = input("Enter the name of the Book that you want to Borrow")
                municipal.Borrow_book(book)
            elif regular_choice == 2:
                name = input("Enter the name of the Book that you want to return")
                retuning_Book = student.Return_a_book(name)
                removed_book = retuning_Book
            elif regular_choice == 3:
                loan_period_exten = input("Enter the amount of days that you want to extend the due date to")
                loan_extension_request = user.loan_period_maximum_value(loan_period_exten)

    elif main_menu == 3:
        menu = int(input(print("==========================================================\n"
                               "             Welcome to the Online National Library       \n"
                               "==========================================================\n"
                               " Choose the user type \n"
                               "1) Admin \n"
                               "2) Librarian \n"
                               "3) user\n"
                               "==========================================================\n")))
        if menu == 1:
            admin_choice = int(input(print("==========================================================\n"
                                           "             Welcome to the Admin user Menu               \n"
                                           "==========================================================\n"
                                           "1) Add a User\n"
                                           "2) Remove a user\n"
                                           "3) Get library stats\n"
                                           "==========================================================\n")))

            if admin_choice == 1:
            # setting the new user info
                national_user_name = input("Enter the username of the user you want to add to the library data base : ")
                national_type = input("Enter the New-User Type : ")
                national_id = input("Enter the new user ID : ")
                national_email = input("Enter the New-User Email : ")
                national_social_n = int(input("Please enter your Social-Number : "))
                national.add_user(national_social_n)
            # STORING THE INPUT INSIDE THE CREATED METHODS
                national_ad_usr_name =  admin.List_of_already_registered_users.append(national_user_name)
                national_ad_usr_type = admin.List_of_already_registered_users.append(national_type)
                national_ad_usr_social_n =  admin.List_of_already_registered_users.append(national_social_n)
                national_ad_usr_id = admin.List_of_already_registered_users.append(national_id)
            # STORING ALL THE VARS USED TO STORE METHODS USED FOE ADDING A USER TO THE LIBRARY
                national_added_user = national_ad_usr_name, national_ad_usr_type, national_ad_usr_social_n, national_ad_usr_id

            elif admin_choice == 2:
                national_deleted_account_name = input("Enter the name of the user that you want to remove")
                national_del_type = input("Enter the Type of the user you want to remove : ")
                national_del_id = input("Enter the ID of the user that you want to remove " )
                national_email = input("Enter the Email of the user that you want to remove : ")
                national_social_n = int(input("Please enter the Social-Number of the user that you want to remove"))
                user_deletion = admin.Remove_user(national_deleted_account_name)
            # STORING THE INPUT INSIDE THE CREATED METHODS FOR REMOVING THE USER FROM THE SYSTEM
                national_usr_del_acc_name = admin.List_of_already_registered_users.pop(national_deleted_account_name)
                national_usr_del_acc_type = admin.List_of_already_registered_users.pop(national_del_type)
                national_usr_del_acc_id = admin.List_of_already_registered_users.pop(national_del_id)
                national_usr_del_acc_email = admin.List_of_already_registered_users.pop(national_email)
                national_usr_del_acc_social_n = admin.List_of_already_registered_users.pop(national_social_n)
                # STORING ALL THE VARS USED TO STORE METHODS USED FOE ADDING A USER TO THE LIBRARY
                national_all_national_del = national_usr_del_acc_name, national_usr_del_acc_type, national_usr_del_acc_id, national_usr_del_acc_email, national_usr_del_acc_social_n
            elif admin_choice == 3:
                stats = admin.library_stats()
                print(stats)

        elif menu == 2:
            librarian_choice = int(input(print("==========================================================\n"
                                           "           Welcome to the Librarian user Menu             \n"
                                           "==========================================================\n"
                                           "1) Add a book \n"
                                           "2) Remove a book\n"
                                           "3) search for a book \n"
                                           "4) Active loans \n"
                                           "5) Set maximum loan period duration\n"
                                           "6) Set the Borrowing functionality conditions\n"
                                           "==========================================================\n")))

            if librarian_choice == 1:
                n = int(input("Enter the number of books the you're going to add : "))
                for i in range(n):
# settin the books info
                    title = input("Enter the name of the Book that you want to add : ")
                    authors = input("Enter the Author name : ")
                    ISBN = int(input("Enter the ISBN number of the book : "))
                    no_of_copies = int(input("Enter the number of copies available at the library : "))
                    no_of_copies_borrowed = int(input("Enter the nuber of copies that are loaned at the moment : "))
                    physOrOnline = str(input("Enter the type of the book whether if it's available as a PHYSICAL or ONLINE : "))
# ENTERING THE ADDED BOOKS INFO INSIDE THE METHODS CREATED IN ORDER TO ADD THE BOOKS
                    BookTitle = book.title(title)
                    BookAuthor = book.authors(authors)
                    Book_ISBN = book.ISBN(ISBN)
                    book_copies = book.noOfCps(no_of_copies)
                    borrowed_copies = book.noOfCpsBorrowed(no_of_copies_borrowed)
                    book_Type = book.physOrOnline(physOrOnline)
# STORING THE INPUT INSIDE THE CREATED METHODS FOR REMOVING THE USER FROM THE SYSTEM
                    appended_book_title = main_lib.list_of_books_in_this_library.append(BookTitle)
                    appended_book_author = main_lib.list_of_books_in_this_library.append(BookAuthor)
                    appended_book_ISBN = main_lib.list_of_books_in_this_library.append(Book_ISBN)
                    appended_book_no_of_copies = main_lib.list_of_books_in_this_library.append(book_copies)
                    appended_book_borrowed_copies = main_lib.list_of_books_in_this_library.append(borrowed_copies)
                    appended_book_type = main_lib.list_of_books_in_this_library.append(book_Type)
# ADDING ALL THE VARIABLES THAT CONTAINS ALL THE BOOK INFO THAT WAS ADDED TO THE LIST, WHICH LATER ON IS GOING TO BE USED IN DUMPING THE BOK INFO INSIDE THE JSON FILE
                    all_of_appended_books = appended_book_title, appended_book_author, appended_book_ISBN, appended_book_no_of_copies, appended_book_borrowed_copies, appended_book_type

            elif librarian_choice == 2:
                n = int(input("Enter the number of books you want to remove : "))
                for i in range(n):
# settin the books info
                    title = input("Enter the name of the Book that you want to remove : ")
                    authors = input("Enter the Author name that you want to remove : ")
                    ISBN = int(input("Enter the ISBN number of the book that you want to reomve : "))
                    no_of_copies = int(input("Enter the number of copies available at the library, so that all the books will be removed : "))
                    no_of_copies_borrowed = int(input("Enter the nuber of copies that are loaned at the moment : "))
                    physOrOnline = str(input("Enter the type of the book whether if it's available as a PHYSICAL or ONLINE : "))
# ENTERING THE ADDED BOOKS INFO INSIDE THE METHODS CREATED IN ORDER TO ADD THE BOOKS
                    BookTitle = book.title(title)
                    BookAuthor = book.authors(authors)
                    Book_ISBN = book.ISBN(ISBN)
                    book_copies = book.noOfCps(no_of_copies)
                    borrowed_copies = book.noOfCpsBorrowed(no_of_copies_borrowed)
                    book_Type = book.physOrOnline(physOrOnline)
# STORING THE INPUT INSIDE THE CREATED METHODS FOR REMOVING THE USER FROM THE SYSTEM
                    national_removed_book_title = main_lib.list_of_books_in_this_library.pop(BookTitle)
                    national_removed_book_author = main_lib.list_of_books_in_this_library.pop(BookAuthor)
                    national_removed_book_ISBN = main_lib.list_of_books_in_this_library.pop(Book_ISBN)
                    national_removed_book_no_of_copies = main_lib.list_of_books_in_this_library.pop(book_copies)
                    national_removed_book_borrowed_copies = main_lib.list_of_books_in_this_library.pop(borrowed_copies)
                    national_removed_book_type = main_lib.list_of_books_in_this_library.pop(book_Type)
# ADDING ALL THE VARIABLES THAT CONTAINS ALL THE BOOK INFO THAT WAS ADDED TO THE LIST, WHICH LATER ON IS GOING TO BE USED IN DUMPING THE BOK INFO INSIDE THE JSON FILE
                    all_of_national_removed_books = national_removed_book_title, national_removed_book_author, national_removed_book_ISBN, national_removed_book_no_of_copies, national_removed_book_borrowed_copies, national_removed_book_type
            elif librarian_choice == 3:
# THIS OPTION IS USED BY THE LIBRARIAN / REGULAR USERS IN ORDER OT SEARCH FOR A CERTIAN BOOK
                bookname = input("Enter the name of the book you're searching for : ")
                Book_search_engine = librarian.Search_For_Book(bookname)
                print(Book_search_engine)


            elif librarian_choice == 4:
                active_loans = librarian.list_of_active_loans()
                print(active_loans)

            elif librarian_choice == 5:
                address = input("Enter the maximum number of days the users are allowed to borrow a certain book  :")
                borrow_limit = user.loan_period_maximum_value(address)
                print("the borrow limit has been set successfully")

            elif librarian_choice ==  6 :
                condition = input("Enter the conditions for the borrowing functionality, so that the users follow it : ")
                librarian.borrowing_policy(condition)
        elif menu == 3:
            regular_choice = int(input(print("==========================================================\n"
                                         "              Welcome to the Regular user Menu            \n"
                                         "==========================================================\n"
                                         "1) Borrow a book \n"
                                         "2) Return a book \n"
                                         "3) Extend loan period\n"
                                         "==========================================================\n")))
            if regular_choice == 1:

                Book_name = input("Enter the name of the book you want to borrow : ")
                municipal.Borrow_book(Book_name)
            elif regular_choice == 2:
                address = input("Enter the name of the Book that you want to return : ")
                retuning_Book = student.Return_a_book(address)
                returned_book = retuning_Book
            elif regular_choice == 3:
                period = input("Enter the amount of days that you want to extend the due date to : ")
                loan_extension_request = user.loan_period_maximum_value(period)



   