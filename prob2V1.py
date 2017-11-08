# -*- coding: utf-8 -*-
num_list = [x for x in range(11)]
bonus_list = ["S","D","T"]
option_list = ["*","#"]

def input_divider(str1):
    result = []
    for i in range(len(str1)):
        if str1[i] in bonus_list:
            if i != (len(str1)-1):
                if str1[i+1] in option_list:
                    if not str1[i-2].isnumeric():
                        result.append(str1[i-1:i+2])
                    else:
                        result.append(str1[i-2:i+2])
                else:
                    if not str1[i-2].isnumeric():
                        result.append(str1[i-1:i+1])
                    else:
                        result.append(str1[i-2:i+1])
            else:
                if not str1[i-2].isnumeric():
                    result.append(str1[i-1:i+1])
                else:
                    result.append(str1[i-2:i+1])
    return result 
        
        

def score_cal(list1):
    first = list1[0]
    second = list1[1]
    third = list1[2]
    temp1 = []
    temp2 = []
    temp3 = []
    if "*" in first:
        temp1.append(2)
        first = first[:-1]
    elif "#" in first:
        temp1.append(-1)
        first = first[:-1]
    else:
        temp1.append(1)
    if "S" in first:
        temp1.append(1)
        first = first[:-1]
    if "D" in first:
        temp1.append(2)
        first = first[:-1]
    if "T" in first:
        temp1.append(3)
        first = first[:-1]
    temp1.append(int(first))
    temp1.append(1)
    
    if "*" in second:
        temp2.append(2)
        temp1[3] = 2
        second = second[:-1]
    elif "#" in second:
        temp2.append(-1)
        second = second[:-1]
    else:
        temp2.append(1)
    if "S" in second:
        temp2.append(1)
        second = second[:-1]
    if "D" in second:
        temp2.append(2)
        second = second[:-1]
    if "T" in second:
        temp2.append(3)
        second = second[:-1]
    temp2.append(int(second))
    temp2.append(1)    
    
    if "*" in third:
        temp3.append(2)
        temp2[3] = 2
        third = third[:-1]
    elif "#" in third:
        temp3.append(-1)
        third = third[:-1]
    else:
        temp3.append(1)
    if "S" in third:
        temp3.append(1)
        third = third[:-1]
    if "D" in third:
        temp3.append(2)
        third = third[:-1]
    if "T" in third:
        temp3.append(3)
        third = third[:-1]
    temp3.append(int(third))
    temp3.append(1)   
    
    result = temp1[2]**temp1[1]*temp1[0]*temp1[3] + temp2[2]**temp2[1]*temp2[0]*temp2[3]+temp3[2]**temp3[1]*temp3[0]*temp3[3]
    
    return result


input_example_list = ["1S2D*3T","1D2S#10S","1D2S0T","1S*2T*3S","1D#2S*3S","1T2D3D#","1D2S3T*"]
for i in range(len(input_example_list)):
    w = input_divider(input_example_list[i])
    print(score_cal(w))
                