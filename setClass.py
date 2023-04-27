class mySet:
    def __init__(self, *args):
        self.values = ''
        self.convToSet(*args)
    
    def convToSet(self, *args):
        _k = []
        for i in args:
            if i in _k:
                continue
            else:
                _k.append(i)
        self.values = _k
    
    def add(self, value):
        if str(value) in self.values:
            return self.values
        else:
            self.values.append(value)
        return self.values
    
    def remove(self, value):
        if str(value) not in str(self.values):
            raise KeyError('%d does not exist in setClass' % value)
        else:
            self.values.remove(value)
    
    def intersect(self, *args):
        res = []
        for i in args:
            if str(i) in str(self.values):
                res.append(i)
            else:
                continue
        return '{' + str(res)[1:-1] + '}'
    
    def union(self, *args):
        val = self.values[:]
        a = mySet(*args)[:]
        for i in a:
            if i in self.values:
                continue
            else:
                val.append(i)
        return '{' + str(val)[1:-1] + '}'
    
    def __str__(self):
        openBrace = '{'
        expr = str(self.values)[1:-1]
        closedBrace = '}'
        return openBrace + expr + closedBrace
    
    def __add__(self, other):
        raise TypeError('unsupported opperand')
    
    def __len__(self):
        return len(self.values)
    
    def __iter__(self):
        return iter(self.values)
    
    def __contains__(self, item):
        return item in self.values
    
    def __getitem__(self, item):
        return self.values[item]


if __name__ == '__main__':
    a = mySet(1, 2, 4)
