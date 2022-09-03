from src.Solution import Solution
from ..Solution import Solution

from queue import PriorityQueue

class Node:
    
    def __init__(self, position, cost, path):
        self.position = position
        self.cost = cost
        self.path = path
    
    def __lt__(self, other):
        return self.cost < other.cost


class P4(Solution):

    @staticmethod
    def get_arguments(args):
        start_position = eval(args[0])
        end_position = eval(args[1])
        return [start_position, end_position]

    @staticmethod
    def solve(start: tuple, end: tuple):
        def get_edges(node):
            types = [(1, 2), (2, 1)]
            positions_offset = [(y*i1, x*i2) for x, y in types for i1 in (-1, 1) for i2 in (-1, 1)]
            
            return [(offset[0] + node[0], offset[1] + node[1]) for offset in positions_offset]

        def distance(a, b):
            return (abs(a[0] - b[0]) + abs(a[1] - b[1])) / 3 #Knights travel 4 squares at a time

        queue = PriorityQueue()
        node = Node(start, 0, [start])
        
        #Queue has a tuple with (heuristic, Node)
        queue.put((0, node))
        visited = {}
        while node.position != end and not queue.empty():
            h, node = queue.get() #pop
            visited[node.position] = node
            edges = get_edges(node.position)
            for edge in edges:
                if not edge in visited or visited[edge].cost > node.cost + 1:
                    heuristic = node.cost + 1 + distance(edge, end)
                    new_path = node.path + [edge]
                    new_node = Node(edge, node.cost + 1, new_path)
                    queue.put((heuristic, new_node))
        return len(node.path)


        
        

    @staticmethod 
    def format_result(result): 
        return "{0}\n".format(result)

    
    
    
