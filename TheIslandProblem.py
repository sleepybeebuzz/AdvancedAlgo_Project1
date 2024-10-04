from typing import List


# Helper functions
def findNeighbors(row, col, rowL, colL):
    neighbors = []
    LRUP_Directions = [(row, col-1), (row, col+1), (row+1, col), (row-1, col)]
    for r, c in LRUP_Directions:
        # Filters for the bounds of the island matrix.
        if 0 <= r < rowL and 0 <= c < colL:
            neighbors.append((r, c))
    # Note: This doesn't check for water or visited
    return neighbors


def DFS(island, rowPos, colPos, visited):
    # Check for water and visited. This returns no value for mass.
    if island[rowPos][colPos] != 0 or (rowPos, colPos) in visited:
        return 0

    # The current iteration is now visited.
    visited.add((rowPos, colPos))

    # This instance of land brings up the mass by 1.
    mass = 1

    neighbors = findNeighbors(rowPos, colPos, len(island), len(island[0]))

    # the _Coord is to distinguish the neighbor positions from the starting position.
    for row_Coord, col_Coord in neighbors:
        mass += DFS(island, row_Coord, col_Coord, visited)

    return mass


def calcMass(island: List[List[int]]) -> List[List[int]]:
    # Islands are clusters of land. Identify clusters and assign mass value.
    rowL = len(island)
    colL = len(island[0])
    cluster = [[0 for _ in range(colL)] for _ in range(rowL)]

    for i in range(rowL):
        for j in range(colL):
            visited = set()
            clusterValue = DFS(island, i, j, visited)
            cluster[i][j] = clusterValue
    # print(cluster)
    return cluster


def largestMass(island: List[List[int]]) -> int:
    oldIsland = calcMass(island)
    theMax = 0

    # After oldIsland mass is calculated, there is a 2nd pass that iterates both concurrently
    for i in range(len(island)):
        for j in range(len(island[0])):
            theMax = max(theMax, oldIsland[i][j])
            if island[i][j] == 1:
                # The clusters and mass values are already solved for old island
                adjacentClusters = findNeighbors(i, j, len(oldIsland), len(oldIsland[0]))
                currentMass = 1
                # Need to account for neighbors part of the same island that might count multiple times.
                duplicateException = set()
                for r, c in adjacentClusters:
                    if not (oldIsland[r][c] in duplicateException):
                        currentMass += oldIsland[r][c]
                        duplicateException.add(oldIsland[r][c])
                    theMax = max(theMax, currentMass)

    return theMax




