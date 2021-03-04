def number_game():
    name = input("Please enter your name: ")
    print('Hi ' + name + "!")

    count = 0
    target = 12

    while count < 6:
        guess = input("Guess a number: ")
        guess = int(guess)
        count += 1

        if guess < target:
            print("Your guess is too low")
        if guess > target:
            print("Your guess is too high")
        if guess == target:
            print("Good job " + name + "! " + "You guessed the number in " + str(count) + " guesses!")
            return
        if count == 6:
            print("Sorry " + name + ". You could not guess my number " + str(target) + ".")
            return


number_game()