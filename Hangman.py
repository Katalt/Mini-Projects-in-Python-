import random

f=open("words.txt","r")
words = f.readlines()
word = random.choice(words)[:-1]

allow_errors = 7
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter,end = " ")
        else:
            print("_",end=" ")
    print("")

    guess = input(f"allowed errors left {allow_errors}, next guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allow_errors -= 1
        if allow_errors == 0:
            break
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False
if done:
    print(f"you found the word! it was {word}!")
else:
    print(f"game over! The word was {word}")
