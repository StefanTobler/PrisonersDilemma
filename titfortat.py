from enum import Enum


class Choices(Enum):
    NONE = 0
    COOPERATE = 1
    DEFECT = 2


class TitForTat:
    user_choice = Choices.NONE
    computer_choice = Choices.COOPERATE

    user_score: int = 0
    computer_score: int = 0

    turns = 0

    def play_turn(self):
        print("Please pick a choice:")
        print("1. Defect")
        print("2. Cooperate")
        selection = input()

        if int(selection) == 1:
            self.user_choice = Choices.DEFECT
        elif int(selection) == 2:
            self.user_choice = Choices.COOPERATE
        else:
            self.play_turn()
        print()
        self.check_choices()

    def start_game(self):
        print("|############################|")
        print("|###| Prisoner's Dilemma |###|")
        print("|############################|\n\n\n")
        print("Welcome to the Prisoner's Dilemma.")
        input("Press Enter to Continue...\n")
        print("You and an acquaintance just got arrested for planning to rob a bank.")
        input()
        print("Now you not must make a choice, keep quite or rat on your partner.")
        input()
        print("But there is a catch, if both of you rat you each get 5 years, if \n" +
              "you both keep quite you each get 6 months, your best bet is to rat and \nmake sure they are kept quit" +
              "e. If they don't rat on you, you get \noff free and they get 10 years.\n")

        input()
        turns = int(input("How many rounds would you like to play? "))
        print()

        for i in range(turns):
            self.play_turn()

        self.end_game()

    def check_choices(self):
        if self.user_choice == self.computer_choice:
            if self.user_choice == Choices.DEFECT:
                print("Looks like you both defected, uh oh...")
            else:
                print("Looks like you both helped each other.")
                self.computer_score += 1
                self.user_score += 1
        else:
            if self.user_choice == Choices.DEFECT:
                print("Looks like you got lucky this time, enjoy the outside.")
                self.user_score += 3
            else:
                print("Looks like you trust to easily, enjoy your time.")
                self.computer_score += 3
        self.computer_choice = self.user_choice
        print()
        self.print_scores()

    def print_scores(self):
        print("Your score is {}".format(self.user_score))
        print("Your acquaintance's score is {}".format(self.computer_score))
        input()

    def end_game(self):
        print()
        if self.computer_score > self.user_score:
            print("Looks like your acquaintance did a bit better than you. He got {}".format(self.computer_score) +
                  " {} points.".format(self.user_score))
        else:
            print("Looks like you outsmarted your acquaintance. You got {}".format(self.user_score) +
                  " points, he only got points, you only got {} points.".format(self.computer_score))


game = TitForTat()

game.start_game()
