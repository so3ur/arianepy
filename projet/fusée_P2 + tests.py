import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math


# Paramètres du mouvement:
t0 = 0  # Temps initial (s)
dt = 2  # Pas de temps (s)
y0 = 0
v0_y = 0  #   vitesse initiale (m/s)
m01 = 530000 # masse initiale
mf1 = 190000 # masse finale
mf2 = 36000  # 2e etage tout seul fait 31000kg
mf3 = 33500 # 3e masse finale
mf4 = 4000 # dernière masse
dm1 = 2260 # débit de masse 1er étage
dm2 = 735 # débit de masse 2e étage
dm3 = 40
dm4 = 11
ve1 = 2710 # vitesse d'éjection du carburant (m/s)
ve2 = 4220
ve3 = 4560
ve4 = 4560
x0 = 0
v0_x = 0  # Vitesse initiale (m/s)
g0 = 9.81
p = 1 # masse volumique (kg/m³)
Cd = 0.1 # coefficient de traînée
Cl = 0.1 # coeff. portée
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
Ox = Ox0 
Oy = Oy0
mf = 0
g = g0




# fonction étage en fonction de la masse finale, la masse, et le débit de masse
def etage(mf, m, dm, ve):

    global v_y , t , dt , Ly , ve_y , Dy , y , x ,  Cd , Cl , v_x , ve_x , g , A , al , p , Oy , Ox , d , g , G , M , Lx , Dx , rT 
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
       
        
        temps.append(t)
        # vitesse_y.append(v_y)
        # position_y.append(y)

        
        position_y.append(y)
        vitesse_y.append(v_y)
        vitesse_x.append(v_x)
        position_x.append(x)
        
        
        


# si la masse > que la 1e masse finale, 1er étage
if m1 >= mf1:
    etage(mf1 , m1 , dm1 , ve1)


print("FIN ETAGE 1")

# si la masse > que la 2e masse finale, 2e etage
if m1 >= mf2:
    m1 = m1 - 23000 # moins le poids de l'étage largué 
    etage(mf2 , m1, dm2 , ve2)

print('FIN ETAGE 2')
# si la masse > que la 3e masse finale, 3e etage
if m1 >= mf3:
    m1 = m1 - 14000
    etage(mf3, m1, dm3 , ve3) 

print('FIN ETAGE 3')
if m1 > mf4:
    # m1 = m1 - 4000
    etage(mf4, m1, dm4 , ve4)

print('RETOMBÉE')
while y >= 0:
    v_y = ((-mf2*g*dt + mf2*v_y) + Ly*dt + Dy*dt) / (mf2)
    y = v_y*dt + y
    t = t + dt 
    print(v_y)
    temps.append(t)
    position_y.append(y)
    vitesse_y.append(v_y)
    

# Tracé des courbes
plt.figure(figsize=(10, 6))
# Courbe de la vitesse (axe y)
plt.subplot(1, 1, 1)
plt.plot(temps, position_y, label="hauteur(m)", color="purple")
plt.title("hauteur en fonction du temps(Méthode d'Euler) ")
plt.xlabel("Temps (s)")
plt.ylabel("Hauteur (m)")
plt.grid(True)
plt.legend()

plt.show()

## ////////// TEST VITESSE DE LIBERATION

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
ve1 = 2710 # vitesse d'éjection du carburant (m/s)
ve2 = 4220
ve3 = 4560
ve4 = 4560
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


print(g)
# si la masse > que la 1e masse finale, 1er étage
if m1 >= mf1:
    etage(mf1 , m1 , dm1 , ve1)


print("FIN ETAGE 1")

# si la masse > que la 2e masse finale, 2e etage
if m1 >= mf2:
    m1 = m1 - 23000 # moins le poids de l'étage largué 
    etage(mf2 , m1, dm2 , ve2)
    print(g)
print('FIN ETAGE 2')
# si la masse > que la 3e masse finale, 3e etage
if m1 >= mf3:
    m1 = m1 - 14000
    etage(mf3, m1, dm3 , ve3) 

print('FIN ETAGE 3')
if m1 > mf4:
    # m1 = m1 - 4000
    etage(mf4, m1, dm4 , ve4)

print('RETOMBÉE')
while y >= 0 and t<300:
    v_y = ((-mf2*g*dt + mf2*v_y) + Ly*dt + Dy*dt) / (mf2)
    y = v_y*dt + y
    t = t + dt 
    temps.append(t)
    position_y.append(y)
    vitesse_y.append(v_y)
    print(g)
        


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


# TEST
#       CONSERVATION DE L'ENERGIE
#                                   & GRAPHIQUE MASSE-TEMPS

# Paramètres du mouvement:
t0 = 0  # Temps initial (s)
dt = 2  # Pas de temps (s)
y0 = 0
v0_y = 0  #   Vitesse initiale (m/s)
m01 = 530000 # masse initiale
mf1 = 190000 # masse finale
mf2 = 36000  # 2e etage tout seul fait 31000kg
mf3 = 33500 # 3e masse finale
mf4 = 4000 # dernière masse
dm1 = 2260 # débit de masse 1er étage
dm2 = 735 # débit de masse 2e étage
dm3 = 40
dm4 = 11
ve1 = 2710 # vitesse d'éjection du carburant (m/s)
ve2 = 4220
ve3 = 4560
ve4 = 4560
x0 = 0
v0_x = 0  # Vitesse initiale (m/s)
g0 = 9.81
p = 1 # masse volumique (kg/m³)
Cd = 0.0 # coefficient de traînée
Cl = 0.1 # coeff. portée
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
energie_cin = []
energie_pot = []
masse = []

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
mf = 0
g = g0

# fonction étage en fonction de la masse finale, la masse, et le débit de masse
def etage(mf, m, dm, ve):

    global v_y , t , dt , Ly , ve_y , Dy , y , x ,  Cd , Cl , v_x , ve_x , g , A , al , p , Oy , Ox , d , g , G , M , Lx , Dx , rT 
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
       
        
        temps.append(t)
        # vitesse_y.append(v_y)
        # position_y.append(y)

        
        position_y.append(y)
        vitesse_y.append(v_y)
        vitesse_x.append(v_x)
        position_x.append(x)
        masse.append(m)
        #calcul de l'energie cinetique et de pesanteur
        Ecin = 0.5*m*v_y*v_y
        print(Ecin)
        energie_cin.append(Ecin)
        print("/////////////////")
        Epot = m*g*y
        energie_pot.append(Epot)
        print(Epot)
        print("////////////")
        
        if abs(Epot) - abs(Ecin)==0: 
            print("la masse est conservée")
            quit() #(pour vérifier sans lire l'output)



# si la masse > que la 1e masse finale, 1er étage
if m1 >= mf1:
    etage(mf1 , m1 , dm1 , ve1)


print("FIN ETAGE 1")

# si la masse > que la 2e masse finale, 2e etage
if m1 >= mf2:
    m1 = m1 - 23000 # moins le poids de l'étage largué 
    etage(mf2 , m1, dm2 , ve2)

print('FIN ETAGE 2')
# si la masse > que la 3e masse finale, 3e etage
if m1 >= mf3:
    m1 = m1 - 14000
    etage(mf3, m1, dm3 , ve3) 

print('FIN ETAGE 3')
if m1 > mf4:
    # m1 = m1 - 4000
    etage(mf4, m1, dm4 , ve4)

print('RETOMBÉE')
while y >= 0:
    v_y = ((-mf2*g*dt + mf2*v_y) + Ly*dt + Dy*dt) / (mf2)
    y = v_y*dt + y
    t = t + dt 
    print(v_y)
    temps.append(t)
    position_y.append(y)
    vitesse_y.append(v_y)
    masse.append(m1)
    #calcul de l'energie cinetique et de pesanteur
    Ecin = 0.5*m1*v_y*v_y
    print(Ecin)
    energie_cin.append(Ecin)
    print("/////////////////")
    Epot = 1*g*y
    energie_pot.append(Epot)
    print(Epot)
    print("////////////")
    
    if abs(Epot) - abs(Ecin)==0: 
        print("la masse est conservée")
        quit() #(pour vérifier sans lire l'output)
        

# graph Ecin(t)

# Tracé des courbes
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.plot(temps, energie_cin, label="hauteur(m)", color="purple")
plt.title("Energie cinétique en fonction du temps (Méthode d'Euler)")
plt.xlabel("Temps (s)")
plt.ylabel("Energie cinétique (J)")
plt.grid(True)
plt.legend()


# graph Epot(t)
plt.subplot(1, 2, 2)
plt.plot(temps, energie_pot, label="hauteur(m)", color="purple")
plt.title("Energie potentielle de pesanteur en fonction du temps (Méthode d'Euler)")
plt.xlabel("Temps (s)")
plt.ylabel("Energie potentielle (J)")
plt.grid(True)
plt.legend()

plt.show()

# Tracé des courbes
plt.figure(figsize=(10, 6))
# Courbe de la vitesse (axe y)
plt.subplot(1, 1, 1)
# CORRECTION UNIQUE ICI : Remplacement de 'm1' (variable unique) par 'masse' (liste) pour que le graphique s'affiche
plt.plot(temps, masse, label="masse(kg)", color="purple") 
plt.title("Masse en fonction du temps (Méthode d'Euler) ")
plt.xlabel("Temps (s)")
plt.ylabel("Masse (kg)")
plt.grid(True)
plt.legend()

plt.show()