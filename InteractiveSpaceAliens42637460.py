import math
from matplotlib.pyplot import xlabel, plot, ylabel, ylim, grid, show, title
from numpy.ma import arange, zeros, absolute

######################  some constants used throughout ###########################

# Model detects exoplanets that are orbiting a star with the same size and mass as our sun
# Radius of star = radius of sun = 695,510km (according to Google)
r_star = 695510

# The radius and velocity of the exoplanet is calculated as a proportion of the same for Earth
# Radius of Earth = 6,371km (according to Google)
r_Earth = 6371

# Velocity of Earth = 30km per second
velocity_Earth = 30
# Distance from Earth to the sun = 148,180,000km
dist_Earth_sun = 148180000

ascii_spaceship = """
        |
       / \.
      / _ \.
     |.o '.|
     |'._.'|
     |     |
   ,'|  |  |`.
  /  |  |  |  \.
  |,-'--|--'-.| 
"""
ascii_planet = """
                 *       +
           '                  |
       ()    .-.,="``"=.    - o -
             '=/_       \     |
          *   |  '=._    |
               \     `=./`,        '
            .   '=.__.=' `='      *
   +                         +
        O      *        '       .
"""

ascii_alien = """
                       .-.
        .-""`""-.    |(@ @)
     _/`oOoOoOoOo`\_ \ \-/
    '.-=-=-=-=-=-=-.' \/ \.
      `-=.=-.-=.=-'    \ /\.
         ^  ^  ^       _H_ \.
"""

ascii_telescope = """
 .    '                   .  "   '
            .  .  .                 '      '
    "`       .   .
                                     '     '
  .    '      _______________
          ==c(___(o(______(_()
                  \===\.
                   )===\.
                  /`/|\`\.
                 /`/|| \`\.
                /`/ ||  \`\.
               /`/  ||   \`\.
              /`/         \`\.
"""


######################  functions are defined here ###########################

# PROVIDED FUNCTIONS
def get_period_of_planet(dist_exo_star, velocity_exo):
    """ Determine the period of an exoplanet using the distance of the planet
    from its star and the velocity of the planet. The period is the time, in
    seconds, for the exoplanet to make one complete orbit around its star

    period [s] = circumference of orbit [km] / velocity of the exoplanet [km/s]

    Paramaters:
        dist_exo_star (flt): Input from user of the distance of the exoplanet
            from its star, relative to Earth and the sun [km]
        velocity_exo (flt): Velocity of exoplanet, dependant on distance from
            its star and gravitational attraction of the star [km/s]
    Return:
        flt: The period of the exoplanet [s]
    """
    return (2 * math.pi * dist_exo_star) / velocity_exo


def get_transit_time(velocity_exo):
    """ Determine the transit time of the exoplanet using its velocity and the
    diameter of its star. The faster the exoplanet is moving, the shorter the
    transit time. The transit time is the time, in seconds, for the exoplanet
    to pass across its star (from an observed point on Earth).

    transit time [s] = diameter of star [km] / velocity of exoplanet [km/s]

    Paramaters:
        velocity_exo (flt): Velocity of exoplanet, dependant on distance from
            its star and gravitational attraction of the star [km/s]
    Return:
        flt: The transit time of the exoplanet [s]
    """
    return (2 * r_star) / velocity_exo


def get_min_rel_intensity(r_exo):
    """ Determine the minimum relative intensity of the exoplanet's star from an
    observed point on Earth. The minimum intensity is when the exoplanet is
    completely in front of its star, that is when the star's intensity is the
    lowest. When an exoplanet is not in front of its star, the star's intensity
    is 1 (the maximum).

    relative intensity
        = (area of star[km**2] - area of planet[km**2]) / area of star[km**2]

    Parameters:
        r_exo (flt): Radius of exoplanet [km**2]
    Return:
        flt: The minimum observed relative intensity of the exoplanet
    """
    return 1 - ((r_exo / r_star) ** 2)


# ADDITIONAL FUNCTIONS
def drake_equation(c):
    """ Estimate the probability of finding civilisations in the Milky Way. The
    drake equation is used as a guide to determine the number of civilisations
    in our galaxy in which we could communicate (N). The most recent estimates
    are used for all variables, except 'c' which is supplied by the param.

    N = R * p * n * L * c
    R = 7 = average rate of star formation (per year) in the galaxy
    p = 0.5 = proportion of stars with planetary systems = 0.5
    n = 1 = number of planets per solar system with conditions suitable for life
    L = 10 = average lifetime (years) of a civilisation within detection window

    Paramaters:
        c (flt): proportion of potentially habitable planets on which a
         techonological civilisation develops (recent = 0.02)
    Return:
        flt: Number of civilisation in galaxy that can communicate with Earth
    """
    return 7 * 0.5 * 1 * 10000 * c


def get_r_exo(user_size):
    """ Determine the radius of the exoplanet, given a proportion to the radius
    of Earth.

    Radius of exoplanet [km] = radius of Earth [km] * user proportion

    Paramaters:
        user_size (flt): Proportion of the exoplanet relative to Earth
    Variables:
        r_Earth (flt): The radius of the earth [km]
    Return:
        flt: The radius of the exoplanet [km]
    """
    return r_Earth * user_size


def get_dist_exo_star(user_dist):
    """ Determine the radius of the exoplanet, given an input of the distance as
    a proportion of the distance of the Earth from the sun.

    Distance of exoplanet from star [km]
        = distance of Earth from the Sun [km] * user proportion

    Paramaters:
        user_dist (flt): Proportion of the distance of the exoplanet to its star
            relative to the Earth and the sun
    Variables:
        dist_Earth_sun (flt): The distance of the Earth from the sun [km]
    Return:
        flt: The distance of the exoplanet from its star [km]
    """
    return dist_Earth_sun * user_dist


def get_velocity_exo(dist_exo_star):
    """ Determine the velocity of the exoplanet, that is the speed at which the
    exoplanet travels. This is dependent on how far it is from its own star and
    the gravitational attraction of the star. The velocitity is calculated using
    the known velocity of the Earth with the proportional difference between
    the distance of Earth and the sun, and the exoplanet and its star.

    velocity of exoplanet [km/s] = velocity of Earth [km/s]
        * sqrt(distance of Earth from the sun [km]
            / distance of exoplanet from it's star [km])

    Paramaters:
        dist_exo_star (flt): The distance of the exoplanet from its star [km]
    Variables:
        velocity_Earth (flt): The speed at which the Earthtravels [km/s]
        dist_Earth_sun (flt): The distance of the Earth from the sun [km]
    Return:
        flt: The velocity of the exoplanet [km/s]
    """
    return velocity_Earth * math.sqrt(dist_Earth_sun / dist_exo_star)


def get_t_times(transit_time, midpoint):
    """ Calculate the intensity of the light from the star for a series of times
    and store these values in an array. The times start from half the time before
    the the start of the transit and half the time after the transit to represent
    the difference between the exoplanet not in front of its star (time of
    relative intensity of 1) and when it is transiting its star (either
    overlapping or in front of its star)

    Parameters:
        transit_time (flt): The time for the exoplanet to cross its star [s]
        midpoint (flt): Half the transit time [s]
    Return:
        array: Times [s] starting from equal distances of max relative intensity
            in intervals of 60s
    """
    return arange(0 - midpoint, transit_time + midpoint, 60)


def get_x_positions(r_exo, t_times, velocity_exo):
    """ Calculate the position of the exoplanet for a set of times. The position
    and time are related by velocity

    position of exoplanet [km] = last position of exoplanet before transit [km]
        + (velocity of exoplanet [km/s] * array of times [s])

    Parameters:
        r_exo (flt): The radius of the exoplanet [km]
        t_times (flt array): An array of times in 1 minute intervals for the
            duration of the exoplanet's transit time plus 1 more step [s]
        velocity_exo (flt): The velocity of the exoplanet [km/s]
    Variables:
        x_zero (flt): Starting x_position [km], last position of the exoplanet
        before it starts to cross its star. (i.e. last position where intensity
        is equal to 1 before decreasing)
    Return:
        array: Positions [km] of the planet as the exoplanet transits its star
    """
    x_zero = -r_star - r_exo
    return x_zero + (velocity_exo * t_times)


def get_y_intensity(r_exo, x_positions, min_rel_intensity):
    """ Calculate the relative intensity of each position of the exoplanet during
    its transit across its star.

    The intensity depends on where the exoplanet is relative to its star:
        NO overlap of star (x_out) = max intensity = 1
        FULL overlap of star (x_in) = minimum relative intensity of star
        PARTIAL overlap of star = 1
            - ((current position - no overlap) / (full overlap - no overlap))
            * (1 - minimum relative intensity)

    Parameters:
        r_exo (flt): The radius of the exoplanet [km]
        x_positions (flt): An array of positions of the planet as the exoplanet
            transits its star [km]
        min_rel_intensity: The intensity of the exoplanet when it has full
            overlap with its star
    Variables:
        x_out (flt): Absolute position of exoplanet when it has no overlap
        x_in (flt): Absolute position of the exoplanet when it has full overlap
    Return:
        array: Intensity for each x_position of exoplanet as crosses its star
    """
    x_out = r_star + r_exo
    x_in = r_star - r_exo

    # Create an empty array for the intensity - size should be same as positions
    y_intensity = zeros(len(x_positions))
    # Calculate relative intensity for each position, based on relative to star
    i = 0
    while i < len(x_positions):
        # For every position in x_positions, assign an intensity in y_positions
        x = absolute(x_positions[i])
        if x > x_out:
            # Exoplanet has no overlap with star
            y_intensity[i] = 1
        elif x < x_in:
            # Exoplanet has full overlap with star
            y_intensity[i] = min_rel_intensity
        else:
            # Exoplanet overlapping the edge of the star
            y_intensity[i] = 1 - (
                    ((x - x_out) / (x_in - x_out)) * (1 - min_rel_intensity))
        i = i + 1
    return y_intensity


def get_intensity_plot(transit_time, velocity_exo, r_exo, min_rel_intensity):
    """Plot the intensity of the exoplanet as it transits its star in a graph. A
    series of times of the exoplanet are plotted against the intensity of the
    exoplanet at each position [km] in time [s]

    Parameters:
        transit_time(flt): The time for the exoplanet to cross its star [s]
        velocity_exo (flt): The velocity of the exoplanet [km/s]
        r_exo (flt): The radius of the exoplanet [km]
        min_rel_intensity: Intensity of star when an exoplanet has full overlap
    Variables:
        t_times: An array of times from 0 to one step after the transit time [s]
        x_positions: An array of positions of the planet as the exoplanet
            transits its star [km]
        y_intensity: An array of intensity's for each position of the exoplanet
            as it transits across its star.
    """

    # Plot the intensity of light from the star against the times of transit
    print(
        "This graph shows the relative intensity of light for a star as your exoplanet travels across the face of it."
        "\n"
        "\nWhen the relative intensity is ..."
        "\n\t 1 \t\t the exoplanet is not in front of the star \t\t (there is no overlap)"
        "\n\t min \t the exoplanet is completely in front of the star \t (full overlap)."
        "\n\t other \t the exoplanet is crossing the border of the star \t (partial overlap")

    # get the midpoint of the transit time
    midpoint = transit_time / 2
    # Create an array of times (60s) as exoplanet transit star
    t_times = get_t_times(transit_time, midpoint)
    # Calculate the position of the exoplanet at each time
    x_positions = get_x_positions(r_exo, t_times, velocity_exo)
    # Calculate the intensity of light at each position
    y_intensity = get_y_intensity(r_exo, x_positions, min_rel_intensity)

    # plot times as hours from midpoint
    t_times = (t_times - midpoint) / 3600
    plot(t_times, y_intensity, 'k')
    title("Relative intensity of a star during the transit of an exoplanet")
    xlabel("Time from midpoint of transit (hours)")
    ylabel("Relative light intensity")
    grid(True)
    show()

    # todo: (c) Write a short paragraph about the limitation of the modelling
    print("\nThe limitation of this model is ......")


def get_detection(min_rel_intensity):
    """Determine whether the exoplanet can be detected given the change in
    observed intensity of it's star from Earth.The detection limit to observe a
    planet is an intensity decrease of 1 part in 10.00 as the exoplanet transits
    its star. The time at which the this happens is commented on.

    Parameters:
        min_rel_intensity: Intensity of star when an exoplanet has full overlap
    """
    if min_rel_intensity <= 0.9999:
        return True


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
          "This is an exhibit on exoplanets.........\n",
          ascii_spaceship)
    patron_type = float(
        input("Are you a science rookie (1) or a science enthusiast (2)? "))

    # Remaining steps and text differ for each patron_type
    if patron_type == 1:
        # ROOKIE
        # Part A - Searching for other civilisations
        # Step 2 - Estimates of civilisations with technology multiplied by 10,000 for easier proportional understanding
        print("\n*LETS IMAGINE TALKING WITH OTHER LIFE FORMS*\n"
              "\nThe drake equation is used to guess the chance of finding life on other planets in our galaxy that we would be able to understand.\n"
              "To work this out we need to know how many planets could have life forms that use technology.\n"
              "Some guesses to this question have been that out of 10,000 planets there is 1 planet like this and more recently 200 planets.\n"
              "\nNow it's your turn to guess!", ascii_alien)

        # Step 3 - Divide c by 10,000 to convert to proportion for drake equation
        c = float(input(
            "How many planets do you think there are with technology out of 10,000? "))
        num_civil = drake_equation(c/ 10000)

        # Step 4
        print(
            "\nWith your guess, the number of planets in our galaxy that we could talk to are: ",
            round(num_civil, 2))

        # Part B - Searching for exoplanets
        # Step 5
        print("\n*NOW, LETS FIND SOME NEW PLANETS*\n"
              "\nExoplanets are planets that are not a part of our solar system and so they have their own suns.\n"
              "We can try and find these other planets by watching these other suns and measuring the light from them.\n"
              "If the sun has less light then a planet must be blocking it. Like when the moon blocks our sun.\n"
              "There is a telescope that is very good at finding other planets this way and has found thousands.\n"
              "\nNow it's your turn to try and find an exoplanet!", ascii_telescope)

       # Point where user can search for exoplanets continuously
        while search == 1:
            # Step 6 - Divide by 100 to convert to proportion
            user_size = float(input(
                "What is the size of the planet you want to find, compared to Earth? (%)\n"
                "(50) Half the size\n"
                "(100) The same size\n"
                "(200) Double the size\n")) / 100
            # Step 7 - Divide by 100 to convert to proportion
            user_dist = float(input(
                "How far away from its sun do you want the planet to be, compared to Earth's distance to our sun? (%)\n"
                "(50) Closer by half\n"
                "(100) The same distance\n"
                "(200) Twice as far\n")) / 100
            # Step 8
            r_exo = get_r_exo(user_size)
            dist_exo_star = get_dist_exo_star(user_dist)
            velocity_exo = get_velocity_exo(dist_exo_star)

            # convert secs to days
            period = get_period_of_planet(dist_exo_star, velocity_exo) / 86400
            # convert secs to hours
            transit_time = get_transit_time(velocity_exo) / 3600
            min_rel_intensity = get_min_rel_intensity(r_exo)

            print(
                "\nThere are now three important things we know about your exoplanet: "
                "\n(1) The time it takes for your planet to go completely around its star (this is 1 year for Earth) is ",
                round(period, 2), " days"

                                  "\n(2) The time it takes for your planet to move acros its star (the bigger the star, the longer this will be) is",
                round(transit_time, 2), " hours"

                                        "\n(3) The brightness of your planet's star from Earth when it is being blocked by your planet is ",
                round(min_rel_intensity, 6))

            # Step 9 - NOT an enthusiast so continue
            # Step 10
            get_detection(min_rel_intensity)
            print(
                "To properly find your planet we need to watch the change in light for at least ",
                round(period * 3, 2), " days")

            # Step 11
            search = float(input("\nDo you want to search again?\n"
                                 " (1) Yes\n"
                                 " (0) NO\n"))


    else:
        # ENTHUSIAST
        # Part A - Searching for other civilisations
        # Step 2
        print("\n*LETS IMAGINE POTENTIAL CIVILISATIONS IN THE MILKY WAY*\n"
              "\nThe drake equation is used as a guide to speculate the probability of finding "
              "\ncivilisations in the Milky Way with whom it may be possible to communicate."
              "\n"
              "\nOne of the factors of this equation is estimating the proportion of potentially "
              "\nhabitable planets on which a technological civilisation develops."
              "\n"
              "\nIn 1960's the proportion was estimated at 0.0001 and more recently at 0.02. ",
              ascii_alien,
              "\nNow its your turn to estimate!")
        # Step 3
        c = float(input("\nQ: What do you think is the proportion? "))
        num_civil = drake_equation(c)
        # Step 4
        print(
            "\nA: Using your proportion and the most recent estimates for all other factors,"
            "\nthere are", round(num_civil), "civilisations in the galaxy that can communicate with Earth!"
            "\n"
            "\nThis is pretty amazing! Maybe UFO's aren't a conspiracy after all?"
            "\nSo all these civilisations must be living somewhere, but where?")

        # Part B - Searching for exoplanets
        # Step 5
        print("\n*LETS FIND SOME EXOPLANETS*\n"
              "\nExoplanets are planets that orbit around stars other than our sun. We can detect "
              "\nexoplanets by observing the intensity of the light emitted by another star in our "
              "\ngalaxy as a function of time."
              "\n"
              "\nIf an exoplanet passes in front of this star, it partially blocks the star and the "
              "\nmeasured intensity of the star will slightly decrease. Multiple measurements at "
              "\nregular intervals can be used to confirm the existence of an exoplanet."
              "\n"
              "\nThis method has been very succesful at detecting exoplanets. The Kepler space "
              "\ntelescope, which uses this approach, has detected several thousand exoplanets.",
              ascii_telescope,
              "\nNow it's your turn to try and find an exoplanet!")

        print("\n--STEP 1--\n"
              "\nTo model the transit of the exoplanet in front its star, we need to specify the size of "
              "\nthe planet and the distance of that planet from its star.")
        # Point where user can search for exoplanets continuously
        while search == 1:
            # Step 6
            print("\nAs a proportion of Earth and our sun...")
            user_size = float(input(
                "\nQ: What is the size of the planet you want to find?"                
                "  \n(0.5) Half the size of Earth"
                "  \n(1) Same size as Earth"
                "  \n(2) Twice as big"))
            # Step 7 Ask the user for the distance of the planet to its star
            user_dist = float(input(
                "\nQ: How far away from its star do you want the planet to be?"               
                "  \n(0.5) Closer by half"
                "  \n(1) Same distance"
                "  \n(2) Twice as far"))
            # Step 8
            print("\n--STEP 2--\n"
                  "\nThere are now three important factors that we know about your exoplanet:")
            r_exo = get_r_exo(user_size) #km
            dist_exo_star = get_dist_exo_star(user_dist) #km
            velocity_exo = get_velocity_exo(dist_exo_star) #km/s

            period = get_period_of_planet(dist_exo_star, velocity_exo)
            transit_time = get_transit_time(velocity_exo)
            min_rel_intensity = get_min_rel_intensity(r_exo)

            # convert Peroid (s to days) and transit time (s to hr)
            print("\n(1) Period of orbit is", round(period / 86400, 2), "days"
                "\nThis is the time for the exoplanet to make one complete orbit around its star (this is 1 year for Earth). "
                "\nThe period of orbit is determined by the exoplanet's speed, and the distance the exoplanet is from its star."
                "\n"
                "\n(2) Transit time is", round(transit_time / 3600, 2),"hours"
                "\n he velocity of the exoplanet and the diameter of its star will determine the transit time. "
                "\nThe faster the exoplanet is moving, the shorter the transit time."
                "\nLikewise the larger the diameter of the star, the longer the transit time."
                "\n"
                "\n(3) Minimum relative intensity is ", round(min_rel_intensity, 6),
                "\n This is when the exoplanet is fully between Earth and the star i.e. completely overlapping its star."
                "\n The intensity of the star observed from Earth will be decreased as the exoplanet blocks some of the light.")

            # Step 9 - Is an enthusiast
            print("\n--STEP 3--\n")
            get_intensity_plot(transit_time, velocity_exo, r_exo, min_rel_intensity)

            # Step 10



            print("\n--STEP 4--\n"
                  "\nThe detection limit for Kepler to find a planet is an intensity decrease of 1 part in 10 as the exoplanet transits the star."
                  "\n"
                  "\nTo confirm the existence of an exoplanet multiple measurements at regular intervals (at least 3 periods) can be used.",
                  ascii_planet)
            print("\nFor your planet..")
            if get_detection(min_rel_intensity):
                print("\nThe intensity decreased enough so We detected your planet!!!")
                # convert period to days and multiply by 3
                print("To confirm its existence, we would need to take measurements for", round((period / 31536000) * 3, 2), "years")
            else:
                print("\nThe intensity didn't decrease enough to find it.")

            # Step 11
            search = float(input("\nDo you want to search again?\n"
                                 " (1) Yes\n"
                                 " (0) NO\n"))

    # Step 12
    print("Thanks for searching!")


if __name__ == "__main__":
    main()
