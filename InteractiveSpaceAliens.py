from pylab import *

######################  bibliography  ###########################
"""
ASCII Art Archive. (2019). Space. Retrieved from https://www.asciiart.eu/space
Herman, R. (1998). How fast is the Earth Moving? Scientific American. Retrieved from https://www.scientificamerican.com/article/how-fast-is-the-earth-mov/
Howell, E. (2017). How fast is the Earth moving? Space.com. Retrieved from https://www.space.com/33527-how-fast-is-earth-moving.html
IAU. (2019). Measuring the Universe. International Astronomical Union. Retrieved from https://www.iau.org/public/themes/measuring/
IOP. (2019). Useful Facts. Institute of Physics. Retrieved from https://www.iop.org/activity/outreach/resources/pips/topics/earth/facts/page_43079.html#gref
Lumen. (2019). Using Spectra to Measure Stellar Radius. Astronomy. Retrieved from https://courses.lumenlearning.com/astronomy/chapter/using-spectra-to-measure-stellar-radius-composition-and-motion/
NASA. (2019). Earth Fact Sheet. Retrieved from https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
NASA. (2019). Measuring the Distance. Retrieved from https://www.nasa.gov/audience/foreducators/k-4/features/F_Measuring_the_Distance_Student_Pages.html
NASA. (2018). Mission Overview. Retrieved from https://www.nasa.gov/mission_pages/kepler/overview/index.html
The Planetary Society. (2019) Transit Photometry. Retrieved from https://www.planetary.org/explore/space-topics/exoplanets/transit-photometry.html
Sharp, T. (2017). How big is Earth? Space.com. Retrieved from https://www.space.com/
Skyserver. (2019). Light from Stars. Sloan Digital Sky Survey. Retrieved from https://skyserver.sdss.org/dr1/en/proj/basic/color/fromstars.asp
Skyserver. (2019). Spectra of Stars. Sloan Digital Sky Survey. Retrieved from https://cas.sdss.org/dr6/en/proj/basic/spectraltypes/stellarspectra.asp
Vanderburg, A. (2019). Transit Light Curve Tutorial. Harvard Center for Astophysics. Retrieved from https://www.cfa.harvard.edu/~avanderb/tutorial/tutorial.html
"""

######################  functions are defined here ###########################

# PROVIDED FUNCTIONS
def get_period_of_planet(dist_exo_star, velocity_exo):
    """ Determine the period of an exoplanet using the distance of the planet
    from its star and the velocity of the planet. The period is the time, in
    seconds, for the exoplanet to make one complete orbit around its star

    Paramaters:
        dist_exo_star (flt): Input from user of the distance of the exoplanet
            from its star, relative to Earth and the sun [km]
        velocity_exo (flt): Velocity of exoplanet, dependant on distance from
            its star and gravitational attraction of the star [km/s]
    Variables:
        circum_exo (flt) The circumference of the exoplanet [km]
    Return:
        flt: The period of the exoplanet [s]
    """
    circum_exo = (2 * pi * dist_exo_star)  # km
    return circum_exo / velocity_exo  # s


def get_transit_time(velocity_exo, r_star):
    """ Determine the transit time of the exoplanet using its velocity and the
    diameter of its star. The faster the exoplanet is moving, the shorter the
    transit time. The transit time is the time, in seconds, for the exoplanet
    to pass across its star (from an observed point on Earth).

    Paramaters:
        velocity_exo (flt): Velocity of exoplanet, dependant on distance from
            its star and gravitational attraction of the star [km/s]
        r_star (flt): The radius of the star [km]
    Variables:
        diam_star (flt_: Diameter of exoplanet [km]
    Return:
        flt: The transit time of the exoplanet [s]
    """
    diam_star = (2 * r_star) # km
    return diam_star / velocity_exo  # km/s


def get_min_rel_intensity(r_exo, r_star):
    """ Determine the minimum relative intensity of the exoplanet's star from an
    observed point on Earth. The minimum intensity is when the exoplanet is
    completely in front of its star, that is when the star's intensity is the
    lowest. When an exoplanet is not in front of its star, the star's intensity
    is 1 (the maximum).

    Parameters:
        r_exo (flt): Radius of exoplanet [km**2]
        r_star (flt): The radius of the star [km]
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
    # N = R * p * n * L * c
    return 7 * 0.5 * 1 * 10000 * c


def get_exo_dimension(dimension, proportion):
    """Return the measurement of an exoplanet, given a proportion to Earth.

    Paramater:
        dimension (flt): Measurement of exoplanet
        proportion (flt): Proportion of measurement in relation to Earth
    Return:
        flt: The proportional dimension of the exoplanet
    """
    return dimension * proportion


def get_velocity_exo(velocity_Earth, dist_Earth_sun, dist_exo_star):
    """ Determine the velocity of the exoplanet, that is the speed at which the
    exoplanet travels. This is dependent on how far it is from its own star and
    the gravitational attraction of the star. The velocitity is calculated using
    the known velocity of the Earth with the proportional difference between
    the distance of Earth and the sun, and the exoplanet and its star.

    Paramaters:
        velocity_Earth (flt): The speed at which the Earthtravels [km/s]
        dist_Earth_sun (flt): The distance of the Earth from the sun [km]
        dist_exo_star (flt): The distance of the exoplanet from its star [km]
    Return:
        flt: The velocity of the exoplanet [km/s]
    """
    return velocity_Earth * sqrt(dist_Earth_sun / dist_exo_star) # km/s


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
            in intervals of 1s
    """
    return arange(0 - midpoint, transit_time + midpoint, 1)


def get_x_positions(r_star, r_exo, velocity_exo, t_times):
    """ Calculate the position of the exoplanet for a set of times. The position
    and time are related by velocity.

    Parameters:
        r_star (flt): The radius of the star [km]
        r_exo (flt): Radius of exoplanet [km]
        velocity_exo (flt): The velocity of the exoplanet [km/s]
        t_times (flt array): An array of times in 1 minute intervals for the
            duration of the exoplanet's transit time plus 1 more step [s]
    Variables:
        x_zero (flt): Starting x_position [km], last position of the exoplanet
            before it starts to cross its star. (i.e. last position where
            intensity is equal to 1 before decreasing)
    Return:
        array: Positions [km] of the planet as the exoplanet transits its star
    """
    x_zero = -r_star - r_exo # km
    return x_zero + (velocity_exo * t_times)


def get_y_intensity(r_star, r_exo, x_positions, min_rel_intensity):
    """ Calculate the relative intensity of each position of the exoplanet during
    its transit across its star. The intensity depends on where the exoplanet is
    relative to its star.

    Parameters:
        r_star (flt): The radius of the star [km]
        r_exo (flt): The radius of the exoplanet [km]
        x_positions (flt): An array of positions of the planet as the exoplanet
            transits its star [km]
        min_rel_intensity: The intensity of the exoplanet when it has full
            overlap with its star
    Variables:
        x_out (flt): Absolute position of exoplanet when it has no overlap [km]
        x_in (flt): Absolute position of the exoplanet when it has full overlap [km]
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
        if x >= x_out:
            # Exoplanet has no overlap with star
            y_intensity[i] = 1
        elif x <= x_in:
            # Exoplanet has full overlap with star
            y_intensity[i] = min_rel_intensity
        else:
            # Exoplanet overlapping the edge of the star
            y_intensity[i] = 1 - (
                    ((x - x_out) / (x_in - x_out)) * (1 - min_rel_intensity))
        i = i + 1
    return y_intensity


def plot_intensity(midpoint, t_times, y_intensity):
    """Plot the intensity of the exoplanet as it transits its star in a graph. A
    series of times of the exoplanet are plotted against the intensity of the
    exoplanet at each position [km] in time [s]

    Parameters:
        midpoint (flt): Half the transit time [s]
        t_times (flt array): An array of times in 1s intervals for the
            duration of the exoplanet's transit time [s]
        y_intensity (flt array): intensity of each position of exoplanet as
            crosses its star
    """
    # plot times as hours from midpoint
    t_times = (t_times - midpoint) / 3600
    # create plot
    plot(t_times, y_intensity, 'ko')
    title("Relative intensity of a star during the transit of an exoplanet")
    xlabel("Time from midpoint of transit (hours)")
    ylabel("Relative light intensity")
    ticklabel_format(useOffset=False)
    grid(True)
    show()

    print("\nThis table shows the position of the exoplanet at each time."
          "\n"
          "\nIntensity \t| Exoplanet position \t\t\t| Overlap with star"
          "\n-------------------------------------------------------------------------"
          "\n 1 \t\t| not in front of the star \t\t| None"
          "\n minimum \t| completely in front of the star \t| Full"
          "\n other \t\t| crossing the border of the star \t| Partial")


def get_detection(min_rel_intensity):
    """Determine whether the exoplanet can be detected given the change in
    observed intensity of it's star from Earth. The detection limit to observe a
    planet is an intensity decrease of 1 part in 10.00 as the exoplanet transits
    its star.

    Parameters:
        min_rel_intensity: Intensity of star when an exoplanet has full overlap
    """
    if min_rel_intensity <= 0.9999:
        # Intensity has decreased enough to detect a planet
        return True


def search_again():
    """Asks the user if they want to search again for another exoplanet

    Variables:
        user (flt): Input to search again
    Return:
        boolean: Returns true if user wants to search again.
    """
    user = float(input("\nDo you want to search again?"
                       "\n\t(1) Yes"
                       "\n\t(0) No\n"))
    if user == 1:
        return True


######################  some constants used throughout ###########################

# Radius of star = radius of sun [km] (NASA, 2019)
r_star = 695700
# Radius of Earth [km] (Sharp, 2017; NASA, 2019)
r_Earth = 6378
# Velocity of Earth [km/s] (Herman, 1998; IOP, 2019)
velocity_Earth = 30
# Distance from Earth to the sun [km] (IAU; Howell, 2018)
dist_Earth_sun = 149597870

# Define constant to allow user to continuously search for exoplanets (step 11)
searching = True

# Images for user interaction (ASCII Art Archive, 2019)
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
ascii_rocket_launch = """
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

######################  main body of the code here ###########################

""" Logic for the exhibit item on exoplanets at the Science musuem as part
of the 'Exploring Our Galaxy Exhibit'

    Step 1. Introductory message for all patrons and prompt for patron_type

PART A - FIND CIVILISATIONS
    Step 2. Print an intro about other potential civilisations in our galaxy
    Step 3. Ask user what they think is the proportion (or percentage) of
        habitable planets that develop technological civilisations
    Step 4. Calculate and print N using their estimation, with a useful message

PART B - FIND EXOPLANETS
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
    Step 9. If user is an enthuasiast, 
        (a) calculate the intensity of light from the star for a series of times 
            and stores these values in an array. 
        (b) plot a graph of the intensity of light from the star over times as 
            the planet transits across the star.
        (c) Write a short paragraph about a limitation of the modelling
    Step 10. Inform the user whether their chosen planet could be detected or not
    Step 11. Ask the user if they want to try again with another exoplanet search
    Step 12. Print a farewell message
 """

# STEP 1 - Introductory message for all patrons
print("Hope you have been enjoying your time 'Exploring Our Galaxy!'"
      "\n"
      "\nBy know you know that our galaxy is a huge mystery with so much we don't know about it."
      "\n"
      "\nSo it's easy to start wondering, are there other life forms out there?"
      "\nIf so, where do they live and how do we find their home?"
      "\n"
      "\nJump aboard and let's find out!",
      ascii_spaceship)
# Prompt for patron_type
patron_type = float(input("\nBefore you start your adventure, when it comes to science are you..."
                          "\n\t(1) a rookie, or"
                          "\n\t(0) an enthusiast?\n"))

# Remaining steps and text differ for each patron_type
if patron_type == 1:
    # ROOKIE
    print("\nWelcome aboard Rookie! "
          "\nLet's start the countdown..."
          "\n3 \t2 \t1 \tBLAST OFF",
          ascii_rocket_launch)

    # PART A - SEARCHING FOR OTHER CIVILISATIONS
    # Step 2 - Intro about other civilisations - estimates multiplied by 10,000
    print("\n*LET'S IMAGINE TALKING WITH ALIENS*"
          "\n"
          "\nHave you ever wondered the possibility of finding other life forms?"
          "\nWell, there is an equation that is used to guess the chance of finding life on other planets that we would be able to understand."
          "\n"
          "\nTo work this out we need to know how many planets could have life forms that use technology."
          "\nSome guesses to this question have been that out of 10,000 planets there is 1 planet and more recently 200 planets.",
          ascii_alien,
          "\n--Now it's your turn to guess!--")

    # Step 3 - Ask user for their input on variable c for drake equation
    # Divide c by 10,000 to get as proportion
    c = float(input(
        "\nQ: Out of 10,000 planets, how many planets do you think there are with technology?\n")) / 10000
    # Step 4 - Calculate N from drake equation and display
    print(
        "\nA: With your guess, there are", round(drake_equation(c)),
        "planets in our galaxy that we could talk to."
        "\n"
        "\nThis is pretty amazing! Maybe UFO's aren't a conspiracy after all?"
        "\nSo all these aliens must be living somewhere, but where?")

    # PART B - SEARCHING FOR EXOPLANETS
    # Step 5 - Intro about exoplanets
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
        print("--Now it's your turn to try and find an exoplanet!--\n"
              "\nTo know the change in light we need to know the size of your planet and how far it is from its sun."
              "\n"
              "\nCompared to Earth and our sun...")

        # Step 6 - Ask user for size of planet
        user_size = float(input(
            "\nQ: What is the size of the planet you want to find?"
            "\n\t(1) Same size as Earth"
            "\n\t(2) Double the size of Earth"
            "\n\t(3) Triple the size of Earth"
            "\n\t(4) Around the size as Uranus"            
            "\n\t(9) Around the same size as Saturn"
            "\n\t(11) Around the size as Jupiter\n"))

        # Step 7 - Ask user for distance of planet from sun
        user_dist = float(input(
            "\nQ: How far away from its sun do you want the planet to be? "
            "\n\t(0.5) Half the distance as Earth and our sun"
            "\n\t(1) The same distance as Earth and our sun"
            "\n\t(2) Twice as far as Earth and our sun"
            "\n\t(3) Three times as far as Earth and our sun"
            "\n\t(5) About the distance from Jupiter to our sun"
            "\n\t(10) About the distance from Saturn to our sun\n"))

        # Step 8 - Calculate important facts about exoplanet and print info
        r_exo = get_exo_dimension(r_Earth, user_size)  # km
        dist_exo_star = get_exo_dimension(dist_Earth_sun, user_dist)  #km
        velocity_exo = get_velocity_exo(velocity_Earth, dist_Earth_sun, dist_exo_star)  # km/s

        period = get_period_of_planet(dist_exo_star, velocity_exo)  #s
        transit_time = get_transit_time(velocity_exo, r_star)  #s
        min_rel_intensity = get_min_rel_intensity(r_exo, r_star)

        print("\n--There are now three important things we know about your exoplanet--\n"
              "\n(1) The time it takes for your planet to go completely around its star (this is 1 year for Earth) is",
              round(period / 86400, 2), "days"  # convert from seconds to days              
              "\n(2) The time it takes for your planet to move across its star (the bigger the star, the longer this will be) is",
              round(transit_time / 3600, 2), "hours"  # convert from seconds to hours
              "\n(3) The brightness of your planet's star from Earth when it is being blocked by your planet is",
              round(min_rel_intensity, 6),
              ascii_planet)

        # Step 9 - NOT an enthusiast so continue

        # Step 10 - Try and detect planet
        print("--Now let's see if we can find your planet--\n"
              "\nTo find your planet we need to see a certain amount of change in the light of your planet's sun as your planet blocks it."
              "\nOnce we know if the change is enough, we need to watch it go around its sun at least 3 times to be sure.")
        if get_detection(min_rel_intensity):
            # Planet found - intensity decreased enough
            print("\nA: Yay, we found your planet!!!")
            # convert period from seconds to years and multiply by 3 years
            detect_time = (period / 31536000) * 3
            print("\nTo be sure we need to watch it for", round(detect_time, 2), "years")
        else:
            print("\nA: Sorry...We couldn't find your planet")

        # Step 11 - Ask user if they want to search again
        print(ascii_space)
        searching = search_again()

else:
    # ENTHUSIAST
    print("\nWelcome aboard Enthusiast! "
          "\nLet's start the countdown..."
          "\n3, \t2, \t1, \tBLAST OFF",
          ascii_rocket_launch)

    # Part A - Searching for other civilisations
    # Step 2 - Intro about other civilisations
    print("\n*LETS IMAGINE POTENTIAL CIVILISATIONS IN THE MILKY WAY*\n"
          "\nThe drake equation is used as a guide to speculate the probability of finding "
          "\ncivilisations in the Milky Way with whom it may be possible to communicate."
          "\n"
          "\nOne of the factors of this equation is estimating the proportion of potentially "
          "\nhabitable planets on which a technological civilisation develops."
          "\n"
          "\nIn the 1960's the proportion was estimated at 0.0001 and more recently at 0.02. ",
          ascii_alien)

    # Step 3 - Ask user for their input on variable c for drake equation
    print("\n--Now it's your turn to estimate!--")
    c = float(input("\nQ: What do you think is the proportion?\n"))

    # Step 4 - Calculate N from drake equation and display
    print(
        "\nA: Using your proportion and the most recent estimates for all other factors,"
        "\nthere are", round(drake_equation(c)),"civilisations in the galaxy that can communicate with Earth!"
        "\n"
        "\nThis is pretty amazing! Maybe UFO's aren't a conspiracy after all?"
        "\nSo all these civilisations must be living somewhere, but where?")

    # PART B - SEARCHING FOR EXOPLANETS
    # Step 5 - Intro about exoplanets
    print("\n*LETS FIND SOME EXOPLANETS*\n"
          "\nExoplanets are planets that orbit around stars other than our sun. We can detect "
          "\nexoplanets by observing the intensity of the light emitted by another star in our "
          "\ngalaxy over time."
          "\n"
          "\nIf the measured intensity of a star decreases then an exoplanet is passing in front "
          "\nof the the star and partially blocking its light from our observation point on Earth."
          "\n"
          "\nThis method has been very successful at detecting exoplanets. The Kepler space "
          "\ntelescope, which uses this approach, has detected several thousand exoplanets.",
          ascii_telescope)

    # Point where user can search for exoplanets continuously
    while searching:
        print("\n--Now it's your turn to try and find an exoplanet!--\n"
              "\nTo model the transit of the exoplanet in front its star, we need to specify the size of "
              "\nthe planet and the distance of that planet from its star."
              "\n"
              "\nAs a percentage of Earth and our sun...")

        # Step 6 - Ask user for size of planet
        # Divide by 100 to convert to proportion
        user_size = float(input(
            "\nQ: What is the size of the planet you want to find? (%)"
            "\n\t(100) Same size as Earth"
            "\n\t(200) Double the size of Earth"
            "\n\t(300) Triple the size of Earth"
            "\n\t(400) Approx. the size as Uranus"            
            "\n\t(900) Approx. the same size as Saturn"
            "\n\t(1100) Approx. the size as Jupiter\n")) / 100

        # Step 7 Ask the user for the distance of the planet to its star
        # Divide by 100 to convert to proportion
        user_dist = float(input(
            "\nQ: How far away from its sun do you want the planet to be? (%)"
            "\n\t(50) Half the distance"
            "\n\t(100) The same distance"
            "\n\t(200) Double the distance"
            "\n\t(300) Triple the distance"
            "\n\t(500) Approx. the same distance as Jupiter from our sun"
	          "\n\t(1000) Approx. the same distance as Saturn from our sun\n")) / 100

        # Step 8 - Calculate important facts about exoplanet and print info
        r_exo = get_exo_dimension(r_Earth, user_size)  # km
        dist_exo_star = get_exo_dimension(dist_Earth_sun, user_dist)  # km
        velocity_exo = get_velocity_exo(velocity_Earth, dist_Earth_sun, dist_exo_star)  #km/s

        period = get_period_of_planet(dist_exo_star, velocity_exo)  #s
        transit_time = get_transit_time(velocity_exo, r_star)  #s
        min_rel_intensity = get_min_rel_intensity(r_exo, r_star)
        print("\n--There are now three important factors that we know about your exoplanet--\n"
              "\n(1) Period of orbit is", round(period / 86400, 2), "days"  # convert seconds to days
              "\nThis is the time for the exoplanet to make one complete orbit around its star (this is 1 year for Earth). "
              "\nThe period of orbit is determined by the exoplanet's speed, and the distance the exoplanet is from its star."
              "\n"
              "\n(2) Transit time is", round(transit_time / 3600, 2), "hours"  # convert seconds to hours
              "\nThe velocity of the exoplanet and the diameter of its star will determine the transit time. "
              "\nThe faster the exoplanet is moving, the shorter the transit time."
              "\nLikewise the larger the diameter of the star, the longer the transit time."
              "\n"
              "\n(3) Minimum relative intensity is", round(min_rel_intensity, 6),
              "\nThis is when the exoplanet is fully between Earth and the star i.e. completely overlapping its star."
              "\nThe intensity of the star observed from Earth will be decreased as the exoplanet blocks some of the light.",
              ascii_planet)

        # Step 9 - Is an enthusiast
        # Get the midpoint of the transit time
        midpoint = transit_time / 2

        # (a) Calculate the intensity of light from star over time
        # Create an array of times as exoplanet transit star [s]
        t_times = get_t_times(transit_time, midpoint)
        # Calculate the position of the exoplanet at each time [km]
        x_positions = get_x_positions(r_star, r_exo, velocity_exo, t_times)
        # Calculate the intensity of light at each position
        y_intensity = get_y_intensity(r_star, r_exo, x_positions, min_rel_intensity)

        # (b) Plot the time against the intensity
        print("\n--Let's see a graph of how the light intensity changes as your exoplanet travels across its face--\n")
        plot_intensity(midpoint, t_times, y_intensity)

        # c) About a limitation of model (Skyserver, 2019; Lumen, 2019)
        print("\n--About the model used and its limitations--"
              "\n"
              "\nIn our quest to find other planets we have made a few key assumptions. One of which is that the amount of light "
              "\nemitted by a star is constant across its entire width. Using this assumption, when a planet is completely in front"
              "\nof its star we can say that the star must be at its minimum relative intensity always (showed by the flat linear line). Also, if its "
              "\npartially overlapping then the intensity must be the same at say -5 hours from the midpoint and +5 hours from "
              "\nthe midpoint, as shown by the linear decline/increase between 1 and the minimum intensity on the graph."
              "\n"
              "\nHowever, this is not the case. The the amount of light emitted from a star varies greatly. The difference in light is the "
              "\nspectrum of a star and is composed of lots of different wavelengths. These wavelengths emit differing levels of intensity."              
              "\nEvery star and planet is different so there are lots of factors that need to be adjusted and accounted for. However, by "
              "\nmaking such assumptions, we can start to get a glimpse at other potential planets. With each glimpse we "
              "\ncan learn a little more about the wonders of our galaxy.")

        # Step 10 - See if planet can be detected
        print("\n--Let's see if we can detect your planet--\n"
              "\nThe detection limit to find a planet is an intensity decrease of 1 part in 10,000 as the exoplanet transits the star."
              "\nTo confirm the existence of an exoplanet multiple measurements at regular intervals (at least 3 periods) can be used.")
        if get_detection(min_rel_intensity):
            # Planet found - intensity decreased enough
            print("\nA: We detected your planet!!!"
                  "\nThis means the intensity decreased enough to find it.")
            # get detection time - convert period to years
            detect_time = (period / 31536000) * 3
            print("\nTo confirm its existence, we would need to take measurements for",
                  round(detect_time, 2), "years")
        else:
            print("\nA: Sorry...we couldn't detect your planet."
                  "\nThis means intensity didn't decrease enough to find it.")

        # Step 11 - Ask user if they want to try again
        print(ascii_space)
        searching = search_again()

# Step 12 - Farewell message for all users
print("\nWelcome back to Earth!"
      "\n"
      "\nContinue to enjoy your adventure of exploring the wonders of our galaxy."      
      "\nAnd don't forget to keep your eyes open for any UFO's.",
      ascii_rocket_landed)