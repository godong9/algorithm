#-*- coding: utf-8 -*-
"""
    소수 판별
"""

n = int(raw_input("Input n: "))

i = 1
count = 0

while i <= n:
    if n % i == 0:
        count += 1
    if count > 2:
        break
    i += 1

if count == 2:
    print "Prime Number"
else:
    print "Not Prime Number"

