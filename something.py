import numpy as np
import matplotlib.pyplot as plt
import random

def generate_random_segments(num_segments):
    segments = []
    for _ in range(num_segments):
        x1, y1, x2, y2 = random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)
        segments.append([x1, y1, x2, y2])
    return segments

def parse_segments(segments):
    for segment in segments:
        x1, y1, x2, y2 = segment
        plt.plot([x1, x2], [y1, y2])

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Segments Plot')
plt.grid(True)


segments = generate_random_segments(100000)
parse_segments(segments)

plt.show()