import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import pandas as pd

# Define constants
mu = 1.0  # Reduced mass (assumed value)
omega = 1.0  # Angular frequency (assumed value)
hbar = 1.0  # Planck's reduced constant (assumed value)

alpha = (mu * omega) / hbar  # Calculate alpha using the given formula
y = np.linspace(-4, 4, 500)  # Generate 50 values for y

# Function to compute normalized vibrational wavefunctions
def psi_n(n, y, alpha):
    normalization = (alpha / np.pi) ** 0.25 / np.sqrt(2**n * np.math.factorial(n))
    hermite_poly = sp.hermite(n)(y)
    wavefunction = normalization * hermite_poly * np.exp(-y**2 / 2)
    return wavefunction

# Compute probability densities for n = 0, 1, 2, 3
n_values = [0, 1, 2, 3]
colors = ['r', 'b', 'g', 'purple']

data = {"y": y}

for n in n_values:
    psi_n_y = psi_n(n, y, alpha)
    P_r = np.abs(psi_n_y) ** 2  # Probability density
    data[f"P_r_n{n}"] = P_r

# Create DataFrame and display table
df = pd.DataFrame(data)
print(df.to_string(index=False))

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()

for i, (n, color) in enumerate(zip(n_values, colors)):
    psi_n_y = psi_n(n, y, alpha)
    P_r = np.abs(psi_n_y) ** 2  # Probability density
    
    axes[i].plot(y, P_r, color=color)
    axes[i].set_xlabel(r'$\sqrt{\alpha}r$', fontsize=12)
    axes[i].set_ylabel(r'$P(r) = |\psi_n(r)|^2$', fontsize=12)
    axes[i].set_title(f'Probability Density for n={n}', fontsize=14)
    axes[i].grid(True)

# Adjust layout for better readability
plt.tight_layout()
plt.show()
