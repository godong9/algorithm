#-*- coding: utf-8 -*-
"""
    하노이의 탑
"""

def Hanoi(n, fromBoard, middleBoard, toBoard):
    if n == 1:
        print("board #%s %s -> %s\n" % (n, fromBoard, toBoard))
    else:
        Hanoi(n-1, fromBoard, toBoard, middleBoard)
        print("board #%s %s -> %s\n" % (n, fromBoard, toBoard))
        Hanoi(n-1, middleBoard, fromBoard, toBoard)

n = int(raw_input("Input n: "))
print("="*20)
Hanoi(n, 'A', 'B', 'C')