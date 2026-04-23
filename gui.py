book = []

def add_book():
    name_user = str(input("book name: \n" ))
    autor = int(input("autor book : \n"))
    price = int(input("price : \n"))

    
   # newbook.append (f"{name_user} {autor} {price} \n")
    newbook = {
        "title": name_user,
        "autor": autor,
        "price": price
    }
    book.append(newbook)

def show_books():
    for i in book:
        print(i) 







