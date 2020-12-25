import random
gamewords=["momo","şeker portakalı","fareler ve insanlar","satranç","savaş sanatı"]
username = input("Please,enter user name:")
print("Welcome",username)
print("Let's go,play the game!!")
print("\n\n\n\t\t ***Word Guessing Game*** ")
print("\n You have 10 attempts to guess the word correctly .")
wrong_list=[]
word=random.choice(gamewords)
print(f"The word is of {len(word)} letters. ")
guessed_word = []
for i in range(len(word)):
    guessed_word.append("__")
print(*([i for i in guessed_word]))
c=8
while(c):
    c=c-1 
    guessed_letter = input("Please enter letter:")
    if not guessed_letter.isalpha():
        print("Please only a letter!!")
    elif(len(guessed_letter)>1):
        print("Only one letter...")
    elif(guessed_letter in wrong_list):
        print("You have already used this letter!")
    if guessed_letter in word:
        for i in range(len(word)):
            if word[i] == guessed_letter:
                guessed_word[i]=word[i] 
    else:
        print("Wrong letter")
        wrong_list.append(guessed_letter)
    guess_word = [i for i in guessed_word]
    guess_word = "".join(guess_word)
    if word ==guess_word :
        print('YESS !!, You have got the letter ...')
        exit(0)
    print(*([i for i in guessed_word]))
    print(f"You have {c} attempts left")
    if c==0:
        if  word!=guessed_word  :
            print(f"GAME OVER!!! ,The Word was {word}")
            exit(0)