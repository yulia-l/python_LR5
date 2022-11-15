from book import Book


class EBook(Book):
    def __init__(self, name, memory, pages, style, price):
        super().__init__(name, pages, style, price)
        self.memory = memory
        self.__name = name
        self.__pages = pages
        self.__style = style
        self.__price = price

    def __str__(self):
        return "\nНазвание: {} ({} мб) \nКол-во страниц: {} \nЖанр: {} \nЦена: {}".format(
            self.__name, self.__pages, self.memory, self.__style, self.__price)

    @staticmethod
    def details():
        print("Скачать книгу")
