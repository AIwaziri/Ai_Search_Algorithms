import tkinter as tk
from tkinter import messagebox
import turtle
import sys
# from BFS import*
from PIL import Image


class Turtle_GUI:

    def __init__(self, states):
        self.timmy = turtle.Turtle()

        # Setting all the prefered properties for the turtle figure 
        self.timmy.resizemode("user")
        self.timmy.shapesize(0.5, 0.5,0)
        self.timmy.shape("square")
        self.timmy.color("dark red")
        self.timmy.pensize(3)
        self.timmy.speed(-1)

        self.states = states
        self.start_pos = ()
        self.end_pos = ()

        # self.callback = callback

        # Create a simple tkinter root window (it will not be shown)
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        # print(states)



    def initialize_screen(self):
        self.my_screen = turtle.Screen()
        self.my_screen.listen()
        self.my_screen.bgpic("smallMaze.gif")
        self.width, self.height = Image.open("smallMaze.gif").size
        self.px_width = round(self.width / 4)
        self.px_height = round(self.height / 4)
        self.movement_size_width = self.width / self.px_width
        self.movement_size_height = self.height / self.px_height
        self.my_screen.setup(width=(self.width + 30), height=(self.height + 20))
        self.my_screen.screensize(self.width, self.height)

        self.timmy.penup()
        # self.get_start_position()


        # self.my_screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", self.close_window)
        # self.my_screen.exitonclick()
        # self.my_screen.onclose(self.close_window())  # Set the close window callback
        # turtle.mainloop()

        # print(f"\n\n\n(main) start pos: {self.get_start_pos()}")
        # print(f"(main) end pos: {self.get_end_pos()} \n\n\n")

        # if self.callback:
        #     self.callback()

    def close_window(self):
        print("Closing the window...")
        self.my_screen.bye() 
        


    def get_start_position(self):
        self.timmy.penup()

        # Show a message box
        messagebox.showinfo("Start Position", "Click somewhere to set the starting position.")

        def on_click(x, y):
            self.timmy.setpos(x, y)
            print(f"start position at {self.timmy.pos()}")
            self.start_pos = (x, y)

            self.my_screen.onclick(None)  # Unbind click event after the first click
            return self.get_end_position() # Continue with the program
            # print("2 here")

        return self.my_screen.onclick(on_click)


    def get_end_position(self):
        self.timmy.penup()
        messagebox.showinfo("End Position", "Click somewhere to set the goal position")

        def on_click(x, y):
            print(f"end position at ({x}, {y})")
            self.end_pos = (x, y)

            self.my_screen.onclick(None)  # Unbind click event after the first click
            self.solve_maze()  # Continue with the program

        self.my_screen.onclick(on_click)
        return [self.get_start_pos(), self.get_end_pos()]


    def solve_maze (self):
        # self.timmy.penup()
        self.timmy.setpos(self.set_x(2), self.set_y(0)) # setting the starting position
        self.timmy.pendown()

        # Add your loop using self.timmy.setpos() here
        for state in (self.states):
            # print("originl:", state)
            self.timmy.setpos(self.set_x(state[1]), self.set_y(state[0]))
            # print("mutated: (", self.set_y(state[0]), ", ", self.set_x(state[1]), ")")
        
        # sys.exit()
        self.my_screen.exitonclick()


    


    # def forward(self):
    #     if self.timmy.heading() in (0, 180):
    #         self.timmy.forward(self.movement_size_width)
    #         print("moving right/left")
    #     elif self.timmy.heading() in (90, 270):
    #         self.timmy.forward(self.movement_size_height)
    #         print("moving up/down")

    def set_x (self, x_index):
        x_index = (x_index * self.movement_size_width) - (self.width/2)
        return x_index

    def set_y (self, y_index):
        y_index = -y_index + (self.px_height/2)
        # y_index = (y_index * movement_size_height)  + (height/2)
        y_index *= self.movement_size_height
        return y_index

    def translate_x_to_matrix(self, x_index):
        # this maps the x coordinate back to its position in the matrix
        x_index = (x_index + (self.width/2)) / self.movement_size_width
        return x_index

    def translate_y_to_matrix(self, y_index):
        # this maps the y coordinate back to its position in the matrix
        y_index /= self.movement_size_height
        y_index -= (self.px_height/2)
        y_index /= -1
        return y_index
    
    def get_start_pos (self):
        self.start_pos = (self.translate_x_to_matrix(self.start_pos[0]), self.translate_y_to_matrix(self.start_pos[1]))
        return self.start_pos

    def get_end_pos (self):
        self.end_pos = (self.translate_x_to_matrix(self.end_pos[0]), self.translate_y_to_matrix(self.end_pos[1]))
        return self.end_pos