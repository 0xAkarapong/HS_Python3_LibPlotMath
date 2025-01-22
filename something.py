import numpy as np
import matplotlib.pyplot as plt

def parse_segments(segments):
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Segments Plot')
    plt.grid(True)
    for segment in segments:
        x1, y1, x2, y2 = segment
        plt.plot([x1, x2], [y1, y2])

segments = [[1, 1, 2, 3], [0, 1, 4, 4], [-1, -1, 3, 2]]
parse_segments(segments)

plt.show()