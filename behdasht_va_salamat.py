'''
This is an answer to this quera question
https://quera.org/problemset/51865

'''

score = int(input())
days = int(input())

if days == 0:
    score = 20
    print(score)
elif days == 7:
    print(score)
else:
    score = score - days
    if score < 0:
        print(0)
    else:
        print(score)
