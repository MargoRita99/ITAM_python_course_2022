number=int(input())
k=1 #кол-во уровней
for i in range(1,100):
    if (number-i)>k:
        k+=1
        number-=i
print(k)