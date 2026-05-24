# GUI Snake Game – Python & Tkinter

A classic Snake game with a graphical user interface, developed in Python using `tkinter`.
The project supports keyboard controls, a scoring system, win conditions, and game-over logic.

---

# Preview

The game consists of:

* A controllable snake
* Randomly generated apples
* Score display
* Win and game-over screens
* Keyboard controls via arrow keys or WASD

---

# Technologies

* Python 3
* Tkinter (GUI)
* Random
* OS module

---

# Project Structure

```bash
project/
│
├── snake.py
├── tetris.png
└── README.md
```

---

# Installation & Execution

## 1. Install Python

Required:

* Python 3.10 or newer

Check with:

```bash
python --version
```

---

## 2. Download the Project

```bash
git clone https://github.com/Mythryl-dev/Python_Snake_Game_in_Tkinter.git
cd Python_Snake_Game_in_Tkinter
```

---

## 3. Start the Game

```bash
python snake.py
```

---

# Controls

| Key   | Function   |
| ----- | ---------- |
| ↑ / W | Move up    |
| ↓ / S | Move down  |
| ← / A | Move left  |
| → / D | Move right |
| Q     | Quit game  |
| ESC   | Quit game  |

---

# Game Mechanics

* The snake continuously moves across the game field.
* When collecting an apple:

  * the snake grows,
  * the score increases,
  * a new apple appears randomly.
* The game ends when:

  * colliding with the wall,
  * colliding with its own body.
* The player wins at 30 points.

---

# Screen Resolution

The game is currently optimized for:

* 2560×1440 with 225% scaling

Alternative values for 1920×1080 are already included in the code and can be enabled.

---

# Customization Options

The following values can easily be changed in the code:

```python
SPEED = 100
SPACE_SIZE = 100
BODY_PARTS = 3
```

## Change Colors

```python
SNAKE_COLOUR = "#00FF00"
FOOD_COLOUR = "#FF0000"
BACKGROUND_COLOUR = "#000000"
```

---

## Game Field Size

```python
GAME_WIDTH = 1137 * 2
GAME_HEIGHT = 640 * 2
```

## Speed

```python
SPEED = 100
```

The higher the value, the slower the game runs.

---

## Zoom / Grid Size

```python
SPACE_SIZE = 50 * 2
```

---

# Features

* GUI with Tkinter
* Score system
* Random food generation
* Win condition
* Game-over screen
* Keyboard controls
* Centered game window
* Custom window icon

---

# Learning Goals of the Project

This project is especially suitable for learning:

* Object-oriented programming (OOP)
* GUI development with Tkinter
* Event handling
* Game logic
* Collision detection
* Working with classes and functions

---

# Known Bugs

* Sometimes an apple spawns inside the snake’s body
