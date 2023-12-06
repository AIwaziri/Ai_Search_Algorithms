from image_processing import*
from Problem import*

       

reached=[]
Agent_actions=[]        
states=[]
frontierMaxSize=0
        
def BFS(problem):
    global frontierMaxSize,reached
    node=Node(problem.initial)
    if problem.isGoal(node.state):
        return node
    frontier=Frontier("FIFO")
    frontier.push(node)
    reached.append(problem.initial)
    while not frontier.isEmpty():
        if frontierMaxSize<frontier.size():
            frontierMaxSize=frontier.size()
        node=frontier.pop()
        for child in expand(problem, node):
            s=child.state
            if problem.isGoal(s):
                return child
            if not s in reached:
                reached.append(s)
                frontier.push(child)




def best_first_search(problem,f,weight=1):
    node=Node(state=problem.initial)
    node.evaluation=f(node,weight)
    frontier=Frontier("Priority")
    frontier.push(node,node.evaluation)
    reached={problem.initial:node}
    while not frontier.isEmpty():
        node=frontier.pop()[1]
        if problem.isGoal(node.state): return node
        for child in expand(problem,node):
            s=child.state
            child.evaluation=f(node,weight)
            if not s in reached or child.path_cost < reached[s].path_cost:
                reached[s]=child
                frontier.push(child, child.evaluation)

    return "failure"


def greedyManh_search(problem):
    return best_first_search(problem,ManhattanHeuristic)
def greedyEucl_search(problem):
    return best_first_search(problem,EuclideanHeuristic)
def A_starManh(problem):
    return best_first_search(problem,A_starManhHeuristic)
def A_starEucl(problem):
    return best_first_search(problem,A_starEuclHeuristic)

def weightedA_starManh(problem,w):
    return best_first_search(problem,A_starManhHeuristic,w)
def weightedA_starEucl(problem,w):
    return best_first_search(problem,A_starEuclHeuristic,w)

# temp = weightedA_starManh(maze,1.4)
# temp = weightedA_starEucl(maze,1.4)
temp = A_starManh(maze)
# temp = A_starManh(maze)
# temp = greedyEucl_search(maze)
# temp = greedyManh_search(maze)
# temp = BFS(maze)
cost=temp.path_cost


while temp.parent != None:
    states.append(temp.state)
    Agent_actions.append(temp.action)
    temp = temp.parent

states.reverse()
Agent_actions.reverse()
# for i in Agent_actions:
#     print(i)
# print(frontierMaxSize)
# print(states)
print('----------------------------------------')
print(cost)