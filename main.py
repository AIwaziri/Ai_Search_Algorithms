import tkinter as tk
from tkinter import simpledialog
import turtleGUI
import BFS
import DFS
# import Greedy

image_path = input("\nEnter the path to the image file:\n")

# Create the root window

# root = tk.Tk()
# root.withdraw()  # Hide the main window

# Get user input using a dialog
# user_input = simpledialog.askstring("Path to Image", "Enter the path to image file:")

# Display the user input
# print("Image path:", user_input)

valid_choice = False
states = []

while (not valid_choice):
    valid_choice = True

    algorithm_chioce = input( "\nAlgorithm Options:\n 1. BFS\n 2. DFS\n 3. Greedy\n 4. A*\n" + 
                         "Which algorithm would you like to use to solve the maze? Enter one of the numbers:\n")

    if (algorithm_chioce == 1 or algorithm_chioce == "1"):
        print("BFS chosen")
        states = BFS.states
    elif (algorithm_chioce == 2 or algorithm_chioce == "2"):
        print("DFS chosen")
        states = DFS.states
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










def main():
    gui = turtleGUI.Turtle_GUI(states)
    gui.initialize_screen()
    print(gui.get_start_position())
    # gui.get_end_position()
    print(f"\n\n\n(main) start pos: {gui.get_start_pos()}")
    print(f"(main) end pos: {gui.get_end_pos()} \n\n\n")

# def main():
#     def callback_after_turtle_close():
#         print(f"\n\n\n(main) start pos: {gui.get_start_pos()}")
#         print(f"(main) end pos: {gui.get_end_pos()} \n\n\n")

#     gui = turtleGUI.Turtle_GUI(states, callback=callback_after_turtle_close)
#     gui.initialize_screen()


if __name__ == "__main__":
    main()
