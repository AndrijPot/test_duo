from books_function import add_book, show_books

system = True
while system:
    user_choice = input("Додати книгу - 1 \n Показати всі книги - 2\n Вийти - 3\n").strip()
    if user_choice == "1":
        add_book()  
    elif user_choice == "2":
        show_books()
    elif user_choice == "3":
        system = False
    else:
        print("Введіть число яке є в списку команд!")

