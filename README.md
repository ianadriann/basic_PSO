# basic_PSO
Basic example of Particle Swarm Optimization (PSO) implementation

Minimize f(x,y)=x^2 +y^2

Search Space Limitations:
-10 ≤ x ≤ 10
-10 ≤ y ≤ 10

Speed ​​Update:
v_{i}^{(t+1)} = w * v_{i}^{(t)} + c_1 * r_1 * (pbest_{i} - x_{i}^{(t)}) + c_2 * r_2 * (gbest - x_{i}^{(t)})

Position Update:
x_{i}^(t+1) = x_{i}^(t) + v_{i}^(t+1)

Flow:
1. Initialize random positions and velocities for all particles in the space [-10,10]
2. Compute fitness f(x,y)=x^2 +y^2
3. Store pbest and gbest
4. Repeat for N iterations:
5. Update the velocity of each particle.
6. Update the position of each particle.
7. Re-evaluate fitness → update pbest and gbest if necessary.

""" Indonesia
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