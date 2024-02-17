
import json
class Library():
    def __init__(self):
        self.file = open("books.txt", "a+")
        self.file.seek(0)
        try:
            self.books = [json.loads(line) for line in self.file.readlines()]
        except:
            self.books = []

    def __del__(self):
        self.file.seek(0)
        self.file.truncate()
        for book in self.books:
            json.dump(book, self.file)
            self.file.write('\n')
        self.file.close()

    def ListBooks(self):
        for book in self.books:
            print( f"Title:{book['title']}\nauthor:{book['author']}\nyear:{book['release_year']}\npages:{book['pages']}\n**")

    def AddBook(self):
        title = input("Kitap ismini giriniz: ")
        author = input("Yazar adı giriniz: ")
        release_year = input("Basım yılını giriniz:")
        pages = input("Sayfa sayısını giriniz:")


        if title.strip() == "":
            print("Lütfen geçerli bir kitap adı giriniz!")
        elif author.strip() == "":
            print("Lütfen geçerli bir yazar adı giriniz!")
        elif release_year.strip() == "":
            print("Lütfen geçerli bir yıl giriniz!")
        elif not release_year.strip().isdigit():
            print("Yıl bir sayı olmalıdır!")
        elif pages.strip() == "":
            print("Lütfen geçerli bir sayfa sayısı giriniz!")
        elif not pages.strip().isdigit():
            print("Sayfa sayısı bir sayı olmalıdır!")
        else:
            book = {"title": title, "author": author, "release_year": release_year, "pages": pages}
            self.books.append(book)
            print("Kitap başarıyla eklendi.")

    def RemoveBook(self):
        title_to_remove = input("Enter book title: ").lower()
        print(f"{title_to_remove} kitabını silmek istediğinize emin misiniz? (Evet / Hayır)")
        cevap = input().lower()

        if cevap == "evet":
            self.books = [book for book in self.books if title_to_remove not in book['title'].lower()]
            print(f"{title_to_remove} kitabı silindi.")

        elif cevap == "hayır":
            print("Silme işlemi iptal edildi.")

        else:
            print("lütfen geçerli bir ifade giriniz!")


lib = Library()

while True:
    print("1. kitap ekle")
    print("2. kitap sil")
    print("3. kitap listesi")
    print("4. çıkış")

    choice = input("seçiminizi girin:")

    if choice == "1":
        lib.AddBook()
    elif choice == "2":
        lib.RemoveBook()
    elif choice == "3":
        lib.ListBooks()
    elif choice == "4":
        break
    elif not choice.strip().isdigit():
        print("seçiminiz bir sayı olmalıdır!")
    else:
        print("hatalı tuşlama! Lütfen geçerli sayı giriniz!")
