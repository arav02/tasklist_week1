n = list(map(int, input().split()))
prdt = 1
for i in range(len(n)): 
    prdt= prdt*n[i]
print(prdt)
