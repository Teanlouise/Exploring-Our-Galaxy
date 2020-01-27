[Back to Home](https://teanlouise.github.io)

![exoplanet_title](https://user-images.githubusercontent.com/19520346/73152900-5a1e1780-411d-11ea-9ec3-d88945a6fed0.PNG)

This project was submitted for the 'Python and Communication Assignment' for Theory and Practice in Science (SCIE1000) at University of Queensland.
The purpose of the assessment was to create an exhibit item for a museum as a part of an "Exploring Our Galaxy" exhibition.
The user can be either a science rookie or a science enthusiast and all communication must be appropriate for the selected audience. 

The first part was to explore the idea of finding civilisations with whome we can communicate and the second part was to detect an exoplanet based on the change of intensity of its sun. In addition,
science enthusiast, were shown a graph of how the intensity changes. The project was limited to the use of functions, arrays, graphing, while loops and conditionals only.

## LOGIC FOR THE EXHIBIT ITEM:

1. Introductory message for all patrons and prompt for patron_type
    
**Part A - Find Civilisations**

2. Print an intro about other potential civilisations in our galaxy
3. Ask user what they think is the proportion (or percentage) of habitable planets that develop technological civilisations
4. Calculate and print N using their estimation, with a useful message

**Part B - Find Exoplanets**

5. Introduce the idea of searching for planets around stars other than our own
6. Ask the user for the relative size of the planet they want to find (relative to Earth)
7. Ask the user for the distance of the planet to its star(relative to the Earth's distance from the sun)
8. Calculate and print each of these values with useful messages
- (a) the period for the planet's orbit using get_period_of_planet
- (b) the transit time for the planet using get_transit_time
- (c) the minimum relative intensity of the planet using get_min_rel_intensity
9. If user is an enthuasiast, 
- (a) calculate the intensity of light from the star for a series of times and stores these values in an array. 
- (b) plot a graph of the intensity of light from the star over times as the planet transits across the star.
- (c) Write a short paragraph about a limitation of the modelling
10. Inform the user whether their chosen planet could be detected or not
11. Ask the user if they want to try again with another exoplanet search
12. Print a farewell message
    
## OUTPUT – ROOKIE

Hope you have been enjoying your time 'Exploring Our Galaxy!'

By know you know that our galaxy is a huge mystery with so much we don't know about it.

So it's easy to start wondering, are there other life forms out there?
If so, where do they live and how do we find their home?

Jump aboard and let's find out! 
```
        |
       / \.
      / _ \.
     |.o '.|
     |'._.'|
     |     |
   ,'|  |  |`.
  /  |  |  |  \.
  |,-'--|--'-.| 
```

Before you start your adventure, when it comes to science are you...
	(1) a rookie, or
	(0) an enthusiast?
1

Welcome aboard Rookie! 
Let's start the countdown...
3 	2 	1 	BLAST OFF 
```
                    .   
                   .'.
                   |o|
                  .'o'.
                  |.-.|
                  '   '
                   ( )
                    )
                   ( )
```

*LET'S IMAGINE TALKING WITH ALIENS*

Have you ever wondered the possibility of finding other life forms?
Well, there is an equation that is used to guess the chance of finding life on other planets that we would be able to understand.

To work this out we need to know how many planets could have life forms that use technology.
Some guesses to this question have been that out of 10,000 planets there is 1 planet and more recently 200 planets. 
```
                       .-.
        .-""`""-.    |(@ @)
     _/`oOoOoOoOo`\_ \ \-/
    '.-=-=-=-=-=-=-.' \/ \.
      `-=.=-.-=.=-'    \ /\.
         ^  ^  ^       _H_ \.
 ```
 
--Now it's your turn to guess!--

Q: Out of 10,000 planets, how many planets do you think there are with technology?
500

A: With your guess, there are 1750 planets in our galaxy that we could talk to.

This is pretty amazing! Maybe UFO's aren't a conspiracy after all?
So all these aliens must be living somewhere, but where?

*LETS FIND SOME NEW PLANETS*

Exoplanets are planets that are not a part of our solar system and so they have their own suns.

We can try and find these other planets by watching these other suns and measuring the light from them here on Earth. If the sun has less light then a planet must be blocking it. Like when the moon blocks our sun.

There is a telescope that is very good at finding other planets this way and has found thousands. 
```
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
 ```

--Now it's your turn to try and find an exoplanet!--

To know the change in light we need to know the size of your planet and how far it is from its sun.

Compared to Earth and our sun...

Q: What is the size of the planet you want to find?
	(1) Same size as Earth
	(2) Double the size of Earth
	(3) Triple the size of Earth
	(4) Around the size as Uranus
	(9) Around the same size as Saturn
	(11) Around the size as Jupiter
1

Q: How far away from its sun do you want the planet to be? 
	(0.5) Half the distance as Earth and our sun
	(1) The same distance as Earth and our sun
	(2) Twice as far as Earth and our sun
	(3) Three times as far
(5) About the distance from Jupiter to our sun
	(10) About the distance from Saturn to our sun
0.5

--There are now three important things we know about your exoplanet--

(1) The time it takes for your planet to go completely around its star (this is 1 year for Earth) is 128.21  days
(2) The time it takes for your planet to move across its star (the bigger the star, the longer this will be) is 9.11  hours
(3) The brightness of your planet's star from Earth when it is being blocked by your planet is 0.999916 

```
                 *       +
           '                  |
       ()    .-.,="``"=.    - o -
             '=/_       \     |
          *   |  '=._    |
               \     `=./`,        '
            .   '=.__.=' `='      *
   +                         +
        O      *        '       .

```
--Now let's see if we can find your planet--

To find your planet we need to see a certain amount of change in the light of your planet's sun as your planet blocks it.
Once we know if the change is enough, we need to watch it go around its sun at least 3 times to be sure.

A: Sorry...We couldn't find your planet

```
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
```

Do you want to search again?
	(1) Yes
	(0) No
1

--Now it's your turn to try and find an exoplanet!--

To know the change in light we need to know the size of your planet and how far it is from its sun.

Compared to Earth and our sun...

Q: What is the size of the planet you want to find?
	(1) Same size as Earth
	(2) Double the size of Earth
	(3) Triple the size of Earth
	(4) Around the size as Uranus
	(9) Around the same size as Saturn
	(11) Around the size as Jupiter
11

Q: How far away from its sun do you want the planet to be? 
	(0.5) Half the distance as Earth and our sun
	(1) The same distance as Earth and our sun
	(2) Twice as far as Earth and our sun
	(3) Three times as far
(5) About the distance from Jupiter to our sun
	(10) About the distance from Saturn to our sun
2

--There are now three important things we know about your exoplanet--

(1) The time it takes for your planet to go completely around its star (this is 1 year for Earth) is 1025.69 days
(2) The time it takes for your planet to move across its star (the bigger the star, the longer this will be) is 18.22 hours
(3) The brightness of your planet's star from Earth when it is being blocked by your planet is 0.98983 

```
                 *       +
           '                  |
       ()    .-.,="``"=.    - o -
             '=/_       \     |
          *   |  '=._    |
               \     `=./`,        '
            .   '=.__.=' `='      *
   +                         +
        O      *        '       .
```

--Now let's see if we can find your planet--

To find your planet we need to see a certain amount of change in the light of your planet's sun as your planet blocks it.
Once we know if the change is enough, we need to watch it go around its sun at least 3 times to be sure.

A: Yay, we found your planet!!!

To be sure we need to watch it for 8.43 years

```
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
 ```
 
Do you want to search again?
	(1) Yes
	(0) No
0

Welcome back to Earth!

Continue to enjoy your adventure of exploring the wonders of our galaxy.
And don't forget to keep your eyes open for any UFO's. 
```
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
```



## OUTPUT – ENTHUSIAST

Hope you have been enjoying your time 'Exploring Our Galaxy!'

By know you know that our galaxy is a huge mystery with so much we don't know about it.

So it's easy to start wondering, are there other life forms out there?
If so, where do they live and how do we find their home?

Jump aboard and let's find out! 

```
        |
       / \.
      / _ \.
     |.o '.|
     |'._.'|
     |     |
   ,'|  |  |`.
  /  |  |  |  \.
  |,-'--|--'-.| 
```

Before you start your adventure, when it comes to science are you...
	(1) a rookie, or
	(0) an enthusiast?
0

Welcome aboard Enthusiast! 
Let's start the countdown...
3, 	2, 	1, 	BLAST OFF 
```
                    .   
                   .'.
                   |o|
                  .'o'.
                  |.-.|
                  '   '
                   ( )
                    )
                   ( )
```


*LETS IMAGINE POTENTIAL CIVILISATIONS IN THE MILKY WAY*

The drake equation is used as a guide to speculate the probability of finding 
civilisations in the Milky Way with whom it may be possible to communicate.

One of the factors of this equation is estimating the proportion of potentially 
habitable planets on which a technological civilisation develops.

In the 1960's the proportion was estimated at 0.0001 and more recently at 0.02.  
```
                       .-.
        .-""`""-.    |(@ @)
     _/`oOoOoOoOo`\_ \ \-/
    '.-=-=-=-=-=-=-.' \/ \.
      `-=.=-.-=.=-'    \ /\.
         ^  ^  ^       _H_ \.
```

--Now it’s your turn to estimate!--

Q: What do you think is the proportion?
0.02

A: Using your proportion and the most recent estimates for all other factors,
there are 700 civilisations in the galaxy that can communicate with Earth!

This is pretty amazing! Maybe UFO's aren't a conspiracy after all?
So all these civilisations must be living somewhere, but where?

*LETS FIND SOME EXOPLANETS*

Exoplanets are planets that orbit around stars other than our sun. We can detect 
exoplanets by observing the intensity of the light emitted by another star in our 
galaxy over time.

If the measured intensity of a star decreases then an exoplanet is passing in front 
of the the star and partially blocking its light from our observation point on Earth.

This method has been very successful at detecting exoplanets. The Kepler space 
telescope, which uses this approach, has detected several thousand exoplanets.
```
    '                   .  "   '
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
```

--Now it's your turn to try and find an exoplanet!--

To model the transit of the exoplanet in front its star, we need to specify the size of 
the planet and the distance of that planet from its star.

As a percentage of Earth and our sun...

Q: What is the size of the planet you want to find? (%)
	(100) Same size as Earth
	(200) Double the size of Earth
	(300) Triple the size of Earth
	(400) Approx. the size as Uranus
	(900) Approx. the same size as Saturn
	(1100) Approx. the size as Jupiter
400

Q: How far away from its sun do you want the planet to be? (%)
	(50) Half the distance
	(100) The same distance
	(200) Double the distance
	(300) Triple the distance
	(500 Approx. the same distance as Jupiter from our sun
	(1000) Approx. the same distance as Saturn from our sun
300

--There are now three important factors that we know about your exoplanet--

(1) Period of orbit is 1884.31 days
This is the time for the exoplanet to make one complete orbit around its star (this is 1 year for Earth). 
The period of orbit is determined by the exoplanet's speed, and the distance the exoplanet is from its star.

(2) Transit time is 22.31 hours
The velocity of the exoplanet and the diameter of its star will determine the transit time. 
The faster the exoplanet is moving, the shorter the transit time.
Likewise the larger the diameter of the star, the longer the transit time.

(3) Minimum relative intensity is 0.998655 
This is when the exoplanet is fully between Earth and the star i.e. completely overlapping its star.
The intensity of the star observed from Earth will be decreased as the exoplanet blocks some of the light. 

```
                 *       +
           '                  |
       ()    .-.,="``"=.    - o -
             '=/_       \     |
          *   |  '=._    |
               \     `=./`,        '
            .   '=.__.=' `='      *
   +                         +
        O      *        '       .
```


--Let's see a graph of how the light intensity changes as your exoplanet travels across its face—

![exoplanet_graph_1](https://user-images.githubusercontent.com/19520346/73152852-2f33c380-411d-11ea-9381-d6e14151464a.png)

This table shows the position of the exoplanet at each time on the graph.
```
Intensity 	| Exoplanet position	  	| Overlap with star
------------------------------------------------------------------------------------------------------------
 1 		| not in front of the star 		| None
 minimum 	| completely in front of the star 	| Full
 other 		| crossing the border of the star 	| Partial
```
--About the model used and its limitations--

In our quest to find other planets we have made a few key assumptions. One of which is that the amount of light 
emitted by a star is constant across its entire width. Using this assumption, when a planet is completely in front
of its star we can say that the star must be at its minimum relative intensity (showed by the flat linear line). Also, if its 
partially overlapping then the intensity must be the same at say -5 hours from the midpoint and +5 hours from 
the midpoint, as shown by the linear decline/increase between 1 and the minimum intensity on the graph.

However, this is not the case as the amount of light emitted from a star varies greatly. The difference in light is the 
spectrum of a star and is composed of lots of different wavelengths. These wavelengths emit differing levels of intensity. Every star and planet is different so there are lots of factors that need to be adjusted and accounted for. However, by making such assumptions, we can start to get a glimpse at other potential planets. With each glimpse we can learn a little more about the wonders of our galaxy.

--Let's see if we can detect your planet--

The detection limit  to find a planet is an intensity decrease of 1 part in 10,000 as the exoplanet transits the star.
To confirm the existence of an exoplanet multiple measurements at regular intervals (at least 3 periods) can be used.

A: We detected your planet!!!
This means the intensity decreased enough to find it.

To confirm its existence, we would need to take measurements for 15.49 years

```
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
 ```
 
Do you want to search again?
	(1) Yes
	(0) No
1

--Now it's your turn to try and find an exoplanet!--

To model the transit of the exoplanet in front its star, we need to specify the size of 
the planet and the distance of that planet from its star.

As a percentage of Earth and our sun...

Q: What is the size of the planet you want to find? (%)
	(100) Same size as Earth
	(200) Double the size of Earth
	(300) Triple the size of Earth
	(400) Approx. the size as Uranus
	(900) Approx. the same size as Saturn
	(1100) Approx. the size as Jupiter
900

Q: How far away from its sun do you want the planet to be? (%)
	(50) Half the distance
	(100) The same distance
	(200) Double the distance
	(300) Triple the distance
	(500 Approx. the same distance as Jupiter from our sun
	(1000) Approx. the same distance as Saturn from our sun
100

--There are now three important factors that we know about your exoplanet--

(1) Period of orbit is 362.64 days
This is the time for the exoplanet to make one complete orbit around its star (this is 1 year for Earth). 
The period of orbit is determined by the exoplanet's speed, and the distance the exoplanet is from its star.

(2) Transit time is 12.88 hours
The velocity of the exoplanet and the diameter of its star will determine the transit time. 
The faster the exoplanet is moving, the shorter the transit time.
Likewise the larger the diameter of the star, the longer the transit time.

(3) Minimum relative intensity is 0.993192 
This is when the exoplanet is fully between Earth and the star i.e. completely overlapping its star.
The intensity of the star observed from Earth will be decreased as the exoplanet blocks some of the light. 

```
                 *       +
           '                  |
       ()    .-.,="``"=.    - o -
             '=/_       \     |
          *   |  '=._    |
               \     `=./`,        '
            .   '=.__.=' `='      *
   +                         +
        O      *        '       .
 ```
--Let's see a graph of how the light intensity changes as your exoplanet travels across its face--

![exoplanet_graph_2](https://user-images.githubusercontent.com/19520346/73152853-2f33c380-411d-11ea-8499-e56134315e0b.png)
 
This table shows the position of the exoplanet at each time on the graph.
```
Intensity 	| Exoplanet position   	| Overlap with star
------------------------------------------------------------------------------------------------------------
 1 		| not in front of the star 		| None
 minimum 	| completely in front of the star 	| Full
 other 		| crossing the border of the star 	| Partial
```
--About the model used and its limitations--

In our quest to find other planets we have made a few key assumptions. One of which is that the amount of light 
emitted by a star is constant across its entire width. Using this assumption, when a planet is completely in front
of its star we can say that the star must be at its minimum relative intensity (showed by the flat linear line). Also, if its 
partially overlapping then the intensity must be the same at say -5 hours from the midpoint and +5 hours from 
the midpoint, as shown by the linear decline/increase between 1 and the minimum intensity on the graph.

However, this is not the case as the amount of light emitted from a star varies greatly. The difference in light is the 
spectrum of a star and is composed of lots of different wavelengths. These wavelengths emit differing levels of intensity. Every star and planet is different so there are lots of factors that need to be adjusted and accounted for. However, by making such assumptions, we can start to get a glimpse at other potential planets. With each glimpse we can learn a little more about the wonders of our galaxy.

--Let's see if we can detect your planet--

The detection limit to find a planet is an intensity decrease of 1 part in 10,000 as the exoplanet transits the star. 
To confirm the existence of an exoplanet multiple measurements at regular intervals (at least 3 periods) can be used.

A: We detected your planet!!!
This means the intensity decreased enough to find it.

To confirm its existence, we would need to take measurements for 2.98 years

```
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
 ```
 

Do you want to search again?
	(1) Yes
	(0) No
1

--Now it's your turn to try and find an exoplanet!--

To model the transit of the exoplanet in front its star, we need to specify the size of 
the planet and the distance of that planet from its star.

As a percentage of Earth and our sun...

Q: What is the size of the planet you want to find? (%)
	(100) Same size as Earth
	(200) Double the size of Earth
	(300) Triple the size of Earth
	(400) Approx. the size as Uranus
	(900) Approx. the same size as Saturn
	(1100) Approx. the size as Jupiter
100

Q: How far away from its sun do you want the planet to be? (%)
	(50) Half the distance
	(100) The same distance
	(200) Double the distance
	(300) Triple the distance
	(500 Approx. the same distance as Jupiter from our sun
	(1000) Approx. the same distance as Saturn from our sun
1000

--There are now three important factors that we know about your exoplanet--

(1) Period of orbit is 11467.54 days
This is the time for the exoplanet to make one complete orbit around its star (this is 1 year for Earth). 
The period of orbit is determined by the exoplanet's speed, and the distance the exoplanet is from its star.

(2) Transit time is 40.74 hours
The velocity of the exoplanet and the diameter of its star will determine the transit time. 
The faster the exoplanet is moving, the shorter the transit time.
Likewise the larger the diameter of the star, the longer the transit time.

(3) Minimum relative intensity is 0.999916 
This is when the exoplanet is fully between Earth and the star i.e. completely overlapping its star.
The intensity of the star observed from Earth will be decreased as the exoplanet blocks some of the light. 

```
                 *       +
           '                  |
       ()    .-.,="``"=.    - o -
             '=/_       \     |
          *   |  '=._    |
               \     `=./`,        '
            .   '=.__.=' `='      *
   +                         +
        O      *        '       .
```

--Let's see a graph of how the light intensity changes as your exoplanet travels across its face—

![exoplanet_graph_3](https://user-images.githubusercontent.com/19520346/73152854-2f33c380-411d-11ea-92c0-88822fb0d63e.png)
 
This table shows the position of the exoplanet at each time.
```
Intensity 	| Exoplanet position 	   	| Overlap with star
---------------------------------------------------------------------------------------------------------------
 1 		| not in front of the star 		| None
 minimum 	| completely in front of the star 	| Full
 other 		| crossing the border of the star 	| Partial
```
--About the model used and its limitations--

In our quest to find other planets we have made a few key assumptions. One of which is that the amount of light 
emitted by a star is constant across its entire width. Using this assumption, when a planet is completely in front
of its star we can say that the star must be at its minimum relative intensity (showed by the flat linear line). Also, if its 
partially overlapping then the intensity must be the same at say -5 hours from the midpoint and +5 hours from 
the midpoint, as shown by the linear decline/increase between 1 and the minimum intensity on the graph.

However, this is not the case as the amount of light emitted from a star varies greatly. The difference in light is the 
spectrum of a star and is composed of lots of different wavelengths. These wavelengths emit differing levels of intensity. Every star and planet is different so there are lots of factors that need to be adjusted and accounted for. However, by making such assumptions, we can start to get a glimpse at other potential planets. With each glimpse we can learn a little more about the wonders of our galaxy.

--Let's see if we can detect your planet--

The detection limit  to find a planet is an intensity decrease of 1 part in 10,000 as the exoplanet transits the star.
To confirm the existence of an exoplanet multiple measurements at regular intervals (at least 3 periods) can be used.

A: Sorry...we couldn't detect your planet.
This means intensity didn't decrease enough to find it.

```
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
 ```
 

Do you want to search again?
	(1) Yes
	(0) No
0

Welcome back to Earth!

Continue to enjoy your adventure of exploring the wonders of our galaxy.
And don't forget to keep your eyes open for any UFO's. 

```
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
```
