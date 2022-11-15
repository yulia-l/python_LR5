from myExceptions import NegValException


class Book:
    def __init__(self, name, pages, style, price):
        self.__name = name
        self.__pages = pages
        self.__style = style
        if name.startswith('Программирование'):
            self.__price = price * 2
        else:
            self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def pages(self):
        return self.__pages

    @property
    def style(self):
        return self.__style

    @property
    def price(self):
        return self.__price

    @name.setter
    def name(self, name):
        self.__name = name

    @pages.setter
    def pages(self, pages):
        if pages > 0:
            self.__price = pages
        else:
            raise Exception("Некорректный ввод кол-ва страниц")

    @style.setter
    def style(self, style):
        self.__style = style

    @price.setter
    def price(self, price):
        try:
            self.__price = price
            if price < 0:
                raise NegValException("Cтоимость должна быть положительным числом")
        except NegValException as e:
            print(e)

    def display_info(self):
        print(self.__str__)

    def __str__(self):
        return "\nНазвание: {} \nКол-во страниц: {} \nЖанр: {} \nЦена: {}".format(
            self.__name, self.__pages, self.__style, self.__price)

    def page_price(self):
        return self.price / self.pages

    def change_price(self):
        if self.name.startswith('Программирование'):
            self.price = self.price * 2