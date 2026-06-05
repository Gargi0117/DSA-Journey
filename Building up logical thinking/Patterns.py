# 1st Pattern
for i in range(5):
    for j in range(5):
        print("*",end="")
    print()

#Pattern 11
n=5
a=1
for i in range(n):
    b=a
    for j in range(i+1):
        print(b,end="")
        b=1-b # b=b^1
    a=1-a # a=a^1
    print()
# Pattern 12
n=4
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end="")
    for j in range(((2*n)-(2*i)),0,-1):
        print(" ",end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()

# n=6
# for i in range(1,n+1):
#     for j in range(i):
#         print(j+1,end="")
#     # for j in range(((2*n)-(2*i)),0,-1):
#     for j in range(2*(n-i),0,-1):
#         print(" ",end="")
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()

# Pattern 13
a=1
for i in range(5):
    for j in range(i+1):
        print(a,end=" ")
        a=a+1
    print()