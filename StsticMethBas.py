"""
Подсчёт экземпляров статистическим методом

"""


class Spam:
    """
    Эквивалентный статистический метод подсчёта экземпляра,
    ему экземпляр не передаётся
    
    """
    numInstances = 0
    
    def __init__(self):
        Spam.numInstances += 1
    
    def printNumInstnces():
        print('Количество экземпляров: %s' % Spam.numInstances)
    
    printNumInstnces = staticmethod(printNumInstnces)  # требует дополнительного вызовы StaticMethod


class Sub(Spam):
    def printNumInstnces():
        print('Extra Stuff...')
        Spam.printNumInstnces()
    
    printNumInstnces = staticmethod(printNumInstnces)


if __name__ == '__main__':
    a = Spam()
    b = Spam()
    c = Spam()
    Spam.printNumInstnces()
    a.printNumInstnces()
    
    # Добавили статистический подкласс
    
    a = Sub()
    b = Sub()
    a.printNumInstnces()
    Sub.printNumInstnces()
    Spam.printNumInstnces()
