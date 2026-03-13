import random
print("Welcome to MoodLift!")
print("This app helps improve your mood.")
print("\nHow are you feeling today?")
print("1. Happy :) ")
print("2. Sad :( ")
print("3. Stressed :|")
print("4. Bored :} ")

mood = input("Enter your choice: ")

if mood == "1":
    print("\nSongs: Happy - Pharrell Williams")
    print("Movie: La La Land")

elif mood == "2":
    print("\nSongs: Fight Song")
    print("Movie: The Pursuit of Happyness")

elif mood == "3":
    print("\nSongs: Weightless")
    print("Movie: Inside Out")

elif mood == "4":
    print("\nSongs: Can't Stop the Feeling")
    print("Movie: Jumanji")

else:
    print("Invalid choice")
jokes = [
"Why don’t skeletons fight each other? Because they don’t have the guts.",
"Why did the scarecrow win an award? Because he was outstanding in his field.",
"What did the ocean say to the beach? Nothing, it just waved.",
"Why did the student eat his homework? Because the teacher said it was a piece of cake.",
"Why can't your nose be 12 inches long? Because then it would be a foot."
]

print("\nMood Booster Joke:")
print(random.choice(jokes))

print("\nLet's play a quick game!")

number = random.randint(1,10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Correct! You win!")
else:
    print("Nice try! The number was", number)
