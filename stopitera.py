class numbs:
    def __iter__(self):
        self.pp = 11
        return self
    
    def __next__(self):
        if self.pp <= 22:
            ll = self.pp
            self.pp += 1
            return ll
        else:
            raise StopIteration
        
cclass = numbs()
iiter = iter(cclass)

for x in iiter:
    print(x)
    