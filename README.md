# F1 Reaction Timer

A Raspberry Pi powered reaction time game inspired by the Formula 1 race start sequence.

Players arm the system by pressing their buttons, wait through a five-light countdown, and then react as quickly as possible when the lights go out. The system records both reaction times and displays the winner.

---

## Features

- Two-player reaction timer
- Formula 1 style five-light countdown
- Randomized start delay
- Individual player reaction timing
- Automatic winner determination
- Physical reset button
- Active-low relay support
- Raspberry Pi GPIO interrupt handling

---

## Hardware Used

### Controller

- Raspberry Pi (any model capable of running RPi.GPIO)

### Inputs

| Function | GPIO |
|----------|------|
| Player A Button | GPIO 4 |
| Player B Button | GPIO 26 |
| Reset Button | GPIO 21 |

### Outputs

| Function | GPIO |
|----------|------|
| Player A Indicator | GPIO 12 |
| Player B Indicator | GPIO 16 |
| Countdown Light 5 | GPIO 22 |
| Countdown Light 4 | GPIO 23 |
| Countdown Light 3 | GPIO 27 |
| Countdown Light 2 | GPIO 18 |
| Countdown Light 1 | GPIO 17 |

### Additional Hardware

- 8-channel solid-state relay (SSR) board
- 12V power supply for lighting
- 5V power supply for Raspberry Pi
- Momentary push buttons
- Inline protection resistors for button circuits
- 12V indicator lamps

---

## System Overview

```text
Players Press Buttons
          │
          ▼
  Game Arms
          │
          ▼
5-Light Countdown
          │
          ▼
 Random Delay
          │
          ▼
  Lights Out!
          │
          ▼
 Players React
          │
          ▼
Results Displayed
          │
          ▼
  Reset Button
```

---

## Wiring Overview

### Button Inputs

The buttons use internal pull-up resistors.

```text
GPIO ---- Button ---- GND
```

When a button is pressed, the GPIO input is pulled LOW.

### Relay Outputs

The relay board is configured as active-low.

```text
GPIO LOW   = Relay ON
GPIO HIGH  = Relay OFF
```

### Lighting Circuit

```text
12V PSU +
    │
    ├── Relay Channel
    │
    └── 12V Lamp
               │
               ▼
          12V PSU -
```

The Raspberry Pi only controls the relay inputs. The relay board switches the 12V lighting circuit.

---

## Software Requirements

### Install RPi.GPIO

```bash
sudo apt update
sudo apt install python3-rpi.gpio
```

or

```bash
pip3 install RPi.GPIO
```

---

## Running the Project

Navigate to the project directory:

```bash
cd F1-Community-Experience-Programme-COTA-2025
```

Run the game:

```bash
python3 f1_reaction_timer.py
```

---

## How to Play

1. Power the system.
2. Player A presses their button.
3. Player B presses their button.
4. The five countdown lights illuminate.
5. After a random delay, all lights turn off.
6. React as quickly as possible.
7. The system records both reaction times.
8. The fastest player wins.
9. Press RESET to start another round.

---

## Example Output

```text
Ready. Both players press their buttons.

Player A armed.
Player B armed.

Starting countdown...

LIGHTS OUT! GO!

Player B reacted #1: 0.284 seconds
Player A reacted #2: 0.361 seconds

------ RESULTS ------

Player A: 0.361 s
Player B: 0.284 s

Winner: Player B
```

---

## Educational Objectives

This project demonstrates:

- GPIO input handling
- GPIO output control
- Relay interfacing
- Event-driven programming
- Threading
- State machines
- Timing and measurement
- Python programming on Raspberry Pi
- Embedded systems design

---

## Future Improvements

- False-start detection
- OLED/LCD scoreboard
- Lap timing mode
- Best-of-five tournaments
- Networked multiplayer statistics
- Sound effects and race-start audio
- Data logging to CSV

---

## License

This project is provided for educational purposes.
