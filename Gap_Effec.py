import matplotlib.pyplot as plt
from numpy.random import random
import numpy as np

size = 60

# ---------------------------------------------------------------------------------------------------------------------------------
#  Carbon-1 collections
# ---------------------------------------------------------------------------------------------------------------------------------
Carbon1_x_1 = np.array([-0.254, -0.466])
Carbon1_y_1 = np.array([0.540, 0.540])
Carbon1_x_2 = np.array([0.387, 1.852])
Carbon1_y_2 = np.array([0.540, 0.540])
Carbon1_1 = plt.scatter(Carbon1_x_1, Carbon1_y_1, marker='o', s=size, color='black', label='Carbon-1')
Carbon1_2 = plt.scatter(Carbon1_x_2, Carbon1_y_2, marker='o', s=size, color='white', edgecolors='black', label='Cabon-1')

C1PA_x_1 = np.array([-0.176, -2.911])
C1PA_y_1 = np.array([0.363, 0.363])
C1PA_x_2 = np.array([0.676])
C1PA_y_2 = np.array([0.363])
C1PA_1 = plt.scatter(C1PA_x_1, C1PA_y_1, marker='o', s=size, color='crimson', label='C1-Porous-A')
C1PA_2 = plt.scatter(C1PA_x_2, C1PA_y_2, marker='o', s=size, color='white', edgecolors='crimson', label='C1-Porous-A')

C1PG_x_1 = np.array([-0.410, -0.431])
C1PG_y_1 = np.array([2.186, 2.186])
C1PG_x_2 = np.array([0.676])
C1PG_y_2 = np.array([2.186])
C1PG_1 = plt.scatter(C1PG_x_1, C1PG_y_1, marker='o', s=size, color='dodgerblue', label='C1-Porous-G')
C1PG_2 = plt.scatter(C1PG_x_2, C1PG_y_2, marker='o', s=size, color='white', edgecolors='dodgerblue', label='C1-Porous-G')

# ---------------------------------------------------------------------------------------------------------------------------------
#  Carbon-2 collections
# ---------------------------------------------------------------------------------------------------------------------------------

# CARBON-2 is metalic

Carbon2_x_1 = np.array([])
Carbon2_y_1 = np.array([])
Carbon2_x_2 = np.array([])
Carbon2_y_2 = np.array([])
Carbon2_1 = plt.scatter(Carbon2_x_1, Carbon2_y_1, marker='s', s=size, color='black', label='Carbon-2')
Carbon2_2 = plt.scatter(Carbon2_x_2, Carbon2_y_2, marker='s', s=size, color='white', edgecolors='black', label='Cabon-2')

C2PA_x_1 = np.array([-0.456, -0.383])
C2PA_y_1 = np.array([0.017, 0.017])
C2PA_x_2 = np.array([0.407, 0.259])
C2PA_y_2 = np.array([0.017, 0.017])
C2PA_1 = plt.scatter(C2PA_x_1, C2PA_y_1, marker='s', s=size, color='crimson', label='C2-Porous-A')
C2PA_2 = plt.scatter(C2PA_x_2, C2PA_y_2, marker='s', s=size, color='white', edgecolors='crimson', label='C2-Porous-A')

C2PG_x_1 = np.array([-0.824, -4.965])
C2PG_y_1 = np.array([0.382, 0.382])
C2PG_x_2 = np.array([0.692, 4.348])
C2PG_y_2 = np.array([0.382, 0.382])
C2PG_1 = plt.scatter(C2PG_x_1, C2PG_y_1, marker='s', s=size, color='dodgerblue', label='C2-Porous-G')
C2PG_2 = plt.scatter(C2PG_x_2, C2PG_y_2, marker='s', s=size, color='white', edgecolors='dodgerblue', label='C2-Porous-G')

# ---------------------------------------------------------------------------------------------------------------------------------
#  Carbon-3 collections
# ---------------------------------------------------------------------------------------------------------------------------------

Carbon3_x_1 = np.array([-0.544, -1.237])
Carbon3_y_1 = np.array([0.837, 0.837])
Carbon3_x_2 = np.array([1.351])
Carbon3_y_2 = np.array([0.837])
Carbon3_1 = plt.scatter(Carbon3_x_1, Carbon3_y_1, marker='d', s=size, color='black', label='Carbon-3')
Carbon3_2 = plt.scatter(Carbon3_x_2, Carbon3_y_2, marker='d', s=size, color='white', edgecolors='black', label='Cabon-3')

C3PA_x_1 = np.array([-0.290, -0.518])
C3PA_y_1 = np.array([0.122, 0.122])
C3PA_x_2 = np.array([0.449, 0.428])
C3PA_y_2 = np.array([0.122, 0.122])
C3PA_1 = plt.scatter(C3PA_x_1, C3PA_y_1, marker='d', s=size, color='crimson', label='C3-Porous-A')
C3PA_2 = plt.scatter(C3PA_x_2, C3PA_y_2, marker='d', s=size, color='white', edgecolors='crimson', label='C3-Porous-A')

C3PG_x_1 = np.array([-0.777, -1.232])
C3PG_y_1 = np.array([1.727, 1.727])
C3PG_x_2 = np.array([0.566, 0.843])
C3PG_y_2 = np.array([1.727, 1.727])
C3PG_1 = plt.scatter(C3PG_x_1, C3PG_y_1, marker='d', s=size, color='dodgerblue', label='C3-Porous-G')
C3PG_2 = plt.scatter(C3PG_x_2, C3PG_y_2, marker='d', s=size, color='white', edgecolors='dodgerblue', label='C3-Porous-G')

# ---------------------------------------------------------------------------------------------------------------------------------
#  Carbon-4 collections
# ---------------------------------------------------------------------------------------------------------------------------------

Carbon4_x_1 = np.array([-0.824, -4.965])
Carbon4_y_1 = np.array([0.382, 0.382])
Carbon4_x_2 = np.array([0.692, 4.348])
Carbon4_y_2 = np.array([0.382, 0.382])
Carbon4_1 = plt.scatter(Carbon4_x_1, Carbon4_y_1, marker='*', s=size, color='black', label='Carbon-4')
Carbon4_2 = plt.scatter(Carbon4_x_2, Carbon4_y_2, marker='*', s=size, color='white', edgecolors='black', label='Cabon-4')

C4PA_x_1 = np.array([-0.505])
C4PA_y_1 = np.array([0.254])
C4PA_x_2 = np.array([0.532, 2.891])
C4PA_y_2 = np.array([0.254, 0.254])
C4PA_1 = plt.scatter(C4PA_x_1, C4PA_y_1, marker='*', s=size, color='crimson', label='C4-Porous-A')
C4PA_2 = plt.scatter(C4PA_x_2, C4PA_y_2, marker='*', s=size, color='white', edgecolors='crimson', label='C4-Porous-A')

C4PG_x_1 = np.array([-35.662])
C4PG_y_1 = np.array([3.181])
C4PG_x_2 = np.array([7.762, 1.151])
C4PG_y_2 = np.array([3.181, 3.181])
C4PG_1 = plt.scatter(C4PG_x_1, C4PG_y_1, marker='*', s=size, color='dodgerblue', label='C4-Porous-G')
C4PG_2 = plt.scatter(C4PG_x_2, C4PG_y_2, marker='*', s=size, color='white', edgecolors='dodgerblue', label='C4-Porous-G')


# ---------------------------------------------------------------------------------------------------------------------------------
#  Carbon-5 collections
# ---------------------------------------------------------------------------------------------------------------------------------

# CARBON-5 is metalic

Carbon5_x_1 = np.array([])
Carbon5_y_1 = np.array([])
Carbon5_x_2 = np.array([])
Carbon5_y_2 = np.array([])
Carbon5_1 = plt.scatter(Carbon5_x_1, Carbon5_y_1, marker='P', s=size, color='black', label='Carbon-5')
Carbon5_2 = plt.scatter(Carbon5_x_2, Carbon5_y_2, marker='P', s=size, color='white', edgecolors='black', label='Cabon-5')

C5PA_x_1 = np.array([-0.655, -1.036])
C5PA_y_1 = np.array([0.129, 0.129])
C5PA_x_2 = np.array([0.179, 0.312])
C5PA_y_2 = np.array([0.129, 0.129])
C5PA_1 = plt.scatter(C5PA_x_1, C5PA_y_1, marker='P', s=size, color='crimson', label='C5-Porous-A')
C5PA_2 = plt.scatter(C5PA_x_2, C5PA_y_2, marker='P', s=size, color='white', edgecolors='crimson', label='C5-Porous-A')

C5PG_x_1 = np.array([-0.14, -0.505])
C5PG_y_1 = np.array([0.256, 0.256])
C5PG_x_2 = np.array([0.136, 0.497])
C5PG_y_2 = np.array([0.256, 0.256])
C5PG_1 = plt.scatter(C5PG_x_1, C5PG_y_1, marker='P', s=size, color='dodgerblue', label='C5-Porous-G')
C5PG_2 = plt.scatter(C5PG_x_2, C5PG_y_2, marker='P', s=size, color='white', edgecolors='dodgerblue', label='C5-Porous-G')

# ---------------------------------------------------------------------------------------------------------------------------------
#  Carbon-6 collections
# ---------------------------------------------------------------------------------------------------------------------------------

Carbon6_x_1 = np.array([-0.158, -0.223])
Carbon6_y_1 = np.array([0.058, 0.058])
Carbon6_x_2 = np.array([0.418, 1.798])
Carbon6_y_2 = np.array([0.058, 0.058])
Carbon6_1 = plt.scatter(Carbon6_x_1, Carbon6_y_1, marker='v', s=size, color='black', label='Carbon-6')
Carbon6_2 = plt.scatter(Carbon6_x_2, Carbon6_y_2, marker='v', s=size, color='white', edgecolors='black', label='Cabon-6')

C6PA_x_1 = np.array([-0.124, -0.217])
C6PA_y_1 = np.array([0.063, 0.063])
C6PA_x_2 = np.array([0.263, 0.419])
C6PA_y_2 = np.array([0.063, 0.063])
C6PA_1 = plt.scatter(C6PA_x_1, C6PA_y_1, marker='v', s=size, color='crimson', label='C6-Porous-A')
C6PA_2 = plt.scatter(C6PA_x_2, C6PA_y_2, marker='v', s=size, color='white', edgecolors='crimson', label='C6-Porous-A')

C6PG_x_1 = np.array([-0.139, -0.472])
C6PG_y_1 = np.array([0.121, 0.121])
C6PG_x_2 = np.array([0.146, 0.482])
C6PG_y_2 = np.array([0.121, 0.121])
C6PG_1 = plt.scatter(C6PG_x_1, C6PG_y_1, marker='v', s=size, color='dodgerblue', label='C6-Porous-G')
C6PG_2 = plt.scatter(C6PG_x_2, C6PG_y_2, marker='v', s=size, color='white', edgecolors='dodgerblue', label='C6-Porous-G')

# ---------------------------------------------------------------------------------------------------------------------------------
#  Carbon-7 collections
# ---------------------------------------------------------------------------------------------------------------------------------

Carbon7_x_1 = np.array([-0.165, -0.25])
Carbon7_y_1 = np.array([0.016, 0.016])
Carbon7_x_2 = np.array([0.291, 0.32])
Carbon7_y_2 = np.array([0.016, 0.016])
Carbon7_1 = plt.scatter(Carbon7_x_1, Carbon7_y_1, marker='^', s=size, color='black', label='Carbon-7')
Carbon7_2 = plt.scatter(Carbon7_x_2, Carbon7_y_2, marker='^', s=size, color='white', edgecolors='black', label='Cabon-7')

C7PA_x_1 = np.array([-0.169, -0.383])
C7PA_y_1 = np.array([0.018, 0.018])
C7PA_x_2 = np.array([0.194, 0.223])
C7PA_y_2 = np.array([0.018, 0.018])
C7PA_1 = plt.scatter(C7PA_x_1, C7PA_y_1, marker='^', s=size, color='crimson', label='C7-Porous-A')
C7PA_2 = plt.scatter(C7PA_x_2, C7PA_y_2, marker='^', s=size, color='white', edgecolors='crimson', label='C7-Porous-A')

C7PG_x_1 = np.array([-0.194, -0.424])
C7PG_y_1 = np.array([0.097, 0.097])
C7PG_x_2 = np.array([0.199, 0.422])
C7PG_y_2 = np.array([0.097, 0.097])
C7PG_1 = plt.scatter(C7PG_x_1, C7PG_y_1, marker='^', s=size, color='dodgerblue', label='C6-Porous-7')
C7PG_2 = plt.scatter(C7PG_x_2, C7PG_y_2, marker='^', s=size, color='white', edgecolors='dodgerblue', label='C6-Porous-7')


plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08),
          fancybox=True, shadow=True, ncol=7, prop={'size': 8})

plt.grid(color='black', linestyle='--', linewidth=0.5)
plt.xlim(-6, 6)
plt.xticks(np.arange(-6, 6))
plt.ylim(-2, 4)
plt.yticks(np.arange(-2, 4, 0.5))
plt.xlabel('Effective mass of holes and electrons', fontsize=12)
plt.ylabel('Band gap (eV)', fontsize=12)


plt.show()