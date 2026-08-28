
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import numpy as np

# Paramètres du mouvement:
t0 = 0  # Temps initial (s)
dt = 0.002  # Pas de temps (s)
y0 = 0
v0_y = 1  #   Vitesse initiale (m/s)
m01 = 860000 # masse initiale
mf1 = 165000 # masse finale
mf2 = 34000  # 2e etage tout seul fait 31000kg
mf3 = 18000 # 3e masse finale
mf4 = 4000
dm1 = 3800 # débit de masse 1er étage
dm2 = 750 # débit de masse 2e étage
dm3 = 45
dm4 = 11
ve1 = 2800 # vitesse d'éjection du carburant (m/s)
ve2 = 4220
ve3 = 4560
ve4 = 4560
x0 = 0
v0_x = 1000  # Vitesse initiale (m/s)
g0 = 9.81
p0 = 1.225 # masse volumique (kg/m³) - NIVEAU MER
Cd = 0.1 # coefficient de traînée
Cl = 0.1 # coeff. portée
A = 10
Ox0 = 2.65 * (10**(-4))
Oy0 = math.sqrt(1-Ox0**2)
rT = 6371000 # Rayon de la terre (m)
G = 0.0000000000667 #Nm²/Kg² 
M = 5972000000000000000000000 # Masse de la terre (kg)
R = 8.314       # Constante des gaz parfaits (J/(mol·K))
tempDepart = 288.15      # Température moyenne (K) ~15°C 
Mmo = 0.02896     # Masse molaire de l'air (kg/mol)

# Initialisation des listes
temps = []
vitesse_y = []
position_y = []
vitesse_x = []
position_x = []



# Conditions initiales
t = t0
m1 = m01
v_y = v0_y 
y = y0
y2 = y0
v_x = v0_x
x = x0
Ox = Ox0 
Oy = Oy0
mf = mf1
g = g0
p = p0
Temp = tempDepart



# fonction étage en fonction de la masse finale, la masse, et le débit de masse
def etage(mf, m, dm, ve):

    global v_y , t , dt , Ly , ve_y , Dy , y , x ,  Cd , Cl , v_x , ve_x , g , A , al , p , Oy , Ox , d , g , G , M , Lx , Dx , rT , Hs , R , Mmo , Tmoy , Temp , tempDepart , Ox0 , Oy0 
    # méthode d'Euler pour calculer la vitesse et la position
    while y >= 0 and m > mf:
        
        t = t + dt 
        y = v_y*dt + y
        x = x + v_x*dt

        if y < 11000:
        # temp. de l'air en fonction de la hauteur. tous les 100m, on perd 0.65K
            Temp = tempDepart - y*(0.0065)
            
        # pression atmospherique:
        Hs = (R * Temp) / (Mmo * g)
        p = p0 * math.exp(- y / Hs)
        

        L = (Cl*p*(v_x*v_x*+v_y*v_y)*A)/2
        D = (Cd*p*(v_x*v_x + v_y*v_y)*A)/2 #traînée, pas projetée


        
        # if not (v_x == 0 and v_y== 0):

        Oy = v_y/math.hypot(v_x , v_y)
        Ox = v_x/math.hypot(v_x , v_y)

        Lx = L*Oy
        Ly = L*Ox
        Dx = -D*Ox
        Dy = -D*Oy

        ve_x = (-ve*Ox) +v_x
        ve_y = (-ve*Oy) + v_y
        v_y = ((-m*g*dt - dm*dt*ve_y + m*v_y) + Ly*dt + Dy*dt) / (m - dm*dt)
        v_x = ((-m*v_x -dm*dt*ve_x)+ Dx*dt + Lx*dt) / (m - dm*dt)
        d = rT + y # distance au centre de la terre (rayon terre + hauteur fusée)
        
        print(v_x)
        m = m - dm*dt # masse 
        g = (G*M)/(d*d) # nouveau g 
        
        temps.append(t)
    

        position_y.append(y)
        vitesse_y.append(v_y)
        vitesse_x.append(v_x)
        position_x.append(x)
        

        if Ox == 0:
            break

    return(m)
        
        


# si la masse > que la 1e masse finale, 1er étage
if m1 >= mf1:
    print(m1)
    m1=etage(mf1 , m1 , dm1 , ve1)
    print(m1)


print("FIN ETAGE 1")

# si la masse > que la 2e masse finale, 2e etage
if m1 >= mf2:
   # m1 = etage(mf1, m1, dm1, ve1)
    m1 = m1 - 35000 # moins le poids de l'étage largué 

    m1=etage(mf2 , m1, dm2 , ve2)

print('FIN ETAGE 2')

# si la masse > que la 3e masse finale, 3e etage
if m1 >= mf3:
   # m1 = etage(mf2, m1, dm2, ve2)
    m1 = m1 - 8000
    m1=etage(mf3, m1, dm3 , ve3) 

print('FIN ETAGE 3')

if m1 > mf4:
    #m1 = etage(mf3, m1, dm3, ve3)

    m1=etage(mf4, m1, dm4 , ve4)

print('RETOMBÉE')

# while y >= 0:
    
    
#     if not (v_x == 0 and v_y== 0):
#         Oy = v_y/math.sqrt(v_x*v_x + v_y*v_y)
#         Ox = v_x/math.sqrt(v_x*v_x + v_y*v_y)
        
#     L = (Cl*p*(v_x*v_x*+v_y*v_y)*A)/2
#     D = (Cd*p*(v_x*v_x + v_y*v_y)*A)/2
#     Ly = L*Ox
#     Dy = -D*Oy
#     Hs = (R * Temp) / (Mmo * g)
#     p = p0 * math.exp(- y / Hs)
#     v_y = ((-m1*g*dt + m1*v_y) + Ly*dt + Dy*dt) / (m1)
#     v_x = ((-mf*v_x)+ Dx*dt + Lx*dt) / (mf)
#     y = v_y*dt + y
#     x = x + v_x*dt
#     t = t + dt 
#     d = rT + y
#     g = (G*M)/(d*d) 
    
#     temps.append(t)
    
#     vitesse_x.append(v_x)
#     position_x.append(x)
#     position_y.append(y)
#     vitesse_y.append(v_y)
    

print('Fin!')




# Cercle de rayon rT
R=rT
theta = np.linspace(0, 2 * np.pi, 400)
x_cercle = R * np.cos(theta)
y_cercle = R * np.sin(theta)
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x_cercle, y_cercle, "b-", label=f"Terre")
ax.plot(position_x , position_y, "r-", label="Trajectoire (x, y)")
ax.set_aspect("equal")
ax.grid(True, alpha = 0.3)
ax.axhline(0, color="k", lw=0.5)
ax.axvline(0, color="k", lw=0.5)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Cercle de rayon rT et points (x, y)")
ax.legend()
plt.show() 

"""

# graph y(t)

# Tracé des courbes
plt.figure(figsize=(10, 6))
# Courbe de la vitesse (axe y)
plt.subplot(1, 1, 1)
plt.plot(temps,position_y , label="hauteur(m)", color="purple")
plt.title("hauteur en fonction du temps (Méthode d'Euler) ")
plt.xlabel("Temps (s)")
plt.ylabel("Hauteur (m)")
plt.grid(True)
plt.legend()

plt.show()
 """