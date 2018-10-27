#Question-Find Largest Palindrome Word in Any String ? [Given String-"Madam Teaches the Malayalam"]
#Answer
a="Madam Teaches the Malayalam"
b=a.split()
pal=[]
for i in range(len(b)):
    check=b[i]
    if b[i].upper()==check[::-1].upper():
        pal.append(b[i])    
print(max(pal,key=len))



