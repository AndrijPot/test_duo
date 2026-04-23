def add_book():
    b = []
    us = input("fgfdv ")
    b.append(us)
    print(b)

system = True
while system:
    user_choice = input("Додати книгу - 1 \n оказати всі книги - 2\n Вийти - 3\n").strip()
    if user_choice == "1":
        add_book()  
    elif user_choice == "2":
        show_books()
    elif user_choice == "3":
        system = False
    else:
        print("Введіть число яке є в списку команд!")