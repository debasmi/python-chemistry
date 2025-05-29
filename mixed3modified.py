import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import pandas as pd

# Constants (can be parameterized later)
MU = 1.0
OMEGA = 1.0
HBAR = 1.0

def calculate_alpha(mu=MU, omega=OMEGA, hbar=HBAR):
    return (mu * omega) / hbar

def psi_n(n, y, alpha):
    """Compute normalized vibrational wavefunction ψₙ(y)."""
    normalization = (alpha / np.pi)**0.25 / np.sqrt(2**n * np.math.factorial(n))
    hermite_poly = sp.hermite(n)(y)
    return normalization * hermite_poly * np.exp(-y**2 / 2)

def psi_n_squared(n, y, alpha):
    """Compute probability density |ψₙ(y)|²."""
    return psi_n(n, y, alpha) ** 2

def V(y):
    """Harmonic oscillator potential."""
    return 0.5 * y**2

def build_dataframe(y, n_values, alpha):
    """Build a DataFrame of squared wavefunction values over y."""
    data = []
    for i, y_val in enumerate(y):
        row = [i + 1, y_val]
        for n in n_values:
            row.append(psi_n_squared(n, y_val, alpha))
        data.append(row)
    columns = ["Serial No", "y"] + [f"psi_{n}^2(y)" for n in n_values]
    return pd.DataFrame(data, columns=columns)

def plot_wavefunctions(y, n_values, alpha, scale=1.5):
    """Plot potential well and wavefunction probability densities."""
    colors = ['r', 'b', 'g', 'purple']
    fig, ax = plt.subplots(figsize=(8, 10))
    
    ax.plot(y, V(y), color='black', linestyle='--', label='Potential V(y)')
    
    for n, color in zip(n_values, colors):
        psi_sq = psi_n_squared(n, y, alpha) * scale
        E_n = n + 0.5
        ax.plot(y, psi_sq + E_n, color=color, label=f'$|\psi_{n}(y)|^2$')
        ax.axhline(E_n, color=color, linestyle=':', linewidth=0.8)

    ax.set_xlabel(r'$y = \sqrt{\alpha}r$', fontsize=14)
    ax.set_ylabel('Energy Levels and Probability Densities', fontsize=14)
    ax.legend(fontsize=12)
    ax.grid(True)
    plt.show()

def main():
    y = np.linspace(-4, 4, 200)
    n_values = [0, 1, 2, 3]
    alpha = calculate_alpha()

    df = build_dataframe(y, n_values, alpha)
    
    # Configure Pandas display
    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 1000)
    pd.set_option("display.float_format", "{:.6f}".format)

    print(df)
    plot_wavefunctions(y, n_values, alpha)

if __name__ == "__main__":
    main()

