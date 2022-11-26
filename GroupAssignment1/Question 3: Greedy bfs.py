import matplotlib.pyplot as plt
import networkx as nx

c_graph = {
    'Sports Complex': ['Siwaka'],
    'Siwaka': ['Ph.1A', 'Ph.1B'],
    'Ph.1A': ['Mada', 'Ph.1B'],
    'Ph.1B': ['Phase 2', 'STC'],
    'Phase 2': ['Phase 3', 'J1', 'STC'],
    'Phase 3': ['Parking lot'],
    'J1': ['Mada'],
    'Parking lot': ['Mada']
}


def show(graph):
    nx_graph = nx.Graph()

    for node in graph:
        for neighbour in graph[node]:
            nx_graph.add_edge(node, neighbour, color="black")

    x = nx.spring_layout(nx_graph)
    colors = [nx_graph[u][v]['color'] for u, v in nx_graph.edges()]
    nx.draw(nx_graph, x, node_color="#ADD8E6", edge_color=colors, width=2, with_labels=True)
    plt.show()


show(c_graph)

from queue import PriorityQueue

v = 14
graph = [[] for i in range(v)]


def best_first_search(actual_Src, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, actual_Src))
    visited[actual_Src] = True

    while pq.empty() == False:
        u = pq.get()[1]
        # Displaying the path having the lowest cost
        print(u, end=" ")
        if u == target:
            break

        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))
    print()


# Function for adding edges to graph


def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))


# The nodes shown in the graph(by alphabets) are
# implemented using integers add edge(x,y,cost);
addedge(0, 0, 730)
addedge(0, 1, 405)
addedge(1, 2, 380)
addedge(2, 3, 280)
addedge(1, 3, 280)
addedge(3, 4, 213)
addedge(4, 5, 210)
addedge(3, 5, 210)
addedge(5, 6, 160)
addedge(6, 7, 0)
addedge(7, 8, 630)
addedge(8, 2, 380)
addedge(8, 9, 500)
addedge(9, 5, 210)

source = 0
target = 7
best_first_search(source, target, v)

import sys
import operator


class Node:
    def _init_(self, state, parent, action, heuristic):
        self.state = state
        self.parent = parent
        self.action = action

        self.heuristic = heuristic


class Greedy:
    def _init_(self):
        self.frontier = []

    def add(self, node):

        self.frontier.append(node)

        self.frontier.sort(key=operator.attrgetter("heuristic"))

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


class colournode:
    def _init_(self, filename):

        with open(filename) as f:
            contents = f.read()

        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")

        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Keep track of walls
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None

    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1)),
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

    def solve(self):
        """Finds a solution to maze, if one exists."""

        self.num_explored = 0

        start = Node(state=self.start, parent=None, action=None, heuristic=999)
        frontier = Greedy()
        frontier.add(start)

        self.explored = set()

        while True:

            if frontier.empty():
                raise Exception("no solution")

            node = frontier.remove()
            self.num_explored += 1

            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            self.explored.add(node.state)

            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    heuristic = 0
                    if self.goal[0] > state[0]:
                        heuristic = self.goal[0] - state[0]
                    else:
                        heuristic = state[0] - self.goal[0]

                    if self.goal[1] > state[1]:
                        heuristic += self.goal[1] - state[1]
                    else:
                        heuristic += state[1] - self.goal[1]

                    child = Node(
                        state=state, parent=node, action=action, heuristic=heuristic
                    )
                    frontier.add(child)

    def output_image(self, filename, show_solution=True, show_explored=False):
        from PIL import Image, ImageDraw

        cell_size = 50
        cell_border = 2

        img = Image.new(
            "RGBA", (self.width * cell_size, self.height * cell_size), "black"
        )
        draw = ImageDraw.Draw(img)

        solution = self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):

                # Walls
                if col:
                    fill = ()

                # Start
                elif (i, j) == self.start:
                    fill = ()

                # Goal
                elif (i, j) == self.goal:
                    fill = ()

                # Solution
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = ()

                # Explored
                elif solution is not None and show_explored and (i, j) in self.explored:
                    fill = ()

                # Empty cell
                else:
                    fill = ()

                draw.rectangle(
                    (
                        [
                            (j * cell_size + cell_border, i * cell_size + cell_border),
                            (
                                (j + 1) * cell_size - cell_border,
                                (i + 1) * cell_size - cell_border,
                            ),
                        ]
                    ),
                    fill=fill,
                )

        img.save(filename)


if len(sys.argv) != 2:
    sys.exit()


class Maze:
    pass


m = Maze(sys.argv[1])
print("Graph:")
m.print()
print("Solving...")
m.solve()
print("States Explored:", m.num_explored)
print("Solution:")
m.print()
m.output_image("graph.png", show_explored=True)
