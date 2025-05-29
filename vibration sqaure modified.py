import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import pandas as pd

# --- Constants ---
MU = 1.0
OMEGA = 1.0
HBAR = 1.0
ALPHA = (MU * OMEGA) / HBAR

# --- Functions ---

def psi_n(n, y, alpha=ALPHA):
    """Compute the normalized vibrational wavefunction ψₙ(y)."""
    normalization = (alpha / np.pi) ** 0.25 / np.sqrt(2**n * np.math.factorial(n))
    hermite_poly = sp.hermite(n)(y)
    return normalization * hermite_poly * np.exp(-y**2 / 2)

def compute_probability_densities(y, n_values, alpha=ALPHA):
    """Return a dictionary with y and the probability densities for each n."""
    data = {"y": y}
    for n in n_values:
        wavefunction = psi_n(n, y, alpha)
        data[f"P_r_n{n}"] = np.abs(wavefunction) ** 2
    return pd.DataFrame(data)

def plot_probability_densities(y, n_values, colors):
    """Plot probability densities in subplots."""
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    axes = axes.flatten()
    
    for i, (n, color) in enumerate(zip(n_values, colors)):
        P_r = np.abs(psi_n(n, y)) ** 2
        axes[i].plot(y, P_r, color=color)
        axes[i].set_xlabel(r'$\sqrt{\alpha}r$', fontsize=12)
        axes[i].set_ylabel(r'$P(r) = |\psi_n(r)|^2$', fontsize=12)
        axes[i].set_title(f'Probability Density for n={n}', fontsize=14)
        axes[i].grid(True)
    
    plt.tight_layout()
    plt.show()

# --- Main Routine ---
def main():
    y = np.linspace(-4, 4, 500)
    n_values = [0, 1, 2, 3]
    colors = ['r', 'b', 'g', 'purple']
    
    df = compute_probability_densities(y, n_values)
    print(df.to_string(index=False))
    
    plot_probability_densities(y, n_values, colors)

if __name__ == "__main__":
    main()
