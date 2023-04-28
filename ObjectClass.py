class C:
    pass


if __name__ == '__main__':
    x = C()
    print(type(x), type(C))
    print(isinstance(x, object), isinstance(C, object))  # True, True
    # Отношение справедливо для встроенных типов вроде строк
    print(type('spam'), type(str))  # <class 'str'> <class 'type'>
    print(isinstance('spam', object), isinstance(str, object))  # True, True
    # Тип унаследован от object
    print(type(type), type(object))  # <class 'type'> <class 'type'>
    # Все классы являются производными от object, даже type
    print(isinstance(type, object), isinstance(object, type)) # True True
    # Типы создают классы, и type - это класс
    print(isinstance(object, type)) # True
    
    # Практические последствия.
    # Мы должны знать о методах, поступающих явно или неявно из корневого каталога
    print(C.__bases__) # <class 'object'>
    print(C().__repr__) # <method-wrapper '__repr__' of C object at 0x00000044D926EF70>
    
    
