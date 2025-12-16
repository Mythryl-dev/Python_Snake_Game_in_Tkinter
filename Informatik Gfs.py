#Der Import von tkinter wird benötigt um eine Nutzeroberfläche erzeugen zu können
from tkinter import *

#random wird benötigit um zufällige operationen aufrufen zu könnnen.
import random

import os

#Größe des Spielfeldes
GAME_WIDTH =  700
GAME_HEIGHT = 700

# Je höher die Zahl bei Speed desto langsamer läuft das Spiel
SPEED = 100

#Spielfeld "Zoom" je höher die Zahl desto geringer der Zoom, je kleiner desto stärker der Zoom
SPACE_SIZE = 50

#Größe der Schlange
BODY_PARTS = 3

#Farbe der Schlange
SNAKE_COLOUR = "#00FF00"

#Farbe des Apfels
FOOD_COLOUR ="#FF0000"

#Hintergrund Farbe
BACKGROUND_COLOUR = "#000000"


# Klassen
#__________________________________________________________________________________________________________
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.square = []
        
        for s in range(0,BODY_PARTS):
            self.coordinates.append([0,0])
        
        for x ,y in self.coordinates:
            square = canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOUR, tag ="snake")
            self.square.append(square)

class Food:
    def __init__(self):
        #random.ranint generiert einen Zufälligen integer diesen kann man begrenzen durch die Angabe eines Rahmens z.b (0, 4).
        #Hier würde eine zufällige volle Zahl zwischen 0 und 4 generiert.
        x = random.randint(0, int(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y =random.randint(0, int(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x,y]

        canvas.create_oval(x,y, x +SPACE_SIZE, y +SPACE_SIZE, fill = FOOD_COLOUR, tag ="food")

# Funktionen
#__________________________________________________________________________________________________________

def next_turn(snake,food):
    x ,y = snake.coordinates[0]
    if direction =="up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction =="left":
        x -= SPACE_SIZE
    elif direction =="right":
        x += SPACE_SIZE

    snake.coordinates.insert(0,(x,y))
   
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE,fill = SNAKE_COLOUR)
    
    snake.square.insert(0,square)
            
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text = "Punktestand:{}".format(score))
        canvas.delete("food")
        food = Food()
  
    else:
        del snake.coordinates [-1]
        canvas.delete(snake.square[-1])
        del snake.square[-1]

    if check_collision(snake):
        game_over()
    
    else:
        window.after(SPEED , next_turn,snake , food)

#def test_spawnverhinderung
    #Verhindert, dass der Apfel im Kopf der Schlange generiert wird.
    #if food.coordinates == snake.coordinates:
     #   canvas.delete("food")
      #  food = Food()
   #Verhindert, dass der Apfel im Körper der Schlange generiert wird. 
    #for body_part in snake.coordinates[0:]:
     #   if food.coordinates[0] == body_part[0] and food.coordinates[1] == body_part[1]:
      #      print("Error 255")
        #    canvas.delete("food")
         #   food = Food()
    

    # An dieser Stelle wird Festgelegt ,wass die zu ereichende Punktzahl ist um zu gewinnen.
#    if score == 15:
    if score == 100:
        you_win()

def change_direction(new_direction):
    global direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    
    if new_direction == 'right':
            if direction != 'left':
             direction = new_direction

    elif new_direction == 'up':
            if direction != 'down':
             direction = new_direction
    
    elif new_direction == 'down':
            if direction != 'up':
             direction = new_direction

def check_collision(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas',70), text="GAME OVER",fill="red",tag="game_over")
    print("Dein Highscore ist: " ,score)
    
def you_win():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas',70), text="You Win !!!",fill="green",tag="you_win")



window = Tk()

#window.title() bestimmt den angezeigten Namen der Application der oben angezeigt wird
window.title("GUI SNAKE TEST")
#Das erste False sperrt die Anpassung in die Breite und das Zweite Sperrt die Anpassung in die Höhe
window.resizable(False,False)

#Iconphoto bestimmt das oberige icon des Programmes
#window.iconphoto(False, PhotoImage(file="/home/noah/Dokumente/After 12.9.23/Informatik/tetris.png"))

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "tetris.png")  # Builds the full path
icon = PhotoImage(file=image_path)
window.iconphoto(False, icon)


score = 0
direction = 'down'

label = Label(window, text = "Punktestand:{}".format(score), font = ('consolas', 40))
label.pack()

canvas = Canvas(window, bg = BACKGROUND_COLOUR, height = GAME_HEIGHT, width = GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width  = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))


# normale tasten können in "r" angegeben werden während tasten wie die Pfeiltasten oder Enter in '<Enter>' angegeben werden müsssen
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

#Wasd
window.bind("a", lambda event: change_direction('left'))
window.bind("d", lambda event: change_direction('right'))
window.bind("w", lambda event: change_direction('up'))
window.bind("s", lambda event: change_direction('down'))

def exit():
      window.destroy()
      print("\033[38;2;0;255;0m You left the Matrix")
      print(r"""                  __
      _______    /*_>-<
  ___/ _____ \__/ /
 <____/     \____/""")

#Schließt das Programm
#Das progarmm ist schließbar mit q für quit und Escape
window.bind('<Escape>', lambda event: exit())
window.bind("q", lambda event: exit())

snake = Snake()
food = Food()

next_turn(snake,food)
window.mainloop()
