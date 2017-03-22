class Car:
    def __init__(self):
        self.name = "honda"
        
    def getName(self):
        return self.name
    
    
def test():
    c = Car()
    print(c.getName())
    
test()