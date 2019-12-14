class zespolone:
    def __init__(self,x,y):
        self.x=x
        self.y=y
       
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return zespolone(x,y)
       
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return zespolone(x,y)
       
    def __mul__(self, other):
        x=self.x*other.x - self.y*other.y
        y=self.y*other.x + self.x*other.y
        return zespolone(x,y)
       
    def __truediv__(self, other):
        m=other.x*other.x+other.y*other.y
        x=(self.x*other.x+self.y*other.y)/m
        y=(self.y*other.x-self.x*other.y)/m
        return zespolone(x,y)
a=zespolone(2,3)
b=zespolone(3,4)
print(a+b)
