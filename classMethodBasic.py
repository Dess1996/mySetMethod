"""
Подсчёт экземпляров методов класса

"""


class Spam:
    """
    Эквивалентный метод класса

    """
    numInstances = 0
    
    def __init__(self):
        Spam.numInstances += 1
    
    def printNumInstnces(cls):
        print('Количество экземпляров: %s' % Spam.numInstances)
    
    printNumInstnces = classmethod(printNumInstnces)  # требует дополнительного вызовы StaticMethod


class Sub(Spam):
    def printNumInstnces(cls):
        print('Extra Stuff...', cls)
        Spam.printNumInstnces()
    
    printNumInstnces = classmethod(printNumInstnces)


class Other(Spam):
    pass


if __name__ == '__main__':
    a, b = Spam(), Spam()
    a.printNumInstnces()  # В первом аргументе передаётся класс
    Spam.printNumInstnces()  # В первом аргументе передаётся класс
    
    # Добавили наследование
    
    x = Sub()
    y = Spam()
    x.printNumInstnces()
    Sub.printNumInstnces()
    y.printNumInstnces()
    
    z = Other()
    z.printNumInstnces()
