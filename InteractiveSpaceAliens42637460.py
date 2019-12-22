import math

from pylab import *


######################  functions are defined here ###########################

# PROVIDED FUNCTIONS
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

# ADDITIONAL FUNCTIONS
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
        L = average lifetime (years) of a civilisation within the detection window
            (estimate: 10)

    Paramaters:
        c (flt): proportion of potentially habitable planets on which a
        techonological civilisation develops
            (estimates: 1960 = 0.0001, recent  0.02)
    Return:
        flt: Number of civilisation in the galaxy that can communicate with Earth (N)
    """
    return 7 * 0.5 * 1 * 10000 * c

def get_r_exo(user_size):
    """ Determine the radius of the exoplanet given an input from the user as a
    proportion of the size of Earth.

    Paramaters:
        user_size (flt): Proportion of the exoplanet relative to the size of Earth
    Variables:
        r_Earth (flt): The radius of the earth (km)
    Return:
        flt: The radius of the exoplanet (km)
    """
    return r_Earth * user_size

def get_dist_exo_star(user_dist):
    """ Determine the radius of the exoplanet given an input from the user as a
    proportion of the distance of the Earth from the sun.

    Paramaters:
        user_dist (flt): Proportion of the distance of the exoplanet to its star
            relative to the Earth and the sun
    Variables:
        dist_Earth_sun (flt): The distance of the Earth from the sun (km)
    Return:
        flt: The distance of the exoplanet from its star(km)
    """
    return dist_Earth_sun * user_dist

def get_velocity_exo(user_dist):
    """ Determine the velocity of the exoplanet given the velocity of the Earth,
    the distance of the Earth from the sun and the distance of the exoplanet
    from its star. The velocity is the speed at which it travels.

    Paramaters:
        user_dist (flt): Proportion of the distance of the exoplanet to its star
            relative to the Earth and the sun
    Variables:
        velocity_Earth (flt): The speed at which the Earthtravels (km/s)
        dist_Earth_sun (flt): The distance of the Earth from the sun (km)
        dist_exo_star (flt): The distance of the exoplanet from its star (km)
    Return:
        flt: The velocity of the exoplanet (km/s)
    """
    dist_exo_star = get_dist_exo_star(user_dist)
    return velocity_Earth * math.sqrt(dist_Earth_sun / dist_exo_star)

def get_exo_outputs(user_size, user_dist):
    """ Calculate the outputs of the exoplanets using the patron's input for the
    size of the exoplanet and the distance of the exoplanet from its star,
    relative to the Earth and the sun

    Parameters:
        user_size (flt): Proportion of the exoplanet relative to the size of Earth
        user_dist (flt): Proportion of the distance of the exoplanet to its star
            relative to the Earth and the sun
    Variables:
        r_exo (float): Radius of the exoplanet, proportional to the Earth
        dist_exo_star (float): The distance of the exoplanet to its star,
            proportational to Earth
        velocity_exo (float): The velocity of the exoplanet
        outputs:Array containing these parameters of the exoplanet
    Return:
        array: outputs containing appropriately converted period, transit_time
            and min_intensity of the exoplanet
    """

    r_exo = get_r_exo(user_size)
    dist_exo_star = get_dist_exo_star(user_dist)
    velocity_exo = get_velocity_exo(user_dist)
    outputs = ["period", "transit_time", "min_intensity"]

    # Period - convert from seconds to days
    outputs[0] = float(get_period_of_planet(dist_exo_star, velocity_exo))/86400
    # Transit time - convert from seconds to hours
    outputs[1] = float(get_transit_time(velocity_exo, r_star))/3600
    outputs[2] = float(get_min_rel_intensity(r_exo, r_star))
    return outputs

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
    # Define constant to allow user to continuously search for exoplanets in step 11
    search = 1

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

        # Part B - Searching for exoplanets
        # Step 5
        print("\n*NOW, LETS FIND SOME NEW PLANETS*\n"
              "Exoplanets are planets that are not a part of our solar system and so they have their own suns.\n"
              "We can try and find these other planets by watching these other suns and measuring the light from them.\n"
              "If the sun has less light then a planet must be blocking it. Like when the moon blocks our sun.\n"
              "There is a telescope that is very good at finding other planets this way and has found thousands.\n"
              "\nNow it's your turn to try and find an exoplanet!")
        # Point where user can search for exoplanets continuously
        while search == 1:
            # Step 6
            user_size = float(input("What is the size of the planet you want to find, compared to Earth? (%)\n"
                "(50) Half the size\n"
                "(100) The same size\n"
                "(200) Double the size\n")) / 100
            # Step 7
            user_dist = float(input("How far away from its sun do you want the planet to be, compared to Earth's distance to our sun? (%)\n"
                "(50) Closer by half\n"
                "(100) The same distance\n"
                "(200) Twice as far\n")) / 100
            # Step 8
            outputs = get_exo_outputs(user_size, user_dist)
            print(
                "\nThere are now three important things we know about your exoplanet: "
                "\n(1) The time it takes for your planet to go completely around its star (this is 1 year for Earth) is ", round(outputs[0], 2), " days"
                "\n(2) The time it takes for your planet to move acros its star (the bigger the star, the longer this will be) is", round(outputs[1], 2), " hours"
                "\n(3) The brightness of your planet's star from Earth when it is being blocked by your planet is ", round(outputs[2], 6))

            # Step 11
            search = float(input("\nDo you want to search again?\n "
                                 " (1) Yes\n"
                                 " (0) NO\n"))

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

        # Part B - Searching for exoplanets
        # Step 5
        print("\n*NOW, LETS FIND SOME EXOPLANETS*\n"
              "\nExoplanets are planets that orbit around stars other than our sun.\n"
              "We can detect exoplanets by observing the intensity of the light emitted by another star in our galaxy as a function of time.\n"
              "If an exoplanet passes in front of this star, it partially blocks the star and the measured intensity of the star will slightly decrease.\n"
              "Multiple measurements at regular intervals can be used to confirm the existence of an exoplanet.\n"
              "This method has been very succesful at detecting exoplanets. The Kepler space telescope, which uses this approach, has detected several thousand exoplanets.\n"
              "To model the transit of the exoplanet in front its star, we need to specify the size of the planet and the distance of that planet from its star.\n"
              "\nNow it's your turn to try and find an exoplanet!")
        # Point where user can search for exoplanets continuously
        while search == 1:
            # Step 6
            user_size = float(input("What is the size of the planet you want to find, as a percentage of Earth?\n"
                                    " For example:\n"
                                    "  (0.5) Half the size of Earth (0.5)\n"
                                    "  (1) Same size as Earth\n"
                                    "  (2) Twice as big\n"))
            # 7. Ask the user for the distance of the planet to its star (relative to the Earth's distance from the sun)
            user_dist = float(input("How far away from its star do you want the planet to be, as a percentage of Earth's distance to the sun?\n"
                                    " For example:\n"
                                    "  (0.5) Closer by half\n"
                                    "  (1) Same distance\n"
                                    "  (2) Twice as far\n"))
            # Step 8
            outputs = get_exo_outputs(user_size, user_dist)
            print("\nNow, there are three important factors that need to be calculated to detect your exoplanet:\n"
                "\n(1) Period of orbit is ", round(outputs[0], 2), " days"
                "\nThis is the time for the exoplanet to make one complete orbit around its star (this is 1 year for Earth).\n"
                "The period of orbit is determined by the exoplanet's speed, and the distance the exoplanet is from its star.\n"

                "\n(2) Transit time is ", round(outputs[1], 2), " hours"
                "\nThe velocity of the exoplanet and the diameter of its star will determine the transit time.\n"
                "The faster the exoplanet is moving, the shorter the transit time and likewise the larger the diameter of the star, the longer the transit time.\n"

                "\n(3) Minimum relative intensity is ", round(outputs[2], 2),
                "\nWhen the exoplanet is fully between Eath and the exoplanet's star, the intensity of the star observed from Earth will be decreased as the exoplanet blocks some of the light from the star.\n"
                "We can define a relative intensity as the ratio of the observed intensity when the exoplanet is in front of the star to the observed intensity when the exoplanet is not in front of the star.")

            # Step 11
            search = float(input("\nDo you want to search again?\n"
                                 " (1) Yes\n"
                                 " (0) NO\n"))

    # Step 12
    print("Thanks for searching!")

if __name__ == "__main__":
    main()
