


##########################################
# animation
###########################################
# Création de la figure et des axes
fig, axe = plt.subplots()
(line,) = axe.plot([], [], "x", markersize=1)  # 'bo' pour un point bleu

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
    interval=dt * 1000,
    # permet de changer la vitesse de la simulation ( ici mis à temps réel)
    repeat=True,
)

# Affichage de l'animation
plt.show()
