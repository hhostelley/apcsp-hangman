from googleplaces import GooglePlaces, types, lang
from random import randrange
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

YOUR_API_KEY = 'AIzaSyCzUJbo-SRdXzrHX5FitEHDiPi071UNbgg'

google_places = GooglePlaces(YOUR_API_KEY)

def choose_answer():
    print "\nChoose a category: Fast Food(a), Stores(b), or Schools(c)"
    flush()
    answer = raw_input()
    return answer

def flush():
        sys.stdout.flush()

def hangman(phrase):
    phrase_without_dash = phrase.replace("-", "")
    phrase_final = phrase_without_dash.replace("/", "")
    constructed_word = ''
    fails_left = 10
    end_game = False
    print "\n Location Selected! Press any key to start your game of hangman!"
    raw_input()
    flush()
    print "Start!\n"
    time.sleep(1)
    while fails_left > 0 or end_game == False:
        print "Lives left:", fails_left
        print "Please type your guess:"
        guess = raw_input()
        flush()
        if guess not in phrase_final:
            print "Guess incorrect."
            fails_left = fails_left - 1
        else:
            for char in phrase_final:
                if char not " ":
                    if char == guess:
                        print char
                        constructed_word = constructed_word + char
                    else:
                        print "_"
                        constructed_word = constructed_word + "_"
        constructed_word = ''


def get_hint():
    pass

def get_phrases(result):
    phrases = []
    print "Places found:\n"
    for place in result.places:
        current_phrase = place.name
        print place.name
        phrases.append(current_phrase)
    phrase_index = randrange(0,len(phrases))
    phrase = phrases[phrase_index]
    print "Selected Word For Hangman:", phrase
    return phrase

def Game():
    print "WELCOME TO: Super Radical Hangman Go"
    print "\nPlease input location (ex: 10585 Mountian Vista Ridge, Highlands Ranch, CO)"
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

    phrase = get_phrases(query_result)

    game_result = hangman(phrase)

Game()
