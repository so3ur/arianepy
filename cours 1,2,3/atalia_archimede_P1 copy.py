# à calculer:
# Vy(t) ; Posy(t) 

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


# Paramètres du mouvement
t0 = 0  # Temps initial (s)
tf = 100  # Temps final (s)
dt = 0.1  # Pas de temps (s)
y0 = -200    # Position y (m)
vy0 = 0  # Vitesse initiale (m/s)
pf = 1000 # Masse volumique de l'eau (kg/m³)
po = 980 # Masse volumique de l'objet (kg/m³)
a = ((pf-po)/po)*10 # Accélération constante (m/s²)



# Initialisation des listes
temps = []
vitesse_y = []
position_y = []



# Conditions initiales
t = t0
vy = vy0
y = y0


# Méthode d'Euler pour calculer la vitesse et la position


# finalement pas ajouté de t >= tf parce que cette condition d'arrêt marche très bien seule
while y <= 0:
    t = t + dt 
    y = vy*dt + y
    vy = a*dt + vy
    
    temps.append(t)
    vitesse_y.append(vy)
    position_y.append(y)
    print(t, y) #pour vérifier que les calculs soient faits (et pour la partie 1.6)


# Tracé des courbes
plt.figure(figsize=(10, 6))

# Courbe de la vitesse
plt.subplot(2, 1, 1)
plt.plot(temps, vitesse_y, label="Vitesse (m/s)", color="purple")
plt.title("Vitesse en fonction du temps (Méthode d'Euler)")
plt.xlabel("Temps (s)")
plt.ylabel("Vitesse (m/s)")
plt.grid(True)
plt.legend()

# Courbe de la position
plt.subplot(2, 1, 2)
plt.plot(temps, position_y, label="Position (m)", color="blue")
plt.title("Position en fonction du temps (Méthode d'Euler)")
plt.xlabel("Temps (s)")
plt.ylabel("Position (m)")
plt.grid(True)
plt.legend()

plt.show()
