import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def flush():
        sys.stdout.flush()

def hangman():
    phrase = 'AT&T'
    phrase_no_spaces = phrase.replace(" ", "")
    phrase_final = phrase_no_spaces.lower()
    print phrase_final
    constructed_word = []
    for char in phrase_final:
        constructed_word.append("_")
    fails_left = 10
    guessed_letters = []

    flush()
    print "\nLocation Selected! Press any key to start your game of hangman!"
    flush()
    raw_input()
    print "Start!\n"
    while fails_left != 0 and "_" in constructed_word:
        print "\nLives left:", fails_left
        joined_word = "".join(constructed_word)
        print joined_word, "\n"
        try:
            print "Please type your guess (should be one letter, number, or symbol):"
            flush()
            guess = raw_input()
            flush()
            player_guess = guess.lower()
        except:
            print "That is not valid input. Please try again."
            continue
        else:
            if len(player_guess) > 1:
                print "That's more than one character. Try again."
                continue
            elif player_guess in guessed_letters:
                print "You have already guessed that! Try again."
                continue
            else:
                pass

        guessed_letters.append(player_guess)

        for letter in range(len(phrase_final)):
            if player_guess == phrase_final[letter]:
                constructed_word[letter] = player_guess

        if player_guess not in phrase_final:
            fails_left = fails_left - 1
            print "\nGuess not correct. Please try agian."

    if "_" not in constructed_word:
            print "\nCongratulations! You won! The phrase was %r!" % phrase_final
    else:
        print "\nSorry :( You lost. The phrase was %r." % phrase_final

hangman()
