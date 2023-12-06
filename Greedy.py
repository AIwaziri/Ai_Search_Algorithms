import heapq
import math
import re
import sys
from Problem import *
import numpy as np

initial = (0, 2)
goal = (108,209)
maze = Maze(initial, goal)
reached = []  # to avoid infinite loops and redundant states
Agent_actions = []  # These are the actions that the agent should do to reach the goal
states = []  # These are the states that the agent go through to reach the goal


def ManhattanTable():
    array = np.array(matrix)  # to avoid TypeError
    rows, cols = array.shape  # taking the rows and columns
    HeuristicArray = np.zeros((rows, cols))  # creating an "empty" array with zeroes

    for i in range(HeuristicArray.shape[0]):  # looping through array using rows and columns
        for j in range(HeuristicArray.shape[1]):
            heuristic = (i, j)  # simulating how the state would be if it enters the heuristic function
            if array[i][j] == 0:  # if in the actual matrix there is a wall
                HeuristicArray[i][j] = 9999  # assign a high number to never be considered
                # HeuristicArray[i][j]=sys.maxsize
            else:
                result = ManhattanHeuristic(str(heuristic))  # find the value of heuristic
                HeuristicArray[i][j] = result  # assign it into table

    for i in range(HeuristicArray.shape[0]):  # looping through array using rows and columns
        for j in range(HeuristicArray.shape[1]):
            print(
                f"x= {i}, y= {j}, value= {HeuristicArray[i][j]}")  # just print the x and y coordinates and the value(just for testing)
        print()
    return HeuristicArray


def EuclideanTable():
    array = np.array(matrix)  # to avoid TypeError
    rows, cols = array.shape  # taking the rows and columns
    HeuristicArray = np.zeros((rows, cols))  # creating an "empty" array with zeroes

    for i in range(HeuristicArray.shape[0]):  # looping through array using rows and columns
        for j in range(HeuristicArray.shape[1]):
            heuristic = (i, j)  # simulating how the state would be if it enters the heuristic function
            if array[i][j] == 0:  # if in the actual matrix there is a wall
                # HeuristicArray[i][j] = 9999  # assign a high number to never be considered
                HeuristicArray[i][j] = sys.maxsize
            else:
                result = EuclideanHeuristic(str(heuristic))  # find the value of heuristic
                HeuristicArray[i][j] = result  # assign it into table

    for i in range(HeuristicArray.shape[0]):  # looping through array using rows and columns
        for j in range(HeuristicArray.shape[1]):
            print(
                f"x= {i}, y= {j}, value= {HeuristicArray[i][j]}")  # just print the x and y coordinates and the value (just for testing)
        print()
    return HeuristicArray


def ManhattanHeuristic(state):
    goal_x_coordinate = goal[0]
    goal_y_coordinate = goal[1]
    digits = re.findall(r'\d+', state)  # function to find all digits in a string
    state_x_coordinate = int(digits[0])
    state_y_coordinate = int(digits[1])
    resultX = abs(state_x_coordinate - goal_x_coordinate)  # absolute value used to element any negatives
    resultY = abs(state_y_coordinate - goal_y_coordinate)
    result = resultX + resultY
    return result


def EuclideanHeuristic(state):
    goal_x_coordinate = goal[0]
    goal_y_coordinate = goal[1]
    digits = re.findall(r'\d+', state)  # function to find all digits in a string
    state_x_coordinate = int(digits[0])
    state_y_coordinate = int(digits[1])
    resultX = (state_x_coordinate - goal_x_coordinate) ** 2
    resultY = (state_y_coordinate - goal_y_coordinate) ** 2
    temp = resultX + resultY
    result = math.sqrt(temp)
    return result



def isEmpty(heap):
    return len(heap) == 0


def isFull(heap):
    return len(heap) == heap.max_size


def GS_Manhattan(problem):
    node = Node(problem.initial)  # initializing the node
    if problem.initial == problem.goal:  # if node is goal, return
        return node
    heap = []  # initializing the heap
    heapq.heappush(heap, (ManhattanHeuristic(str(problem.initial)), problem.initial))  # pushing the priority and the state into the heap
    reached = {problem.initial: ManhattanHeuristic(str(node.state))}  # reached nodes are saved to prevent repetition
    while not isEmpty(heap):
        temp = heapq.heappop(heap)  # pop the heuristic and state
        state = temp[1]  # take only the state
        states.append(state)  # add it to the states we visited
        if state == problem.goal:  # if node is goal, return
            return state
        for position in expand(problem, state):  # expand with all possible children
            child = position.state  # take the child's state
            h = ManhattanHeuristic(str(child))  # and find it's heuristic
            if child not in reached:  # if we didn't visit the child before
                reached[child] = h  # add the child in reached with the heuristic
                heapq.heappush(heap, (h, child))  # add child into the heap with its priority


def GS_Euclidean(problem):
    node = Node(problem.initial)  # initializing the node
    if problem.initial == problem.goal:  # if node is goal, return
        return node
    heap = []  # initializing the heap
    heapq.heappush(heap, (
    EuclideanHeuristic(str(problem.initial)), problem.initial))  # pushing the priority and the state into the heap
    reached = {problem.initial: EuclideanHeuristic(str(node.state))}  # reached nodes are saved to prevent repetition
    while not isEmpty(heap):
        temp = heapq.heappop(heap)  # pop the heuristic and state
        state = temp[1]  # take only the state
        states.append(state)  # add it to the states we visited
        if state == problem.goal:  # if node is goal, return
            return state
        for position in expand(problem, state):  # expand with all possible children
            child = position.state  # take the child's state
            h = EuclideanHeuristic(str(child))  # and find its heuristic
            if child not in reached:  # if we didn't visit the child before
                reached[child] = h  # add the child in reached with the heuristic
                heapq.heappush(heap, (h, child))  # add child into the heap with its priority


def ActionFinder():  # go through states take one state, and the one before it, then compare between them, to find north,south,east,west,ne,nw,se,sw
    for i in range(1, len(states)):  # incomplete function as not needed, ignore it
        current = states[i]
        previous = states[i - 1]
        x_previous = previous[0]
        y_previous = previous[1]
        x_current = current[0]
        y_current = current[1]


#in case you want to see the heuristic tables
# ManhattanTable()
# EuclideanTable()

GS_Euclidean(maze)  # for testing run one of them at a time so that states list doesn't get mixed up
# GS_Manhattan(maze)

# print(states)
# EuclideanTable()