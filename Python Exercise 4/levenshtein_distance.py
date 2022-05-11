import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

word_1 = input()
word_2 = input()
len_1 = len(word_1)
len_2 = len(word_2)

# d = {}
# for i in range(len_1):
#     d[i, 0] = i
# for j in range (len_2):
#     d[0, j] = j
# for i in range(1, len_1):
#     for j in range(1, len_2):
#         if word_1[i] == word_2[j]:
#             d[i, j] = d[i-1, j-1]
#         else:
#             d[i, j] = min(d[i-1, j], d[i, j-1], d[i-1, j-1]) + 1

# help from https://www.codegrepper.com/code-examples/python/levenshtein+distance

m = [[*range(len_1 + 1)] for _ in range(len_2 + 1)]
for i in range(len_2 + 1):
    m[i][0] = i
for i in range(1, len_2 + 1):
    for j in range(1, len_1 + 1):
        m[i][j] = min(m[i-1][j] + 1, m[i][j-1] + 1, m[i-1][j-1] + (word_2[i-1] != word_1[j-1]))

print(m[-1][-1])
