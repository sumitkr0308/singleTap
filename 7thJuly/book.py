#make a book class title ,author ,price ,add discount method to reduce price by 10%

class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def reducedPrice(self):
        return self.price-(self.price*10/100)

b1=Book("Harry Potter","J K Rowling",1000)

print(f"Price after adding 10% discounts: {b1.reducedPrice()}")    
