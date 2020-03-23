# This is for homework

## It is the index file

1. This is the first item in the list
2. This is the second item
3. and the third
4. and finally the fourth

class Cat:
    
    def __init__(self, name):
        self.name = name
        
cats = [Cat("Kitty"), Cat("Peterle"), Cat("Amanda"), Cat("Olaf")]

cats.sort(key=lambda feline: feline.name)
names=[x.name for x in cats]
print(names)
