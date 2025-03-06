n=int(input())
SolveCount = 0
for i in range(n):
    j=input().split()
    s=0
    for x in j:
        s=s+int(x)
    if(s>=2):
        SolveCount=SolveCount+1
print(SolveCount)