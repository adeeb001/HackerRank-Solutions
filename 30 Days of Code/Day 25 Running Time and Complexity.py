# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt

t=int(input())

def prime(n):
    if n == 1:
        return "Not prime"
    for a in range(2,int(sqrt(n)+1)):
        if n%a == 0:
            return "Not prime"
    return "Prime"
            
for i in range(1,t+1):
    n=float(input())
    print(prime(n))