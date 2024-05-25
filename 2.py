import matplotlib.pyplot as plt
import numpy as np


def draw_tree(ax, x, y, size, angle, depth):
    if depth == 0:
        return

    x1 = x + size * np.cos(angle)
    y1 = y + size * np.sin(angle)

    ax.plot([x, x1], [y, y1], 'b')

    new_size = size * np.sqrt(2) / 2
    left_angle = angle + np.pi / 4
    right_angle = angle - np.pi / 4

    draw_tree(ax, x1, y1, new_size, left_angle, depth - 1)
    draw_tree(ax, x1, y1, new_size, right_angle, depth - 1)


if __name__ == "__main__":
    depth = int(input('Enter the depth of tree'))

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    initial_x = 0
    initial_y = 0
    initial_size = 100
    initial_angle = np.pi / 2

    draw_tree(ax, initial_x, initial_y, initial_size, initial_angle, depth)

    plt.show()
