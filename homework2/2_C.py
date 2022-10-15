a,b=map(int,input().split(" "))
alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
new=''
if 2<=b<=9:
    while a>0:
        new=str(a%b) + new
        a//=b
elif 10<=b<=36:
    while a>0:
        if 10<=(a%b)<=36:
            g=a%b
            for i in range(0,len(alphabet)+1):
                if g==i+10:
                    g=alphabet[i]
        new=str(g) + new
        a//=b

print(new)

        