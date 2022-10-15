# Решение для трех целых чисел 
def F(a,b,c):
    summa=0
    if a<0:
        a=a*(-2)
    if b<0:
        b=b*(-2)
    if c<0:
        c=c*(-2)
    mx=-1
    a=[a,b,c]
    for i in a:
        if i>mx:
            mx=i
    for i in a:
        i=i/mx        
        summa=summa+i
    return(summa)            
print(F(5,8,-2))             