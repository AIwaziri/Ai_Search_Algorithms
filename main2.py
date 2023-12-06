# import BFS
import cDFS
import DFS
from cDFS import DFS
from image_processing import image_to_matrix
from PIL import Image
from Problem import Maze
# import tkinter as tk
from tkinter import messagebox
import turtle


# defining the variables
start_pos = ()
end_pos = ()
states = []
image_path = ""
maze = []
mayze = None

# Defining the methods that will be used in the code
def get_end_position():
    global end_pos
    timmy.penup()
    messagebox.showinfo("End Position", "Click somewhere to set the goal position")

    def on_click(x, y):
        global end_pos
        print(f"end position at ({x}, {y})")
        end_pos = (x, y)

        my_screen.onclick(None)  # Unbind click event after the first click
        # solve_maze()  # Continue with the program

    my_screen.onclick(on_click)

def get_start_position():
    global start_pos
    timmy.penup()

    # Show a message box
    messagebox.showinfo("Start Position", "Click somewhere to set the starting position.")

    def on_click(x, y):
        global start_pos
        timmy.setpos(x, y)
        print(f"start position at {timmy.pos()}")
        start_pos = (x, y)

        my_screen.onclick(None)  # Unbind click event after the first click
        # get_end_position() # Continue with the program
            # print("2 here")

    my_screen.onclick(on_click)

def translate_x_to_matrix(x_index):
    # this maps the x coordinate back to its position in the matrix
    x_index = (x_index + (width/2)) / movement_size_width
    return round(x_index)

def translate_y_to_matrix(y_index):
    # this maps the y coordinate back to its position in the matrix
    y_index /= movement_size_height
    y_index -= (px_height/2)
    y_index /= -1
    return round(y_index)

def get_start_pos ():
    global start_pos
    # start_pos = (translate_x_to_matrix(start_pos[0]), translate_y_to_matrix(start_pos[1]))
    start_pos = (translate_y_to_matrix(start_pos[1]), translate_x_to_matrix(start_pos[0]))

    return start_pos

def get_end_pos ():
    global end_pos
    # end_pos = (translate_x_to_matrix(end_pos[0]), translate_y_to_matrix(end_pos[1]))
    end_pos = (translate_y_to_matrix(end_pos[1]), translate_x_to_matrix(end_pos[0]))
    return end_pos


def set_x (x_index):
    x_index = (x_index * movement_size_width) - (width/2)
    return x_index

def set_y (y_index):
    y_index = -y_index + (px_height/2)
    # y_index = (y_index * movement_size_height)  + (height/2)
    y_index *= movement_size_height
    return y_index






# start of the code execution
image_path = input("\nEnter the path to the image file:\n")
maze = image_to_matrix(image_path)


timmy = turtle.Turtle()
# setting the properties of the turtle
timmy.resizemode("user")
timmy.shapesize(0.5, 0.5,0)
timmy.shape("square")
timmy.color("dark red")
timmy.pensize(3)
timmy.speed(5)

my_screen = turtle.Screen()
my_screen.listen()
my_screen.bgpic(image_path)
# getting the number of pixels in the width and height of the image
width, height = Image.open(image_path).size    
px_width = round(width / 4)     # the size of the matrix width created from the image
px_height = round(height / 4)
movement_size_width = width / px_width
movement_size_height = height / px_height

my_screen.setup(width=(width + 30), height=(height + 20))
my_screen.screensize(width, height)

get_start_position()
input("Press enter to continue...")
get_end_position() 
input("Press enter to continue...")

print(f"\n\n\n(main) start pos: {get_start_pos()}")
print(f"(main) end pos: {get_end_pos()} \n\n\n")


# timmy.setpos(set_x(2), set_y(0)) # setting the starting position
timmy.pendown()

valid_choice = False

while (not valid_choice):
    valid_choice = True

    algorithm_chioce = input( "\nAlgorithm Options:\n 1. BFS\n 2. DFS\n 3. Greedy\n 4. A*\n" + 
                         "Which algorithm would you like to use to solve the maze? Enter one of the numbers:\n")

    if (algorithm_chioce == 1 or algorithm_chioce == "1"):
        print("BFS chosen")
        mayze = Maze(start_pos,[end_pos])
        # bfs_algorithm = cBFS.BFS(mayze)
        # states = cBFS.states
    elif (algorithm_chioce == 2 or algorithm_chioce == "2"):
        print("DFS chosen")
        dfs_algorithm = DFS(maze, start_pos, end_pos)
        states = dfs_algorithm.states
    elif (algorithm_chioce == 3 or algorithm_chioce == "3"):
        print("Greedy chosen")
        # states = Greedy.states
    elif (algorithm_chioce == 4 or algorithm_chioce == "4"):
        print("A* chosen")
        # states = Greedy.states
    else:
        print("Invalid Value try again")
        valid_choice = False


if (algorithm_chioce == "3" or algorithm_chioce == "4"):
    print("Heuristic Options:\n 1. Manhattan\n 2. Equalidian\n" + 
            "Which heurisitic function would like to use? Enter a number:\n")




# Add your loop using timmy.setpos() here
for state in (states):
    # print("originl:", state)
    timmy.setpos(set_x(state[1]), set_y(state[0]))
    # print("mutated: (", set_y(state[0]), ", ", set_x(state[1]), ")")




































# my_screen.exitonclick()
turtle.mainloop()