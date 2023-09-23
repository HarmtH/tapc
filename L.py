#!/usr/bin/python3

import sys
import math

data = sys.stdin.readlines()
num_nodes, total_knippies = map(int, data[0].split(' '))
knippies = 0

class Node:
    def __init__(self, parent, children):
        self.parent = parent
        self.children = children

    def has_siblings(self, depth):
        node = self
        for _ in range(depth):
            if node is None:
                return False
            node = node.parent
        return node and len(node.children) >= 2

    def is_endnode(self):
        return len(self.children) == 0

    def kill_child(self, child):
        self.children.remove(child)

root = Node(None, [])
nodes = [root]

for parent in map(int, data[1:]):
    parent_node = nodes[parent]
    node = Node(parent_node, [])
    nodes.append(node)
    parent_node.children.append(node)

# print(nodes)
depth = 1
while True:
    if depth = 1000:
        return 'x'
    for i, node in enumerate(nodes):
        if node and node.is_endnode() and node.has_siblings(depth):
            knippies +=1
            node.parent.kill_child(node)
            nodes[i] = None
            if knippies == total_knippies:
                ans = 0
                for ansnode in nodes:
                    if ansnode and ansnode.is_endnode():
                        ans += 1
                print(ans)
                sys.exit(0)
            depth = 1
            break
    else:
        depth += 1

# print(nodes)
