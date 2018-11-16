
#input '(())' #output 2
#input '()(' #output -1

def checkDoorClose(string):
    count1=0
    count2=0
    for i in range(len(string)):
        if string[i]=='(':
            count1=count1+1
        if string[i]==')':
            count2=count2+1
    if (count2-count1)<0:
        return (count2-count1)
    else:
        return count1
string='(())'
print(checkDoorClose(string))
string='()('
print(checkDoorClose(string))
    

