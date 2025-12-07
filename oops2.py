class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d
    
    def __str__(self):
        return "{}/{}".format(self.num,self.den)
        
    def __add__(self,other):
        new_num=self.num*other.den+self.den*other.num
        new_den=self.den*other.den
        return Fraction(new_num,new_den)
        
    def __sub__(self,other):
        new_num=self.num*other.den-self.den*other.num
        new_den=self.den*other.den
        return Fraction(new_num,new_den)
    
    def __mul__(self,other):
        return Fraction(self.num*other.num,self.den*other.den)
        
x=Fraction(1,2)
y=Fraction(1,3)
print(x)
print(y)
print("Add:",x+y)
print("Sub:",x-y)
print("Mul:",x*y)