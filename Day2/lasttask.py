def guessTheWord():
    numberOfGuess = 0
    word_idx = 0
    words = ["magdi", "love", "banana", "mango"]
    username = input("please enter your name  ")
    random_word = words[word_idx]
    shownWord = '$' * len(random_word)
    while numberOfGuess < 7 and shownWord != random_word:
        print("The word is:", shownWord)
        userGuess = input("plwase guess a letter ")

        if userGuess in random_word:
            print("good work")
            shownWord = "".join([letter if letter in random_word else '$' for letter in shownWord])
        else:
            print("sorry but the letter is not here")

        numberOfGuess += 1

    if shownWord == random_word:
        print("congrats you guessed it right,The word was: " + random_word)
    else:
        print("sorry, The word was: " + random_word)

guessTheWord()
