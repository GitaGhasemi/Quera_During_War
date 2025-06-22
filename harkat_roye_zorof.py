'''
This is an answer to this quera question
https://quera.org/problemset/6375

'''

a, b, c = map(int, input().split())
mid = (a + b + c) / 3

if a == b and b == c:
    print(0)
elif a == mid or b == mid or c == mid:
    print(1)
else:
    print(2)
    