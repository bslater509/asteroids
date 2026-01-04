# Asteroids

A classic Asteroids arcade game implementation in Python using Pygame.

## Overview

This project recreates the iconic Asteroids arcade game where players control a spaceship and destroy asteroids by shooting them. The game features collision detection, scoring, and event logging for gameplay tracking.

## Features

- **Player-controlled spaceship** - Navigate and rotate your ship, fire shots at asteroids
- **Asteroid spawning system** - Asteroids spawn dynamically and split into smaller pieces when destroyed
- **Collision detection** - Detect collisions between player, shots, and asteroids
- **Score tracking** - Keep track of your score as you destroy asteroids
- **Event logging** - Game events and state are logged for analysis
- **Sprite-based rendering** - Efficient 2D graphics using Pygame's sprite system

## Requirements

- Python 3.13+
- Pygame 2.6.1

## Installation

```bash
pip install -e .
```

Or install dependencies directly:

```bash
pip install pygame==2.6.1
```

## How to Play

Run the game with:

```bash
python main.py
```

### Controls

- **Arrow Keys** - Rotate your spaceship left and right
- **Space** - Fire shots
- **Close Window** - Quit the game

### Objective

Destroy all asteroids to earn points. When you hit an asteroid, it splits into smaller pieces. Avoid colliding with asteroids or you'll lose!

## Project Structure

- `main.py` - Game loop and initialization
- `player.py` - Player spaceship class
- `asteroid.py` - Asteroid class and behavior
- `shot.py` - Projectile class
- `asteroidfield.py` - Asteroid spawning system
- `circleshape.py` - Base class for circular game objects
- `constants.py` - Game configuration (screen size, velocities, etc.)
- `logger.py` - Event and state logging utilities
- `test.py` - Test suite
 - `ideas.md` - Project ideas and planned improvements

## Logging

The game logs gameplay events and state information to JSON files:
- `game_events.jsonl` - Individual game events
- `game_state.jsonl` - Game state snapshots

These logs can be useful for debugging and analyzing gameplay patterns.

## License

This is a personal project implementation of the classic Asteroids arcade game.
