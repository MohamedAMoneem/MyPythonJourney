#this code is a library

library = []
wishlist = []
donation = []
book1 = input("enter the name of a book you own : ")
book2 = input("enter another book or press enter to skip: ")
library.append(book1.lower())
if book2:
    library.append(book2.lower())
    print(f"your library : {library}")
else:
    print(f"your library : {library}")
wishbook1 = input("enter the name of a book you wish to own in the future : ")
wishlist.append(wishbook1.lower())
wishbook2 = input("enter another book or press enter to skip: ")
if wishbook2:
    wishlist.append(wishbook2.lower())
    print(f"your wishlist : {wishlist}")
else:
    print(f"your wishlist : {wishlist}")
aquired = input("enter a book from your wishlist that you have aquired or press enter to skip: ")
if aquired:
    if aquired.lower() in wishlist:
        wishlist.remove(aquired.lower())
        library.append(aquired.lower())
        print(f"your updated wishlist : {wishlist} ")
        print(f"your updated library : {library} ")

    else:
        print("this book is not in your wishlist")
else:
    print("no updates to wishlist and library. . .")
donate = input("enter name of book you want to donate or press enter to skip: ")
if donate:
    if donate.lower() in library:
        library.remove(donate.lower())
        donation.append(donate.lower())
        print(f"your library after donation : {library}")
    else:
        print("this book is not in your library. . .")
else:
    print(f"your library : {library}")