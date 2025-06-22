'''
This is an answer to this quera question
https://quera.org/problemset/10230

'''

a, b, c = map(int, input().split())

if (a > 0 and b > 0 and c > 0) and (a + b + c == 180):
    print("Yes")
else:
    print("No")
    