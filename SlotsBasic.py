class limiter:
    __slots__ = ['age', 'name', 'job']  # задумывалось как способ отлавлиявания опечаток в коде


# Словари и слоты пространства имён

class C:
    __slots__ = ['a', 'b']


# Без словаря пространств атрибутов выполнять присваивание в экземплярах без __slots__ невозможно

class D:
    __slots__ = ['a', 'b', '__dict__']  # если существуют атрибуты, значит надо добавить __dict__
    
    def __init__(self):
        self.d = 4


# Слоты в суперклассах
class E:
    __slots__ = ['c', 'd']


class F(E):
    __slots__ = ['a', '__dict__']


# Обработка слотов и других атрибутов

class Slotfull:
    __slots__ = ['a', 'b', '__dict__']
    
    def __init__(self, data):
        self.c = data


if __name__ == '__main__':
    x = limiter()
    #   print(x.age), AttributeError: age, перед использованием необходимо присвоить значение
    x.age = 40
    print(x.age)  # выдал 40
    #    x.ape = 1000 # если имя не находится в слоте, тоже ошибка атрибута
    X = C()
    X.a = 1
    print(X.a)  # Вывел 1
    #    X.__dict__  нет такого атрибута
    
    # Извлечение атрибутов на слотах
    
    print(getattr(X, 'a'))  # получить атрибут а
    setattr(X, 'b', 2)  # назначить b атрибут 2
    print(getattr(X, 'b'))  # получить атрибут b
    
    # dir находит слотовые атрибуты
    
    print('a' in dir(X))  # True
    print('b' in dir(X))  # True
    # Без словаря пространств атрибутов выполнять присваивание в экземплярах без __slots__ невозможно
    X = D()  # Ошибка, если в слотах не указан __dict__
    
    # Множество слотов в суперклассах
    
    D = F()
    D.a, D.b, D.c = 1, 2, 3
    print(D.a, D.c)
    
    # Слоты не объединяются
    print(E.__slots__)
    print(F.__slots__)
    print(D.__slots__)  # экземпляр наследует нижний список __slots__
    print(D.__dict__)  # экземпляр имеет свой словарь атрибутов
    for attr in list(getattr(D, '__dict__', [])) + getattr(D, '__slots__', []):  # Слоты суперклассов отсутствуют
        print(attr, '=>', getattr(D, attr))
    print(dir(D))  # dir включает все слотовые имена
    
    # Обобщённая обработка слотов
    
    I = Slotfull(3)
    I.a, I.b = 1, 2
    print(I.a, I.b, I.c) # 1,2, 3
    
