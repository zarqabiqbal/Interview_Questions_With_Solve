#Find The Nth Term of the Series ? Series([0,0,1,2,2,4,3,6,4,8,5,10,....])
#Answer
num=int(input())
if int(num%2)==0:
    print(int((2*(num-2))/2))
elif int(num%2)!=0:
    print(int((num/2)))

