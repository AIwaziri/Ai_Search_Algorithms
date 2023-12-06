import math
import queue as q
import sys

from image_processing import matrix


class Node:
    count=0
    def __init__(self, state, parent=None, cost=0, action=None,priority=sys.maxsize):
        self.state = state
        self.parent = parent
        self.path_cost = cost
        self.action = action
        self.evaluation=priority
        Node.count+=1
        self.Num=Node.count
    def __lt__(self, other):
        if self.evaluation==other.evaluation:
            return self.Num<other.Num
        return self.evaluation<other.evaluation


class Problem:
    def __init__(self, init, goals):
        self.initial = init
        self.goal = goals

    def isGoal(self, state):
        return state in self.goal

    def Actions(self, state):
        pass

    def Results(self, state, action):
        pass

    def Action_Cost(self, state, action, next_state):
        pass


class Frontier:
    def __init__(self, type):
        if type == "FIFO":
            self.queue = q.Queue()
        elif type == "LIFO":
            self.queue = q.LifoQueue()
        elif type == "Priority" or type == "priority":
            self.queue = q.PriorityQueue()

    def pop(self):
        return self.queue.get()

    def push(self, x, priority=sys.maxsize):
        if priority == sys.maxsize:
            self.queue.put(x)
        else:
            self.queue.put((priority, x))

    def isEmpty(self):
        return self.queue.empty()

    def isFull(self):
        return self.queue.full()

    def size(self):
        return self.queue.qsize()


def north(pos):
    pos = list(pos)
    pos[0] -= 1
    return tuple(pos)


def south(pos):
    pos = list(pos)
    pos[0] += 1
    return tuple(pos)


def east(pos):
    pos = list(pos)
    pos[1] += 1
    return tuple(pos)


def west(pos):
    pos = list(pos)
    pos[1] -= 1
    return tuple(pos)


def north_east(pos):
    return north(east(pos))


def north_west(pos):
    return north(west(pos))


def south_east(pos):
    return south(east(pos))


def south_west(pos):
    return south(west(pos))


def expand(problem, node):
    s = node.state
    for action in problem.Actions(s):
        sdash = problem.Result(s, action)
        cost=node.path_cost+1
        yield Node(state=sdash, parent=node, action=action,cost=cost)


class Maze(Problem):
    def __init__(self, init, goals):
        super().__init__(init, goals)

    def Actions(self, state):
        actions = []
        for i in (north, south, east, west):
            try:
                x, y = i(state)
                if matrix[x][y] == 1:
                    actions.append(i)
            except:
                pass
        if north in actions:
            if east in actions:
                actions.append(north_east)
            elif west in actions:
                actions.append(north_west)
        elif (south in actions):
            if east in actions:
                actions.append(south_east)
            elif west in actions:
                actions.append(south_west)

        return actions

    def Result(self, state, action):
        return action(state)

    def Action_Cost(self, state, action, next_state):
        return 1

maze=Maze((0,2),[(108,209)])



def ManhattanHeuristic(node,weight=1):
    goal_x_coordinate = maze.goal[0][0]
    goal_y_coordinate = maze.goal[0][1]
    state_x_coordinate = node.state[0]
    state_y_coordinate = node.state[1]
    resultX = abs(state_x_coordinate - goal_x_coordinate)  # absolute value used to element any negatives
    resultY = abs(state_y_coordinate - goal_y_coordinate)
    result = resultX + resultY
    return result*weight


def EuclideanHeuristic(node,weight=1):
    goal_x_coordinate = maze.goal[0][0]
    goal_y_coordinate = maze.goal[0][1]
    state_x_coordinate = node.state[0]
    state_y_coordinate = node.state[1]
    resultX = (state_x_coordinate - goal_x_coordinate) ** 2
    resultY = (state_y_coordinate - goal_y_coordinate) ** 2
    result = math.sqrt(resultX + resultY)
    return result*weight

def A_starEuclHeuristic(node,weight=1):
    return node.path_cost+EuclideanHeuristic(node,weight)
def A_starManhHeuristic(node,weight=1):
    return node.path_cost+ManhattanHeuristic(node,weight)