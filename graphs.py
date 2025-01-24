import numpy as np
import matplotlib.pyplot as plt

# Define points
W = np.array([0, 0])       # Westborough
A = np.array([30, 10])     # Agri Town
E = np.array([20, 0])      # Eastborough

# Calculate the slope of WA and the perpendicular slope
slope_WA = (A[1] - W[1]) / (A[0] - W[0])  # Slope of WA
slope_perpendicular = -1 / slope_WA        # Slope of the perpendicular road

# Equation of line WA: y - y1 = m(x - x1)
# Equation of perpendicular line from E with slope_perpendicular
# Let's solve for the intersection point (J) where these two lines meet

# Using the line equations:
# Line WA: y = slope_WA * x
# Perpendicular line through E: y = slope_perpendicular * (x - E[0])

# Solving for intersection:
x_j = (slope_perpendicular * E[0]) / (slope_perpendicular - slope_WA)
y_j = slope_WA * x_j

# Junction point J
J = np.array([x_j, y_j])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot([W[0], A[0]], [W[1], A[1]], 'b-', label="Road WA (Westborough to Agri Town)")
plt.plot([E[0], J[0]], [E[1], J[1]], 'g--', label="Road to Eastborough (Perpendicular)")
plt.scatter(*W, color='red', label="Westborough (W)")
plt.scatter(*A, color='blue', label="Agri Town (A)")
plt.scatter(*E, color='green', label="Eastborough (E)")
plt.scatter(*J, color='purple', label="Junction Point (J)")

# Label points
plt.text(W[0], W[1], ' W', verticalalignment='bottom', horizontalalignment='right', color='red')
plt.text(A[0], A[1], ' A', verticalalignment='bottom', horizontalalignment='right', color='blue')
plt.text(E[0], E[1], ' E', verticalalignment='bottom', horizontalalignment='right', color='green')
plt.text(J[0], J[1], ' J', verticalalignment='bottom', horizontalalignment='right', color='purple')

# Setting up the plot
plt.xlabel("Miles East")
plt.ylabel("Miles North")
plt.title("Roads from Westborough to Agri Town and Eastborough")
plt.legend()
plt.grid(True)
plt.show()