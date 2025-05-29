import numpy as np
import matplotlib.pyplot as plt

# Constants
k = 1902  # N/m
h = 6.626e-34  # Planck's constant (Js)
mu = 1.0e-30   # Example value for reduced mass (kg)
v = np.array([1, 2, 3, 4, 5, 6])  # Quantum numbers as an array


# Range of r values
r = np.linspace(-10, 10, 500)  # From -10 to 10

# Calculate E
E = 0.5 * k * r**2



# Plot the graph
plt.figure(figsize=(8, 6))
plt.plot(r, E, label=r'$E = \frac{1}{2} k r^2$', color='b')
plt.xlabel('r (m)')
plt.ylabel('E (J)')
plt.title('Graph of E vs r')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show()
