'''
This is an answer to this quera question
https://quera.org/problemset/283

'''


a = int(input())
b = int(input())

margin = (a - b) // 2

if b >= a:
    print("Wrong order!")
elif ((a-b) % 2) != 0:
    print("Wrong difference!")
else:
    for i in range(a):
        for j in range(a):
            if (margin <= i) and (i < a - margin) and (margin <= j) and (j < a - margin):
                print(" ", end=" ")
            else:
                print("*", end=" ")
                
        print()  
