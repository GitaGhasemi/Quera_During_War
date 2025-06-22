'''
This is an answer to this quera question
https://quera.org/problemset/26651

'''

n = int(input())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

sum = 0

for i in range(n):
    sum += (list_a[i] * list_b[i])
print(sum)
