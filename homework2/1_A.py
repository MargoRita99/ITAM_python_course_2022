def greetings(a):
    words=a.split()
    return "Доброго времени суток, " + words[0] + " Человек " + words[-1]
print(greetings("Гендо Геннадий"))    
