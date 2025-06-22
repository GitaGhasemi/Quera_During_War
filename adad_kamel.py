'''
This is an answer to this quera question
https://quera.org/problemset/282

'''

n = int(input())
sum = 0
for num in range(1, n):
    if n % num == 0:
        sum += num

if sum == n:
    print("YES")
else:
    print("NO")    
