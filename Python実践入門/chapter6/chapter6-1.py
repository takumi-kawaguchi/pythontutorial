class Page:
    def __init__(self, num, content, section=None):
        self.num = num
        self.content = content
        self.section = section

    def output(self):
        return f'{self.content}'

# print(Page)

title_page = Page(0, 'python book')
# print(type(title_page))
# print(isinstance(title_page, Page))
# print(dir(title_page))

# print(title_page.output())

title_page.section = 0
print(title_page.section)
first_page = Page(1, 'first page', 123)
print(first_page.section)



# class Klass:
#     def some_methhod():
#         print('method')

# def some_function(self):
#     print('function')

# print(some_function)
# print(Klass.some_methhod)
# kls = Klass()
# print(type (kls.some_methhod))
# Klass.some_function = some_function
# kls.some_function()