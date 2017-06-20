```python
class newBaby:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        
    def sayHello(self):
        print('Hello world, I am %s'%self.name)
        
    def showWeight(self):
        print('I am %.1f pounds'%self.weight)
        
baby2 = newBaby('Fanqi', 9)
baby2.sayHello()
baby2.showWeight()
```

    Hello world, I am Fanqi
    I am 9.0 pounds

