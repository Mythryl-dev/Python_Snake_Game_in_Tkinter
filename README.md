#  GUI Snake Game – Python & Tkinter

Ein klassisches Snake-Spiel mit grafischer Benutzeroberfläche, entwickelt in Python mit `tkinter`.  
Das Projekt unterstützt Tastatursteuerung, Punktesystem, Gewinnbedingung und Game-Over-Logik.

---

#  Vorschau

Das Spiel besteht aus:

- Einer steuerbaren Schlange
- Zufällig generierenden Äpfeln
- Punktestand-Anzeige
- Gewinn- und Game-Over-Screen
- Tastatursteuerung via Pfeiltasten oder WASD

---

#  Technologien

- Python 3
- Tkinter (GUI)
- Random
- OS-Modul

---

# Projektstruktur

```bash
project/
│
├── snake.py
├── tetris.png
└── README.md
```

---

# Installation & Ausführung

## 1. Python installieren

Benötigt wird:

- Python 3.10 oder neuer

Prüfen mit:

```bash
python --version
```

---

## 2. Projekt herunterladen

```bash
git clone https://github.com/Mythryl-dev/Python_Snake_Game_in_Tkinter.git
cd Python_Snake_Game_in_Tkinter
```

---

## 3. Spiel starten

```bash
python snake.py
```

---

# Steuerung

| Taste | Funktion |
|------|-----------|
| ↑ / W | Nach oben |
| ↓ / S | Nach unten |
| ← / A | Nach links |
| → / D | Nach rechts |
| Q | Spiel beenden |
| ESC | Spiel beenden |

---

#  Spielmechanik

- Die Schlange bewegt sich kontinuierlich über das Spielfeld.
- Beim Einsammeln eines Apfels:
  - wächst die Schlange,
  - der Punktestand erhöht sich,
  - ein neuer Apfel erscheint zufällig.
- Das Spiel endet bei:
  - Kollision mit dem Rand,
  - Kollision mit dem eigenen Körper.
- Bei 30 Punkten gewinnt der Spieler.

---

# Bildschirmauflösung

Das Spiel ist aktuell optimiert für:

- 2560×1440 mit 225 % Skalierung

Alternative Werte für 1920×1080 sind bereits im Code vorhanden und können aktiviert werden.

---

# Anpassungsmöglichkeiten

Folgende Werte können einfach im Code verändert werden:

```python
SPEED = 100
SPACE_SIZE = 100
BODY_PARTS = 3
```

## Farben ändern

```python
SNAKE_COLOUR = "#00FF00"
FOOD_COLOUR = "#FF0000"
BACKGROUND_COLOUR = "#000000"
```

---
## Spielfeldgröße

```python
GAME_WIDTH = 1137 * 2
GAME_HEIGHT = 640 * 2
```

## Geschwindigkeit

```python
SPEED = 100
```

Je höher der Wert, desto langsamer läuft das Spiel.

---

## Zoom / Rastergröße

```python
SPACE_SIZE = 50 * 2
```

---

#  Features

- GUI mit Tkinter  
- Punktestand-System  
- Zufällige Food-Generierung  
- Gewinnbedingung  
- Game-Over-Screen  
- Tastatursteuerung  
- Zentrierung des Fensters  
- Eigenes Fenster-Icon  

---
#  Lernziele des Projekts

Dieses Projekt eignet sich besonders zum Lernen von:

- Objektorientierter Programmierung (OOP)
- GUI-Entwicklung mit Tkinter
- Event-Handling
- Spiel-Logik
- Kollisionsabfragen
- Arbeiten mit Klassen und Funktionen

---

# Bekannte Bugs

- manchmal generiert ein Apfel in dem Körper der Schlange

---
