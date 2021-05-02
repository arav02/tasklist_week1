s=input()
lower=[]
upper=[]
odd=[]
even=[]

a=sorted(s)
for i in a:
    if i.islower():
        lower.append(i)
    elif i.isupper():
        upper.append(i)
    elif int(i)%2!=0:
        odd.append(i)
    else:
        even.append(i)
lower=''.join(lower)
upper=''.join(upper)
odd=''.join(odd)
even=''.join(even)
print(lower+upper+odd+even)
