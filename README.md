# FLASH Builder Software

<center>
<img src="docs/flash-software-128.png?raw=true" alt="logo">
</center>

## Creation Edition

Creation Edition for FLASH Modelling software. Allows you to build models to print on a LEGO 3D Printer.

## The Software

Keeping with the theme of lightning, I called it FLASH. It's also down to how fast and easy it is to create simple models to be printed.

![GIF of Software](docs/flash-1.gif?raw=true "FLASH Software Preview")

You'll notice that there are 5 estimated instructions even though no bricks have been placed. As default, the printer will add instructions to home itself and calibrate each axis. This was done using LEGO EV3 Press sensors.

### Features

- 3 colours of bricks avaliable
- Model saving and loading using JSON
- Preview Window Dark Mode
- Model Validation. This includes:
  - prevention of building bricks outside grid area
  - resize grid if imported model is too large for current settings
  - prevention of building bricks inside one another
  - prevention of building floating bricks

![Image of Model in Software](docs/flash-2.PNG?raw=true "FLASH Model Preview")

### Controls

```none
A-D Keys: Move placer on the X-Axis
W-S Keys: Move placer on the Y-Axis
Q-E Keys: Move placer on the Z-Axis
Spacebar: Place brick at placer position
X Key: Delete brick at placer position

1 Key: Select Red brick
2 Key: Select Blue brick
3 Key: Select Yellow brick
```

## Backstory

![Image of 3D Printer](docs/printer-original.png?raw=true "Team Lightning's 3D Printer")

As part of the 2018 Technocamps competition, Team Lighting build a LEGO 3D Printer out of Technic pieces for the main project. The theme for the 2018 year was Art & Music. In the live challenge, teams would have to change or build a new robot in an hour that could represent Technocamps. The team adapted the 3D Printer into a printer on wheels, that was successfully able to write "TECHNO" on a piece of paper before time ran out. This ultimately won the team first place in the Live Challenge, earning themselves keyrings, certificates, and an Arduino kit for the robotics club.

![Image of 3D Printer at Event](docs/printer-at-event.png?raw=true "Team Lightning's 3D Printer")

The EV3 Brick simply read coordinates from 3 `.rtf` files that would contain all the model data. However at the time of the event, we had to hard code 3D-arrays of models we wanted to build. This is what inspired me to create this software.

After the competiton, we rebuilt the printer which was more accurate and stronger. It uses the LEGO tracks on the print bed rather than using string, so it is similar to a real 3D Printer with the rubber belt.

![Image of Rebuilt Printer](docs/printer-256.png?raw=true "Rebuilt 3D Printer")

## Thank you

I just want to say thank you to some people who have made this possible:

**Edward Upton** ([engiego](http://github.com/engiego)) for the collaboration and ideas for the software.

**Team Lightning** crew for creating the printer idea and building it, and being successful in the Technocamps competition.

## More Photos

![Image of Brick Cartridges](docs/printer-cartridges.png?raw=true "Printer Cartridges")

These are the printer LEGO Brick Cartridges. Each brick instruction also adds an instruction to go to the brick dispenser to pick up a new brick.

----------

![GIF of Printer in action](docs/printer-working.gif?raw=true "Printer in action")

Programmed with synchronous axis movement. You can see the original string method we used to move the print bed.

----------

![GIF of Printer placing brick](docs/printer-place-brick.gif?raw=true "Printer placing brick")

The first development of the printer had problems with the print head slipping when it placed bricks. However, we managed to get the final model to place bricks without requiring a motor to press it on to the plate.

----------

![Photo of Y & Z axis mechanics](docs/printer-mechanics.png?raw=true "Printer Mechanics")

Final Model Y & Z axis mechanics built by Edward.

----------

![GIF of Printer movement](docs/printer-movement.gif?raw=true "Printer Movement")

More synchronous movement.
