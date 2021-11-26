class Page:
    book_title = 'Python Practice Book'

print(Page.book_title)
print(Page().book_title)
Page.book_title = 'test'
print(Page.book_title)
p = Page()
print(p.book_title)

p.book_title = 'p book title'
print(Page.book_title)
print(p.book_title)