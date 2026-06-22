import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

## TEST VITESSE DE LIBERATION

# Paramètres du mouvement:
t0 = 0  # Temps initial (s)
dt = 2  # Pas de temps (s)
y0 = 0
v0_y = 11200 # Vitesse initiale (m/s)
m01 = 530000 # masse initiale
mf1 = 31000 # masse finale
mf2 = 31000  # 2e etage tout seul fait 31000kg
dm1 = 1600 # débit de masse 1er étage
dm2 = 4000 # débit de masse 2e étage
ve = 4560 # vitesse d'éjection du carburant
x0 = 0
v0_x = 0  # Vitesse initiale (m/s)
g0 = 9.81
al0 = 0 # inclinasion initiale (degrés)
p = 1 # masse volumique (kg/m³)
Cd = 0#0.1 # coefficient de traînée
Cl = 0#0.1 # coeff. portée
A = 10
Ox0 = 0
Oy0 = 1
rT = 6371000 # rayon de la terre (m)
G = 0.0000000000667 #Nm²/Kg² 
M = 5972000000000000000000000 # masse de la terre (kg)


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
al = al0
Ox = Ox0 
Oy = Oy0
mf = 0
g = g0





def etage(mf, m, dm):

    global v_y , t , dt , Ly , ve_y , Dy , y , x ,  Cd , Cl , v_x , ve_x , g , ve , A , al , ve , p , Oy , Ox , d , g , G , M , Lx , Dx , rT 
    # Méthode d'Euler pour calculer la vitesse et la position
    while y >= 0 and m > mf:
        


        t = t + dt 
      

        y = v_y*dt + y
      
        # x = x + v_x*dt
       
        L = (Cl*p*(v_x*v_x*+v_y*v_y)*A)/2
        D = (Cd*p*(v_x*v_x + v_y*v_y)*A)/2 #traînée, pas projetée

        if not (v_x == 0 and v_y== 0):
            Oy = v_y/math.sqrt(v_x*v_x+v_y*v_y)
            Ox = v_x/math.sqrt(v_x*v_x+v_y*v_y)

        Lx = L*Oy
        Ly = L*Ox
        Dx = -D*Ox
        Dy = -D*Oy

        # ve_x = (-ve*Ox) +v_x
        ve_y = (-ve*Oy) + v_y
        v_y = ((-m*g*dt - dm*dt*ve_y + m*v_y) + Ly*dt + Dy*dt) / (m - dm*dt)

        d = rT + y # distance au centre (rayon terre + hauteur fusée)

        m = m - dm*dt # masse 
        g = (G*M)/(d*d) # nouveau g 
        print(y)
       
        
        temps.append(t)
        # vitesse_y.append(v_y)
        # position_y.append(y)

        
        position_y.append(y)
        vitesse_y.append(v_y)
        vitesse_x.append(v_x)
        position_x.append(x)
        
        
        



if m1 >= mf1:
    etage(mf1 , m1 , dm1)


print("étage 2:")

if m1 >= mf2:
    m1 = m1 - 1
    etage(mf2 , m1, dm2)



while y >= 0 and t < 100000 :
    d = rT + y
    g = (G*M)/(d*d)
    v_y = ((-mf2*g*dt + mf2*v_y) + Ly*dt + Dy*dt) / (mf2)
    y = v_y*dt + y
    t = t + dt 
    print(g)
    temps.append(t)
    position_y.append(y)
    vitesse_y.append(v_y)
    


# graph y(t)

# Tracé des courbes
plt.figure(figsize=(10, 6))
# Courbe de la vitesse (axe y)
plt.subplot(1, 1, 1)
plt.plot(temps, position_y, label="hauteur(m)", color="purple")
plt.title("Hauteur en fonction du temps (Méthode d'Euler) ")
plt.xlabel("temps (s)")
plt.ylabel("hauteur (m)")
plt.grid(True)
plt.legend()

plt.show()

