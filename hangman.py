from googleplaces import GooglePlaces, types, lang
from random import randrange
import googlemaps
from datetime import datetime
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def flush():
        sys.stdout.flush()

API_KEY = 'AIzaSyCzUJbo-SRdXzrHX5FitEHDiPi071UNbgg'
gmaps = googlemaps.Client(key='AIzaSyDqmC_4c0wXpq6iWj-Z92M_AGxic2P0E8I')

google_places = GooglePlaces(API_KEY)

def choose_answer():
    print "\nChoose a category: Fast Food(a), Stores(b), or Schools(c)"
    flush()
    answer = raw_input()
    return answer

def get_hint():
    pass

def get_phrases(result, number):
    phrases = []
    for place in result.places:
        current_phrase = place.name
        print place.name
        phrases.append(current_phrase)
    phrase_index = number
    phrase = phrases[phrase_index]
    print "Selected Word For Hangman:", phrase
    return phrase

def hangman(phrase):
    start_phrase = phrase
    phrase_no_spaces = start_phrase.replace(" ", "")
    phrase_no_dashes = phrase_no_spaces.replace("/", "")
    phrase_no_slashes = phrase_no_dashes.replace("-", "")
    phrase_final = phrase_no_slashes.lower()
    print phrase_final
    constructed_word = []
    for char in phrase_final:
        constructed_word.append("_")
    fails_left = 10
    guessed_letters = []

    flush()
    print "\nLocation Selected! Press start to start your game of hangman!"
    flush()
    raw_input()
    print "Start!\n"
    while fails_left != 0 and "_" in constructed_word:
        print "\nLives left:", fails_left
        joined_word = "".join(constructed_word)
        print joined_word, "\n"
        input = False
        while input == False:
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
                    input = True
                    pass

        guessed_letters.append(player_guess)

        for letter in range(len(phrase_final)):
            if player_guess == phrase_final[letter]:
                constructed_word[letter] = player_guess

        if player_guess not in phrase_final:
            fails_left = fails_left - 1
            print "\nGuess not correct. Please try agian."

    if "_" not in constructed_word:
        print "\nCongratulations! You won! The phrase was %s!" % phrase_final
        return True
    else:
        print "\nSorry :( You lost. The phrase was %s." % phrase_final
        return False

def Main():
    print "WELCOME TO: Super Radical Hangman"
    print "\nPlease input location (ex: Highlands Ranch, CO)"
    flush()
    location = raw_input()
    flush()
    answer = choose_answer()
    valid_input = False

    while valid_input == False:
        if answer == 'a':
            place_type = 'Fast food'
            valid_input = True
        elif answer == 'b':
            place_type = 'Stores'
            valid_input = True
        elif answer == 'c':
            place_type = 'Schools'
            valid_input = True
        else:
            print "\nInput (",answer,") not valid. Please try again."
            answer = choose_answer()

    flush()

    query_result = google_places.nearby_search(
        location=location, keyword=place_type,
        radius=12000, rankby='distance')

    length = 0
    for places in query_result.places:
        length += 1
    phrase_index = randrange(0,length)
    search = query_result.places[phrase_index]
    search_dict = search.geo_location

    now = datetime.now()
    directions_result = gmaps.directions(location,
                                     search_dict,
                                     mode="driving",
                                     departure_time=now)

    first_result = directions_result[0]
    print first_result['legs']

    phrase = get_phrases(query_result, phrase_index)

    game_result = hangman(phrase)

Main()
