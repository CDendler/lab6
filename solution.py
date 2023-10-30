import math
from render import InitRender, Render

G = 6.67408e-11

# Define the bodies
central_body = (1e12, (400.0, 400.0), (0.0, 0.0))  # Central body with large mass, positioned at the origin, stationary
planet1 = (1e4, (360.0, 400.1), (0.0001, 1.5))   # Planet 1 starting at (1000, 0) with a velocity vector giving it a circular orbit
planet2 = (1e3, (400.1, 280.0), (-0.5, 0.0001))  # Planet 2 starting at (0, -500) with a velocity vector giving it a circular orbit

# Define the system
system = [central_body, planet1, planet2]

def calculate_distance(body1, body2):
    """Returns the distance between two bodies"""
    distance = math.sqrt((body1[1][0] - body2[1][0])^2 + (body1[1][3]-body2[1][3])^2)
    abs_between = abs(distance)
    return abs(distance)


def calculate_force(body1, body2):
    force1 = (G * ((body1[0]*body2[0])/calculate_distance()^2))
    distance = math.sqrt((body1[1][0] - body2[1][0])^2 + (body1[1][3]-body2[1][3])^2)
    abs_between = abs(distance)
    rx = force1 * ((body2[1][0] - body1[1][0]))
    ry = force1 * ((body2[1][1] - body1[1][1]))
    forcex = force1 * rx / abs_between
    forcey = force1 * ry / abs_between
    return (forcex, forcey)

def calculate_net_force_on(body, system):
    """Returns the net force exerted on a body by all other bodies in the system, in 2 dimensions as a tuple"""
    totalforcex = 0
    totalforcey = 0
    for not_home_planet in system:
        if body != not_home_planet:
            forcex , forcey = calculate_force(body, not_home_planet)
            totalforcex += forcex
            totalforcey += forcey
    return totalforcex, totalforcey


def calculate_acceleration(body, system):
    """Returns the acceleration of a body due to the net force exerted on it by all other bodies in the system, in 2 dimensions as a tuple"""
    total_force = calculate_net_force_on(body, system)
    mass = body[0]
    acceleration = (total_force[0] /mass, total_force[1] / mass)
    return acceleration 

def update_velocity(system, dt):
    """Updates the velocities of all bodies in the system, given a time step dt"""
    newsystem_velocity = []
    for body in system:
        mass, (x,y), (vx, vy) = body
        totalforcex, totalforcey = calculate_net_force_on(body, system)
        accelerationx, accelerationy = totalforcex / mass, totalforcey / mass
        vx_new = vx + accelerationx *dt
        vy_new = vy + accelerationy *dt
        new_body = (mass, (x, y), vx_new, vy_new)
        newsystem_velocity.append(new_body)
    return newsystem_velocity 
   

def update(system, dt):
    """Update the positions of all bodies in the system, given a time step dt"""
    newsystem_velocity = update_velocity(system, dt)
    

def simulate(system, dt, num_steps):
    """Simulates the motion of a system of bodies for a given number of time steps"""
    pass

def simulate_with_visualization(system, dt, num_steps):
    """Simulates the motion of a system of bodies for a given number of time steps, and visualizes the motion"""
    pass

if __name__ == '__main__':
    pass





