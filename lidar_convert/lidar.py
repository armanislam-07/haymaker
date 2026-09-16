import laspy
import numpy as np
import matplotlib.pyplot as plt

las = laspy.read("USGS_LPC_KS_25_COUNTIES_LiDAR_LAS_14SNG4045.laz")

n = len(las.x)

max_points = 500_000

if n > max_points:
    indices = np.random.choice(n, max_points, replace=False)
else:
    indices = np.arange(n)

x = np.asarray(las.x)[indices]
y = np.asarray(las.y)[indices]
z = np.asarray(las.z)[indices]

plt.figure(figsize=(12, 10))
plt.scatter(x, y, c=z, s=0.2, cmap="terrain")
plt.axis("equal")
plt.colorbar(label="Elevation")
plt.show()


def lidar_3d_2d(timestamp):
    # 3d - 2d to feed the general area theamear /ml should be looking at to see what is different
    # mask 
    #las.points[mask] then see 
    #dom returns the ponts that change so look to that regioin we can take from eithe the 1 or nth scan

    get_image(timestamp)

    return objectDetection() # transfers to the object detection 


def get_image(timestemp_):
    return False

def objectDetection():
    return False