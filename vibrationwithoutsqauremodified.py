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

def generate_wavefunction_table(y, n_values, alpha=ALPHA):
    """Return a DataFrame of ψₙ(y) values for given quantum states."""
    data = []
    for i, y_val in enumerate(y):
        row = [i + 1, y_val] + [psi_n(n, y_val, alpha) for n in n_values]
        data.append(row)
    
    columns = ["Serial No", "y"] + [f"psi_{n}(y)" for n in n_values]
    return pd.DataFrame(data, columns=columns)

def plot_wavefunctions(y, n_values, colors):
    """Plot ψₙ(y) for multiple quantum numbers."""
    fig, axes = plt.subplots(len(n_values), 1, figsize=(6, 10), sharex=True)
    
    for i, (n, color) in enumerate(zip(n_values, colors)):
        axes[i].plot(y, psi_n(n, y), color=color)
        axes[i].set_ylabel(f'$\\psi_{n}(y)$', fontsize=12, rotation=0, labelpad=15)
        axes[i].grid(True)
        axes[i].axhline(0, color='black', linewidth=0.5)
        axes[i].axvline(0, color='black', linewidth=0.5)
        axes[i].set_yticks([])
    
    axes[-1].set_xlabel(r'$y = \sqrt{\alpha}r$', fontsize=12)
    plt.tight_layout()
    plt.show()

# --- Main Routine ---
def main():
    y = np.linspace(-4, 4, 500)
    n_values = [0, 1, 2, 3]
    colors = ['r', 'b', 'g', 'purple']
    
    df = generate_wavefunction_table(y, n_values)
    
    # Display settings for full table (optional)
    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 1000)
    pd.set_option("display.float_format", "{:.6f}".format)
    
    print(df)
    plot_wavefunctions(y, n_values, colors)

if __name__ == "__main__":
    main()
