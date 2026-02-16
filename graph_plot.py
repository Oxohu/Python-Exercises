import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# --- Data Input ---
Vp_data = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
Vpt_data = np.array([0.00, 0.00, 0.02, 0.09, 0.21, 0.34, 0.49, 0.62])

# --- Setup "Simulation" Aesthetic ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))

# Background color tweak for a more 'technical' dark gray
ax.set_facecolor('#1e1e1e')
fig.patch.set_facecolor('#121212')

# --- Data smoothing (Interpolation) ---
# This makes the line look like a continuous simulation sweep rather than just connected dots
spline = make_interp_spline(Vp_data, Vpt_data, k=3)  # Cubic spline
Vp_smooth = np.linspace(Vp_data.min(), Vp_data.max(), 500)
Vpt_smooth = spline(Vp_smooth)

# --- Plotting ---
# 1. The smooth simulation trace
ax.plot(Vp_smooth, Vpt_smooth, color='#00ff00', linewidth=2.5, alpha=0.8, label='Vpt Trace (Simulated Sweep)')

# 2. The actual measured data points
ax.scatter(Vp_data, Vpt_data, color='#ff3300', marker='o', s=50, zorder=5, label='Measured Data Points')

# --- Grid Customization ---
# Major grid
ax.grid(True, which='major', color='#555555', linestyle='-', linewidth=0.8, alpha=0.5)
# Minor grid for more detail
ax.minorticks_on()
ax.grid(True, which='minor', color='#444444', linestyle=':', linewidth=0.5, alpha=0.3)

# --- Labels and Title with technical font style ---
font_style = {'family': 'monospace', 'weight': 'bold'}
ax.set_xlabel('Power Output Voltage (Vp) [V]', fontdict=font_style, fontsize=12, labelpad=10)
ax.set_ylabel('Phototransistor Voltage (Vpt) [V]', fontdict=font_style, fontsize=12, labelpad=10)
ax.set_title('DC Transfer Characteristic: Vpt vs. Vp', fontdict=font_style, fontsize=14, color='#ffffff', pad=15)

# --- Axis adjustments ---
ax.set_xlim(0, 4.2)
ax.set_ylim(-0.05, 0.7)
ax.tick_params(axis='both', which='major', labelsize=10, colors='#cccccc')

# Add legend
ax.legend(frameon=True, facecolor='#333333', edgecolor='#555555')

plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt

# Data from your table
vp = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
omega = [90, 240, 378, 510, 624, 762, 840, 744, 870]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(vp, omega, marker='o', linestyle='-', color='b', label='Speed vs Voltage')

# Adding titles and labels
plt.title('Relationship Between Power Output Voltage ($V_P$) and Speed ($\omega$)', fontsize=14)
plt.xlabel('Power Output Voltage $V_P$ (V)', fontsize=12)
plt.ylabel('Speed $\omega$ (RPM)', fontsize=12)

# Adding a grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Show the plot
plt.show()