import sys
input = sys.stdin.readline

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # 각 노드의 자식 노드들을 저장하는 리스트

class Tree:
    def __init__(self):
        self.nodes = {}  # 각 노드의 값을 키로 가지는 딕셔너리

    def add_edge(self, parent_value, child_value, distance):
        if parent_value not in self.nodes:
            self.nodes[parent_value] = TreeNode(parent_value)
        if child_value not in self.nodes:
            self.nodes[child_value] = TreeNode(child_value)

        parent_node = self.nodes[parent_value]
        child_node = self.nodes[child_value]
        parent_node.children.append((child_node, distance))
        child_node.children.append((parent_node, distance))

    def dfs_iterative(self, start_node, visited):
        stack = [(start_node, 0)]  # 스택에 시작 노드와 거리 0을 추가
        max_distance_node = [None, 0]  # [노드, 거리]

        while stack:
            current_node, current_distance = stack.pop()
            visited[current_node.value] = True

            if current_distance > max_distance_node[1]:
                max_distance_node[0] = current_node
                max_distance_node[1] = current_distance

            for child, distance in current_node.children:
                if not visited[child.value]:
                    stack.append((child, current_distance + distance))

        return max_distance_node

    def get_diameter(self):
        start_node = list(self.nodes.values())[0]

        # DFS_1: 임의의 노드에서 가장 먼 노드를 찾음
        visited1 = {node_value: False for node_value in self.nodes}
        max_distance_node1 = self.dfs_iterative(start_node, visited1)

        # DFS_2: 첫 번째 DFS에서 찾은 노드에서 가장 먼 노드를 찾음
        visited2 = {node_value: False for node_value in self.nodes}
        max_distance_node2 = self.dfs_iterative(max_distance_node1[0], visited2)

        return max_distance_node2[1]

tree = Tree()
n = int(input())

for _ in range(n-1):
    u, v, w = map(int, input().split())
    tree.add_edge(u, v, w)

print(tree.get_diameter())
