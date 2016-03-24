#!/bin/python

import sys


t = int(raw_input().strip())
result = []
for a0 in xrange(t):
    n = int(raw_input().strip())
    height = 1
    for idx in range(1, n+1):
        if idx % 2 == 1:
            height = height * 2
        else:
            height = height + 1
    result.append(height)

for item in result:
    print item