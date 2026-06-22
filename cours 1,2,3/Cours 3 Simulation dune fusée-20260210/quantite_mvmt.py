import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math


# Paramètres du mouvement: axe y
t0 = 0  # Temps initial (s)
dt = 2  # Pas de temps (s)
y0 = 0
v0_y = 3  # Vitesse initiale (m/s)
m0 = 1000 # masse initiale
mf = 40 # masse finale
dm = 30 # débit de masse
ve = 550 # vitesse d'éjection du carburant
# axe x:
x0 = 0
v0_x = 1  # Vitesse initiale (m/s)
g = 9.81



# Initialisation des listes
temps = []
vitesse_y = []
position_y = []
vitesse_x = []
position_x = []



# Conditions initiales
t = t0
m = m0
v_y = v0_y
y = y0
y2 = y0
v_x = v0_x
x = x0


# Méthode d'Euler pour calculer la vitesse et la position
while m >= mf:
    t = t + dt 
    m = m - dm*dt

    y = v_y*dt + y
    x = x + v_x*dt

    ve_x = -ve*v_x /math.sqrt(v_x*v_x+v_y*v_y)
    ve_y = -ve*v_y/math.sqrt(v_x*v_x+v_y*v_y)
    v_y = (-m*g*dt - dm*dt*ve_y + m*v_y) / (m - dm*dt)
    temps.append(t)
    vitesse_y.append(v_y)
    position_y.append(y)

    
    v_x = (m*v_x-dm*dt*ve_x)/(m - dm*dt)
    vitesse_x.append(v_x)
    position_x.append(x)
    print(t, m, v_y)





# Tracé des courbes
plt.figure(figsize=(10, 6))
# Courbe de la vitesse (axe y)
plt.subplot(3, 2, 2)
plt.plot(temps, vitesse_y, label="Vitesse (m/s)", color="pink")
plt.title("Vitesse Y en fonction du temps (Méthode d'Euler) ")
plt.xlabel("Temps! (s)")
plt.ylabel("Vitesse! (m/s)")
plt.grid(True)
plt.legend()

# Courbe de la position (axe y)
plt.subplot(3, 2, 1)
plt.plot(temps, position_y, label="Position (m)", color="black")
plt.title("Position Y en fonction du temps (Méthode d'Euler)")
plt.xlabel("Temps!! (s)")
plt.ylabel("Position!! (m)")
plt.grid(True)
plt.legend()

# Courbe de la vitesse (axe x)
plt.subplot(3, 2, 3)
plt.plot(temps, vitesse_x, label="Vitesse (m/s)", color="pink")
plt.title("Vitesse X en fonction du temps (Méthode d'Euler)")
plt.xlabel("Temps! (s)")
plt.ylabel("Vitesse! (m/s)")
plt.grid(True)
plt.legend()

# Courbe de la position (axe x)
plt.subplot(3, 2, 4)
plt.plot(temps, position_x, label="Position (m)", color="black")
plt.title("Position X en fonction du temps (Méthode d'Euler)")
plt.xlabel("Temps!! (s)")
plt.ylabel("Position!! (m)")
plt.grid(True)
plt.legend()

# position y en fonction de position x
plt.subplot(3, 2, 5)
plt.plot(position_x, position_y, label="Vitesse (m/s)", color="pink")
plt.title("position y en fonction de position x")
plt.xlabel("pos x (m/s)")
plt.ylabel(" pos y (m/s)")
plt.grid(True)
plt.legend()

# vitesse x en fonction de vitesse y
plt.subplot(3, 2, 6)
plt.plot(vitesse_y, vitesse_x, label="Vitesse (m/s)", color="pink")
plt.title("vitesse x en fonction de vitesse y")
plt.xlabel("vitesse y (m/s)")
plt.ylabel("vitesse (m/s)")
plt.grid(True)
plt.legend()



plt.tight_layout()

plt.savefig('figure.png')




##########################################
# animation
###########################################
# Création de la figure et des axes
fig, axe = plt.subplots()
(line,) = axe.plot([], [], "o", markersize=5)  # 'bo' pour un point bleu

# Configuration des limites des axes
axe.set_xlim(0, max(position_x) + 1)
axe.set_ylim(0, max(position_y) + 1)
axe.set_xlabel("Position X")
axe.set_ylabel("Position Y")
axe.set_title("Animation de la position")


# Fonction d'initialisation
def init():
    line.set_data([], [])
    return (line,)


# Fonction d'animation
def animate(frame):
    line.set_data(
        [position_x[:frame], position_y[:frame]]
    )  # Définie les éléments à tracer
    axe.set_title(f"Animation de la position (t={temps[frame]} s)")
    return (line,)


# Création de l'animation
ani = animation.FuncAnimation(
    fig,
    animate,
    frames=len(temps),
    init_func=init,
    blit=True,  # Optimisation
    interval= dt*10,
    # permet de changer la vitesse de la simulation ( ici mis à temps réel)
    repeat=True,
)

# Affichage de l'animation
plt.show()
