# -*- coding: utf-8 -*-
cityLists = [["A","B","C","D","E","A","B","C","D","E"],
         ["A","B","C","A","B","C","A","B","C"],
         ["A","B","C","D","E","F","C","G","H","A","D","G"],
         ["A","B","C","D","E","F","C","G","H","A","D","G"],
         ["A","B","C","c"],
         ["A","B","C","D","E"],
         ["A","A","A"]]
cacheSizeList = [3,3,2,5,2,0,0]

def upperList(list1):
    result = []
    for i in list1:
        result.append(i.upper())
    return result

def time_cal(cacheSize, cities):
    cache = [0] * cacheSize
    cities1 = upperList(cities)
    cost = 0
    for i in cities1:
        print(cache)
        if i not in cache:
            if 0 in cache:
                temp = cache.index(0)
                cache[temp] = i
                cost += 5
            else:
                cache = cache[1:] +list(i)
                cost += 5
        else:
            temp = cache.index(i)
            cache.pop(temp)
            cache = cache + list(i)
            cost +=1
            
    if cacheSize == 0:
        cost = 5 * len(cities)
    return cost

for i in range(len(cacheSizeList)):
    print(time_cal(cacheSizeList[i],cityLists[i]))
    
    