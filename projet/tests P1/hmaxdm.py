import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

# hmax(dm)

# Paramètres du mouvement (Ariane 62):
t0 = 0  # Temps initial (s)
dt = 0.02  # Pas de temps (s) (diminué pour éviter les oscillations)
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
Cl = 0 # coeff. portée
A = 10
Ox0 = 0
Oy0 = 1
h_max0 = 0
# Initialisation des listes
temps = []
vitesse_y = []
position_y = []
vitesse_x = []
position_x = []
dm_liste = []
h_maxliste= []





# Méthode d'Euler pour calculer la vitesse et la position


for dm in range (100, 5000, 10): # start stop step

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
    h_max = h_max0


    

    while y >= 0:
        t = t + dt 
        

        y = v_y*dt + y
        x = x + v_x*dt

        L = (Cl*p*(v_x*v_x*+v_y*v_y)*A)/2 # portance, pas projetée
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


        if m >= mf:
            v_y = ((-m*g*dt - dm*dt*ve_y + m*v_y) + Ly*dt + Dy*dt) / (m - dm*dt)
            v_x = ((m*v_x-dm*dt*ve_x) + Dx*dt + Lx*dt) /(m - dm*dt) 
        else: #dm*dt = 0
            v_y = ((-mf*g*dt + mf*v_y) + Ly*dt + Dy*dt) / (mf)
            v_x = ((-mf*v_x)+ Dx*dt + Lx*dt) / (mf)

        m = m - dm*dt

        if y > h_max:
            h_max = y


        #         # gestion du sol (pour éviter les vitesses négatives) si la poussée < la pesanteur
        # if y <= 0:
        #     # si on est au sol (ou en dessous)
        #     if v_y < 0:
        #         # et si la vitesse va vers le bas
        #         v_y = 0 #le sol nous bloque
        #         y = 0  # on n'a pas décollé



    h_maxliste.append(h_max)
    dm_liste.append(dm)
    


# Tracé des courbes
plt.figure(figsize=(10, 6))
# Courbe de la vitesse (axe y)
plt.subplot(1, 1, 1)
plt.plot(dm_liste, h_maxliste, label="hauteur max (m)", color="purple")
plt.title("Hauteur max (m) en fonction du débit de masse (Méthode d'Euler) ")
plt.xlabel("débit de masse (kg/s)")
plt.ylabel("hauteur max (m)")
plt.grid(True)
plt.legend()

plt.show()





