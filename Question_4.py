#Question : Check hom much times String will be shifted on Right Side ? (example="school" will be shifted 4 times("oolsch") then it gives the following output("4") ) 

import itertools as it#itertools use for iteration of string

#define cmp function for comparing two tuple if both tuple are same it return 0 and if its not then it return 1
def cmp(a, b):
    return (a > b) - (a < b)

#define function for check the how time the string will be right shifted example ABCD shift two times CDAB
def check_string(str1,str2):
    counter=0
    item_check=''
    for i in it.permutations(str1):
        if (cmp(tuple(map(str,str2)),i)==0):
            counter=counter+1
            item_check=i[0]
    if counter!=0:
        print(list(map(str,str1)).index(item_check))
    else:
        print("You Entered Wrong String")

        
str1="ABCD"
str2="CDAB"
check_string(str1,str2)

