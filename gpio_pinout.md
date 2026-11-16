## DC SSR Wiring Diagram

This project used an 8-channel DC-input/DC-output Solid State Relay (SSR) module.

The Raspberry Pi GPIO pins control the relay inputs, while the relay outputs switch the 12V lamp circuits.

### Control Side (Raspberry Pi → SSR)

```text
Raspberry Pi                SSR Module

GPIO12 -----------------> IN1
GPIO16 -----------------> IN2
GPIO22 -----------------> IN3
GPIO23 -----------------> IN4
GPIO27 -----------------> IN5
GPIO18 -----------------> IN6
GPIO17 -----------------> IN7

GND --------------------> GND
3.3V -------------------> VCC
```

### Load Side (SSR → 12V Lamps)

```text
12V PSU (+)
     |
     +------ SSR CH1 ------ Player A Lamp (+)
     |
     +------ SSR CH2 ------ Player B Lamp (+)
     |
     +------ SSR CH3 ------ Countdown Light 5 (+)
     |
     +------ SSR CH4 ------ Countdown Light 4 (+)
     |
     +------ SSR CH5 ------ Countdown Light 3 (+)
     |
     +------ SSR CH6 ------ Countdown Light 2 (+)
     |
     +------ SSR CH7 ------ Countdown Light 1 (+)

All Lamp Negatives
     |
     +--------------------- 12V PSU (-)
```

### Button Wiring

Buttons use the Raspberry Pi's internal pull-up resistors.

```text
GPIO4  ----[220Ω]---- Button A ---- GND

GPIO26 ----[220Ω]---- Button B ---- GND

GPIO21 ----[220Ω]---- Reset Button ---- GND
```

### Power Distribution

```text
+-----------------+
|     12V PSU     |
+-----------------+
        |
        +---------------- Lamps
        |
        +---- 5V Buck Converter
                    |
                    v
             Raspberry Pi
```

### System Overview

```text
                Raspberry Pi
               (GPIO Outputs)
                      |
                      v
              8-Channel SSR Board
                      |
        +-------------+-------------+
        |             |             |
        v             v             v
   Player A      Player B      Countdown
     Lamp          Lamp        Lights 1-5
                      |
                      v
                 12V Power
```

### GPIO Mapping

```text
GPIO12 → SSR1 → Player A Lamp
GPIO16 → SSR2 → Player B Lamp

GPIO22 → SSR3 → Light 5
GPIO23 → SSR4 → Light 4
GPIO27 → SSR5 → Light 3
GPIO18 → SSR6 → Light 2
GPIO17 → SSR7 → Light 1

GPIO4  ← Player A Button
GPIO26 ← Player B Button
GPIO21 ← Reset Button
```
