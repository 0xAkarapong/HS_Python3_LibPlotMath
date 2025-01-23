import numpy as np
import matplotlib.pyplot as plt
import time

def generate_random_segments(num_segments):
    segments = np.random.randint(0, 11, (num_segments, 4))
    return segments

def plot_segments(segments):
    x = segments[:, [0, 2]].T
    y = segments[:, [1, 3]].T
    plt.plot(x, y)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Segments Plot')
plt.grid(True)

segments = generate_random_segments(100000)
t1 = time.time()
plot_segments(segments)
t2 = time.time()
plt.show()
print(f"Time taken: {t2-t1} seconds")