import math

from pylab import *


######################  functions are defined here ###########################

def get_period_of_planet(dist_exo_star, velocity_exo):
    """ Determine the period of an exoplanet using the distance of the planet
    from its star and the velocity of the planet. The period is the time, in
    seconds, for the exoplanet to make one complete orbit around its star

    t_period (s) = circumference of oribit(km) /velocity of the exoplanet(km/s)

    Paramaters:
        dist_exo_star (flt): Input from user of the distance of the exoplanet
            from its star, relative to Earth and the sun (km)
        velocity_exo (flt): Velocity of exoplanet, dependant on distance from
            its star and gravitational attraction of the star (km/s)
    Return:
        flt: The period of the exoplanet (s)
    """
    return (2 * math.pi * dist_exo_star / velocity_exo)


def get_transit_time(velocity_exo, r_star):
    """ Determine the transit time of the exoplanet using its velocity and the
    diameter of its star. The faster the exoplanet is moving, the shorter the
    transit time. The transit time is the time, in seconds, for the exoplanet
    to pass across its star (from an observed point on Earth).

    t_transit (s) = diameter of the star (km) / velocity of the exoplanet (km/s)

    Paramaters:
        r_star (flt): Input from user of radius of star, relative to the sun (km)
        velocity_exo (flt): Velocity of exoplanet, dependant on distance from
            its star and gravitational attraction of the star (km/s)
    Return:
        flt: The transit time of the exoplanet (s)
    """
    return (2 * r_star) / velocity_exo

def get_min_rel_intensity(r_exo, r_star):
    """ Determine the minimum relative intensity of the exoplanet's star from an
    observed point on Earth. The minimum intensity is when the exoplanet is
    completely in front of its star, that is when the star's intensity is the
    lowest. When an exoplanet is not in front of its star, the star's intensity
    is 1 (the maximum).

    i_relative = (area of star(km^2) - area of planet(km^2))/ area of star (km^2)

    Paramaters:
        r_exo (flt): Input from user of radius of exoplanet, relative to Earth (km^2)
        r_star (flt): Input from user of radius of star, relative to the sun (km^2)
    Return:
        flt: The minimum observed relative intensity of the exoplanet
    """
    return 1 - ((r_exo / r_star)**2)


######################  some constants used throughout ###########################

# This model detects exoplanets that are orbiting a star with the same size and mass as our sun
# Radius of star = radius of sun = 695,510km
r_star = 695510
# Radius of Earth = 6,371km
r_Earth = 6371
# Velocity of Earth = 30km per second
velocity_Earth = 30
# Distance from Earth to the sun = 148,180,000km
dist_Earth_sun = 148180000

######################  main body of the code here ###########################

# Write the rest of your code here.
# You may call on any of the above functions (and any other functions you chose to write)
# You may use any of the constants defined above throughout the main body of your code