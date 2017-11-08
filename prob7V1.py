# -*- coding: utf-8 -*-

input1 = [ "2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s" ]
input2 = [ "2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s" ]
input3 = [ "2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s" ]

def into_flat_time(timeString):
    hour = int(timeString[:2])
    minute = int(timeString[3:5])
    second = float(timeString[6:])
    return hour*3600+minute*60+second

def log_into_better_form(logString):
    day = logString[:10]
    time = logString[11:23]
    process = logString[24:-1]
    result = []
    result.append(round(into_flat_time(time)-float(process)+0.001,4))
    result.append(into_flat_time(time))
    return result


def per_sec_best(timeLogList):
    result = []
    for i in timeLogList:
        result.append(log_into_better_form(i))
    mostBig = 0
    for x in range(int(round(result[-1][-1]-1-result[0][0],4)*1000)):  
        count = 0
        temp = [round(result[0][0]+x*0.001+0.001,4),round(result[0][0]+x*0.001+1,4)]
        for i in result:
            if temp[0] >= i[0]:
                if i[1] >= temp[0]:
                    count +=1
            elif temp[1] <= i[1]:
                if i[0] <= temp[1]:
                    count +=1
            elif temp[0] <= i[0]:
                if i[1] <= temp[1]:
                    count +=1
                
                
        if count > mostBig:
            print(temp)
            print(count)
            mostBig = count
        #print(temp)
    return result, mostBig

w = per_sec_best(input1)

