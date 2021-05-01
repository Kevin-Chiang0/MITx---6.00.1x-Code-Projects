guess = 0
hint = ' '
high = 100
low = 0

print("Please think of a number between 0 and 100!")
while hint != 'c':
    guess = (high+low)/2
    print("Is your secret number", str(guess) + "?")
    hint = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if hint == 'c':
        break
    elif hint == 'h':
        high = guess
    elif hint == 'l':
        low = guess
    else:
        print("Sorry, I didn't understand that")

print("Game over. Your secret number was:", guess)