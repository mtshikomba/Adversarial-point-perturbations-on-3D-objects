import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from projection import project_point_to_triangle

tri = np.array([[0, 0, 0], [0, 1, 0], [1, 1, 0]])
p = np.array([0.1, 0.1, 0])
p_perturb = np.array([1.5, 1.5, 0.5])

p_proj = project_point_to_triangle(p, p_perturb, tri)

plt.figure(figsize = (15, 15))
plt.subplot(111, projection = "3d")
plt.gca().scatter(*np.vstack((p, p_perturb, p_proj)).T, s = 500, depthshade = False, c = ['b', 'r', 'g'])
plt.gca().plot_trisurf(*tri.T, triangles = ((0, 1, 2)))
plt.show()