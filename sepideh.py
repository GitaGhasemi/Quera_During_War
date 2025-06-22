'''
This is an answer to this quera question
https://quera.org/problemset/31020

'''


students, doors = map(int, input().split()) 

if students % doors == 0:
    print(students // doors)
else:
    print((students // doors) + 1)    
