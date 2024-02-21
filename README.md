# NanoShift
An Arduino Nano script for interfacing with Logitech's Driving Force shifter.

## Story
I bought a Logitech Driving Force shifter, not realizing that it wasn't a direct to USB shifter.
Looking around online, people got it working on the Arduino Micro, but that the Nano was fundamentally incompatible. Out of spite, I decided to look at the pinouts myself, wire, and code everything to get the shifter pressing keys on my computer.
I've now use these scripts almost every single day, definitely every single time I play a driving sim.

## Limitations / Issues
- The Python script just presses keys. Since some games (Assetto Corsa for example) are weird/strict with input devices, they simply wont let you set your shifter to keyboard buttons without mods. (I want to update the companion script to output as a controller soon, may fix this).
- The button for reversing is unwired and unimplemented, this means you have 5+1 gears instead of 6+1. It's a relatively simple fix though, I just drive 5 speed so I never notice.
- Sometimes when shifting from 1st to 2nd, your input is ignored and games like Beam put you into neutral. My best theory is that it's bouncing of the analogue signal (debugging output says it goes 1, 0, 1, 2 usually instead of 1, 0, 2). I just redo the shift to fix it.

## Set-up (images coming soon)
1. Connect 4 jumper wires to the shifter at 4, 6, 8, and 9 according to the shifter's FEMALE pinout. Refer to [here](https://dmadison.github.io/Sim-Racing-Arduino/docs/logitech_shifter.html) for pinout details. (Header socket connectors with jumper wires are really useful  for this).
2. Connect the respective wires to A0, GND, A2, and 5V. Upload the Arduino sketch and find which COM port serial is running on (OS and USB port specific, Arduino IDE will tell you).
3. Update the Python companion file to read that COM port, then run it. When shifting it should show the gear in the terminal as well as output a key to bind with.

If you go to 1 and it says 6, you likely wired your power and ground backwards. It reverses the analogue readings.
