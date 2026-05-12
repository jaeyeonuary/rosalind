'''
import os
import numpy as np
import pandas as pd

#1
import this

#2
a, b = map(int, input().split())
c = a**2 + b**2
print(c)
'''

#3
# Given: A string s of length at most 200 letters and four integers a, b, c and d
# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively.
# In other words, we should include elements s[b] and s[d] in our slice.
# 
# Sample dataset
# HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
# Sample Output
# 22 27 97 102
#
# Solution
# s = input()
# a, b, c, d = map(int, input().split())
# print(s[a:b+1], s[c:d+1])
# *a-b => from a to b-1 index. => [a:b+1]

#4
# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.
#
# Sample Dataset
# 100 200
# Sample Output
# 7500
#
# Solution
# total = 0
# a, b = map(int, input().split())
# for i in range(a, b+1):
#     if i % 2 == 1:
#         total += i
# print(total)
# *input() => '100 200' (recognize as str, split with blank is needed. so add .split())
# *range(a, b) => a ~ b-1 (to include b, add b+1)
# *+= means accumulation => (total = total + i)
# print shoud be out of loop

#5 Reading and Writing
# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
#
# Solution
# f = open(r'C:\Users\gjae9\Downloads\rosalind_ini5.txt', 'r')
# for i, line in enumerate(f, 1):
#     if i % 2 == 0:
#         print(line.strip())

#6 Dictionaries
# Given: A string s of length at most 10000 letters.
# Return: The number of occurrences of each word in s, where words are separated by spaces.
# Words are case-sensitive, and the lines in the output can be in any order.
#
# Solution
s = input().split()
d = {}
for word in s:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
for word, count in d.items():
    print(word, count)