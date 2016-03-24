#!/bin/python

import sys


t = int(raw_input().strip())
result = []
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    current = 0
    for aVal in a:
        if aVal <= 0:
            current += 1
    if current >= k:
        result.append('NO')
    else:
        result.append('YES')

for resultItem in result:
    print resultItem