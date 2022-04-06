"""
The Goal:
In the Computer2000 data center, you are responsible for planning the usage of a supercomputer for scientists.
Therefore, you've decided to organize things a bit by planning everybody’s tasks. The logic is simple:
the higher the number of calculations which can be performed, the more people you can satisfy.

Rules:
Scientists give you the starting day of their calculation and
the number of consecutive days they need to reserve the calculator.

For example:
Calculation	Starting_Day Duration
A	2	5
B	9	7
C	15	6
D	9	3
- Calculation A starts on day 2 and ends on day 6
- Calculation B starts on day 9 and ends on day 15
- Calculation starts on day 15 and ends on day 20
- Calculation D starts on day 9 and ends on day 11
In this example, it’s not possible to carry out all the calculations because the
periods for B and C overlap. 3 calculations maximum can be carried out: A, D and C.

Game Input:
1: The number N of calculations
2: For every calculation, the starting day J and the duration D of reservation, separated by a blank space.

Output: The maximum number of calculations that can be carried out.

Constraints:
0 < N < 100000
0 < J < 1000000
0 < D < 1000
"""

n = int(input())
activities = []
for i in range(n):
    j, d = [int(j) for j in input().split()]
    activities.append((j, j + d))

# sort all activities by end of activity
activities.sort(key=lambda x: x[1])

# solution 1
'''
answer = 0
while activities:
    answer += 1
    earliest_end = activities[0][1]

    for activity in list(activities):
        if activity[0] < earliest_end:
            activities.remove(activity)
'''

# solution 2
answer = 1
earliest_end = activities[0][1]
for activity in activities:
    start, end = activity
    if start >= earliest_end:
        answer += 1
        earliest_end = end

print(answer)
