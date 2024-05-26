import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


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


def draw_tree(list):
    tree_root = create_tree(list)

    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def create_tree(priority_heap):
    def insert_node(arr, node, i, n):
        if i < n:
            node = Node(arr[i])
            node.left = insert_node(arr, node.left, 2 * i + 1, n)
            node.right = insert_node(arr, node.right, 2 * i + 2, n)

        return node

    n = len(priority_heap)
    root = insert_node(priority_heap, None, 0, n)
    return root


def test_create_tree():
    # Test case 1
    list1 = [3, 7, 2, 89, 5, 34, 13, 7, 9, 5, 90, 12]
    heapq.heapify(list1)
    tree1 = create_tree(list1)
    assert tree1.val == 2
    assert tree1.left.val == 5
    assert tree1.right.val == 3

    # Test case 2
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    heapq.heapify(list2)
    tree2 = create_tree(list2)
    assert tree2.val == 1
    assert tree2.left.val == 2
    assert tree2.right.val == 3


def test_draw_tree():
    # Test case 1
    list1 = [3, 7, 2, 89, 5, 34, 13, 7, 9, 5, 90, 12]
    draw_tree(list1)  # This should display a tree with 2 as the root

    # Test case 2
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    draw_tree(list2)  # This should display a tree with 1 as the root


if __name__ == "__main__":
    test_create_tree()
    test_draw_tree()
