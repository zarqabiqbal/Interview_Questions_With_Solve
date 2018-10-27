#Find Largest Prime Number In Sorted Array ? [Given Array-[1,3,5,8,10,12,15]]
#Answer
def check_prime(num):
    count=0
    if num==1:
        return True
    for i in range(1,int(num/2)):
        if (num%i)==0:
            count=count+1
    if count>1:
        return False
    else:
        return True
array=[1,3,5,8,10,12,15]
prime=[]
for i in range(len(array)):
    if check_prime(array[i]):
        prime.append(array[i])
print(max(prime))



