'''
This is an answer to this quera question
https://quera.org/problemset/35253

'''

water_melons = int(input())
weighs = list(map(int, input().split()))
max = -1

for i in range(water_melons):
    if max < weighs[i]:
        max = weighs[i]
# print(max)
water_melon_index = weighs.index(max)
print(water_melon_index + 1)

'''
I wanted to make a list and compare each to elements with eachother and then 
delete the element that was smaller(the watermelon that was eaten).
I failed hard. ^_^

'''
# water_melons = int(input())
# weighs = list(map(int, input().split()))

# for i in range (water_melons - 4):
#     if weighs[i] > weighs[i + 1]:
#         del weighs[i]
#     elif weighs[i] < weighs[i + 1]:
#         del weighs[i + 1]
# print(weighs)
