class MySet:
    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
        
    
    def has(self, value):
        #return self.dictionary[value]
        #the above code will not work becuase it will return None instead of False
        #using the 'in' key word will return true of false
        return value in self.dictionary
    
    def add(self,value):
        self.dictionary[value] = True
        return self.dictionary
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
        
    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary.clear()
        return self.dictionary
    
    def __str__(self):
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'