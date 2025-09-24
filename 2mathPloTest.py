# =========================
# Import Libraries
# =========================
import numpy as np                      # NumPy for math and array operations
import matplotlib.pyplot as plt         # Matplotlib for plotting
from mpl_toolkits.mplot3d import Axes3D # Toolkit for 3D plotting in matplotlib


# =========================
# Create a Figure (canvas)
# =========================
fig = plt.figure(figsize=(12, 4))   # Create one figure with size 12x4 inches


# =========================
# Example 1: 3D Scatter Plot
# =========================
x = np.random.rand(100)  # Generate 100 random points for X
y = np.random.rand(100)  # Generate 100 random points for Y
z = np.random.rand(100)  # Generate 100 random points for Z

ax1 = fig.add_subplot(131, projection='3d')  # Add subplot 1 (1 row, 3 columns, position 1), with 3D projection
ax1.scatter(x, y, z, c='red', marker='o')    # Draw scatter points (red, round marker)
ax1.set_title("3D Scatter Plot")             # Title of subplot
ax1.set_xlabel("X axis")                     # Label for X axis
ax1.set_ylabel("Y axis")                     # Label for Y axis
ax1.set_zlabel("Z axis")                     # Label for Z axis


# =========================
# Example 2: 3D Line Plot
# =========================
t = np.linspace(0, 10, 100)  # Generate 100 values from 0 to 10
x = np.sin(t)                # X = sin(t)
y = np.cos(t)                # Y = cos(t)
z = t                        # Z = t (goes upward, creates spiral)

ax2 = fig.add_subplot(132, projection='3d')      # Add subplot 2 (position 2)
ax2.plot(x, y, z, label="3D Line", color="blue") # Draw 3D line in blue
ax2.set_title("3D Line Plot")                    # Title
ax2.set_xlabel("X axis")                         # Label for X axis
ax2.set_ylabel("Y axis")                         # Label for Y axis
ax2.set_zlabel("Z axis")                         # Label for Z axis
ax2.legend()                                     # Show legend (label name)


# =========================
# Example 3: 3D Surface Plot
# =========================
x = np.linspace(-5, 5, 50)  # Generate 50 points from -5 to 5 for X
y = np.linspace(-5, 5, 50)  # Generate 50 points from -5 to 5 for Y
X, Y = np.meshgrid(x, y)    # Create a grid of X and Y coordinates
Z = np.sin(np.sqrt(X**2 + Y**2))  # Calculate Z as a function of X and Y

ax3 = fig.add_subplot(133, projection='3d')        # Add subplot 3 (position 3)
surf = ax3.plot_surface(X, Y, Z, cmap='viridis')   # Draw 3D surface with colormap
ax3.set_title("3D Surface Plot")                   # Title
ax3.set_xlabel("X axis")                           # Label for X axis
ax3.set_ylabel("Y axis")                           # Label for Y axis
ax3.set_zlabel("Z axis")                           # Label for Z axis

fig.colorbar(surf, ax=ax3, shrink=0.5, aspect=10)  # Add color bar for surface plot


# =========================
# Show All Plots
# =========================
plt.tight_layout()  # Adjust layout to avoid overlap
plt.show()          # Display the figure
