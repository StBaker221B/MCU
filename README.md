
# Embeded Micro Control System

## Fundamental Informaiton

- Chip：STM32F103ZET6
- Development board: Alientek(正点原子) Minimum system (Core board)
- Development environment: Keil MDK(C/C++) 5.31
- GUI development tool: Qt5 & PyQt5

## Functional requests

* Timing control: use the MCU to switch on/off the solenoid valves according to the set time order
* Manual control: instantly switch on/off any valves by hand through the GUI program on PC
* After the manual operation, the system could still work on by timing(auto) control

## File structure

* MCUControl - the program running on the STM32 board
* PCControl - the GUI program running on PC
* Some practice programs were put here. Just for memory.