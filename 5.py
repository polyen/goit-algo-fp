import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def color_interpolation(start_color, end_color, steps):
    if steps == 0:
        return [start_color, end_color]
    start_r = int(start_color[1:3], 16)
    start_g = int(start_color[3:5], 16)
    start_b = int(start_color[5:7], 16)
    end_r = int(end_color[1:3], 16)
    end_g = int(end_color[3:5], 16)
    end_b = int(end_color[5:7], 16)

    step_r = (end_r - start_r) / steps
    step_g = (end_g - start_g) / steps
    step_b = (end_b - start_b) / steps

    colors = []
    for i in range(steps):
        r = int(start_r + step_r * i)
        g = int(start_g + step_g * i)
        b = int(start_b + step_b * i)
        colors.append(f'#{r:02X}{g:02X}{b:02X}')

    return colors


def draw_dfs(root, colors):
    queue = [root]
    i = 0
    while queue:
        node = queue.pop()
        node.color = colors[i]

        if node.right:
            queue.extend([node.right])
        if node.left:
            queue.extend([node.left])

        i += 1

    draw_tree(root)


def draw_bfs(root, colors):
    queue = deque([root])
    i = 0
    while queue:
        node = queue.popleft()
        node.color = colors[i]

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

        i += 1
    draw_tree(root)


def get_tree_height(root):
    if root is None:
        return 0
    else:
        left_height = get_tree_height(root.left)
        right_height = get_tree_height(root.right)

        return max(left_height, right_height) + 1


if __name__ == "__main__":
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    num_nodes = 2 ** get_tree_height(root) - 1
    start_color = "#1296F0"  # Темно-синій
    end_color = "#ADD8E6"  # Світло-блакитний
    colors = color_interpolation(start_color, end_color, num_nodes)

    draw_dfs(root, colors)
    draw_bfs(root, colors)
