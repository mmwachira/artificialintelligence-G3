# Creation of the route to be traversed
graph = [['SportsComplex', 'Siwaka', 450],
         ['Siwaka', 'Ph1A', 10],
         ['Siwaka', 'Ph1B', 230],
         ['Ph1A', 'Mada', 850],
         ['Ph1A', 'Ph1B', 100],
         ['Ph1B', 'Phase2', 112],
         ['Ph1B', 'STC', 50],
         ['STC', 'Phase2', 50],
         ['STC', 'ParkingLot', 250],
         ['Phase2', 'J1', 600],
         ['Phase2', 'Phase3', 500],
         ['J1', 'Mada', 200],
         ['Phase3', 'ParkingLot', 350],
         ['Mada', 'ParkingLot', 700]]

frontier = []
frontier2 = []
for i in graph:
    frontier.append(i[0])
    frontier2.append(i[1])
nodes = set(frontier).union(set(frontier2))


# This is the main function
def UNIFORM_COST_SEARCH(graph, cost, open, explored, curr_node):
    if curr_node in open:
        open.remove(curr_node)
    explored.add(curr_node)

    for i in graph:
        if i[0] == curr_node and cost[i[0]] + i[2] < cost[i[1]]:
            open.add(i[1])
            cost[i[1]] = cost[i[0]] + i[2]
            path[i[1]] = path[i[0]] + ' -> ' + i[1]

    cost[curr_node] = 999999
    smallest = min(cost, key=cost.get)
    if smallest not in explored:
        UNIFORM_COST_SEARCH(graph, cost, open, explored, smallest)


cost = dict()
temp_cost = dict()
path = dict()
for i in nodes:
    cost[i] = 999999
    path[i] = ' '
opened = set()
explored = set()

# This is the starting point for the robot
start_node = "SportsComplex"
# input("Enter the Starting Point: ")

opened.add(start_node)
path[start_node] = start_node
cost[start_node] = 0
UNIFORM_COST_SEARCH(graph, cost, opened, explored, start_node)

# This is the robot's destination
goal_node = "ParkingLot"
# input("Enter the Destination: ")
print("The optimal path for the robot is: ", path[goal_node])
