1. Book
Attributes:
book_id (unique identifier)
title
author
copies_available

Methods:
display_details() - Show book information.
update_copies(count) - Increment or decrement the copies.

2. Member

Attributes:
member_id (unique identifier)
name
borrowed_books (list of book IDs)
Methods:
borrow_book(book_id)
return_book(book_id)



3. Library

Attributes:
books (a dictionary of book_id -> Book objects)
members (a dictionary of member_id -> Member objects)
Methods:
add_book(book_obj)
remove_book(book_id)
register_member(member_obj)
issue_book(book_id, member_id)
return_book(book_id, member_id)
list_available_books() - Display all books with copies_available > 0.