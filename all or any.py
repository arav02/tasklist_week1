n = list(map(int, input().split()))
flag=0
for i in range(len(n)):
    if(n[i]>0):
        if(flag==0):
           temp=n[i]
           rev_num=0
           while(temp>0):
             rem=temp%10
             rev_num=(rev_num*10)+rem
             temp=temp//10
           if (n[i]==rev_num):
                  flag=1
                  
    else:
         flag=0
         break
        
if(flag==1):
    print("True")
else:
    print("False")
