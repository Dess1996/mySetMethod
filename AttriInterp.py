class C:
    """
    Перехват атрибутов ( пример )
    """
    data = 'spam'
    
    def __getattr__(self, item):
        print(item)
        
        return getattr(self.data, item)
