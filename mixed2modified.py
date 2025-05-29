import numpy as np
import matplotlib.pyplot as plt

# Constants (scaled for simplicity)
HBAR = 1
OMEGA = 3

def calculate_energy_levels(n_levels, hbar=HBAR, omega=OMEGA):
    """Calculate quantum harmonic oscillator energy levels."""
    return [(n + 0.5) * hbar * omega for n in range(n_levels)]

def potential_energy(x, omega=OMEGA):
    """Compute the harmonic potential energy V(x) = ½ω²x²."""
    return 0.5 * omega**2 * x**2

def print_energy_table(x_vals, v_x_vals):
    """Print a formatted table of position and potential energy."""
    print("Position (r)    Energy (E)")
    print("-----------------------------------")
    for x, V in zip(x_vals, v_x_vals):
        print(f"{x:.3f}          {V:.3f}")

def plot_energy_levels(n_levels, energy_levels, x, V_x):
    """Plot the harmonic oscillator potential and quantized energy levels."""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(x, V_x, 'k', linewidth=2, label="Potential Well")

    # Plot energy levels
    for n, E in enumerate(energy_levels):
        ax.hlines(E, -2.5, 2.5, colors='b', linestyles='solid', linewidth=2)
        ax.text(1.6, E, f'n = {n}', verticalalignment='center', fontsize=12)

    # Plot transitions as arrows
    for n in range(n_levels - 1):
        ax.arrow(1.2, energy_levels[n], 0, energy_levels[n + 1] - energy_levels[n] - 0.05,
                 head_width=0.08, head_length=0.05, fc='r', ec='r')

    # Labels and formatting
    ax.set_xlabel("Position (r)")
    ax.set_ylabel("Energy (E)")
    ax.set_xticks(np.linspace(-2, 2, 5))
    ax.set_yticks(energy_levels)
    ax.set_yticklabels([f'$E_{n} = {(n+0.5)}\\hbar\\omega$' for n in range(n_levels)])
    ax.set_title("Quantum Harmonic Oscillator Energy Levels")
    ax.set_xlim(-2, 2)
    ax.set_ylim(0, energy_levels[-1] + 0.5)
    ax.grid(False)
    plt.show()

def main():
    n_levels = 6
    x_dense = np.linspace(-2, 2, 100)
    x_table = np.linspace(-2, 2, 50)

    energy_levels = calculate_energy_levels(n_levels)
    V_x = potential_energy(x_dense)
    V_x_table = potential_energy(x_table)

    print_energy_table(x_table, V_x_table)
    plot_energy_levels(n_levels, energy_levels, x_dense, V_x)

if __name__ == "__main__":
    main()
