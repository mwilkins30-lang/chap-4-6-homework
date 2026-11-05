secret = 6

guess = int(input("Guess the secret number: "))

if guess == secret:
    print("just right")
elif guess > secret:
    print("too high")
else:
    print("too low")