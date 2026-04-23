book = []

def add_book():

        while true:
            try:
                name_user = str(input("book name: \n" ))
                autor = str(input("autor book : \n"))
                price = int(input("price : \n"))
                
            except ValueError:
              continue 
          
            book.append(f"{name_user}-{autor} its price--{price}\n")


def show_books():
    for i in book:
        print(i) 







