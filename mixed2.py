import numpy as np
import matplotlib.pyplot as plt

# Define energy levels
n_levels = 6  # Number of energy levels to display
hbar = 1  # Reduced Planck's constant (scaled for simplicity)
omega = 3 # Angular frequency (scaled for simplicity)

# Calculate energy values
energy_levels = [(n + 0.5) * hbar * omega for n in range(n_levels)]

# Define position axis
x = np.linspace(-2, 2, 100)
V_x = (0.5 * omega**2 * x**2)   # Shifted Potential energy curve to cover energy levels

# Generate table of 50 values
x_table = np.linspace(-2, 2, 50)
V_x_table = (0.5 * omega**2 * x_table**2) 

table = np.column_stack((x_table, V_x_table))
print("Position (r)    Energy (E)")
print("-----------------------------------")
for row in table:
    print(f"{row[0]:.3f}          {row[1]:.3f}")

# Plot the potential well
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x, V_x, 'k', linewidth=2, label="Potential Well")

# Plot energy levels
for n, E in enumerate(energy_levels):
    ax.hlines(E, -2.5, 2.5, colors='b', linestyles='solid', linewidth=2)
    ax.text(1.6, E, f'n = {n}', verticalalignment='center', fontsize=12)

# Plot transitions (arrows)
for n in range(n_levels - 1):
    ax.arrow(1.2, energy_levels[n], 0, energy_levels[n + 1] - energy_levels[n] - 0.05,
             head_width=0.08, head_length=0.05, fc='r', ec='r')

# Labels and formatting
ax.set_xlabel("Position (r)")
ax.set_ylabel("Energy (E)")
ax.set_xticks(np.linspace(-2, 2, 5))  # Mark x-axis values
ax.set_yticks(energy_levels)
ax.set_yticklabels([f'$E_{n} = {(n+0.5)}\hbar\omega$' for n in range(n_levels)])
ax.set_title("Quantum Harmonic Oscillator Energy Levels")
ax.set_xlim(-2, 2)
ax.set_ylim(0, energy_levels[-1] + 0.5)
ax.grid(False)

plt.show()
