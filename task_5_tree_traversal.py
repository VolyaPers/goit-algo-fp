import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="#000000"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def build_heap_tree(heap_array, index=0):
    if index >= len(heap_array):
        return None
    node = Node(heap_array[index])
    node.left = build_heap_tree(heap_array, 2 * index + 1)
    node.right = build_heap_tree(heap_array, 2 * index + 2)
    return node


def generate_colors(n, base_color=(18, 150, 240)):
    colors = []
    for i in range(n):
        ratio = i / (n - 1) if n > 1 else 0
        r = int(base_color[0] + (255 - base_color[0]) * ratio * 0.7)
        g = int(base_color[1] + (255 - base_color[1]) * ratio * 0.7)
        b = int(base_color[2] + (255 - base_color[2]) * ratio * 0.7)
        colors.append(f"#{r:02X}{g:02X}{b:02X}")
    return colors


def dfs_iterative(root):
    if not root:
        return []

    visited = []
    stack = [root]

    while stack:
        node = stack.pop()
        visited.append(node)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited


def bfs_iterative(root):
    if not root:
        return []

    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        visited.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title="Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    plt.title(title, fontsize=14, fontweight='bold')
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors, font_color='white', font_weight='bold')
    plt.show()


def visualize_traversal(root, traversal_func, title):
    visited_nodes = traversal_func(root)
    colors = generate_colors(len(visited_nodes))

    order_info = []
    for i, node in enumerate(visited_nodes):
        node.color = colors[i]
        order_info.append(f"{i+1}: {node.val}")

    print(f"\n{title}")
    print(f"Порядок обходу: {' -> '.join(order_info)}")

    draw_tree(root, title)


def reset_colors(root, color="#000000"):
    if root:
        root.color = color
        reset_colors(root.left, color)
        reset_colors(root.right, color)


if __name__ == "__main__":
    heap_data = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    root = build_heap_tree(heap_data)

    print("Структура дерева (min-heap):")
    print("        1")
    print("       / \\")
    print("      3   5")
    print("     / \\ / \\")
    print("    7  9 11 13")
    print("   / \\")
    print("  15 17")

    visualize_traversal(root, dfs_iterative, "DFS (обхід в глибину) - використовує СТЕК")

    reset_colors(root)

    visualize_traversal(root, bfs_iterative, "BFS (обхід в ширину) - використовує ЧЕРГУ")

    print("\n" + "=" * 50)
    print("Алгоритми:")
    print("-" * 50)
    print("DFS (стек): Йде вглиб, потім повертається")
    print("  - Додаємо вузол у стек")
    print("  - Виймаємо з кінця (LIFO)")
    print("  - Спочатку праву, потім ліву дитину в стек")
    print("-" * 50)
    print("BFS (черга): Обходить рівень за рівнем")
    print("  - Додаємо вузол у чергу")
    print("  - Виймаємо з початку (FIFO)")
    print("  - Додаємо ліву, потім праву дитину")
