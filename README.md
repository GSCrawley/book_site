# book_site
How would we filter for all books with titles containing the word ‘Django’?
A: book_list = Book.objects.filter(book__title = 'Django')


How would we filter for all books with tag ‘Fiction’?
A: book_list = Book.objects.filter(book__tag ='Fiction')


How would we filter for all authors who have written books containing the word ‘Django’? HINT: We can use the book field to refer to an author’s books, even though the Author model doesn’t explicitly contain it!

A: author_list = Author.objects.filter(book__title = 'Django')