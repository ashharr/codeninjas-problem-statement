n = int(input()) 
A = input().split() 
A = [int(j) for j in A] 
q1 = 0 
q2 = 0 
for x in range(n): 
    if A[x]%3==1: 
        q1 = q1+1 
    if A[x]%3==2:
        q2 = q2+1 
if q1%2==0 and q2%2==0: 
    print("Aahad") 
else: 
    print("Harshit")
