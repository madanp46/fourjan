n = int(input())
for i in range (n):
    a=input()
    b=input()
    k=0
    for i in a:
        if i in b:
            k+=1
    if k==len(a):
        print("YES")
    else:
        print("No")