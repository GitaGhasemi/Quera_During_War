'''
This is an answer to this quera question
https://quera.org/problemset/34081

'''
###############################################################
# In this question we are learning do-while.
# The key features of a do-while loop are that the loop body
# always executes at least once, and that the condition is
# evaluated at the bottom of the loop body.
#
# while True:
#   stuff()
#   if fail_condition:
#     break
###############################################################

n, k = map(int, input().split())
turn = 1
round = 0

while True:
        turn = (turn + k) % n 
        round += 1
        if turn == 1:
            break

print(round)        
