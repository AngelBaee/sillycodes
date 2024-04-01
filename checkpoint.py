class manumb:
    def __iter__(self):
        self.a = 1
        return self
    

    def __next__(self):
        if self.a <= 21:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        

maclass = manumb()
maiter = iter(maclass)

for x in maiter:
    print(x)