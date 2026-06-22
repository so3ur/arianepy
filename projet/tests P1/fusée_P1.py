import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math


# Paramètres du mouvement:
t0 = 0  # Temps initial (s)
dt = 0.05  # Pas de temps (s)
y0 = 0
v0_y = 0  # Vitesse initiale (m/s)
m0 = 530000 # masse initiale
mf = 530000 - 170000 # masse finale
dm = 1600 # débit de masse
ve = 4000 # vitesse d'éjection du carburant
x0 = 0
v0_x = 0  # Vitesse initiale (m/s)
g = 9.81
al0 = 0 # inclinasion initiale (degrés)
p = 1 # masse volumique (kg/m³)
Cd = 0.1 # coefficient de traînée
Cl = 0.1 # coeff. portée
A = 10
Ox0 = 0
Oy0 = 1
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
al = al0
Ox = Ox0 
Oy = Oy0


# Méthode d'Euler pour calculer la vitesse et la position
while m >= mf:
    t = t + dt 
    

    y = v_y*dt + y
    x = x + v_x*dt

    L = (Cl*p*(v_x*v_x*+v_y*v_y)*A)/2
    D = (Cd*p*(v_x*v_x + v_y*v_y)*A)/2 #traînée, pas projetée

    if not (v_x == 0 and v_y== 0):
        Oy = v_y/math.sqrt(v_x*v_x+v_y*v_y)
        Ox = v_x/math.sqrt(v_x*v_x+v_y*v_y)

    Lx = L*Oy
    Ly = L*Ox
    Dx = -D*Ox
    Dy = -D*Oy

    ve_x = (-ve*Ox) +v_x
    ve_y = (-ve*Oy) + v_y

    v_y = ((-m*g*dt - dm*dt*ve_y + m*v_y) + Ly*dt + Dy*dt) / (m - dm*dt)
    temps.append(t)
    vitesse_y.append(v_y)
    position_y.append(y)

    
    v_x = ((m*v_x-dm*dt*ve_x) + Dx*dt + Lx*dt) /(m - dm*dt) 
    vitesse_x.append(v_x)
    position_x.append(x)
    print(y)

    m = m - dm*dt





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
