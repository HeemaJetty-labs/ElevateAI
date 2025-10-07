def start_adventure()
    print("Welcome to the Forest Adventure!"
    print("You wake up in a mysterious forest. You see two paths ahead.")
    print("Do you want to go 'left' or 'right'?")

    choice = input("Enter your choice: ")

    if choice = "left":
        print("You walk down the left path and encounter a river.")
        print("Do you want to 'swim' across or 'build' a raft?")
        river_choice = input("Enter your choice: ")

        if river_choice == "swim":
            print("You try to swim but the current is too strong. You drown. Game over.")
        elif river_choice == "build":
            print("You build a raft and cross safely. You win!"
        else
            print("Invalid choice. You stand there forever.")

    elif choice == "right":
        print("You walk down the right path and find a cave.")
        print("Do you want to 'enter' the cave or 'walk' past it?")
        cave_choice = input("Enter your choice: ")

        if cave_choice == "enter":
            print("It's dark inside. You hear a noise and run away. Game over.")
        elif cave_choice == "walk":
            print("You walk past the cave and find a treasure chest. You win!")
        else:
            print("Invalid choice. You get lost in the woods.")

    else:
        print("Invalid choice. The forest swallows you.")

start_adventure()
