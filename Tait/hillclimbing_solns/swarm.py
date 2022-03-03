import numpy as np


# 'curr_pos' is a 3-by-n array with rows
#   0. x-position
#   1. y-position
#   2. function values

# 'vel' is a 2-by-n array with rows
#   0. x-velocity
#   1. y-velocity

# 'best_pos' records the best locations so far for the point swarm
#   0. best x
#   1. best y
#   2. best function value

def reevaluate(pos, best_pos, best_glob, func):
    # Evaluate the swarm's current positions
    pos[2, :] = func(pos[0, :], pos[1, :])

    # Possibly update local records
    best_pos[:, :] = np.where(
        best_pos[2, :] < pos[2, :], pos, best_pos)

    best_ind = np.argmax(best_pos[2, :])
    # Possibly update global record
    if best_pos[2, best_ind] > best_glob[2]:
        best_glob[:, 0] = best_pos[:, best_ind]


def bound_pos(pos, clip_box):
    pos[0, :] = np.clip(pos[0, :], clip_box[0], clip_box[1])
    pos[1, :] = np.clip(pos[1, :], clip_box[2], clip_box[3])


def bound_vel(vel, max_vel):
    np.clip(vel, -max_vel, max_vel, out=vel)


def get_acc(pos, best_loc, best_glob, c1, c2):
    to_best = best_loc[0:2, :] - pos[0:2, :]
    to_glob = best_glob[0:2, :] - pos[0:2, :]
    # print(to_best)
    # print(to_glob)
    pop_size = pos.shape[1]
    r = np.random.rand(2, pop_size)
    return c1*r[0, :]*to_best + c2*r[1, :]*to_glob


def advance(pos, vel, timestep):
    pos[0:2, :] += vel * timestep


def classic_update(pos, vel, best, glob, bounds, func, params=None):
    if params is None:
        params = {'maxv': .1, 'timestep': .1, 'cog': 2, 'soc': 2}
    reevaluate(pos, best, glob, func)
    acc = get_acc(pos, best, glob, params['cog'], params['soc'])
    advance(vel, acc, params['timestep'])
    bound_vel(vel, params['maxv'])
    advance(pos, vel, params['timestep'])
    bound_pos(pos, bounds)
