# library_management_system
This was my first assignment for Python subject. It is a simple project for taking care of Library Book.

Sorry if my english is bad. It is not my primary language.

How to use:
There should be "stock" file at the same directory as Book.py file
Just open Book.py and follow guide.

The stock file should contain data in this format:
	Book name(String), Author Name(String), Stock(Integer), Price(float)

Files that are created after you borrow book:
	name_bor.txt = Contains details about the borrower, time, price, book name (This file is like history)
	name[price].txt = Contains the name of book that person borrowed with price. (This file is for returning book, it is like inventory of person)

Files that are created after you return book:
	name_bor.txt = Contains details about the returner, time, price, book name (This file is like history similar to borrowing)
	name[price].txt = Removes the book after they return.
  
There is also a system for penalty if they return book late.
