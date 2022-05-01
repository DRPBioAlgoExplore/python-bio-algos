import matplotlib.pyplot as plt
import numpy as np

# Visualizes function via a heatmap (credit to https://stackoverflow.com/questions/33282368/plotting-a-2d-heatmap-with-matplotlib for heatmap code)


def heatmap(func, x_min, x_max, y_min, y_max):
    y, x = np.meshgrid(np.linspace(x_min, x_max, 100),
                       np.linspace(y_min, y_max, 100))
    z = func(x, y)
    z = z[:-1, :-1]
    z_max = np.abs(z).max()
    z_min = -z_max

    fig, ax = plt.subplots()
    c = ax.pcolormesh(x, y, z, cmap='RdBu', vmin=z_min, vmax=z_max)
    fig.colorbar(c, ax=ax)
    return fig


# e.g. swarm_gif(data, [0,1, 0,1], fivepeaks, 'my_swarm_sim.gif')
# swarm_data is a 3d array of shape (timesteps x 4 x number of particles)
# The 4 data points are x, y, x-velocity, y-velocity, pbest-x, pbest-y
# Globals is a list of the global best position for every timestep, shape (timesteps x 2)
def swarm_gif(swarm_data, swarm_globs,  bounds, objective, name):
    x, y = np.array(np.meshgrid(np.linspace(
        bounds[0], bounds[1], 100), np.linspace(bounds[2], bounds[3], 100)))
    z = objective(x, y)

    n = swarm_data.shape[0]
    first_row = swarm_data[0]
    first_glob = swarm_globs[0]

    # Find the global minimum
    x_max = x.ravel()[z.argmax()]
    y_max = y.ravel()[z.argmax()]

    fig, ax = plt.subplots(figsize=(8, 6))
    fig.set_tight_layout(True)
    img = ax.imshow(z, extent=bounds,
                    origin='lower', cmap='viridis', alpha=0.5)
    fig.colorbar(img, ax=ax)
    ax.plot([x_max], [y_max], marker='x', markersize=5, color="white")
    contours = ax.contour(x, y, z, 10, colors='black', alpha=0.4)
    ax.clabel(contours, inline=True, fontsize=8, fmt="%.0f")

    # Plot positions (columns 1-2)
    p_plot = ax.scatter(first_row[0], first_row[1],
                        marker='o', color='blue', alpha=0.5)
    # Plot velocity vectors (columns 2-3)
    p_arrow = ax.quiver(first_row[0], first_row[1], first_row[2], first_row[3],
                        color='blue', width=0.005, angles='xy', scale_units='xy', scale=1)
    # Plot best positions (columns 4-5)
    pbest_plot = ax.scatter(
        first_row[4], first_row[5], marker='o', color='black', alpha=0.5)
    # Plot the global best
    gbest_plot = plt.scatter([first_glob[0]], [first_glob[1]],
                             marker='*', s=100, color='black', alpha=0.4)
    ax.set_xlim(bounds[0:2])
    ax.set_ylim(bounds[2:4])

    def animate(i):
        "Steps of PSO: algorithm update and show in plot"
        title = 'Iteration {:02d}'.format(i)
        data_row = swarm_data[i]
        glob_row = swarm_globs[i]
        # Set picture
        ax.set_title(title)
        pbest_plot.set_offsets(data_row[4:6].T)
        p_plot.set_offsets(data_row[0:2].T)
        p_arrow.set_offsets(data_row[0:2].T)
        p_arrow.set_UVC(data_row[2], data_row[3])
        gbest_plot.set_offsets(glob_row[0:2].reshape(1, -1))
        return ax, pbest_plot, p_plot, p_arrow, gbest_plot

    anim = FuncAnimation(fig, animate, frames=list(
        range(1, n)), interval=500, blit=False, repeat=True)
    anim.save(name, dpi=120, writer="imagemagick")
