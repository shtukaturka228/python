n=int(input())
a=[1]*(n+1)
a[1]=0
m=2
while m<=n:
    if a[m]!=0:
        j=m*2
        while j<=n:
            a[j]=0
            j=j+m
    m=m+1
for i in range(2,n+1):
    if a[i]!=0:
        print(i)
