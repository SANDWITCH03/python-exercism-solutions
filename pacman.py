"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    return touching_ghost and not power_pellet_active


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    return (
        has_eaten_all_dots and
        (power_pellet_active or not touching_ghost)
    )


power_pellet_active = input(
    "Is power pellet active? (true/false): "
).lower() == "true"

touching_ghost = input(
    "Is Pac-Man touching a ghost? (true/false): "
).lower() == "true"

touching_power_pellet = input(
    "Is Pac-Man touching a power pellet? (true/false): "
).lower() == "true"

touching_dot = input(
    "Is Pac-Man touching a dot? (true/false): "
).lower() == "true"

has_eaten_all_dots = input(
    "Has Pac-Man eaten all dots? (true/false): "
).lower() == "true"


print("Can eat ghost:", eat_ghost(
    power_pellet_active,
    touching_ghost
))

print("Has scored:", score(
    touching_power_pellet,
    touching_dot
))

print("Has lost:", lose(
    power_pellet_active,
    touching_ghost
))

print("Has won:", win(
    has_eaten_all_dots,
    power_pellet_active,
    touching_ghost
))