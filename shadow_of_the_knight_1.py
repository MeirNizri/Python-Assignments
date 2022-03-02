import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

x1 = 0;
y1 = 0;
x2 = w - 1;
y2 = h - 1;

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if bomb_dir.find("U") != -1:
        y2 = y0 - 1
    elif bomb_dir.find("D") != -1:
        y1 = y0 + 1
    if bomb_dir.find("L") != -1:
        x2 = x0 - 1
    elif bomb_dir.find("R") != -1:
        x1 = x0 + 1

    # update the box coordinates
    x0 = x1 + (x2 - x1) // 2;
    y0 = y1 + (y2 - y1) // 2;
    # the location of the next window Batman should jump to.
    print(f'{x0} {y0}')
    # print("0 0")
