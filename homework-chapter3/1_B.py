class Binary:      
    def __init__(self,num):
        k=0
        for i in range(len(num)):
            k+=int(num[i])*(2**(len(num)-i-1))
        self.num=k
    
    def __add__(self,other):
        if isinstance(other,Binary):
            return bin(int(self.num) + int(other.num))[2:]
        if isinstance(other, (int,float)):
            return bin(int(self.num) + int(other))[2:]        

    def __sub__(self,other):
        if isinstance(other,Binary):
            return bin(int(self.num) - int(other.num))[2:]
        if isinstance(other, (int,float)):
            return bin(int(self.num) - int(other))[2:]

    def __mul__(self,other):
        if isinstance(other,Binary):
            return bin(int(self.num) * int(other.num))[2:]
        if isinstance(other, (int,float)):
            return bin(int(self.num) * int(other))[2:]      

    def __floordiv__(self,other):
        if isinstance(other,Binary):
            return bin(int(self.num) // int(other.num))[2:]
        if isinstance(other, (int,float)):
            return bin(int(self.num) // int(other))[2:] 
    def __str__(self):
        return self.num  

class Ternary(Binary):
    def __init__(self,num):
        k=0
        for i in range(len(num)):
            k+=int(num[i])*(3**(len(num)-i-1))
        self.num=k
    def __add__(self,other):
        if isinstance(other,Ternary):
            n = int(self.num) + int(other.num)
            string = ''
            while n > 0:
                string+=str(n%3)
                n//= 3 
            return string[::-1]
        if isinstance(other, (int,float)):
            n = int(self.num) + int(other)
            string = ''
            while n > 0:
                string+=str(n%3)
                n//= 3 
            return string[::-1]

    def __sub__(self,other):
        if isinstance(other,Ternary):
            n= int(self.num) - int(other.num)
            string = ''
            while n > 0:
                string+=str(n%3)
                n//= 3 
            return string[::-1]
        if isinstance(other, (int,float)):
            n = int(self.num) - int(other)
            string = ''
            while n > 0:
                string+=str(n%3)
                n//= 3 
            return string[::-1]
    def __mul__(self,other):
        if isinstance(other,Ternary):
            n = int(self.num) * int(other.num)
            string = ''
            while n > 0:
                string+=str(n%3)
                n//= 3 
            return string[::-1]
        if isinstance(other, (int,float)):
            n = int(self.num) * int(other)
            string = ''
            while n > 0:
                string+=str(n%3)
                n//= 3 
            return string[::-1]
    def __floordiv__(self,other):
        if isinstance(other,Ternary):
            n = int(self.num) // int(other.num)
            string = ''
            while n > 0:
                string+=str(n%3)
                n//= 3 
            return string[::-1]
        if isinstance(other, (int,float)):
            n = int(self.num) // int(other)
            string = ''
            while n > 0:
                string+=str(n%3)
                n//= 3 
            return string[::-1]                       
    
a = Ternary(input()) 
b = Ternary(input())
print(a+b)
print(a-b)
print(a*b)
print(a//b)