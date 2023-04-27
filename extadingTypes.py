class MyList(list):
    def __getitem__(self, item):
        """
        Изеняет поведения списка, добавляет смещение на 1 относительно индекса
        :param item:
        :return:
        """
        print('indexing %s at %s' % (self, item))
        return list.__getitem__(self, item - 1)


class C:
    """
    Перехват атрибутов ( пример )
    """
    data = 'spam'
    
    def __getattr__(self, item):
        print(item)
        
        return getattr(self.data, item)


if __name__ == '__main__':
    print(list('abc'))
    x = MyList('abc')
    print(help(MyList))
    print(x)
    print(x[1])
    print(x[2])
    x.append('spam')
    print(x)
    x.reverse()
    print(x)
