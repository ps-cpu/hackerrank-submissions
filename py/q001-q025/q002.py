# https://www.hackerrank.com/challenges/py-if-else/problem

n = int(input())
if n%2==0:
    if n in range(2,6):
        print("Not Weird")
    elif n in range(6,21):
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")
