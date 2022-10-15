def key_difference(dict1, dict2):
    result={}
    if len(dict1)>len(dict2):
        k=len(dict1)
        for i in dict1:
            if i in dict2:
                if dict1[i]==dict2[i]:
                    result[i]="equal"
                else:
                    result[i]="changed"
            else:
                result[i]="deleted"            

    else:
        k=len(dict2)
        for i in dict2:
            if i in dict1:
                if dict2[i]==dict1[i]:
                    result[i]="equal"
                else:
                    result[i]="changed"
            else:
                result[i]="added"                    
    return result
print(key_difference({"a":"b", "b":"a",  "c": "a"},{"a":"b", "b":"a"})) #Вводим данные двух словарей через запятую               
