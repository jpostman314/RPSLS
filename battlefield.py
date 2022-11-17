# *****CLASS THAT DETERMINES THE FLOW OF THE GAME*****

from human import Human
from ai import Ai
class Battlefield:

    def __init__(self) -> None:
        self.player_one = "player_one"
        self.player_two = "player_two"
        pass

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.choose_num_of_players()
        self.battle_phase()
        self.display_winner()


    def display_welcome(self):
        print("")
        print("Welcome to Rock Paper Scissors Lizard Spock!")
        print("")

    def display_rules(self):
        print("")
        print("Each match will be the best out of 3 rounds.")
        print("You will use the number keys to make your selections throughout the game.")
        print("")
        print("Scissors cut Paper.")
        print("Paper covers Rock.")
        print("Rock crushes Lizard.")
        print("Lizard poisons Spock.")
        print("Spock smashes Scissors.")
        print("Scissors decapitates Lizard.")
        print("Lizard eats Paper.")
        print("Paper disproves Spock.")
        print("Spock vaporizes Rock.")
        print("Rock crushes Scissors.")
        print("")
        

    def choose_num_of_players(self):
        valid_response = False
        
        while valid_response == False:
            number_of_players = int(input("How many players? Please type 1 or 2: "))
            if number_of_players == 1:
                self.player_one = Human()
                self.player_two = Ai()
                self.player_one.name = input("What is your name Player 1? ")
                print(f"Welcome to the game {self.player_one.name}!")
                valid_response = True
                
            elif number_of_players == 2:
                self.player_one = Human()
                self.player_two = Human()
                self.player_one.name = input("What is your name Player 1? ")
                print(f"Welcome to the game {self.player_one.name}!")
                self.player_two.name = input("What is your name Player 2? ")
                print(f"Welccome to the game {self.player_two.name}!")
                valid_response = True
            else:
                print("")
                print("That is an invalid response. Please type 1 or 2.")
                print("")
            return number_of_players
        number_of_players = self.human_players
    
    

    def battle_phase(self):
        self.human_players = 2
        games_played = 0
        turn_counter = 0
        
       
        
        while games_played < 3:
            if turn_counter % 2 == 0 and games_played < 4:
                self.player_one.choose_gesture()
                player_ones_choice = self.player_one.current_gesture
                turn_counter += 1
            elif self.human_players == 2 and turn_counter % 2 != 0 and games_played < 4:
                self.player_two.choose_gesture()
                player_twos_choice = self.player_two.current_gesture
                turn_counter += 1
            
                if player_ones_choice == "0":
                    if player_twos_choice == "0":
                        print("You have both chosen Rock. It's a tie!")
                    elif player_twos_choice == "1":
                        print("Paper covers rock.")
                        self.player_two.score += 1
                    elif player_twos_choice == "2":
                        print("Rock crushes Scissors.")
                        self.player_one.score += 1
                    elif player_twos_choice == "3":
                        print("Rock crushes Lizard.")
                        self.player_one.score += 1
                    elif player_twos_choice == "4":
                        print("Spock vaporizes Rock.")
                        self.player_two.score += 1
                    print(f"{self.player_one.name}'s score is now {self.player_one.score}.")
                    print(f"{self.player_two.name}'s score is now {self.player_two.score}.")
                    games_played += 1

                elif player_ones_choice == "1":
                    if player_twos_choice == "0":
                        print("Paper covers Rock.")
                        self.player_one.score += 1
                    elif player_twos_choice == "1":
                        print("You have both chosen Paper. It's a tie!")
                    elif player_twos_choice == "2":
                        print("Scissors cut Paper.")
                        self.player_two.score += 1
                    elif player_twos_choice == "3":
                        print("Lizard eats Paper.")
                        self.player_two.score += 1
                    elif player_twos_choice == "4":
                        print("Paper disproves Spock.")
                        self.player_one.score += 1
                    print(f"{self.player_one.name}'s score is now {self.player_one.score}.")
                    print(f"{self.player_two.name}'s score is now {self.player_two.score}.")
                    games_played += 1

                elif player_ones_choice == "2":
                    if player_twos_choice == "0":
                        print("Rock crushes Scissors.")
                        self.player_two.score += 1
                    elif player_twos_choice == "1":
                        print("Scissors cut Paper.")
                        self.player_one.score += 1
                    elif player_twos_choice == "2":
                        print("You have both chosen Scissors. It's a tie!")
                    elif player_twos_choice == "3":
                        print("Scissors decapitates Lizard.")
                        self.player_one.score += 1
                    elif player_twos_choice == "4":
                        print("Spock smashes Scissors.")
                        self.player_two.score += 1
                    print(f"{self.player_one.name}'s score is now {self.player_one.score}.")
                    print(f"{self.player_two.name}'s score is now {self.player_two.score}.")
                    games_played += 1

                elif player_ones_choice == "3":
                    if player_twos_choice == "0":
                        print("Rock crushes Lizard.")
                        self.player_two.score += 1
                    elif player_twos_choice == "1":
                        print("Lizard eats Paper.")
                        self.player_one.score += 1
                    elif player_twos_choice == "2":
                        print("Scissors decapitates Lizard.")
                        self.player_two.score += 1
                    elif player_twos_choice == "3":
                        print("You have both chosen Lizard. It's a tie!")
                    elif player_twos_choice == "4":
                        print("Lizard poisons Spock.")
                        self.player_one.score += 1
                    print(f"{self.player_one.name}'s score is now {self.player_one.score}.")
                    print(f"{self.player_two.name}'s score is now {self.player_two.score}.")
                    games_played += 1

                elif player_ones_choice == "4":
                    if player_twos_choice == "0":
                        print("Spock vaporizes Rock.")
                        self.player_one.score += 1
                    elif player_twos_choice == "1":
                        print("Paper disproves Spock.")
                        self.player_two.score += 1
                    elif player_twos_choice == "2":
                        print("Spock smashes Scissors.")
                        self.player_one.score += 1
                    elif player_twos_choice == "3":
                        print("Lizard poisons Spock.")
                    elif player_twos_choice == "4":
                        print("You have both chosen Spock. It's a tie!")
                        self.player_one.score += 1
                    print(f"{self.player_one.name}'s score is now {self.player_one.score}.")
                    print(f"{self.player_two.name}'s score is now {self.player_two.score}.")
                    games_played += 1



            
            
            
            
            else:
                print("")
                print("That is an invalid selection. Please type 0, 1, 2, 3 or 4.")
                print("")


    def display_winner(self):
        if self.player_one.score > self.player_two.score:
            print(f"{self.player_one.name} wins! Congratulations!!")
        elif self.player_two.score > self.player_one.score:
            print(f"{self.player_two.name} wins! Congratulations!!")
        elif self.player_one.score == self.player_two.score:
            print("It's a tie!")
        pass
        


