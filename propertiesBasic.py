"""
Основы свойств ( типов объекта присвоенного имени атрибута класса)
Вызывается встроенной функцией property

"""


class operators:
    def __getattr__(self, item):
        if item == 'age':
            return 40
        else:
            raise AttributeError


"""
Тот же пример с применением свойств

"""


class properties:
    def getAge(self):
        return 40
    
    def setAge(self, value):
        print('set age %s' % value)
        self._age = value
    
    age = property(getAge, setAge, None)  # получениеб установкаб удаление


"""
Эквивалентный класс на перегрузке операций

"""


class operators1:
    def __getattr__(self, item):
        if item == 'age':
            return 40
        else:
            raise AttributeError(name)
    
    def __setattr__(self, key, value):
        print('set: %s %s' % (key, value))
        if key == 'age':
            self.__dict__['_age'] = value
        else:
            self.__dict__[name] = value


"""
C применением декораторов

"""


class properties2:
    @property
    def age(self):
        return 40
    
    @age.setter
    def age(self, value):
        _age = 42


"""

Дескрипторы  ( атрибуты с методами __get__ и __set__ )

"""


class AgeDesc:
    def __get__(self, instance, owner):
        return 40
    
    def __set__(self, instance, value):
        instance._age = 40


class descriptors:
    age = AgeDesc()


if __name__ == '__main__':
    x = operators()
    print(x.age)
    #    print(x.name) Выдаст ошибку атрибута
    
    # C применением свойств
    x = properties()
    print(x.age)
    #    print(x.name) Выдаст ошибку атрибута
    
    # Изменение свойств
    x = properties()
    print(x.age)  # 40
    x.age = 42
    print(x._age)  # 42
    
    # Альтернативный класс без свойств
    
    x = operators1()
    print(x.age)
    x.age = 41
    print(x._age)  # 41
    print(x.age)  # 40
    
    x = properties2()
    print(x.age)
    x._age = 41
    print(x._age)

    # Дескрипторы
    
    x = descriptors()
    print(x.age)
    x.age = 42
    print(x._age)
