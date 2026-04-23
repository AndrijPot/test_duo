# Краще назвати список у множині, бо там буде багато книг
books = []

def add_book():
    while True:
        try:
            name_user = input("book name: \n").strip()
            autor = input("autor book : \n").strip()
            price = int(input("price : \n"))
            break
        except ValueError:
            # Додали повідомлення, щоб користувач розумів помилку
            print("❌ Помилка: Введіть ціну цифрами!") 
            continue

    # Створюємо словник!
    new_book = {
        "title": name_user,
        "author": autor,
        "price": price
    }
    
    books.append(new_book)
    print("✅ Книгу успішно додано!\n")

def show_books():
    # Тепер ми дістаємо дані зі словника по ключах
    print("\n--- СПИСОК КНИГ ---")
    for b in books:
        print(f"📖 {b['title']} - {b['author']} | Ціна: {b['price']} грн")
    print("-------------------\n")




