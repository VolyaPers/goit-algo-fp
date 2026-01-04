import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
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


def draw_tree(tree_root, title="Binary Heap"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def build_heap_tree(heap_array, index=0):
    if index >= len(heap_array):
        return None

    node = Node(heap_array[index])

    left_index = 2 * index + 1
    right_index = 2 * index + 2

    node.left = build_heap_tree(heap_array, left_index)
    node.right = build_heap_tree(heap_array, right_index)

    return node


def visualize_heap(heap_array, title="Binary Heap"):
    if not heap_array:
        print("Купа порожня")
        return

    root = build_heap_tree(heap_array)
    draw_tree(root, title)


if __name__ == "__main__":
    data = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    print(f"Вхідні дані: {data}")

    min_heap = data.copy()
    heapq.heapify(min_heap)
    print(f"Min-купа (масив): {min_heap}")
    visualize_heap(min_heap, "Min-Heap (Мінімальна купа)")

    max_heap = [-x for x in data]
    heapq.heapify(max_heap)
    max_heap_display = [-x for x in max_heap]
    print(f"Max-купа (масив): {max_heap_display}")
    visualize_heap(max_heap_display, "Max-Heap (Максимальна купа)")

    print("\nВластивості купи:")
    print("- Min-heap: батько ≤ дітей")
    print("- Max-heap: батько ≥ дітей")
    print("- Індекс лівої дитини: 2*i + 1")
    print("- Індекс правої дитини: 2*i + 2")
