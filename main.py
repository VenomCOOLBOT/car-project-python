is_game_running = True
is_car_on = False
has_car_stopped = True

while is_game_running:
    command = input("> ").lower()
    if command == "help":
        print("start - to start the car\n"
              "go - to move car forward\n"
              "stop - to stop the car\n"
              "off - to turn off the car\n"
              "quit - to exit")
    elif command == "quit":
        print("Exiting the game...")
        is_game_running = False
    elif command == "off":
        if not is_car_on:
            print("Bruh the car is off already...")
        elif not has_car_stopped:
            print("Don't turn off the car until you stop...")
        else:
            is_car_on = False
            print("Car has turned off...")
    elif command == "start":
        if is_car_on:
            print("Car is already on bozo...")
        else:
            is_car_on = True
            print("Car started...Ready to go!")
    elif command == "go":
        if is_car_on and has_car_stopped:
            has_car_stopped = False
            print("We're moving forward! About time!")
        elif not is_car_on:
            print("Car is off dumbass...")
        else:
            print("We're already moving, captain obvious!")
    elif command == "stop":
        if has_car_stopped:
            print("Car has already stopped bozo...")
        else:
            has_car_stopped = True
            print("The car has stopped. Happy now?")
    else:
        print("Invalid command. Type 'help' if you need it... seriously, how hard can it be?")
