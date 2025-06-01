"""
Minimize f(x,y)=x^2 +y^2

Batasan Ruang Pencarian:
-10 ≤ x ≤ 10
-10 ≤ y ≤ 10

PSO
Update Kecepatan
v_{i}^{(t+1)} = w * v_{i}^{(t)} + c_1 * r_1 * (pbest_{i} - x_{i}^{(t)}) + c_2 * r_2 * (gbest - x_{i}^{(t)})

Update Posisi:
x_{i}^(t+1) = x_{i}^(t) + v_{i}^(t+1)

Alur:
1. Inisialisasi posisi dan kecepatan acak untuk semua partikel dalam ruang [-10,10]
2. Hitung fitness f(x,y)=x^2 +y^2
3. Simpan pbest dan gbest
4. Ulangi selama N iterasi:
5. Update kecepatan tiap partikel.
6. Update posisi tiap partikel.
7. Evaluasi kembali fitness → update pbest dan gbest jika perlu.
"""

import numpy as np
import matplotlib.pyplot as plt

# Fungsi objektif
def objective_function(position):
    x, y = position
    return x**2 + y**2

# Parameter PSO
num_particles = 10
num_iterations = 100
w = 0.7
c1 = 1.5
c2 = 1.5
dim = 2
bounds = [-10, 10]

# Inisialisasi posisi dan kecepatan
positions = np.random.uniform(bounds[0], bounds[1], (num_particles, dim))
velocities = np.random.uniform(-1, 1, (num_particles, dim))
pbest_positions = np.copy(positions)
pbest_scores = np.array([objective_function(pos) for pos in positions])
gbest_index = np.argmin(pbest_scores)
gbest_position = pbest_positions[gbest_index]
gbest_score = pbest_scores[gbest_index]

# Menyimpan posisi tiap iterasi untuk animasi
history = []

# Loop iterasi
for iteration in range(num_iterations):
    for i in range(num_particles):
        fitness = objective_function(positions[i])
        if fitness < pbest_scores[i]:
            pbest_scores[i] = fitness
            pbest_positions[i] = positions[i]

    gbest_index = np.argmin(pbest_scores)
    if pbest_scores[gbest_index] < gbest_score:
        gbest_score = pbest_scores[gbest_index]
        gbest_position = pbest_positions[gbest_index]

    for i in range(num_particles):
        r1 = np.random.rand(dim)
        r2 = np.random.rand(dim)
        velocities[i] = (
            w * velocities[i]
            + c1 * r1 * (pbest_positions[i] - positions[i])
            + c2 * r2 * (gbest_position - positions[i])
        )
        positions[i] += velocities[i]
        positions[i] = np.clip(positions[i], bounds[0], bounds[1])

    # Simpan posisi untuk visualisasi
    history.append(np.copy(positions))

    if (iteration + 1) % 10 == 0 or iteration == 0:
        print(f"Iterasi {iteration+1:3d}: gbest = {gbest_position}, nilai = {gbest_score:.6f}")

print("\n=== HASIL AKHIR ===")
print(f"Posisi terbaik ditemukan: {gbest_position}")
print(f"Nilai minimum fungsi: {gbest_score:.6f}")

# =============================
# Visualisasi Pergerakan Partikel
# =============================

import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_xlim(bounds[0], bounds[1])
ax.set_ylim(bounds[0], bounds[1])
scat = ax.scatter([], [], c='blue')
gbest_dot, = ax.plot([], [], 'ro', label='Global Best')
ax.set_title("Pergerakan Partikel (PSO)")
ax.legend()

def update(frame):
    pos = history[frame]
    scat.set_offsets(pos)
    
    # Bungkus posisi gbest dalam list agar tidak error
    gbest_dot.set_data([gbest_position[0]], [gbest_position[1]])
    
    ax.set_title(f"Iterasi {frame+1}")
    return scat, gbest_dot


ani = animation.FuncAnimation(fig, update, frames=len(history), interval=200, repeat=False)
plt.show()


