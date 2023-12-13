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