N = int(input())
list = []
num = []
nl = []
for i in range(0,N):
    a = input()
    b = float(input())
    num.append(b)
    list.append([a,b])
    num.sort()
    num.reverse()
    c = num.count(min(num))
    number=num[len(num)-c-1]
for i in range(0,N):
    if(number==list[i][1]):
        nl.append(list[i][0])
        nl.sort()
for x in range(len(nl)):
    print (nl[x])
