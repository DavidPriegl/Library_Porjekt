class Item:
    total_items = 0

    def __init__(self, title, item_id, is_borrowed=False):
        if not title:
            raise ValueError("A cim nem lehet ures.")
        if len(item_id) != 4:
            raise ValueError("Az elem azonositoja 4 karakter hosszu kell legyen.")

        self.title = title
        self.item_id = item_id
        self.is_borrowed = is_borrowed
        self.borrowed_by = None
        Item.total_items += 1

    def describe(self):
        return f"Cim: {self.title}, Azonosito: {self.item_id}, Kolcsonozve: {self.is_borrowed}"


class Book(Item):
    def __init__(self, title, author, genre, item_id, is_borrowed=False):
        super().__init__(title, item_id, is_borrowed)
        self.author = author
        self.genre = genre

    def describe(self):
        return f"Cim: {self.title}, Szerzo: {self.author}, Mufaj: {self.genre},Azonosito: {self.item_id}, Kolcsonozve: {self.is_borrowed}"


class DVD(Item):
    def __init__(self, title, duration_min, item_id, is_borrowed=False):
        super().__init__(title, item_id, is_borrowed)
        if duration_min > 0:
            self.duration_min = duration_min
        else:
            raise ValueError("A hossz nem lehet 0 vagy negatív.")

    def describe(self):
        return f"Cim: {self.title}, Hossz: {self.duration_min}, Azonosito: {self.item_id}, Kolcsonozve: {self.is_borrowed}"


class Member():
    def __init__(self, name, member_id):
        if name is None:
            raise ValueError("A tag neve nem lehet ures.")
        if len(member_id) != 4:
                    raise ValueError("A tag azonositoja 4 karakter hosszu kell legyen.")
        if member_id is None:
            raise ValueError("A tag azonositoja nem lehet ures.")
        
        self.name = name
        self.member_id = member_id
        self.__borrowed_items = []

    @property
    def borrowed_items(self):
        return self.__borrowed_items.copy()

    def borrow_item(self, item):
        if item.is_borrowed:
            raise ValueError(f"A(z) {item.title} mar ki van kolcsonozve.")

        item.is_borrowed = True
        item.borrowed_by = self.member_id
        self.__borrowed_items.append(item)

    def return_item(self, item):
        if item not in self.__borrowed_items:
            raise ValueError("A tag nem ezt az elemet kolcsonozte ki.")

        item.is_borrowed = False
        item.borrowed_by = None
        self.__borrowed_items.remove(item)


class Library:
    def __init__(self):
        self.__catalog = {}  # key item_id, value Item object
        self.__members = {}  # key member_id, value Member object

    def add_item(self, item):
        if item.item_id in self.__catalog:
            raise ValueError(f"A(z) {item.item_id} azonositoju elem mar létezik.")
        self.__catalog[item.item_id] = item

    def register_member(self, member):
        if member.member_id in self.__members:
            raise ValueError(f"A(z) {member.member_id} azonositoju tag mar létezik.")
        self.__members[member.member_id] = member

    def checkout(self, member_id, item_id):
        member = self.__members.get(member_id)
        if member is None:
            raise ValueError(f"Nem letezo member_id: {member_id}")

        item = self.__catalog.get(item_id)
        if item is None:
            raise ValueError(f"Nem letezo item_id: {item_id}")

        member.borrow_item(item)

    def check_in(self, member_id, item_id):
        member = self.__members.get(member_id)
        if member is None:
            raise ValueError(f"Nem letezo member_id: {member_id}")

        item = self.__catalog.get(item_id)
        if item is None:
            raise ValueError(f"Nem letezo item_id: {item_id}")

        member.return_item(item)

    def find_by_genre(self, genre):
        return [
            item for item in self.__catalog.values()
            if isinstance(item, Book) and item.genre.lower() == genre.lower()
        ]


if __name__ == "__main__":
    library = Library()

    # 1) Katalogus feltoltese (vegyesen Book + DVD)
    book1 = Book("Dune", "Frank Herbert", "Sci-Fi", "B001")
    book2 = Book("Sapiens", "Yuval Noah Harari", "Ismeretterjeszto", "B002")
    book3 = Book("Neuromancer", "William Gibson", "Sci-Fi", "B003")
    dvd1 = DVD("Inception", 148, "D001")

    for item in [book1, book2, book3, dvd1]:
        library.add_item(item)

    # 2) Ket tag regisztralasa
    member1 = Member("Anna", "M001")
    member2 = Member("Bela", "M002")
    library.register_member(member1)
    library.register_member(member2)

    # 3) Kolcsonzesek + mar kolcsonzott elem ujra kolcsonzese (hiba kezelve)
    library.checkout("M001", "B001")
    library.checkout("M001", "D001")
    library.checkout("M002", "B002")

    try:
        library.checkout("M002", "B001")
    except ValueError as e:
        print(f"Varhato hiba: {e}")

    # 4) Egy tag kolcsonzott listaja
    print("\nAnna kolcsonzott elemei:")
    for borrowed in member1.borrowed_items:
        print("-", borrowed.describe())

    # 5) Adott mufaj konyvei
    print("\nSci-Fi konyvek:")
    for book in library.find_by_genre("Sci-Fi"):
        print("-", book.describe())

    # 6) Osszes Item szama
    print(f"\nOsszes Item: {Item.total_items}")
