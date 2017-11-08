# -*- coding: utf-8 -*-
n =6 
arr1 = [46,33,33,22,31,50]
arr2 = [27,56,19,14,14,10]
#result = ["#####","# # #", "### #", "# ##", "#####"]
['######', '###  #', '##  ##', ' #### ', ' #####', '### # ']
def two_bit_transform(n,int_num):
    transformed = ""
    while(int_num!=0):
        if int_num == 0:
            transformed += "00000"
            break
        remain = int_num % 2
        transformed = str(remain)+transformed
        int_num = int(int_num/2)
    if len(transformed) != n:
        transformed = (n - len(transformed)) * "0" + transformed
    
    return transformed

def decode_map(n,num1,num2):
    trans_num1 = two_bit_transform(n,num1)        
    trans_num2 = two_bit_transform(n,num2)
    final = []
    for i in range(len(trans_num1)):
        if trans_num1[i] == "0":
            if trans_num2[i] == "0":
                final.append(i)
    decoded_map = n * "#"
    #print(final)
    for i in final:
        decoded_map = decoded_map[:int(i)] + " " + decoded_map[int(i)+1:]
    return decoded_map
        

def total_decode_map(n,arr1,arr2):
    result = []
    for i in range(n):
        result.append(decode_map(n,arr1[i],arr2[i]))
    return result

print(total_decode_map(n,arr1,arr2))
