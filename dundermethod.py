class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author}."

    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("The instance of the class has been deleted")


b = Book(title='Love cats', author='Soni', pages=700)
print(b)
str(b)
print(str(b))
print(len(b))
del b
print(b)
