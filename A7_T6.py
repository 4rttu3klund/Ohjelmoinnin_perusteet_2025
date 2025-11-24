import random
random.seed(1234)

rockArt = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paperArt = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissorsArt = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choiceArt = {1: rockArt, 2: paperArt, 3: scissorsArt}
choiceName = {1: "rock", 2: "paper", 3: "scissors"}

def Choice(playerName, choice):
    print("#########################")
    print(f"{playerName} chose {choiceName[choice]}.\n")
    print(choiceArt[choice])
    print("#########################")

def Winner(playerChoice, botChoice, playerName):
    if playerChoice == botChoice:
        print(f"Draw! Both players chose {choiceName[playerChoice]}.\n")
        return "draw"
    wins = (
        (playerChoice == 1 and botChoice == 3) or
        (playerChoice == 2 and botChoice == 1) or
        (playerChoice == 3 and botChoice == 2)
    )
    if wins:
        print(f"{playerName} {choiceName[playerChoice]} beats "
              f"RPS-3PO {choiceName[botChoice]}.\n")
        return "win"
    else:
        print(f"RPS-3PO {choiceName[botChoice]} beats "
              f"{playerName} {choiceName[playerChoice]}.\n")
        return "loss"

def Options(playerName):
    print("Options:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")
    choice = input("Your choice: ")
    if choice == "0":
        return "quit"
    if choice not in ["1", "2", "3"]:
        print("Invalid input. Try again.\n")
        return None
    playerChoice = int(choice)
    botChoice = random.randint(1, 3)
    print("Rock! Paper! Scissors! Shoot!\n")
    Choice(playerName, playerChoice)
    print(f"RPS-3PO chose {choiceName[botChoice]}.\n")
    print(choiceArt[botChoice])
    print("#########################\n")
    return Winner(playerChoice, botChoice, playerName)

def main():
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    playerName = input("Insert player name: ")
    print(f"Welcome {playerName}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...\n")
    wins = losses = draws = 0
    while True:
        result = Options(playerName)
        if result is None:
            continue
        if result == "quit":
            break
        if result == "win":
            wins += 1
        elif result == "loss":
            losses += 1
        elif result == "draw":
            draws += 1
    print("\nResults:")
    print(f"{playerName} - wins ({wins}), losses ({losses}), draws ({draws})")
    print(f"RPS-3PO - wins ({losses}), losses ({wins}), draws ({draws})")
    print("\nProgram ending.")

if __name__ == "__main__":
    main()