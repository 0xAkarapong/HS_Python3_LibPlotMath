import numpy as np
import matplotlib.pyplot as plt
import time

def generate_random_segments(num_segments):
    segments = np.random.randint(0, 11, (num_segments, 4))
    return segments

def filter_segments_loop(segments, region):
    xmin, ymin, xmax, ymax = region
    filtered_segments = []
    for segment in segments:
        x1, y1, x2, y2 = segment
        if (xmin <= x1 <= xmax and ymin <= y1 <= ymax and
                xmin <= x2 <= xmax and ymin <= y2 <= ymax):
            filtered_segments.append(segment)
    return filtered_segments

def filter_segments_numpy(segments, region):
    xmin, ymin, xmax, ymax = region
    segments_np = np.array(segments)
    x1 = segments_np[:, 0]
    y1 = segments_np[:, 1]
    x2 = segments_np[:, 2]
    y2 = segments_np[:, 3]

    mask = (
            (x1 >= xmin) & (x1 <= xmax) &
            (y1 >= ymin) & (y1 <= ymax) &
            (x2 >= xmin) & (x2 <= xmax) &
            (y2 >= ymin) & (y2 <= ymax)
    )
    filtered_segments_np = segments_np[mask]
    return filtered_segments_np.tolist()

def plot_segments(segments):
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Segments Plot')
    plt.grid(True)
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.gca().set_aspect('equal', adjustable='box')
    x_coords = np.array(segments)[:, [0, 2]].T
    y_coords = np.array(segments)[:, [1, 3]].T
    plt.plot(x_coords, y_coords, linewidth=0.5)

segments = generate_random_segments(1000000)
region_of_interest = [0, 1, 4, 4]
t1 = time.time()
filtered_segments = filter_segments_numpy(segments, region_of_interest)
plot_segments(filtered_segments)
t2 = time.time()
plt.show()
print(f"Time taken: {t2-t1} seconds")