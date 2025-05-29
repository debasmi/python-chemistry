import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Constants for the Morse potential
D_e = 1072  # Arbitrary dissociation energy (can be scaled later)
r_e = 1.5  # Equilibrium bond distance (in arbitrary units)
a = 0.8582089552  # Bond stiffness constant

# Define the range of r values
r = np.linspace(0.5, 10.0, 50)  # Internuclear separation

# Morse potential energy equation
E_r = D_e * (1 - np.exp(-a * (r - r_e)))**2

# Create a DataFrame to store values
df = pd.DataFrame({'Internuclear Separation (r)': r, 'Energy (E_r)': E_r})

# Print the table
print(df.head(500))  # Print the first few rows of the table

# Plot the Morse potential
plt.figure(figsize=(8, 6))
plt.plot(r, E_r, color='green', label="Morse Potential")
plt.axhline(0, color='black', linestyle='--', linewidth=0.7)  # Zero energy reference
plt.axvline(r_e, color='black', linestyle='--', linewidth=0.7, label="Equilibrium Distance $r_e$")
plt.title("Morse Potential Energy Curve", fontsize=14)
plt.xlabel("Internuclear Separation ($r$)", fontsize=12)
plt.ylabel("Energy ($E$)", fontsize=12)
plt.grid(alpha=0.4)
plt.legend(fontsize=10)
plt.show()
