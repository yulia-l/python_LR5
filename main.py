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
#print(newPosition.price)



fileForSave = 'fileIn.txt'
#dataForSave = ''

try:
    with open(fileForSave, 'a+', encoding='utf-8') as f:
        fileReading = f.read()
        print("Чтение файла " + fileReading)
    # if not fileReading:
    #     print("Файл {} пуст " + fileReading)
        f.write('newPosition')
        s = f.readlines()
        print("Записаны данные:\n" + s)
except IOError as e:
    print("I/O error({0}): {1}".format(e.errno, e.strerror))
except:
    print("Unexpected error:", sys.exc_info()[0])
print("Работа с файлом завершена")
