import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull

# Generate random points in 3D
np.random.seed(4) # 2
points = np.random.rand(20, 3)

# Compute the convex hull
hull = ConvexHull(points)

# Plot the convex hull with blue lines and remove the inner points
fig = plt.figure(figsize=(20, 8)) 
ax = fig.add_subplot(111, projection='3d')

# Plot only the points on the hull
hull_points = points[hull.vertices]
ax.scatter(hull_points[:,0], hull_points[:,1], hull_points[:,2], s=50)

# Plot the convex hull with blue lines
for simplex in hull.simplices:
    simplex = np.append(simplex, simplex[0])  # Cycle back to the first point
    ax.plot(points[simplex, 0], points[simplex, 1], points[simplex, 2], "b-")

# Set plot details
# ax.set_title('3D Convex Hull')
ax.grid(False)
ax.axis('off')

# Show the plot
# plt.show()

import tikzplotlib

tikzplotlib.save("convex_hull.tex")

