'''
This is an answer to this quera question
https://quera.org/problemset/49028

'''

n = int(input())
list_input = []
change = 0
for n in range(n):
    list_input.append(input())

for i in range(len(list_input) - 1):
    if list_input[i] != list_input[i + 1]:
        change +=1

print(change)
