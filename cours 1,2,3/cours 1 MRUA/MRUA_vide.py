import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


# Paramètres du mouvement
t0 = 0  # Temps initial (s)
tf = 100  # Temps final (s)
dt = 0.1  # Pas de temps (s)
x0 = 0
v0 = 0  # Vitesse initiale (m/s)
a = 2  # Accélération constante (m/s²)

# Initialisation des listes
temps = []
vitesse = []
position = []
position2 = []


# Conditions initiales
t = t0
v = v0
x = x0
x2 = x0




# Méthode d'Euler pour calculer la vitesse et la position
while t <= tf:
    t = t + dt 
    x = v*dt + x
    v = a*dt + v
    x2 = 1/2*a*t*t + v0*t + x0
    temps.append(t)
    vitesse.append(v)
    position.append(x)
    position2.append(x2)
    print(t, x, v)
    
    





# Tracé des courbes
plt.figure(figsize=(10, 6))

# Courbe de la vitesse
plt.subplot(3, 1, 2)
plt.plot(temps, vitesse, label="Vitesse (m/s)", color="pink")
plt.title("Vitesse en fonction du temps (Méthode d'Euler)")
plt.xlabel("Temps! (s)")
plt.ylabel("Vitesse! (m/s)")
plt.grid(True)
plt.legend()

# Courbe de la position
plt.subplot(3, 1, 1)
plt.plot(temps, position, label="Position (m)", color="black")
plt.title("Position en fonction du temps (Méthode d'Euler)")
plt.xlabel("Temps!! (s)")
plt.ylabel("Position!! (m)")
plt.grid(True)
plt.legend()

# Courbe de la position (2)
plt.subplot(3, 1, 3)
plt.plot(temps, position2, label="Position 2 (m)", color="green")
plt.title("Position en fonction du temps (Méthode d'Euler)")
plt.xlabel("Temps!! (s)")
plt.ylabel("Position!! (m)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
plt.savefig('figure.png')
