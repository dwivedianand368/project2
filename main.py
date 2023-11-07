import time

def intro():
    print("You are on a quest to find the legendary treasure hidden in a mysterious cave.")
    time.sleep(2)
    print("As you enter the cave, you see two paths ahead of you.")
    time.sleep(2)
    print("One path is dark and ominous, while the other path is dimly lit.")
    time.sleep(2)
    print("Which path will you choose? (1 or 2)")
    choice = input("> ")

    if choice == "1":
        dark_path()
    elif choice == "2":
        dim_path()
    else:
        print("Invalid choice. Try again.")
        intro()

def dark_path():
    print("You cautiously proceed down the dark path.")
    time.sleep(2)
    print("You encounter a fierce dragon!")
    time.sleep(2)
    print("What will you do? (1. Fight, 2. Flee)")
    choice = input("> ")

    if choice == "1":
        print("You bravely fight the dragon but get defeated. Game over!")
    elif choice == "2":
        print("You wisely flee and find yourself at the entrance of the cave.")
        time.sleep(2)
        print("You decide to take the other path.")
        time.sleep(2)
        dim_path()
    else:
        print("Invalid choice. Try again.")
        dark_path()

def dim_path():
    print("You cautiously proceed down the dimly lit path.")
    time.sleep(2)
    print("You find a chest with a glimmering treasure!")
    time.sleep(2)
    print("Congratulations! You found the treasure. You win!")

intro()
