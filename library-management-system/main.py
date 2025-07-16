libraryMenu =[]

def addBookInLibrary():
    print("Add Book details To Add :-->")
    bookname=input("Name :")
    bookAuthor=input("Author :")
    libraryMenu.append({"bookname":bookname, "Author":bookAuthor , "availability" :True})
    print(f"the book {bookname} is added to library")


def viewBookInLibrary():
    if not libraryMenu:
        print("no book in library")
        return 
    
    print("books in library")
    for i in range(len(libraryMenu)):
        book=libraryMenu[i]
        status = "available" if book["availability"] else "not available"
        print(f"{i +1} .the book {book['bookname']} is {status}")
        print()
            

def removeBookFromLibrary():
    if not libraryMenu:
        print("no book in library")
        return

    viewBookInLibrary()
    bookIndex = int(input("Enter the book number to remove: ")) - 1

    if 0 <= bookIndex < len(libraryMenu):
        removedBook = libraryMenu.pop(bookIndex)
        print(f"Removed book: {removedBook['bookname']}")
    else:
        print("Invalid book number.")


def borrowBookFromLibrary():
    viewBookInLibrary()
    choice =int(input("enter book number to borrow")) -1
    if 0< choice >len(libraryMenu):
        if libraryMenu[choice] ["availability"]:
            libraryMenu[choice] ['availability'] =False
            print("you borrowed book !")
        else :
            print(" book not available")
    else:
        print("invalid book number")


def returnBook():
    viewBookInLibrary()
    choice = int(input("enter the book you want to return :"))
    if 0< choice >len(libraryMenu):
        if not libraryMenu[choice] ["availability"]:
            libraryMenu[choice] ["availability"]==True
            print(f"you returned the book {libraryMenu[choice]['bookname']}")
    else:
        print("invalid book number")
    
def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Remove Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == 1:
            addBookInLibrary()
        elif choice == 2:
            viewBookInLibrary()
        elif choice == '3':
            removeBookFromLibrary()
        elif choice == '4':
            borrowBookFromLibrary()
        elif choice == '5':
            returnBook()
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")



main()
