"""
Drone Flight Planner
You’re an engineer at a disruptive drone delivery startup and your CTO asks you to come up with an efficient algorithm
that calculates the minimum amount of energy required for the company’s drone to complete its flight.
\You know that the drone burns 1 kWh (kilowatt-hour is an energy unit) for every mile it ascends,
and it gains 1 kWh for every mile it descends. Flying sideways neither burns nor adds any energy.

Given an array route of 3D points, implement a function calcDroneMinEnergy that computes and returns the minimal amount
of energy the drone would need to complete its route. Assume that the drone starts its flight at the first point in route.
That is, no energy was expended to place the drone at the starting point.

For simplicity, every 3D point will be represented as an integer array whose length is 3.
Also, the values at indexes 0, 1, and 2 represent the x, y and z coordinates in a 3D point, respectively.

Explain your solution and analyze its time and space complexities.

Example:

input:  route = [ [0,   2, 10],
                  [3,   5,  0],
                  [9,  20,  6],
                  [10, 12, 15],
                  [10, 10,  8] ]

output: 5 # less than 5 kWh and the drone would crash before the finish
          # line. More than `5` kWh and it’d end up with excess energy
Constraints:

[time limit] 5000ms

[input] array.array.integer route

1 ≤ route.length ≤ 100
[output] integer
"""


# Time O(N)
# Space O(1) <= 만들어서 O(N)을 했었으나 이렇게 바로 가능 <= 항상 중복과 필요없는 것들을 정리하는 minimize process를 통해 code를 효율적이고 깔끔하게 만들자.
def calc_drone_min_energy(route):
    needed = acc = 0

    for i in range(1, len(route)):
        acc += route[i - 1][2] - route[i][2]
        if acc < needed:
            needed = acc

    return -1 * needed


"""
*** The more elegant solution ***
This solution is based on one observation: 
the initial energy level is what it takes the drone to climb from the start point to the highest (max) point in its route.

Getting to any altitude below the starting altitude produces energy, 
and going above it consumes at most the difference between the max altitude and the starting altitude.

Even if we descend before climbing to the max altitude, 
by ascending back to the same altitude as the starting altitude, 
our balance is zero and we then need more energy to climb from the starting altitude to the max altitude.
"""


# more Elegant
# Anyway go up more => before down(store) will be consumed
# Time O(N)
# Space O(1)
def calc_drone_min_energy(route):
    max_height = route[0][2]
    for i in range(1, len(route)):
        if route[i][2] > max_height:
            max_height = route[i][2]
    return max_height - route[0][2]


def calc_drone_min_energy(route):
    max_height = route[0][2]
    for i in range(1, len(route)):
        max_height = max(max_height, route[i][2])
    return max_height - route[0][2]


# Time complexity: O(n)
# Space complexity: O(1)
def calc_drone_min_energy(route):
    if len(route) <= 1:
        return 0
    start = route[0][2]
    max_height = max([z for x, y, z in route])
    return max_height - start
