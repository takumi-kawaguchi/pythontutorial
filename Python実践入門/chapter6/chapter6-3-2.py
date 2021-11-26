from operator import attrgetter

class Page:
    book_title = 'Python Practice Book'

    def __init__(self, num, content):
        self.num = num
        self.content = content

    def output(self):
        return f'{self.content}'

    @classmethod
    def print_pages(cls, *pages):
        print(cls.book_title)
        pages = list(pages)
        [print(page.output()) for page in sorted(pages, key=attrgetter('num'))]

    @staticmethod
    def check_blank(page):
        return bool(page.content)

first = Page(1, 'first page')
second = Page(1, 'second page')
third = Page(1, 'third page')

Page.print_pages(first, second, third)

print(Page.check_blank(first))