"""
F1 Reaction Timer Game
----------------------

Players:
    Button A = GPIO 4
    Button B = GPIO 26
    Reset    = GPIO 21

Outputs:
    Player A Light = GPIO 12
    Player B Light = GPIO 16

    Countdown Lights:
        5 = GPIO 22
        4 = GPIO 23
        3 = GPIO 27
        2 = GPIO 18
        1 = GPIO 17

Operation:
    1. Both players press their buttons to arm the game.
    2. Five countdown lights illuminate.
    3. After a random delay, all countdown lights go out.
    4. Players react as quickly as possible.
    5. First and second reaction times are recorded.
    6. Press RESET to start a new round.
"""

import RPi.GPIO as GPIO
import time
import random
import threading

# --------------------------------------------------
# GPIO CONFIGURATION
# --------------------------------------------------

GPIO.setmode(GPIO.BCM)

# Input pins
BUTTON_A = 4
BUTTON_B = 26
RESET_BUTTON = 21

# Output pins
LIGHT_A = 12
LIGHT_B = 16

COUNTDOWN_LIGHTS = [22, 23, 27, 18, 17]

# Inputs with internal pull-ups enabled
GPIO.setup(BUTTON_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RESET_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Relay outputs
OUTPUTS = [LIGHT_A, LIGHT_B] + COUNTDOWN_LIGHTS

GPIO.setup(OUTPUTS, GPIO.OUT)

# Active-low relays:
# HIGH = off
# LOW = on
for pin in OUTPUTS:
    GPIO.output(pin, GPIO.HIGH)

# --------------------------------------------------
# GLOBAL VARIABLES
# --------------------------------------------------

state_lock = threading.Lock()

game_state = "ARMING"

armed_a = False
armed_b = False

reaction_times = {}

start_time = None

countdown_running = False

# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------

def relay_on(pin):
    """Turn relay ON (active low)."""
    GPIO.output(pin, GPIO.LOW)


def relay_off(pin):
    """Turn relay OFF (active low)."""
    GPIO.output(pin, GPIO.HIGH)


def relay_all_off():
    """Turn off every relay."""
    for pin in OUTPUTS:
        relay_off(pin)


# --------------------------------------------------
# RESET SYSTEM
# --------------------------------------------------

def reset_game():
    global armed_a
    global armed_b
    global reaction_times
    global start_time
    global countdown_running
    global game_state

    with state_lock:

        print("\nSystem Reset\n")

        relay_all_off()

        armed_a = False
        armed_b = False

        reaction_times = {}

        start_time = None

        countdown_running = False

        game_state = "ARMING"

        print("Ready. Both players press their buttons.")


# --------------------------------------------------
# COUNTDOWN
# --------------------------------------------------

def countdown_sequence():

    global game_state
    global start_time

    print("\nStarting countdown...\n")

    # F1 light sequence
    for pin in COUNTDOWN_LIGHTS:

        with state_lock:
            if game_state != "COUNTDOWN":
                return

        relay_on(pin)
        time.sleep(1)

    random_delay = random.uniform(0.3, 3.0)

    time.sleep(random_delay)

    # Lights out
    for pin in COUNTDOWN_LIGHTS:
        relay_off(pin)

    start_time = time.perf_counter()

    with state_lock:
        game_state = "REACTION"

    print("\nLIGHTS OUT! GO!\n")


# --------------------------------------------------
# BUTTON HANDLING
# --------------------------------------------------

def handle_button_a(channel):

    global armed_a
    global game_state

    with state_lock:

        # ------------------------
        # ARMING PHASE
        # ------------------------
        if game_state == "ARMING":

            if not armed_a:

                armed_a = True

                relay_on(LIGHT_A)

                print("Player A armed.")

                check_arm_status()

        # ------------------------
        # REACTION PHASE
        # ------------------------
        elif game_state == "REACTION":

            record_reaction("A")


def handle_button_b(channel):

    global armed_b
    global game_state

    with state_lock:

        if game_state == "ARMING":

            if not armed_b:

                armed_b = True

                relay_on(LIGHT_B)

                print("Player B armed.")

                check_arm_status()

        elif game_state == "REACTION":

            record_reaction("B")


# --------------------------------------------------
# START COUNTDOWN
# --------------------------------------------------

def check_arm_status():

    global countdown_running
    global game_state

    if armed_a and armed_b and not countdown_running:

        countdown_running = True

        
