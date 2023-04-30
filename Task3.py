class Attrs:
    args = []
    
    def __getattr__(self, item):
        self.args.append(item)
        return self.args
    
    def __setattr__(self, key, value):
        print('set %s, %s' % (key, value))
        self.__dict__[key] = value
        print(self.__dict__)
    
    def __getitem__(self, item):
        return self.__dict__[item]


if __name__ == '__main__':
    attr = Attrs()
    attr.job = 'dev'
    print(attr.age)
    attr.b = 2
    print(attr.__dict__.values())

