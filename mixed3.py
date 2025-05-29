import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import pandas as pd

# Define constants
mu = 1.0  # Reduced mass (assumed value)
omega = 1.0  # Angular frequency (assumed value)
hbar = 1.0  # Planck's reduced constant (assumed value)

alpha = (mu * omega) / hbar  # Calculate alpha using the given formula
y = np.linspace(-4, 4, 200)  # Generate 200 values for y

# Function to compute normalized vibrational wavefunctions
def psi_n(n, y, alpha):
    normalization = (alpha / np.pi) ** 0.25 / np.sqrt(2**n * np.math.factorial(n))
    hermite_poly = sp.hermite(n)(y)
    wavefunction = normalization * hermite_poly * np.exp(-y**2 / 2)
    return wavefunction

# Function to compute probability density (square of wavefunction)
def psi_n_squared(n, y, alpha):
    return psi_n(n, y, alpha) ** 2

# Harmonic oscillator potential function
def V(y):
    return 0.5 * y**2

# Compute wavefunctions for n = 0, 1, 2, 3
n_values = [0, 1, 2, 3]
colors = ['r', 'b', 'g', 'purple']

# Create table to store values
data = []
for i, y_val in enumerate(y):
    row = [i+1, y_val]  # Serial number and y value
    for n in n_values:
        row.append(psi_n_squared(n, y_val, alpha))
    data.append(row)

columns = ["Serial No", "y"] + [f"psi_{n}^2(y)" for n in n_values]
df = pd.DataFrame(data, columns=columns)

# Adjust Pandas display settings for compact output
pd.set_option("display.max_rows", None)  # Show all rows
pd.set_option("display.max_columns", None)  # Show all columns
pd.set_option("display.width", 1000)  # Increase width of display
pd.set_option("display.float_format", "{:.6f}".format)  # Format float numbers for better readability

print(df)

# Create figure
fig, ax = plt.subplots(figsize=(8, 10))  # Increased figure size

# Plot potential well
ax.plot(y, V(y), color='black', linestyle='--', label='Potential V(y)')

# Overlay squared wavefunctions shifted by energy levels
for i, (n, color) in enumerate(zip(n_values, colors)):
    psi_n_y_squared = psi_n_squared(n, y, alpha) * 1.5  # Scale wavefunctions to make them appear bigger
    energy_level = n + 0.5  # Energy levels E_n = (n + 1/2)ħω
    ax.plot(y, psi_n_y_squared + energy_level, color=color, label=f'$|\psi_{n}(y)|^2$')
    ax.axhline(energy_level, color=color, linestyle=':', linewidth=0.8)

# Labels and aesthetics
ax.set_xlabel(r'$y = \sqrt{\alpha}r$', fontsize=14)
ax.set_ylabel('Energy Levels and Probability Densities', fontsize=14)
ax.legend(fontsize=12)
ax.grid(True)

plt.show()
