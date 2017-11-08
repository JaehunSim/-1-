# -*- coding: utf-8 -*-

timetableLists = [["09:09", "09:10", "08:00"],
                  ["23:59"],
                  ["00:01","00:01","00:01","00:01","00:01"],
                  ["09:00","09:00","09:00","09:00"],
                  ["08:00","08:01","08:02","08:03"]]

def into_flat_time(timeString):
    hour = int(timeString[:2])
    minute = int(timeString[3:])
    return hour*60+minute

def into_compl_time(flatNum):
    result = ""
    hour = int(flatNum / 60)
    minute = flatNum - 60*hour
    if hour < 10:
        result = result + "0" + str(hour)
    else:
        result = result + str(hour)
    if minute < 10:
        result = result + ":0" + str(minute)
    else:
        result = result + ":"+ str(minute)
    return result

def timetable_to_flattimetable(timetable):
    result = []
    for i in timetable:
        result.append(into_flat_time(i))
    return result

def get_bus_arrival_time(n,t):
    timeList = []
    timeList.append(540)
    if n == 1:
        return timeList
    for i in range(n-1):
        timeList.append(540+t*(i+1))
    return timeList
        

def arrive_time(n,t,m,timetable):
    flat = timetable_to_flattimetable(timetable)
    flat.sort()
    timeList = get_bus_arrival_time(n,t)
    for j in timeList:
        if j != timeList[-1]:
            for i in range(m):
                if flat[0] <= j:
                    flat = flat[1:]
        else:
            for i in range(m):
                if i != (m-1):
                    if flat[0] <= j:
                        flat = flat[1:]
                else:
                    if len(flat) != 0:
                        if flat[0] <= j: 
                            return into_compl_time(flat[0]-1)
                        else:
                            return into_compl_time(timeList[-1])
                            
                    else:
                        return into_compl_time(timeList[-1])
                    
            
        
    return flat

print(arrive_time(1,1,5,timetableLists[4]))