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

ascii_rocket_launch =  """
                    .   
                   .'.
                   |o|
                  .'o'.
                  |.-.|
                  '   '
                   ( )
                    )
                   ( )
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

ascii_space = """
   .       . 
 +  :      .
           :       _
       .   !   '  (_)
          ,|.' 
-  -- ---(-O-`--- --  -
         ,`|'`.
       ,   !    .
           :       :  " 
           .     --+--
 .:        .       !
 """

ascii_rocket_landed = """
                           *     .--.
                                / /  `
               +               | |
                      '         \ \__,
                  *          +   '--'  *
                      +   /\.
         +              .'  '.   *
                *      /======\      +
                      ;:.  _   ;
                      |:. (_)  |
                      |:.  _   |
            +         |:. (_)  |          *
                      ;:.      ;
                    .' \:.    / `.
                   / .-'':._.'`-. \.
                   |/    /||\    \|
                 _..--''''````''''--.._
           _.-'``                    ``'-._
         -'                                '-
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
    print("\nIntensity \t| Exoplanet position \t\t\t| Overlap with star"
          "\n------------------------------------------------------------------"
          "\n 1 \t\t| not in front of the star \t\t| None"
          "\n minimum \t| completely in front of the star \t| Full"
          "\n other \t\t| crossing the border of the star \t| Partial")

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
        # Intensity has decreased enough to detect a planet
        return True


def search_again():
    print(ascii_space)
    user = float(input("\nDo you want to search again?"
                         "\n\t(0) Yes"
                         "\n\t(1) NO"))
    if user == 0:
        return True


######################  main body of the code here ###########################

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
    search (boolean): Default is true to continue search
 """
# Define constant to allow user to continuously search for exoplanets in step 11
searching = True

# STEP 1
print("Hope you have been enjoying your time 'Exploring Our Galaxy!'"      
      "\n"
      "\nBy know you know that our galaxy is a huge mystery with so much we don't know about."
      "\n"
      "\nSo it's easy to start wondering, are there other life forms out there?"
      "\nIf so, where do they live and how do we find their home?"
      "\n"
      "\nJump aboard and let's find out!",
      ascii_spaceship)
patron_type = float(input("\nBefore you start your adventure, When it comes to science are you...\n"
                          "\t(0) a rookie, or\n"
                          "\t(1) an enthusiast\n"))

# Remaining steps and text differ for each patron_type
if patron_type == 0:
    # ROOKIE
    print("\nWelcome aboard Rookie! Let's start the countdown..."
          "\n\t3, \t2, \t1, \tBLAST OFF",
          ascii_rocket_launch)
    # Part A - Searching for other civilisations
    # STEP 2 - Estimates multiplied by 10,000
    print("\n*LET'S IMAGINE TALKING WITH ALIENS*"
          "\n"
          "\nHave you ever wondered the possibility of finding other life forms?"
          "\nWell, there is an equation that is used to guess the chance of finding life on other planets that we would be able to understand."
          "\n"
          "\nTo work this out we need to know how many planets could have life forms that use technology."
          "\n"
          "\nSome guesses to this question have been that out of 10,000 planets there is 1 planet and more recently 200 planets.",
          ascii_alien)

    # STEP 3
    print("\n--Now it's your turn to guess!--")
    c = float(input(
        "\nQ: Out of 10,000 planets, how many planets do you think there are with technology? "))
    # Divide by 10,000 to get as proportion for drake equaiton
    num_civil = drake_equation(c / 10000)

    # Step 4
    print(
        "\nA: With your guess, there are", round(num_civil), "planets in our galaxy that we could talk to."
        "\n"
        "\nThis is pretty amazing! Maybe UFO's aren't a conspiracy after all?"
        "\nSo all these aliens must be living somewhere, but where?")

    # Part B - Searching for exoplanets
    # Step 5
    print("\n*LETS FIND SOME NEW PLANETS*"
          "\n"
          "\nExoplanets are planets that are not a part of our solar system and so they have their own suns."
          "\n"
          "\nWe can try and find these other planets by watching these other suns and measuring the light from them here on Earth."
          "\nIf the sun has less light then a planet must be blocking it. Like when the moon blocks our sun."
          "\n"
          "\nThere is a telescope that is very good at finding other planets this way and has found thousands.",
          ascii_telescope)

   # Point where user can search for exoplanets continuously
    while searching:
        print("\n--Now it's your turn to try and find an exoplanet!--"
              "\nTo know the change in light we need to know the size of you planet and how far it is from its sun.")
        # Step 6 - Divide by 100 to convert to proportion
        print("\nAs a percentage of Earth and our sun...")
        user_size = float(input(
            "\nQ: What is the size of the planet you want to find? (%)"
            "\n\t(50) Half the size"
            "\n\t(100) The same size"
            "\n\t(200) Double the size")) / 100
        # Step 7 - Divide by 100 to convert to proportion
        user_dist = float(input(
            "\nQ: How far away from its sun do you want the planet to be? (%)"
            "\n\t(50) Closer by half"
            "\n\t(100) The same distance"
            "\n\t(200) Twice as far")) / 100
        # Step 8
        print("\n--There are now three important things we know about your exoplanet--")
        r_exo = get_r_exo(user_size)  # km
        dist_exo_star = get_dist_exo_star(user_dist)  # km
        velocity_exo = get_velocity_exo(dist_exo_star)  # km/s

        period = get_period_of_planet(dist_exo_star, velocity_exo)  # s
        transit_time = get_transit_time(velocity_exo)  # s
        min_rel_intensity = get_min_rel_intensity(r_exo)

        print("\n(1) The time it takes for your planet to go completely around its star (this is 1 year for Earth) is ",
            round(period / 86400, 2), " days"

                              "\n(2) The time it takes for your planet to move across its star (the bigger the star, the longer this will be) is",
            round(transit_time / 3600, 2), " hours"

                                    "\n(3) The brightness of your planet's star from Earth when it is being blocked by your planet is ",
            round(min_rel_intensity, 6), ascii_planet)

        # Step 9 - NOT an enthusiast so continue
        # Step 10
        print("\n--Now let's see if we can find your planet--\n"
              "\nTo find your planet we need to see a certain amount of change in the light of your planet's sun as your planet blocks it."
              "\nOnce we know if the change is enough, we need to watch it go around its sun at least 3 times to be sure.")
        if get_detection(min_rel_intensity):
            print("\nA: Yay - We found your planet!!!")
            # convert period to from seconds to years and multiply by 3
            print("To be sure we need to watch it for",
                  round((period / 31536000) * 3, 2), "years")
        else:
            print("\nA: Too bad - We couldn't find your planet")
        # Step 11
        searching = search_again()

else:
    # ENTHUSIAST
    print("\nWelcome aboard Enthusiast! Let's start the countdown..."
          "\n\t3, \t2, \t1, \tBLAST OFF",
          ascii_rocket_launch)
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
          ascii_alien)
    # Step 3
    print("\n--Now its your turn to estimate!--")
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
          ascii_telescope)

    print("\n--Now it's your turn to try and find an exoplanet!--\n"
          "\nTo model the transit of the exoplanet in front its star, we need to specify the size of "
          "\nthe planet and the distance of that planet from its star.")
    # Point where user can search for exoplanets continuously
    while searching:
        # Step 6
        print("\nAs a proportion of Earth and our sun...")
        user_size = float(input(
            "\nQ: What is the size of the planet you want to find?"                
            "\n\t(0.5) Half the size of Earth"
            "\n\t(1) Same size as Earth"
            "\n\t(2) Twice as big"))
        # Step 7 Ask the user for the distance of the planet to its star
        user_dist = float(input(
            "\nQ: How far away from its star do you want the planet to be?"               
            "\n\t(0.5) Closer by half"
            "\n\t(1) Same distance"
            "\n\t(2) Twice as far"))
        # Step 8
        print("\n--There are now three important factors that we know about your exoplanet--")
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
            "\nThe velocity of the exoplanet and the diameter of its star will determine the transit time. "
            "\nThe faster the exoplanet is moving, the shorter the transit time."
            "\nLikewise the larger the diameter of the star, the longer the transit time."
            "\n"
            "\n(3) Minimum relative intensity is ", round(min_rel_intensity, 6),
            "\nThis is when the exoplanet is fully between Earth and the star i.e. completely overlapping its star."
            "\nThe intensity of the star observed from Earth will be decreased as the exoplanet blocks some of the light.",
            ascii_planet)

        # Step 9 - Is an enthusiast
        print("\n--Let's see a graph of how the light intensity changes as your exoplanet travels across its face--\n")
        get_intensity_plot(transit_time, velocity_exo, r_exo, min_rel_intensity)

        # Step 10
        print("\n--Let's see if we can detect your planet--\n"
              "\nThe detection limit for Kepler to find a planet is an intensity decrease of 1 part in 10 as the exoplanet transits the star."
              "\n"
              "\nTo confirm the existence of an exoplanet multiple measurements at regular intervals (at least 3 periods) can be used.")

        if get_detection(min_rel_intensity):
            print("\nA: The intensity decreased enough so We detected your planet!!!")
            # convert period to days and multiply by 3
            print("To confirm its existence, we would need to take measurements for", round((period / 31536000) * 3, 2), "years")
        else:
            print("\nA: The intensity didn't decrease enough to find it.")

        # Step 11
        searching = search_again()

# Step 12
print("\nWelcome back to Earth!"
      "\nEnjoy your continued adventure of exploring the wonders of our galaxy."
      "\n"
      "\nAnd don't forget to keep your eyes open for any UFO's.",
      ascii_rocket_landed)