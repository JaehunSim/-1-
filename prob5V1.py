# -*- coding: utf-8 -*-
def split_by_two_interval(str1):
    result = []
    str1 = str1.upper()
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            result.append(str1[i:i+2])
    return result

def intersect(list1,list2):
    temp1 = list1.copy()
    temp2 = list2.copy()
    if len(temp1) < len(temp2):
        temp1, temp2 = temp2, temp1
    result = []
    for i in temp2:
        if i in temp1:
            result.append(i)
            temp1.pop(temp1.index(i))
    return result

def union(list1,list2):
    result = []
    #print(list1)
    #print(list2)
    for i in list1:
        result.append(i)
    
    for i in list2:
        result.append(i)
    interList = intersect(list1,list2)
    #print(result)
    for i in interList:
        result.pop(result.index(i))
    return result


        
    
def similarity(str1, str2):
    str1List = split_by_two_interval(str1)
    str2List = split_by_two_interval(str2)
    #print(str1List)
    #print(str2List)
    interList = intersect(str1List,str2List)
    #print(interList)
    uniList = union(str1List,str2List)
    #print(uniList)
    #print(interList)
    if len(uniList) != 0:
        return int(len(interList)/len(uniList) * 65536)
    else:
        return 65536

str1Array = ["FRANCE", "handshake","aa1+aa2", "E=M*C^2"]
str2Array = ["french", "shake hands", "AAAA12", "e=m*c^2"]

for i in range(len(str1Array)):
    print(similarity(str1Array[i],str2Array[i]))