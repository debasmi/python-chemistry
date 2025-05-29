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

# Compute wavefunctions for n = 0, 1, 2, 3
n_values = [0, 1, 2, 3]
colors = ['r', 'b', 'g', 'purple']

# Create table to store values
data = []
for i, y_val in enumerate(y):
    row = [i+1, y_val]  # Serial number and y value
    for n in n_values:
        row.append(psi_n(n, y_val, alpha))
    data.append(row)

columns = ["Serial No", "y"] + [f"psi_{n}(y)" for n in n_values]
df = pd.DataFrame(data, columns=columns)

# Adjust Pandas display settings for compact output
pd.set_option("display.max_rows", None)  # Show all rows
pd.set_option("display.max_columns", None)  # Show all columns
pd.set_option("display.width", 1000)  # Increase width of display
pd.set_option("display.float_format", "{:.6f}".format)  # Format float numbers for better readability

print(df)

# Create subplots for psi_n(y)
fig, axes = plt.subplots(4, 1, figsize=(6, 10), sharex=True)

for i, (n, color) in enumerate(zip(n_values, colors)):
    psi_n_y = psi_n(n, y, alpha)
    axes[i].plot(y, psi_n_y, color=color)  # Ensure different colors are applied
    axes[i].set_ylabel(f'$\\psi_{n}(y)$', fontsize=12, rotation=0, labelpad=15)
    axes[i].grid(True)
    axes[i].axhline(0, color='black', linewidth=0.5)
    axes[i].axvline(0, color='black', linewidth=0.5)
    axes[i].set_yticks([])

axes[-1].set_xlabel(r'$y = \sqrt{\alpha}r$', fontsize=12)
plt.tight_layout()
plt.show()
