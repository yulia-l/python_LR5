from e_book import EBook


class ChildBook(EBook):
    def __init__(self, name, memory, pages, style, price, age):
        super().__init__(name, memory, pages, style, price)
        self.__memory = memory
        self.__name = name
        self.__pages = pages
        self.__style = style
        self.__price = price
        self.__age = age

    def __str__(self):
        if self.__memory > 0:
            return "\nНазвание: {} ({} мб) \nКол-во страниц: {} \nЖанр: {} \nЦена: {}\n".format(
                self.__name, self.memory, self.__pages, self.__style, self.__price)
        else:
            return "\nНазвание: {} \nКол-во страниц: {} \nЖанр: {} \nЦена: {}".format(
                self.__name, self.__pages, self.__style, self.__price)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
            if 0 < age < 6:
                print("Рекомендовано для детей в возрасте 0-5 лет")
            elif 5 < age < 11:
                print("Рекомендовано для детей в возрасте 5-10 лет")
            else:
                print("Рекомендовано для детей старше 10 лет\n")
        else:
            print("Некорректный ввод для вывода возрастных рекомендаций")
