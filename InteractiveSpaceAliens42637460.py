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
    return 1 - ((r_exo / r_star) ** 2)


def drake_equation(c):
    """ The drake equation is used as a guide to determine the number of civilisations
    in our galaxy in which we could communicate (N).

    N = R * p * n * L * c
        R = average rate of star formation (per year) in the galaxy
            (estimates: 1960 = 10, recent = 7)
        p = proportion of stars with planetary systems
            (estimate (1960 and recent) : 0.5)
        n = number of planets per solar system with conditions suitable for life
            (estimates: 1960 = 2, recent = 1)
        L = average lifetime (in years) of such a civilisation within the detection window
            (estimate: 10)

    Paramaters:
        c (flt): proportion of potentially habitable planets on which a techonological civilisation develops
            (estimates: 1960 = 0.0001, recent  0.02)
    Return:
        flt: N - The number of civilisation in the galaxy that can communicate with Earth
    """
    return 7 * 0.5 * 1 * 10000 * c


######################  some constants used throughout ###########################

# Model detects exoplanets that are orbiting a star with the same size and mass as our sun
# Radius of star = radius of sun = 695,510km
r_star = 695510

# The radius and velocity of the exoplanet is calculated as a proportion of the same for Earth
# Radius of Earth = 6,371km
r_Earth = 6371
# Velocity of Earth = 30km per second
velocity_Earth = 30
# Distance from Earth to the sun = 148,180,000km
dist_Earth_sun = 148180000

######################  main body of the code here ###########################

def main():
    """ Logic for the exhibit item on exoplanets at the Science musuem as part
    of the 'Exploring Our Galaxy Exhibit'

    Step 1. Introductory message for all patrons and prompt for patron_type
    Step 2. Print an intro about other potential civilisations in our galaxy
    Step 3. Ask user what they think is the proportion (or percentage) of
        habitable planets that develop technological civilisations
    Step 4. Calculate and print N using their estimation, with a useful message
    Step 5. Introduce the idea of searching for planets around stars other than
        our own
    Step 6. Ask the user for the relative size of the planet they want to find
        (relative to Earth)
    Step 7. Ask the user for the distance of the planet to its star
        (relative to the Earth's distance from the sun)
    Step 8. Calculate and print each of these values with useful messages
        (a) the period for the planet's orbit using get_period_of_planet
        (b) the transit time for the planet using get_transit_time
        (c) the minimum relative intensity of the planet using get_min_rel_intensity
    Step 9. The user is not an enthusasiast so continue
    Step 10. Inform the user whether their chosen planet could be detected or not
    Step 11. Ask the user if they want to try again with another exoplanet search
    Step 12. Print a farewell message

     Variables:
        patron_type (int): Whether the user is an enthusasist or a rookie
        search (Boolean):
     """
    # Step 1
    # todo: Write introduction to exhibit
    print("Welcome to 'Exploring Our Galaxy'!\n"
          "This is an exhibit on exoplanets.........\n")
    patron_type = float(
        input("Are you a science rookie (1) or a science enthusiast (2)? "))

    # Remaining steps and text differ for each patron_type
    if patron_type == 1:
        # ROOKIE
        # Part A - Searching for other civilisations
        # Step 2 - Estimates of civilisations with technology multiplied by 10,000 for easier proportional understanding
        print("\n*LETS IMAGINE TALKING WITH OTHER LIFE FORMS*\n"
              "The drake equation is used to guess the chance of finding life on other planets in our galaxy that we would be able to talk to.\n"
              "To work this out we need to know how many planets could have life forms that use technology.\n"
              "Some guesses to this question have been that out of 10,000 planets there is 1 planet like this and more recently 200 planets.\n"
              "\nNow its your turn to estimate!")
        # Step 3 - Divide c by 10,000 to convert to proportion for drake equation
        c = float(input("How many planets do you think there are with technology out of 10,000? ")) / 10000
        # Step 4
        print("\nWith your guess, the number of planets in our galaxy that we could talk to are: ", round(drake_equation(c), 2))

    else:
        # ENTHUSIAST
        # Part A - Searching for other civilisations
        # Step 2
        print("\n*LETS IMAGINE POTENTIAL CIVILISATIONS IN THE MILKY WAY*\n"
              "\nThe drake equation is used as a guide to speculate the probability of finding civilisations in the Milky Way with whom it may be possible to communicate.\n"
              "One of the factors of this equation is estimating the proportion of potentially habitable planets on which a technological civilisation develops.\n"
              "In 1960's the proportion was estimated at 0.0001 and more recently it was estimated at 0.02. \n"
              "\nNow its your turn to estimate!")
        # Step 3
        c = float(input("What do you think is the proportion? "))
        # Step 4
        print("\nUsing your proportion and the most recent estimates for all other factors, the number of civilisations in the galaxy that can communicate with Earth is: ",
            round(drake_equation(c), 2))


if __name__ == "__main__":
    main()
