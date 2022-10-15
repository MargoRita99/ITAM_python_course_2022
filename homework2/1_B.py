def summation(start,end):
    if start < end:
        return sum(i for i in range(start,end+1))
    else:
        return sum(i for i in range(end,start+1))
print(summation(-4,4))            
            