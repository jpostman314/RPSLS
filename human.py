from player import Player

class Human(Player):

    def __init__(self):
        super().__init__()

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

        print("")
        print(f"{self.name} has chosen {self.gestures_list[int(user_input)]}." )
        print("")
        self.current_gesture = self.gestures_list[int(user_input)]
        return self.current_gesture
