# Problem: https://www.hackerrank.com/challenges/bfsshortreach
# Solved by: Edgardo (Elijah) Gutierrez
# Date: 2/23/17

from __future__ import print_function

def main():
    # Loop through all queries.
    for _ in range(int(raw_input())):
        # Get the amount of nodes and edges.
        nm = [int(x) for x in raw_input().split(" ")]

        # General initializations.
        nodes, visited, queue, current = [], [], [], None

        # Initialize all nodes.
        for i in range(nm[0]):
            nodes.append(Node(i + 1))

        # Loop through all edges.
        for _ in range(nm[1]):
            # Get connected nodes
            edge = [int(x) for x in raw_input().split(" ")]

            # Add each node to eachothers edges.
            nodes[edge[0] - 1].edges.append(nodes[edge[1] - 1])
            nodes[edge[1] - 1].edges.append(nodes[edge[0] - 1])

        # Get start node identity.
        start = int(raw_input())
        nodes[start - 1].value = 0
        queue.append(start)
        visited.append(start)

        # Navigate the graph, starting at the start node, branching out.
        while len(queue) != 0:

            # Get the next node in the queue.
            current = queue.pop(0)

            # Go through all the connecting edges of the current node.
            for node in nodes[current - 1].edges:

                # Not including already visited nodes.
                if (node.id not in visited):

                    # Add cost to get to this node
                    node.value = nodes[current - 1].value + 6

                    # Add this node to the queue for branching.
                    queue.append(node.id)

                    # This node is now visited.
                    visited.append(node.id)

        # Print total edge costs to each node other than the starting node.
        for node in nodes:
            if (node.id != nodes[start - 1].id):
                print((str(node.value) + " "), end='')
        print()

# Node class, with attributes to enable graph structure.
class Node:
    def __init__(self, identifiction):
        self.id = identifiction
        self.value = -1
        self.edges = []
    def __repr__(self):
        return str(self.id)

if __name__ == "__main__":
    main()
