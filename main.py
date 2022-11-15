import sys

from book import Book
from e_book import EBook
from childBook import ChildBook

warAndPiece = Book("война и мир", 100, "худож", 350)
laLaLand = EBook("LaLaLand", 90, 56, "art", 600)
goldFish = ChildBook("GoldFish", 0, 15, "art", 100, 0)
prog = Book("Программирование", 100, "science", 350)

print("Создание новой позиции:")
newPosition = Book
newPosition.name = input("Название: ")
newPosition.pages = input("Кол-во страниц: ")
newPosition.style = input("Стиль: ")
newPosition.price = input("Цена: ")
print(newPosition.price)

fileIn = 'fileIn.csv'
fileOut = 'fileOut.csv'

try:
    with open(fileIn, 'r') as f:
        file_content = f.read()
        print("Чтение файла " + fileIn)
    if not file_content:
        print("Файл {} пуст " + fileIn)
    with open(fileOut, 'w') as dest:
        dest.write(file_content)
        print("Записан файл " + fileOut)
except IOError as e:
    print("I/O error({0}): {1}".format(e.errno, e.strerror))
except:
    print("Unexpected error:", sys.exc_info()[0])
print("Работа с файлом завершена")
