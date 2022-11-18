# *****DO NOT USE UNTIL MVP HAS BEEN REACHED FOR ALL USER STORIES*****
from player import Player

class Gestures(Player):

    def __init__(self):
        super().__init__()
        pass

    def display_gestures(self):
        print("")
        print("Your possible gesture choices are: ")
        print("")
        print("Type 0 for Rock.")
        print("Type 1 for Paper.")
        print("Type 2 for Scissors.")
        print("Type 3 for Lizard.")
        print("Type 4 for Spock.")
        print("")
        print("Please select your gesture using the number keys.")
        print("")

    def choose_gesture(self):
        valid_answer = False
        while valid_answer == False:
            user_input = input(f"Which gesture would you like to choose {self.name}? ")
            if user_input == "0":
                valid_answer = True
            elif user_input == "1":
                valid_answer = True
            elif user_input == "2":
                valid_answer = True
            elif user_input == "3":
                valid_answer = True
            elif user_input == "4":
                valid_answer = True
            else:
                print("That is an invalid selection. Please try again.")