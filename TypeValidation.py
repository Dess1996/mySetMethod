class C:
    pass


class D:
    pass


if __name__ == '__main__':
    c, d = C(), D()
    print(type(c) == type(d)) # False
    print(type(c), type(d)) # <class '__main__.C'> <class '__main__.D'>
    print(c.__class__, d.__class__) # <class '__main__.C'> <class '__main__.D'>
    c1, c2 = C(), C()
    print(type(c1) == type(c2)) # True
    
