'''
This is an answer to this quera question
https://quera.org/problemset/2794

'''

a_x, a_y = map(int,input().split())
b_x, b_y = map(int,input().split())
c_x, c_y = map(int,input().split())

# I used XOR to define which one of the three of x's is different.
d_x = (a_x) ^ (b_x) ^ (c_x)
d_y = (a_y) ^ (b_y) ^ (c_y)

list_d = [d_x, d_y]
print(list_d[0], list_d[1])
